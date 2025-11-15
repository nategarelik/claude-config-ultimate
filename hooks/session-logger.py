#!/usr/bin/env python3
"""
Session Logger Hook for Claude Code
Logs all sessions, prompts, and tool usage via GitHub Copilot CLI integration
"""

import sys
import json
import os
import re
from datetime import datetime
from pathlib import Path

# Use environment variable or default to ~/.claude
CLAUDE_CONFIG_DIR = Path(os.getenv("CLAUDE_CONFIG_DIR", Path.home() / ".claude"))
LOG_DIR = Path(os.getenv("CLAUDE_SESSION_LOG_DIR", CLAUDE_CONFIG_DIR / "logs"))
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Sensitive data patterns to filter from logs
SENSITIVE_PATTERNS = [
    r'password["\s:=]+[^"\s]+',
    r'api[_-]?key["\s:=]+[^"\s]+',
    r'secret["\s:=]+[^"\s]+',
    r'token["\s:=]+[^"\s]+',
    r'authorization:\s*bearer\s+\S+',
]

def filter_sensitive_data(text):
    """Remove sensitive data from text before logging"""
    if not isinstance(text, str):
        text = str(text)

    for pattern in SENSITIVE_PATTERNS:
        text = re.sub(pattern, '[REDACTED]', text, flags=re.IGNORECASE)

    return text

def get_session_file():
    """Get or create session log file"""
    session_id = os.getenv("CLAUDE_SESSION_ID", "unknown")
    date_str = datetime.now().strftime("%Y-%m-%d")
    return LOG_DIR / f"session-{date_str}-{session_id}.jsonl"

def log_event(event_type, data=None):
    """Log an event to the session file"""
    try:
        log_file = get_session_file()

        # Filter sensitive data before logging
        filtered_data = {}
        if data:
            filtered_data = {
                k: filter_sensitive_data(v) if isinstance(v, (str, dict, list)) else v
                for k, v in data.items()
            }

        event = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "session_id": os.getenv("CLAUDE_SESSION_ID", "unknown"),
            "data": filtered_data
        }

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")

        # Also log to gh copilot if available
        try:
            import subprocess
            summary = filter_sensitive_data(
                f"[Claude] {event_type}: {json.dumps(filtered_data, indent=2)}"[:500]
            )
            # Use subprocess stdin to avoid shell injection
            subprocess.run(
                ["gh", "copilot", "suggest", "--"],
                input=f"{summary}\n# Claude Code Log",
                capture_output=True,
                timeout=2,
                text=True
            )
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            pass  # gh CLI not available or failed, continue silently

    except (IOError, OSError) as e:
        # Don't block Claude Code if logging fails
        sys.stderr.write(f"Logging error: {e}\n")
    except Exception as e:
        # Unexpected error
        sys.stderr.write(f"Unexpected logging error: {e}\n")

def main():
    """Main hook entry point"""
    if len(sys.argv) < 2:
        sys.exit(0)

    command = sys.argv[1]

    # Read hook input from stdin if available
    hook_data = {}
    try:
        if not sys.stdin.isatty():
            hook_input = sys.stdin.read()
            if hook_input:
                hook_data = json.loads(hook_input)
    except (json.JSONDecodeError, ValueError) as e:
        sys.stderr.write(f"Failed to parse hook input: {e}\n")

    if command == "start":
        # Windows uses USERNAME, Unix uses USER
        username = os.getenv("USERNAME", os.getenv("USER", "unknown"))
        log_event("session_start", {
            "cwd": os.getcwd(),
            "user": username
        })

    elif command == "end":
        log_event("session_end", {
            "cwd": os.getcwd()
        })

    elif command == "log-tool":
        tool_name = hook_data.get("toolName", "unknown")
        log_event("tool_use", {
            "tool": tool_name,
            "input": str(hook_data.get("input", {}))[:500]  # Truncate for size
        })

    # Always return success JSON for hooks
    print(json.dumps({"status": "success"}))
    sys.exit(0)

if __name__ == "__main__":
    main()
