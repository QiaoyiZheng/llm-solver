#!/usr/bin/env python3
"""实时终端看板：监控三种模型最新的证书实验。

用法：
    python dashboard.py
    python dashboard.py --refresh 1
    python dashboard.py --run-kind any

看板只读取 experiments/*/runs 下的实验产物，不会修改或启动实验。
"""

from __future__ import annotations

import argparse
import ctypes
import json
import os
import time
from collections import Counter, defaultdict, deque
from datetime import datetime
from pathlib import Path

from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.table import Table
from rich.text import Text


ROOT = Path(__file__).resolve().parent
EXPERIMENTS = ROOT / "experiments"
INPUTS = ROOT / "benchmarks" / "certificate-inputs" / "cases"
MODEL_DIRS = (
    ("Codex 5.6 Sol", "codex-gpt-5.6-sol"),
    ("DeepSeek V4 Flash", "deepseek-v4-flash"),
    ("DeepSeek V4 Pro", "deepseek-v4-pro"),
)
RECENT_LIMIT = 12


def load_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return default


def load_jsonl(path: Path):
    rows = []
    try:
        with path.open("r", encoding="utf-8-sig") as handle:
            for line in handle:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    # 正在写入的最后一行可能暂时不完整。
                    continue
    except OSError:
        pass
    return rows


def parse_time(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def fmt_duration(seconds):
    if seconds is None:
        return "—"
    seconds = max(0, int(seconds))
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours}h {minutes:02d}m" if hours else f"{minutes}m {secs:02d}s"


def fmt_tokens(value):
    value = int(value or 0)
    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return str(value)


def ratio(num, den):
    return f"{num / den:.1%}" if den else "—"


def process_alive(pid):
    if not isinstance(pid, int) or pid <= 0:
        return False
    if os.name == "nt":
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        handle = ctypes.windll.kernel32.OpenProcess(
            PROCESS_QUERY_LIMITED_INFORMATION, False, pid
        )
        if handle:
            ctypes.windll.kernel32.CloseHandle(handle)
            return True
        return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def latest_run(model_dir, run_kind):
    runs_dir = EXPERIMENTS / model_dir / "runs"
    if not runs_dir.is_dir():
        return None
    candidates = [p for p in runs_dir.iterdir() if p.is_dir()]
    if run_kind == "formal":
        candidates = [p for p in candidates if "full" in p.name.lower()]
    return max(candidates, key=lambda p: p.name, default=None)


def planned_cases(config):
    repetitions = int(config.get("repetitions", 5) or 5)
    selected_logics = set(config.get("selected_logics") or [])
    selected_benchmarks = set(config.get("selected_benchmarks") or [])
    files = list(INPUTS.rglob("*.json")) if INPUTS.is_dir() else []
    if selected_logics:
        files = [p for p in files if p.parent.name in selected_logics]
    if selected_benchmarks:
        files = [
            p for p in files
            if p.stem in selected_benchmarks or p.name in selected_benchmarks
        ]
    limit = config.get("benchmark_limit")
    if limit:
        files = files[: int(limit)]
    return len(files) * repetitions


def usage_tokens(usage):
    if not isinstance(usage, dict):
        return 0, 0, 0
    inp = usage.get("input_tokens", usage.get("prompt_tokens", 0)) or 0
    out = usage.get("output_tokens", usage.get("completion_tokens", 0)) or 0
    reasoning = usage.get("reasoning_output_tokens") or 0
    details = usage.get("completion_tokens_details") or {}
    reasoning = reasoning or details.get("reasoning_tokens", 0) or 0
    return int(inp), int(out), int(reasoning)


class ModelState:
    def __init__(self, label, model_dir, run_kind):
        self.label = label
        self.model_dir = model_dir
        self.run = latest_run(model_dir, run_kind)
        self.config = load_json(self.run / "configuration.json", {}) if self.run else {}
        self.launcher = load_json(self.run / "launcher.json", {}) if self.run else {}
        self.raw_rows = load_jsonl(self.run / "results" / "runs.jsonl") if self.run else []
        # --resume 和单次重试会追加记录；一个 (case, run) 只能占一个实验槽位。
        latest = {}
        for index, row in enumerate(self.raw_rows):
            key = (row.get("case") or row.get("benchmark"), row.get("run"))
            rank = (int(row.get("attempt") or 0), index)
            if key not in latest or rank > latest[key][0]:
                latest[key] = (rank, row)
        self.rows = [item[1] for item in latest.values()]
        self.errors = load_jsonl(self.run / "results" / "infrastructure-errors.jsonl") if self.run else []
        self.planned = planned_cases(self.config) if self.run else 0
        self.complete = sum(r.get("state") == "complete" for r in self.rows)
        self.correct = sum(r.get("verdict_correct") is True for r in self.rows)
        self.cert_valid = sum(r.get("certificate_valid") is True for r in self.rows)
        self.fully_solved = sum(r.get("fully_solved") is True for r in self.rows)
        self.format_valid = sum(r.get("response_format") in (None, "valid") for r in self.rows)
        self.latency = sum(float(r.get("latency_seconds") or 0) for r in self.rows)
        self.inputs = self.outputs = self.reasoning = 0
        self.logic = defaultdict(lambda: Counter(total=0, correct=0, certificate=0, solved=0))
        for row in self.rows:
            inp, out, reasoning = usage_tokens(row.get("usage"))
            self.inputs += inp
            self.outputs += out
            self.reasoning += reasoning
            bucket = self.logic[row.get("logic") or "?"]
            bucket["total"] += 1
            bucket["correct"] += row.get("verdict_correct") is True
            bucket["certificate"] += row.get("certificate_valid") is True
            bucket["solved"] += row.get("fully_solved") is True
        self.pid = self.launcher.get("pid")
        self.alive = process_alive(self.pid)

    @property
    def status(self):
        if self.alive:
            return "运行中", "green"
        if self.planned and self.complete >= self.planned:
            return "已完成", "cyan"
        if self.run:
            return "已停止", "yellow"
        return "无记录", "dim"


def render_header(states, refreshed):
    done = sum(s.complete for s in states)
    planned = sum(s.planned for s in states)
    running = sum(s.alive for s in states)
    text = Text.from_markup(
        f"[bold cyan]SMT 证书实验看板[/]   "
        f"[bold]{done}[/]/{planned or '?'} 次   "
        f"[green]运行中 {running}[/]   "
        f"[dim]刷新 {refreshed.strftime('%H:%M:%S')} · Ctrl+C 退出[/]"
    )
    return Panel(text, border_style="cyan")


def render_models(states):
    table = Table(expand=True, show_header=True, header_style="bold")
    table.add_column("模型", min_width=18)
    table.add_column("状态", width=9)
    table.add_column("进度", ratio=3)
    table.add_column("分类正确", justify="right")
    table.add_column("证书有效", justify="right")
    table.add_column("完全解出", justify="right")
    table.add_column("均时", justify="right")
    table.add_column("Token (入/出/推理)", justify="right")
    for s in states:
        status, color = s.status
        progress = min(1.0, s.complete / s.planned) if s.planned else 0
        bar = ProgressBar(total=100, completed=progress * 100, width=22)
        progress_cell = Table.grid(expand=True)
        progress_cell.add_row(bar, Text(f" {s.complete}/{s.planned or '?'}", style="bold"))
        avg = s.latency / len(s.rows) if s.rows else None
        table.add_row(
            s.label,
            f"[{color}]{status}[/]\n[dim]PID {s.pid or '—'}[/]",
            progress_cell,
            f"{s.correct}/{len(s.rows)}\n[dim]{ratio(s.correct, len(s.rows))}[/]",
            f"{s.cert_valid}/{len(s.rows)}\n[dim]{ratio(s.cert_valid, len(s.rows))}[/]",
            f"[bold green]{s.fully_solved}[/]/{len(s.rows)}\n[dim]{ratio(s.fully_solved, len(s.rows))}[/]",
            fmt_duration(avg),
            f"{fmt_tokens(s.inputs)}/{fmt_tokens(s.outputs)}/{fmt_tokens(s.reasoning)}",
        )
    return Panel(table, title="最新正式实验", border_style="cyan")


def render_logics(states):
    names = sorted({logic for s in states for logic in s.logic})
    table = Table(expand=True, show_header=True, header_style="bold")
    table.add_column("Logic", style="cyan")
    for state in states:
        table.add_column(state.label.replace("DeepSeek ", "DS "), justify="right")
    for logic in names:
        cells = []
        for state in states:
            b = state.logic.get(logic)
            cells.append("—" if not b else f"{b['solved']}/{b['total']} ({ratio(b['solved'], b['total'])})")
        table.add_row(logic, *cells)
    if not names:
        table.add_row("[dim]暂无结果[/]", *("—" for _ in states))
    return Panel(table, title="各逻辑完全解出（有效分类 + 有效证书）", border_style="green")


def render_recent(states):
    recent = []
    for state in states:
        for row in state.rows[-RECENT_LIMIT:]:
            recent.append((parse_time(row.get("timestamp")), state, row))
    recent.sort(key=lambda item: item[0] or datetime.min.astimezone(), reverse=True)
    table = Table(expand=True, show_header=True, header_style="bold", pad_edge=False)
    table.add_column("时间", style="dim", no_wrap=True)
    table.add_column("模型", no_wrap=True)
    table.add_column("Logic", style="cyan", no_wrap=True)
    table.add_column("用例 / 重复", overflow="ellipsis", no_wrap=True)
    table.add_column("分类", no_wrap=True)
    table.add_column("证书", no_wrap=True)
    table.add_column("最终", no_wrap=True)
    for ts, state, row in recent[:RECENT_LIMIT]:
        correct = row.get("verdict_correct") is True
        cert = row.get("certificate_valid") is True
        solved = row.get("fully_solved") is True
        table.add_row(
            ts.astimezone().strftime("%H:%M:%S") if ts else "—",
            state.label.replace("DeepSeek ", "DS "),
            row.get("logic") or "?",
            f"{Path(row.get('case') or '?').stem} / {row.get('run', '?')}",
            f"[{'green' if correct else 'red'}]{row.get('prediction') or '?'}[/]",
            f"[{'green' if cert else 'red'}]{'有效' if cert else '无效'}[/]",
            f"[{'bold green' if solved else 'bold red'}]{'通过' if solved else '失败'}[/]",
        )
    return Panel(table, title="最近完成", border_style="cyan")


def render_details(states):
    lines = []
    for state in states:
        status, color = state.status
        run_name = state.run.name if state.run else "—"
        errors = len(state.errors)
        model = state.config.get("model", "?")
        effort = state.config.get("reasoning_effort", "?")
        lines.append(
            Text.from_markup(
                f"[{color}]● {state.label}[/]  [dim]{model} · {effort}[/]\n"
                f"  [dim]{run_name}[/]\n"
                f"  基础设施错误 [{'red' if errors else 'green'}]{errors}[/]"
            )
        )
    return Panel(Group(*lines), title="运行信息", border_style="yellow")


def build_layout(states, refreshed):
    layout = Layout()
    layout.split_column(
        Layout(render_header(states, refreshed), size=3),
        Layout(render_models(states), size=11),
        Layout(name="middle", size=12),
        Layout(render_recent(states)),
    )
    layout["middle"].split_row(
        Layout(render_logics(states), ratio=3),
        Layout(render_details(states), ratio=2),
    )
    return layout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", type=float, default=1.5, help="刷新间隔秒数")
    parser.add_argument(
        "--run-kind", choices=("formal", "any"), default="formal",
        help="formal=最新全量实验（默认），any=包括 smoke test",
    )
    args = parser.parse_args()
    console = Console()
    try:
        with Live(console=console, screen=True, refresh_per_second=max(1, 1 / args.refresh)) as live:
            while True:
                states = [ModelState(label, directory, args.run_kind) for label, directory in MODEL_DIRS]
                live.update(build_layout(states, datetime.now()))
                time.sleep(args.refresh)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
