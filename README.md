# Claude Code Ultimate Configuration

**Production-ready Claude Code configuration with intelligent automation, quality gates, and comprehensive tooling**

Version: 2.1.0 | [Installation](#installation) | [Documentation](#documentation) | [Features](#features)

---

## Overview

This is a complete, production-ready Claude Code configuration that provides:

- **🚀 Zero-friction permissions** - Auto-approve all operations, no prompts
- **🎯 Intelligent automation** - Skills auto-activate based on context
- **📝 Comprehensive logging** - All sessions tracked with GitHub Copilot CLI integration
- **🤖 Agent orchestration** - Automatic selection from 85+ specialized expert agents
- **🔄 Workflow integration** - Spec-Kit driven development with quality gates
- **🔍 Codebase analysis** - Repomix integration for fast understanding
- **🔒 Security hardened** - Sensitive data filtering, input validation, secure hooks
- **💻 Cross-platform** - Windows and Unix compatible

## Quick Start

### One-Line Installation

```bash
/plugin marketplace add https://github.com/nategarelik/claude-config-ultimate.git
/plugin install ultimate-config@claude-config-ultimate
```

### Manual Installation

1. **Clone the repository:**
   ```bash
   cd ~/.claude
   git clone https://github.com/nategarelik/claude-config-ultimate.git
   ```

2. **Run the installation script:**
   ```bash
   cd claude-config-ultimate
   bash install.sh
   ```

3. **Restart Claude Code:**
   ```bash
   # Exit current session
   # Start new Claude Code session
   ```

## Features

### 1. Zero-Friction Permissions

No more permission prompts! All operations auto-approved for maximum development speed.

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions"
  }
}
```

### 2. Intelligent Skill Auto-Activation

Skills automatically activate based on your prompt keywords and open files:

| Your Input | Auto-Activated Skill |
|------------|---------------------|
| "bug", "error", "broken" | `systematic-debugging` |
| "implement", "add feature" | `test-driven-development` |
| "review", "completed" | `code-reviewer` |
| "plan", "design" | `spec-kit-orchestrator` |
| "codebase", "explore" | `repomix-analyzer` |
| "select agents" | `agent-orchestrator` |

### 3. Comprehensive Session Logging

Every session, prompt, and tool usage logged to:
- Local JSONL files (`~/.claude/logs/`)
- GitHub Copilot CLI integration (optional)
- **Security:** Automatic filtering of passwords, API keys, tokens, secrets

```python
# Automatically redacts:
"password": "secret123"  →  "password": "[REDACTED]"
"api_key": "sk-abc123"   →  "api_key": "[REDACTED]"
```

### 4. Agent Orchestrator

Intelligently analyzes your project and recommends the perfect combination of agents from 85+ specialized experts:

- **Language Specialists:** Python, JavaScript, Rust, Java, Go, etc.
- **Domain Experts:** Backend, Frontend, Mobile, ML/AI, Blockchain
- **Infrastructure:** Kubernetes, Cloud, CI/CD, Deployment
- **Security:** OWASP, Compliance, API Security
- **Quality:** Testing, TDD, Performance, Code Review

**Example:**
```
User: "Build a React + Node.js web app with PostgreSQL"

Agent Orchestrator:
  ✅ frontend-expert (React/TypeScript)
  ✅ backend-expert (Node.js APIs)
  ✅ database-expert (PostgreSQL)
  ✅ security-expert (Auth, OWASP)

  Install these 4 agents? [Y/n]
```

### 5. Spec-Kit Workflow Integration

Systematic development workflow:

```
Constitution → Specify → **Agent Selection** → Plan → Tasks → Implement
```

**Commands:**
- `/speckit.constitution` - Define coding standards
- `/speckit.specify` - Write requirements
- `/speckit.plan` - Create technical design
- `/speckit.tasks` - Generate task breakdown

### 6. Repomix Codebase Analysis

Fast, token-efficient codebase understanding:

- Pack entire codebases for analysis
- Search patterns across all files
- Understand architecture quickly
- Pre-planning research

### 7. Superpowers Quality Gates

Integrated quality gates at every step:
- `superpowers:brainstorming` - Design exploration
- `superpowers:test-driven-development` - TDD workflow
- `superpowers:systematic-debugging` - Debug framework
- `superpowers:code-reviewer` - Quality verification
- `superpowers:verification-before-completion` - Final checks

## What's Included

### Hooks (3 Python scripts)

| Hook | Purpose | Triggers |
|------|---------|----------|
| `session-logger.py` | Session/tool logging | SessionStart, SessionEnd, PostToolUse |
| `skill-activation.py` | Auto-suggest skills | UserPromptSubmit |
| `agent-orchestrator.py` | Recommend agents | UserPromptSubmit (planning) |

**Security Features:**
- ✅ Sensitive data filtering (passwords, API keys, tokens)
- ✅ Input validation on all hook inputs
- ✅ Shell injection prevention
- ✅ Specific exception handling
- ✅ Cross-platform path handling

### Skills (4 custom)

| Skill | Purpose |
|-------|---------|
| `gh-logger` | GitHub Copilot CLI logging integration |
| `spec-kit-orchestrator` | Spec-driven workflow orchestration |
| `repomix-analyzer` | Codebase analysis with Repomix |
| `agent-orchestrator` | Intelligent agent selection |

### Configuration Files

- `settings.json` - Main Claude Code configuration
- `skill-rules.json` - Skill auto-activation rules (9 rules)

### Documentation (5 files)

- `README.md` - This file
- `QUICK-START.md` - 5-minute quick start guide
- `COMPREHENSIVE-DOCUMENTATION.md` - Complete technical reference
- `CONFIGURATION-SUMMARY.md` - Visual quick reference
- `IMPROVEMENTS-APPLIED.md` - Recent improvements changelog

## Configuration Details

### Enabled Plugins (7)

- `superpowers@superpowers-marketplace` - Quality gates, TDD, debugging
- `superpowers-developing-for-claude-code@superpowers-marketplace` - Dev tools
- `superpowers-lab@superpowers-marketplace` - Experimental features
- `superpowers-chrome@superpowers-marketplace` - Chrome DevTools integration
- `repomix-mcp@repomix` - MCP server for Repomix
- `repomix-explorer@repomix` - Interactive codebase exploration
- `repomix-commands@repomix` - Repomix slash commands

### MCP Servers (2)

- `memory` - Episodic memory across sessions
- `repomix-mcp` - Codebase packing and analysis

### Settings Highlights

```json
{
  "permissions": { "defaultMode": "bypassPermissions" },
  "model": "claude-sonnet-4-5-20250929",
  "enableAllProjectMcpServers": true,
  "outputStyle": "Concise",
  "sandbox": { "enabled": false },
  "cleanupPeriodDays": 90
}
```

## Installation Details

### Prerequisites

**Required:**
- Claude Code >= 1.0.0
- Python >= 3.8

**Optional:**
- `gh` CLI - For GitHub Copilot integration
- `git` - For status line and version control
- `npx` - For Repomix commands

### Installation Script

The `install.sh` script will:

1. ✅ Backup existing configuration
2. ✅ Copy hooks to `~/.claude/hooks/`
3. ✅ Copy skills to `~/.claude/skills/`
4. ✅ Merge settings into `~/.claude/settings.json`
5. ✅ Merge skill rules into `~/.claude/skill-rules.json`
6. ✅ Install required marketplaces
7. ✅ Install recommended plugins
8. ✅ Set proper permissions
9. ✅ Prompt for Claude Code restart

### Customization

After installation, you can customize:

**Disable specific hooks:**
```json
{
  "hooks": {
    "PostToolUse": []  // Disable tool logging
  }
}
```

**Adjust skill activation:**
Edit `~/.claude/skill-rules.json` to change keywords or priorities

**Change permissions:**
```json
{
  "permissions": {
    "defaultMode": "ask"  // Revert to permission prompts
  }
}
```

## Usage Examples

### Example 1: Starting a New Project

```
You: "Let's build a Python web API with FastAPI and PostgreSQL"

Claude: [skill-activation hook suggests: spec-kit-orchestrator]
Claude: [agent-orchestrator hook suggests: python-expert, backend-expert, database-expert]

Would you like me to:
1. Run /speckit.constitution to define standards
2. Install recommended agents (python-expert, backend-expert, database-expert)
```

### Example 2: Debugging an Issue

```
You: "There's a bug in the authentication flow - users can't login"

Claude: [skill-activation hook suggests: systematic-debugging]

I'll help debug this systematically. Let me:
1. Trace the authentication flow
2. Identify the root cause
3. Propose a fix
4. Verify with tests
```

### Example 3: Code Review

```
You: "I've completed the user registration feature"

Claude: [skill-activation hook suggests: code-reviewer]

Great! Let me review the implementation:
✅ Using superpowers:requesting-code-review skill
- Checking against requirements
- Verifying test coverage
- Validating edge cases
```

## Security & Privacy

### Data Protection

- ✅ **Sensitive data filtering** - Passwords, API keys, tokens automatically redacted
- ✅ **Local-only logging** - Logs stored in `~/.claude/logs/` only
- ✅ **No external tracking** - No analytics or telemetry
- ✅ **Input validation** - All hook inputs validated before processing
- ✅ **Shell injection prevention** - Secure subprocess handling

### Patterns Filtered

```regex
password, api_key, api-key, secret, token, authorization: bearer
```

All matched patterns replaced with `[REDACTED]` before logging.

## Troubleshooting

### Hooks not activating?

```bash
# Check hooks directory
ls -la ~/.claude/hooks/

# Verify Python available
python3 --version

# Check settings.json
jq '.hooks' ~/.claude/settings.json
```

### Skills not auto-activating?

```bash
# Verify skill-rules.json exists
cat ~/.claude/skill-rules.json

# Check skill-activation.py works
echo '{"prompt": "I found a bug"}' | python3 ~/.claude/hooks/skill-activation.py
```

### Logging not working?

```bash
# Check logs directory
ls -la ~/.claude/logs/

# Verify session-logger.py
python3 ~/.claude/hooks/session-logger.py start

# Check gh CLI (optional)
gh auth status
```

## Architecture

```
User Input
    │
    ▼
UserPromptSubmit Hooks
├─ skill-activation.py     → Suggests relevant skills
└─ agent-orchestrator.py   → Recommends agents
    │
    ▼
Claude Code Processing
├─ Superpowers (Quality Gates)
├─ Spec-Kit (Workflows)
├─ Repomix (Analysis)
├─ Memory (MCP)
└─ Agents (Specialists)
    │
    ▼
PostToolUse Hooks
└─ session-logger.py       → Logs all tools
    │
    ▼
Output + Logs
```

## Statistics

- **Total Files:** 1,812+
- **Configuration Files:** 2 core
- **Custom Hooks:** 3 Python scripts
- **Custom Skills:** 4 skills
- **Enabled Plugins:** 7
- **MCP Servers:** 2
- **Documentation:** 5 comprehensive docs
- **Lines of Code:** ~600 (hooks + skills)

## Version History

### 2.1.0 (2025-11-15) - Current

**Improvements:**
- ✅ Fixed critical variable collision in agent-orchestrator
- ✅ Added sensitive data filtering
- ✅ Fixed shell injection vulnerability
- ✅ Added Windows compatibility
- ✅ Improved file pattern matching
- ✅ Better error handling across all hooks
- ✅ Updated documentation for accuracy

See `IMPROVEMENTS-APPLIED.md` for complete changelog.

### 2.0.0 (2025-11-06)

**Added:**
- Agent orchestrator hook
- Complete system documentation
- All hooks tested and verified

### 1.0.0 (2025-11-06)

**Initial release:**
- Base configuration with auto-approval
- Auto-activating skills
- Session logging
- Spec-Kit integration

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

- **Issues:** https://github.com/nategarelik/claude-config-ultimate/issues
- **Documentation:** See included docs in repository
- **Discussions:** GitHub Discussions

## License

MIT License - See LICENSE file for details

## Acknowledgments

Built with and for:
- [Claude Code](https://code.claude.com/) by Anthropic
- [Superpowers](https://github.com/simonwisdom/superpowers) by Jesse Hallett
- [Repomix](https://github.com/yamadashy/repomix-mcp) by Yamada
- [Spec-Kit](https://github.com/spec-kit/spec-kit) for structured development

---

**Made with ❤️ for the Claude Code community**

**Repository:** https://github.com/nategarelik/claude-config-ultimate
**Version:** 2.1.0
**Last Updated:** 2025-11-15
