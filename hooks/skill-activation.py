#!/usr/bin/env python3
"""
Skill Auto-Activation Hook for Claude Code
Analyzes user prompts and open files to suggest relevant skills
"""

import sys
import json
import os
from pathlib import Path
from fnmatch import fnmatch

# Use environment variable or default
CLAUDE_CONFIG_DIR = Path(os.getenv("CLAUDE_CONFIG_DIR", Path.home() / ".claude"))
SKILL_RULES_FILE = CLAUDE_CONFIG_DIR / "skill-rules.json"

def load_skill_rules():
    """Load skill activation rules"""
    if not SKILL_RULES_FILE.exists():
        return []

    try:
        with open(SKILL_RULES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Handle both {"rules": [...]} and [...] formats
            if isinstance(data, dict) and "rules" in data:
                return data["rules"]
            elif isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
        sys.stderr.write(f"Failed to load skill rules: {e}\n")
        return []
    except Exception as e:
        sys.stderr.write(f"Unexpected error loading skill rules: {e}\n")
        return []

def match_skill(prompt, files, rule):
    """Check if a skill rule matches the current context"""
    # Check prompt keywords
    keywords = rule.get("keywords", [])
    prompt_lower = prompt.lower()
    keyword_match = any(kw.lower() in prompt_lower for kw in keywords)

    # Check file patterns using proper glob matching
    file_patterns = rule.get("file_patterns", [])
    file_match = False
    for file_path in files:
        # Normalize path separators
        normalized_path = file_path.replace("\\", "/")
        for pattern in file_patterns:
            normalized_pattern = pattern.replace("\\", "/")
            # Match using fnmatch for glob patterns
            if fnmatch(normalized_path, f"*{normalized_pattern}*") or \
               fnmatch(normalized_path, normalized_pattern) or \
               normalized_path.endswith(normalized_pattern):
                file_match = True
                break
        if file_match:
            break

    # Return True if either keywords or files match
    return keyword_match or file_match

def main():
    """Main hook entry point"""
    try:
        # Read hook input from stdin
        hook_input = sys.stdin.read()
        if not hook_input:
            print(json.dumps({}))
            sys.exit(0)

        hook_data = json.loads(hook_input)
        prompt = hook_data.get("prompt", "")

        # Get open files from environment or hook data
        open_files = hook_data.get("openFiles", [])
        cwd = os.getcwd()

        # Load skill rules
        rules = load_skill_rules()

        # Find matching skills
        suggested_skills = []
        for rule in rules:
            if match_skill(prompt, open_files, rule):
                skill_name = rule.get("skill")
                priority = rule.get("priority", 5)
                suggested_skills.append({
                    "skill": skill_name,
                    "priority": priority,
                    "reason": rule.get("reason", f"Detected context for {skill_name}")
                })

        # Sort by priority (higher first) and limit to top 3
        suggested_skills.sort(key=lambda x: x["priority"], reverse=True)
        suggested_skills = suggested_skills[:3]

        # Build suggestion message
        if suggested_skills:
            suggestion_text = "\n\nRelevant skills detected:\n"
            for s in suggested_skills:
                suggestion_text += f"- {s['skill']}: {s['reason']}\n"

            # Return hook output with suggestion
            output = {
                "hookSpecificOutput": {
                    "additionalContext": suggestion_text
                }
            }
            print(json.dumps(output))
        else:
            print(json.dumps({}))

    except (json.JSONDecodeError, KeyError) as e:
        # Don't block on errors
        sys.stderr.write(f"Skill activation error: {e}\n")
        print(json.dumps({}))
    except Exception as e:
        # Unexpected error
        sys.stderr.write(f"Unexpected skill activation error: {e}\n")
        print(json.dumps({}))

    sys.exit(0)

if __name__ == "__main__":
    main()
