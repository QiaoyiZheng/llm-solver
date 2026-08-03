#!/usr/bin/env python3
"""Run the DeepSeek V4 Pro certificate experiment using the shared runner."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SHARED = ROOT / "experiments" / "deepseek-v4-flash" / "scripts" / "run_certificate.py"
SPEC = importlib.util.spec_from_file_location("deepseek_certificate_runner", SHARED)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load shared runner: {SHARED}")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)
runner.MODEL_DIR = Path(__file__).resolve().parent.parent
runner.API_CONFIG = runner.MODEL_DIR / "config" / "api.json"
runner.MODEL = "deepseek-v4-pro"


if __name__ == "__main__":
    raise SystemExit(runner.main())
