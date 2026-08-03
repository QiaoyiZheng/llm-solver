#!/usr/bin/env python3
"""Validate a DeepSeek experiment config without printing its API key."""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_config(path: Path) -> tuple[dict[str, str], str]:
    config = json.loads(path.read_text(encoding="utf-8"))
    required = {"provider", "base_url", "model", "api_key_file", "api_key_environment_fallback"}
    if not isinstance(config, dict) or set(config) != required:
        raise ValueError("invalid DeepSeek API config keys")
    if config["provider"] != "deepseek" or not config["base_url"].startswith("https://"):
        raise ValueError("invalid DeepSeek provider configuration")
    key_path = (path.parent / config["api_key_file"]).resolve()
    try:
        key_path.relative_to(ROOT)
    except ValueError as error:
        raise ValueError("api_key_file must remain inside the repository") from error
    key = key_path.read_text(encoding="utf-8").strip() if key_path.is_file() else ""
    if not key:
        key = os.environ.get(config["api_key_environment_fallback"], "").strip()
    if not key:
        raise ValueError("DeepSeek API key is missing")
    return config, key


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--online", action="store_true", help="Check the read-only /models endpoint")
    args = parser.parse_args()
    config, key = load_config(args.config.resolve())
    available = None
    if args.online:
        request = urllib.request.Request(
            config["base_url"].rstrip("/") + "/models",
            headers={"Authorization": "Bearer " + key},
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.load(response)
        except urllib.error.HTTPError as error:
            raise RuntimeError(f"DeepSeek API returned HTTP {error.code}") from error
        available = config["model"] in {item.get("id") for item in payload.get("data", [])}
        if not available:
            raise RuntimeError(f"configured model is unavailable: {config['model']}")
    print(json.dumps({
        "provider": config["provider"],
        "base_url": config["base_url"],
        "model": config["model"],
        "key_loaded": True,
        "online_checked": args.online,
        "model_available": available,
    }, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, separators=(",", ":")))
        raise SystemExit(1)
