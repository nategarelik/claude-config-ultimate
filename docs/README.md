# Claude Code Ultimate Configuration

**Your complete, production-ready Claude Code setup** - combining Spec-Kit workflow, Superpowers quality gates, auto-activation, comprehensive logging, and zero-friction permissions.

## What You Have

This configuration provides:

- **✅ Full auto-approval** - Zero permission prompts, maximum speed
- **🎯 Auto-activating skills** - Skills suggest themselves based on context
- **📊 Comprehensive logging** - All sessions tracked via GH Copilot CLI
- **🔄 Spec-Kit workflow** - Constitution→Specify→Plan→Tasks→Implement
- **🛡️ Superpowers quality gates** - TDD, systematic debugging, code review
- **📦 Repomix integration** - Fast codebase understanding
- **🧠 Episodic memory** - Persistent memory across sessions
- **🤖 85+ agents** - wshobson marketplace ready to use

## Directory Structure

```
~/.claude/
├── settings.json              # Main configuration (ACTIVE)
├── skill-rules.json           # Auto-activation patterns
├── hooks/
│   ├── session-logger.py      # Logs all sessions/tools
│   └── skill-activation.py    # Auto-suggests relevant skills
├── skills/
│   ├── gh-logger/             # GitHub Copilot CLI logging
│   ├── spec-kit-orchestrator/ # Workflow orchestration
│   └── repomix-analyzer/      # Codebase understanding
└── logs/                      # Session logs (JSONL format)
```

## Quick Start

### 1. Verify Installation

```bash
# Check configuration loaded
cat ~/.claude/settings.json

# Verify hooks exist
ls -la ~/.claude/hooks/

# Verify skills available
ls -la ~/.claude/skills/
```

### 2. Test Logging

```bash
# Start new Claude Code session
# Check logs being created
tail -f ~/.claude/logs/session-*.jsonl
```

### 3. Test Skill Auto-Activation

Try saying:
- "I found a bug..." → Should suggest `systematic-debugging`
- "Let's implement..." → Should suggest `test-driven-development`
- "Understand this codebase..." → Should suggest `repomix-analyzer`

### 4. Initialize Project with Spec-Kit

```bash
cd your-project
specify init your-project --ai claude

# This creates:
# .specify/memory/
# Slash commands: /speckit.constitution, /speckit.specify, etc.
```

## Core Workflows

### Workflow 1: New Feature Development

```bash
# 1. Start with episodic memory
"Remember how we implemented authentication last time"

# 2. Understand existing code
Use repomix-analyzer skill
"Show me existing API patterns"

# 3. Create specification
/speckit.specify
# Define: what, why, success criteria

# 4. Plan implementation
/speckit.plan
# Define: architecture, tech stack, tasks

# 5. Generate tasks
/speckit.tasks
# Breaks plan into implementable chunks

# 6. Implement with TDD
For each task:
  - Use test-driven-development skill
  - Write test first
  - Implement
  - Refactor

# 7. Code review
Use requesting-code-review skill
# Verify against spec and plan

# 8. Verify and merge
Use verification-before-completion skill
# Ensure all quality gates pass
```

### Workflow 2: Bug Fixing

```bash
# 1. Describe issue
"This endpoint is returning 500 errors"
# Auto-suggests: systematic-debugging skill

# 2. Use systematic debugging
Use systematic-debugging skill
# Four-phase: investigate → analyze → test → implement

# 3. Analyze codebase
Use repomix-analyzer skill
# Find all related code paths

# 4. Create fix with test
Use test-driven-development skill
# Reproduce bug in test
# Fix bug
# Verify test passes

# 5. Verify fix
Use verification-before-completion skill
# All tests pass
# No regressions
```

### Workflow 3: Codebase Exploration

```bash
# 1. Pack codebase
Use repomix-analyzer skill
"Pack this codebase and show me the structure"

# 2. Find patterns
"Show me all React components"
"Find authentication code"

# 3. Understand architecture
"Explain the data flow"
"What's the project structure?"

# 4. Document findings
Use gh-logger skill
gh copilot suggest "Architecture: [your summary]"
```

## Installed Plugins

### From Superpowers Marketplace

- **superpowers** - TDD, debugging, code review, planning
- **episodic-memory** - Persistent memory across sessions
- **superpowers-developing-for-claude-code** - Plugin development
- **superpowers-lab** - Experimental features (tmux, etc.)

### From Repomix

- **repomix-mcp** - MCP server for code packing
- **repomix-explorer** - Codebase exploration agent
- **repomix-commands** - Pack local/remote repos

### From wshobson (Optional - Install as Needed)

- **agents@wshobson** - 85+ specialized agents available
- Install specific plugins: `/plugin install <plugin>@wshobson`

## Custom Skills

### 1. gh-logger

**Auto-activates when**: "log", "track", "record"

**Provides**:
- Session logging via hooks (automatic)
- Manual decision logging via gh CLI
- JSONL audit trail in `~/.claude/logs/`
- Team visibility through GH Copilot integration

**Usage**:
```bash
gh copilot suggest "Decision: Using PostgreSQL. Rationale: ACID compliance"
```

### 2. spec-kit-orchestrator

**Auto-activates when**: "plan", "specification", "design", "new feature"

**Provides**:
- 5-phase workflow (Constitution→Specify→Plan→Tasks→Implement)
- Integration with Superpowers quality gates
- Automatic documentation generation
- Team collaboration via clear specs

**Usage**:
```bash
/speckit.specify  # Start specification
/speckit.plan     # Create technical plan
/speckit.tasks    # Generate task checklist
```

### 3. repomix-analyzer

**Auto-activates when**: "codebase", "understand", "explore", "analyze"

**Provides**:
- Fast codebase packing and analysis
- Pattern search and discovery
- Metrics and insights
- Pre-planning research

**Usage**:
```bash
"Pack this codebase"
"Find all API endpoints"
"Show me the authentication code"
```

## Configuration Details

### Permissions: Full Auto-Approval

```json
"permissions": {
  "defaultMode": "bypassPermissions"
}
```

**Result**: Claude can read, write, edit, and execute anything without prompts.

**Safety**: Hooks log all operations to `~/.claude/logs/` for audit trail.

### Hooks: Comprehensive Tracking

**SessionStart**: Logs session initiation
**SessionEnd**: Logs session completion
**UserPromptSubmit**: Suggests relevant skills
**PostToolUse**: Logs every tool invocation

**Log format**: JSONL (JSON Lines) for easy parsing

### Sandbox: Disabled

```json
"sandbox": {
  "enabled": false,
  "allowUnsandboxedCommands": true
}
```

**Result**: Maximum performance, no restrictions.

**Consideration**: Ensure you trust the code Claude writes. All operations logged.

### Model: Latest Sonnet

```json
"model": "claude-sonnet-4-5-20250929"
```

With `alwaysThinkingEnabled: true` for extended reasoning.

### Output Style: Concise

```json
"outputStyle": "Concise"
```

Optimized for terminal display, less verbose.

## Auto-Activation Rules

Skills automatically suggest themselves based on:

| Context | Activated Skills |
|---------|------------------|
| "bug", "error", "failing" | systematic-debugging (priority 10) |
| "implement", "add feature" | test-driven-development (priority 9) |
| "review", "completed" | code-reviewer (priority 8) |
| "remember", "previous" | remembering-conversations (priority 10) |
| "plan", "specification" | spec-kit-orchestrator (priority 9) |
| "codebase", "understand" | repomix-analyzer (priority 8) |
| "log", "track" | gh-logger (priority 5) |
| "design", "approach" | brainstorming (priority 9) |

**Edit rules**: `~/.claude/skill-rules.json`

## Logging System

### Automatic Logging

All sessions logged to: `~/.claude/logs/session-YYYY-MM-DD-{session-id}.jsonl`

Each log entry:
```json
{
  "timestamp": "2025-11-06T20:15:30Z",
  "event_type": "tool_use",
  "session_id": "abc123",
  "data": {
    "tool": "Read",
    "input": "file.ts"
  }
}
```

### Query Logs

```bash
# View today's sessions
ls ~/.claude/logs/session-$(date +%Y-%m-%d)-*.jsonl

# Search for decisions
grep "decision" ~/.claude/logs/*.jsonl

# Count tool usage
jq -r '.data.tool' ~/.claude/logs/*.jsonl | sort | uniq -c

# View recent activity
tail -20 ~/.claude/logs/session-*.jsonl | jq .
```

### Manual Logging via GH CLI

```bash
# Log decisions
gh copilot suggest "Decision: [summary and rationale]"

# Track progress
gh copilot suggest "Progress: Completed X/Y tasks"

# Document debugging
gh copilot suggest "Debug: Found issue in X, fixed by Y"
```

## Extending the Configuration

### Add New Skills

1. Create directory: `~/.claude/skills/your-skill/`
2. Create file: `SKILL.md` with frontmatter:

```markdown
---
description: When to use this skill
allowed-tools: [Read, Write, Bash]
---

# Your Skill

## Purpose
...
```

3. Add activation rule to `~/.claude/skill-rules.json`:

```json
{
  "skill": "your-skill",
  "priority": 8,
  "keywords": ["trigger", "words"],
  "file_patterns": [".ext"],
  "reason": "Why this skill is relevant"
}
```

### Add New Hooks

1. Create Python script in `~/.claude/hooks/your-hook.py`
2. Make it accept stdin (JSON from Claude)
3. Output JSON to stdout
4. Add to `settings.json`:

```json
"hooks": {
  "PreToolUse": [
    {
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "python ~/.claude/hooks/your-hook.py",
        "timeout": 5
      }]
    }
  ]
}
```

### Add Project-Specific Config

Create `.claude/settings.json` in your project:

```json
{
  "env": {
    "PROJECT_SPECIFIC_VAR": "value"
  },
  "hooks": {
    "SessionStart": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "cat .specify/memory/constitution.md"
      }]
    }]
  }
}
```

## Troubleshooting

### Hooks Not Running

```bash
# Check hooks enabled
jq '.disableAllHooks' ~/.claude/settings.json
# Should be: false

# Check hook files exist
ls -la ~/.claude/hooks/

# Check Python available
python --version

# Test hook manually
echo '{}' | python ~/.claude/hooks/session-logger.py start
```

### Skills Not Auto-Activating

```bash
# Check skill-rules.json exists
cat ~/.claude/skill-rules.json

# Verify skill directories exist
ls -la ~/.claude/skills/

# Check SKILL.md files present
find ~/.claude/skills/ -name "SKILL.md"

# Test activation hook
echo '{"prompt": "I found a bug"}' | python ~/.claude/hooks/skill-activation.py
```

### Logs Not Appearing

```bash
# Check log directory exists
ls -la ~/.claude/logs/

# Check permissions
chmod +w ~/.claude/logs/

# Verify SESSION_ID set
echo $CLAUDE_SESSION_ID

# Test logger manually
python ~/.claude/hooks/session-logger.py start
```

### Permissions Still Prompting

Your `settings.json` has `"defaultMode": "bypassPermissions"` which should eliminate all prompts.

If still seeing prompts:
1. Check no project-level override in `.claude/settings.json`
2. Verify no managed policy overriding (enterprise)
3. Restart Claude Code session

## Best Practices

### 1. Start Every Session with Memory

```bash
"Remember what we worked on last session"
# Auto-activates episodic-memory skill
```

### 2. Use Spec-Kit for Complex Features

Don't jump to code - specify first:
```bash
/speckit.specify   # What and why
/speckit.plan      # How
/speckit.tasks     # Breakdown
# Then implement with TDD
```

### 3. Let Skills Auto-Activate

Don't force skills - use natural language:
- "I found a bug" → systematic-debugging activates
- "Let's implement X" → test-driven-development activates
- "Understand this code" → repomix-analyzer activates

### 4. Review After Logical Chunks

Don't wait until end:
```bash
# After each major component
Use requesting-code-review skill
```

### 5. Log Important Decisions

```bash
gh copilot suggest "Decision: [what] Rationale: [why]"
```

### 6. Verify Before Completing

```bash
# Before marking task done
Use verification-before-completion skill
# Runs tests, checks coverage, verifies success
```

## Performance Optimization

### For Large Codebases

```json
// Use Repomix compression
{
  "compress": true,
  "includePatterns": "src/**",
  "ignorePatterns": "**/*.test.*,**/dist/**"
}
```

### For Frequent Sessions

```json
// Increase cleanup retention
{
  "cleanupPeriodDays": 90
}
```

### For Team Collaboration

```bash
# Share configuration
cp ~/.claude/settings.json your-project/.claude/
git add .claude/settings.json
git commit -m "Add team Claude Code configuration"
```

## What Makes This Configuration Special

1. **Zero Friction** - Full auto-approval, no permission interruptions
2. **Self-Improving** - Skills suggest themselves, learning your patterns
3. **Audit Trail** - Every action logged for debugging and compliance
4. **Quality Gates** - TDD, code review, verification built into workflow
5. **Structured Workflow** - Spec-Kit prevents "vibe coding", enforces planning
6. **Codebase Intelligence** - Repomix provides fast understanding
7. **Persistent Memory** - Episodic memory across sessions
8. **Extensible** - Easy to add skills, hooks, and customizations

## Next Steps

### Immediate (Today)

1. ✅ Configuration installed
2. Test auto-activation: "I found a bug"
3. Initialize a project: `specify init project-name --ai claude`
4. Review logs: `tail ~/.claude/logs/session-*.jsonl`

### Short Term (This Week)

1. Create your first spec: `/speckit.specify`
2. Implement with TDD workflow
3. Add project-specific skills as needed
4. Customize skill-rules.json for your patterns

### Long Term

1. Install additional wshobson agents as needed
2. Create team-specific skills
3. Build custom hooks for your workflow
4. Share configuration with team
5. Consider adding Serena MCP for semantic code understanding

## Support and Resources

- **Claude Code Docs**: https://code.claude.com/docs
- **Superpowers**: https://github.com/obra/superpowers-marketplace
- **Spec-Kit**: https://github.com/github/spec-kit
- **Repomix**: https://github.com/yamadashy/repomix
- **wshobson Agents**: https://github.com/wshobson/agents

## Configuration Summary

| Aspect | Configuration | Result |
|--------|---------------|--------|
| **Permissions** | bypassPermissions | No prompts |
| **Sandbox** | Disabled | No restrictions |
| **Hooks** | 4 active hooks | Auto-logging, skill activation |
| **Skills** | 3 custom + superpowers | Auto-activating, workflow orchestration |
| **Plugins** | 7 enabled | Superpowers, Repomix, Memory |
| **Model** | Sonnet 4.5 | Latest, extended thinking |
| **Logging** | Comprehensive | JSONL, GH CLI integration |
| **Workflow** | Spec-Kit + Superpowers | Structured + Quality gates |

---

**You're ready to code with Claude at maximum capability.**

Try starting a new feature and watch the skills activate automatically!
