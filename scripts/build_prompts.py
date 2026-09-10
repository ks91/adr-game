#!/usr/bin/env python3
"""Build self-contained distribution prompts; --check detects stale outputs."""

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.1"


def render():
    core = (ROOT / "prompts/core.md").read_text(encoding="utf-8").strip()
    single = (ROOT / "prompts/single-player.md").read_text(encoding="utf-8").strip()
    multi = (ROOT / "prompts/multi-player.md").read_text(encoding="utf-8").strip()
    return {
        "AGENT_INSTALL.md": (
            f"<!-- prompt-agent-version: {VERSION} -->\n"
            f"# ADR Currency Serious Game v1.0\n\n{core}\n\n{single}\n"
        ),
        "sg-adr-game.md": (
            "# ADR Currency Serious Game v1.0\n\n"
            "```agent\n"
            "id: sg-adr-game\n"
            "name: ADR Currency Serious Game\n"
            "provider: openai_responses\n"
            "model: gpt-5.6-luna\n"
            "description: Multiplayer ADR currency and orbital debris simulation v1.0\n"
            "enabled: true\n"
            "public_instructions: true\n"
            "tools:\n"
            "  web_search: false\n"
            "  code_execution: true\n"
            f"```\n\n{core}\n\n{multi}\n"
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for name, content in render().items():
        path = ROOT / name
        expected = content.encode("utf-8")
        if args.check:
            if not path.exists() or path.read_bytes() != expected:
                stale.append(name)
        else:
            path.write_bytes(expected)
            print(f"Built {name}")
    if stale:
        parser.exit(1, "Stale prompts: " + ", ".join(stale) + "\n")
    if args.check:
        print("Distribution prompts match their sources.")


if __name__ == "__main__":
    main()
