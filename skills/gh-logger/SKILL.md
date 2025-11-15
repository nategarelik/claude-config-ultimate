---
description: Use when you need to log decisions, track progress, or create audit trails via GitHub Copilot CLI - provides comprehensive session logging and history tracking
allowed-tools: [Bash, Read, Write]
---

# GitHub Copilot CLI Logger Skill

## Purpose

This skill provides comprehensive logging capabilities through GitHub Copilot CLI integration, enabling:

- Session logging and audit trails
- Decision tracking and rationale documentation
- Progress tracking across sessions
- Historical context retrieval
- Integration with gh CLI for team visibility

## When to Use

Activate this skill when:
- User explicitly requests logging or tracking
- You need to record important decisions
- Creating audit trails for compliance
- Documenting rationale for major changes
- Tracking progress across multiple sessions

## Core Capabilities

### 1. Session Logging

All sessions are automatically logged to `~/.claude/logs/` via the session-logger hook.

### 2. Manual Decision Logging

Use this skill to explicitly log important decisions:

```bash
gh copilot suggest "Log this decision: [your decision summary]"
```

### 3. Progress Tracking

```bash
# Log milestone completion
gh copilot suggest "Claude Code milestone: Completed authentication system"

# Log blockers
gh copilot suggest "Claude Code blocker: Waiting for API key from team"
```

### 4. Query Historical Logs

```bash
# Search logs
grep "decision" ~/.claude/logs/*.jsonl

# View recent session
tail -20 ~/.claude/logs/session-$(date +%Y-%m-%d)-*.jsonl
```

## Integration with episodic-memory

This skill complements episodic-memory by providing:
- Structured logging format (JSONL)
- GH CLI integration for team visibility
- Real-time session tracking
- Tool usage audit trails

## Usage Examples

### Example 1: Log Architecture Decision

```bash
gh copilot suggest "Architecture decision: Using PostgreSQL for user data storage. Rationale: ACID compliance, team expertise, existing infrastructure"
```

### Example 2: Track Implementation Progress

```bash
gh copilot suggest "Progress: Completed 3/5 API endpoints. Remaining: payment webhook, admin dashboard"
```

### Example 3: Document Debugging Session

```bash
gh copilot suggest "Debug session result: Memory leak in WebSocket handler. Fixed by adding cleanup in disconnect handler. Verified with load test."
```

## Log Structure

Each log entry follows this schema:

```json
{
  "timestamp": "2025-11-06T20:15:30.123Z",
  "event_type": "tool_use|session_start|session_end",
  "session_id": "abc123",
  "data": {
    "tool": "Read",
    "input": "file.ts",
    "output": "..."
  }
}
```

## Best Practices

1. **Be Specific**: Include context, rationale, and outcomes
2. **Use Consistent Format**: Prefix with decision type (Architecture, Implementation, Debug, etc.)
3. **Reference Issues**: Include issue/PR numbers when relevant
4. **Track Time**: Log start/end of major work sessions
5. **Document Failures**: Failed approaches are valuable learning

## Configuration

The logger is configured via `~/.claude/settings.json` hooks:

- **SessionStart**: Logs session initialization
- **SessionEnd**: Logs session completion
- **PostToolUse**: Logs every tool invocation
- **UserPromptSubmit**: Can log user prompts (disabled by default for privacy)

## Privacy Considerations

- Logs are stored locally only
- GH Copilot integration is optional
- No sensitive data is logged by default
- You control what gets explicitly logged via gh commands

## Troubleshooting

**Logs not appearing?**
- Check `~/.claude/logs/` directory exists
- Verify hooks are enabled in settings.json
- Check Python is available in PATH

**GH CLI integration failing?**
- Verify gh CLI installed: `gh --version`
- Authenticate: `gh auth login`
- Test: `gh copilot suggest "test"`

**Logs too verbose?**
- Edit `~/.claude/hooks/session-logger.py`
- Comment out `PostToolUse` hook in settings.json
- Adjust log level or filtering

## Advanced Usage

### Custom Log Queries

```bash
# Find all debugging sessions
jq 'select(.event_type == "tool_use" and .data.tool == "Bash")' ~/.claude/logs/*.jsonl

# Count tool usage
jq -r '.data.tool' ~/.claude/logs/*.jsonl | sort | uniq -c

# Extract decisions
grep -i "decision" ~/.claude/logs/*.jsonl | jq .
```

### Integration with Project Management

```bash
# Create GitHub issue from log
gh issue create --title "$(tail -1 log.jsonl | jq -r '.data')" --body "Logged decision"

# Update project tracking
gh project item-add [PROJECT_ID] --url [ISSUE_URL]
```

## Related Skills

- **episodic-memory:remembering-conversations** - Long-term memory across sessions
- **superpowers:systematic-debugging** - Structured debugging with logging
- **superpowers:verification-before-completion** - Evidence-based completion with logs

## Notes

This skill is always active via hooks but can be explicitly invoked for:
- Custom logging beyond automated tracking
- Team communication via gh CLI
- Historical analysis and reporting
- Decision documentation for stakeholders
