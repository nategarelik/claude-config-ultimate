# Installation Guide

## Quick Installation (Recommended)

### Method 1: Claude Code Marketplace (Easiest)

```bash
# Add the marketplace
/plugin marketplace add https://github.com/nategarelik/claude-config-ultimate.git

# Install the configuration
/plugin install ultimate-config@claude-config-ultimate
```

### Method 2: Direct Clone + Install Script

```bash
# Clone the repository
cd ~/.claude
git clone https://github.com/nategarelik/claude-config-ultimate.git

# Run installation script
cd claude-config-ultimate
bash install.sh

# Restart Claude Code
exit  # Then start new session
```

### Method 3: Manual Installation

See [Manual Installation](#manual-installation-advanced) below.

---

## Installation Methods Comparison

| Method | Difficulty | Time | Best For |
|--------|-----------|------|----------|
| Marketplace | ⭐ Easy | 1 min | Everyone |
| Script | ⭐⭐ Moderate | 3 min | Developers |
| Manual | ⭐⭐⭐ Advanced | 10 min | Customization |

---

## Method 1: Marketplace Installation (Detailed)

### Step 1: Add Marketplace

In Claude Code, run:
```bash
/plugin marketplace add https://github.com/nategarelik/claude-config-ultimate.git
```

You should see:
```
✅ Marketplace added: claude-config-ultimate
```

### Step 2: List Available Plugins

```bash
/plugin list claude-config-ultimate
```

Output:
```
Plugins from claude-config-ultimate:
  - ultimate-config (v2.1.0) - Complete production configuration
```

### Step 3: Install

```bash
/plugin install ultimate-config@claude-config-ultimate
```

The installer will:
1. ✅ Backup existing configuration
2. ✅ Copy hooks to `~/.claude/hooks/`
3. ✅ Copy skills to `~/.claude/skills/`
4. ✅ Merge settings into `~/.claude/settings.json`
5. ✅ Install skill rules
6. ✅ Copy documentation

### Step 4: Restart Claude Code

```bash
exit  # Exit current session
# Start new Claude Code session
```

### Step 5: Verify Installation

Try:
```
"I found a bug"
```

Should see:
```
Relevant skills detected:
- superpowers:systematic-debugging: Detected debugging context
```

✅ **Installation successful!**

---

## Method 2: Script Installation (Detailed)

### Prerequisites

- Python >= 3.8
- Git
- Bash (Git Bash on Windows)

### Step-by-Step

1. **Navigate to Claude config directory:**
   ```bash
   cd ~/.claude
   ```

2. **Clone repository:**
   ```bash
   git clone https://github.com/nategarelik/claude-config-ultimate.git
   ```

3. **Run installer:**
   ```bash
   cd claude-config-ultimate
   bash install.sh
   ```

4. **Follow prompts:**
   - Installer will backup existing config
   - Install hooks, skills, config
   - Merge settings.json (requires jq)

5. **Restart Claude Code:**
   ```bash
   exit  # Then start new session
   ```

### Installer Output

You should see:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Claude Code Ultimate Configuration Installer v2.1.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Installing to: /Users/you/.claude

➤ Creating backup...
  ✓ Backed up settings.json
  ✓ Backed up skill-rules.json
  ✓ Backup created at: ...

➤ Installing hooks...
  ✓ Installed session-logger.py
  ✓ Installed skill-activation.py
  ✓ Installed agent-orchestrator.py

➤ Installing skills...
  ✓ Installed gh-logger skill
  ✓ Installed spec-kit-orchestrator skill
  ✓ Installed repomix-analyzer skill
  ✓ Installed agent-orchestrator skill

➤ Merging configuration...
  ✓ Installed skill-rules.json
  ✓ Merged with existing settings.json

➤ Installing documentation...
  ✓ Copied documentation files

➤ Checking dependencies...
  ✓ Python 3.11.0 found
  ✓ Git found (optional - for status line)
  ℹ GitHub CLI not found (optional)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Installation Complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Manual Installation (Advanced)

### 1. Backup Existing Configuration

```bash
cd ~/.claude
mkdir -p backups
cp settings.json backups/settings-$(date +%Y%m%d).json
cp skill-rules.json backups/skill-rules-$(date +%Y%m%d).json
cp -r hooks backups/hooks-$(date +%Y%m%d)
```

### 2. Clone Repository

```bash
git clone https://github.com/nategarelik/claude-config-ultimate.git
cd claude-config-ultimate
```

### 3. Copy Hooks

```bash
cp hooks/*.py ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.py  # Unix only
```

### 4. Copy Skills

```bash
cp -r skills/* ~/.claude/skills/
```

### 5. Merge Configuration

**skill-rules.json:**
```bash
cp config/skill-rules.json ~/.claude/skill-rules.json
```

**settings.json:**

If you have jq:
```bash
# Replace placeholder
CLAUDE_HOME="$HOME/.claude"
sed "s|{{CLAUDE_HOME}}|$CLAUDE_HOME|g" config/settings-template.json > /tmp/settings-new.json

# Merge
jq -s '.[0] * .[1]' ~/.claude/settings.json /tmp/settings-new.json > ~/.claude/settings-merged.json
mv ~/.claude/settings-merged.json ~/.claude/settings.json
```

Without jq (manual merge):
- Open `config/settings-template.json`
- Copy sections to your `~/.claude/settings.json`
- Replace `{{CLAUDE_HOME}}` with your actual path

### 6. Copy Documentation

```bash
cp docs/*.md ~/.claude/
```

### 7. Restart Claude Code

```bash
exit  # Then start new session
```

---

## Post-Installation

### 1. Install Recommended Marketplaces (Optional)

```bash
/plugin marketplace add https://github.com/simonwisdom/superpowers.git
/plugin marketplace add https://github.com/yamadashy/repomix-mcp.git
```

### 2. Install Recommended Plugins (Optional)

```bash
/plugin install superpowers@superpowers-marketplace
/plugin install superpowers-developing-for-claude-code@superpowers-marketplace
/plugin install repomix-mcp@repomix
/plugin install repomix-explorer@repomix
```

### 3. Test Configuration

**Test skill auto-activation:**
```
"I found a bug"  → Should suggest systematic-debugging
"Let's plan"     → Should suggest spec-kit-orchestrator
"I need agents"  → Should suggest agent-orchestrator
```

**Check session logging:**
```bash
ls ~/.claude/logs/
# Should see session-*.jsonl files
```

**Verify hooks:**
```bash
ls -la ~/.claude/hooks/
# Should see 3 Python files
```

---

## Troubleshooting

### Issue: Hooks not executing

**Check:**
```bash
# Verify hooks exist
ls ~/.claude/hooks/*.py

# Test Python
python3 --version

# Check settings.json
jq '.hooks' ~/.claude/settings.json
```

**Fix:**
- Ensure Python >= 3.8 installed
- Verify hook paths in settings.json
- Check hook permissions (Unix: `chmod +x`)

### Issue: Skills not auto-activating

**Check:**
```bash
# Verify skill-rules.json
cat ~/.claude/skill-rules.json

# Test hook
echo '{"prompt": "I found a bug"}' | python3 ~/.claude/hooks/skill-activation.py
```

**Fix:**
- Ensure skill-rules.json exists
- Verify hook timeout values (5-10 seconds)
- Check Python can execute hooks

### Issue: Settings not merging

**Manual merge:**
1. Open `~/.claude/settings.json`
2. Open `config/settings-template.json`
3. Copy hook configurations
4. Replace `{{CLAUDE_HOME}}` with actual path
5. Save and restart

### Issue: Permission denied on hooks (Unix)

```bash
chmod +x ~/.claude/hooks/*.py
```

### Issue: jq not found

**Install jq:**
- macOS: `brew install jq`
- Ubuntu: `sudo apt install jq`
- Windows: Download from https://stedolan.github.io/jq/

Or merge settings.json manually.

---

## Rollback

If you need to rollback:

```bash
cd ~/.claude/backups

# Find your backup
ls -la

# Restore
cp settings-YYYYMMDD.json ../settings.json
cp skill-rules-YYYYMMDD.json ../skill-rules.json
cp -r hooks-YYYYMMDD ../hooks

# Restart Claude Code
```

---

## Verification Checklist

After installation, verify:

- [ ] `~/.claude/hooks/` contains 3 Python files
- [ ] `~/.claude/skills/` contains 4 skill directories
- [ ] `~/.claude/settings.json` has hooks configured
- [ ] `~/.claude/skill-rules.json` exists
- [ ] Python >= 3.8 available
- [ ] Session logging works (check `~/.claude/logs/`)
- [ ] Skill auto-activation works (test with "bug")
- [ ] Documentation copied to `~/.claude/`

---

## Next Steps

1. **Read documentation:**
   - Quick Start: `~/.claude/QUICK-START.md`
   - Full Docs: `~/.claude/COMPREHENSIVE-DOCUMENTATION.md`

2. **Customize:**
   - Edit `skill-rules.json` for keyword preferences
   - Adjust hook timeouts in `settings.json`
   - Add/remove plugins as needed

3. **Learn workflows:**
   - Spec-Kit: Constitution → Specify → Plan → Tasks → Implement
   - Superpowers: Brainstorm → TDD → Review → Verify
   - Repomix: Pack → Analyze → Understand

---

## Support

- **Issues:** https://github.com/nategarelik/claude-config-ultimate/issues
- **Documentation:** https://github.com/nategarelik/claude-config-ultimate
- **Discussions:** GitHub Discussions

---

**Installation Guide v2.1.0**
**Last Updated:** 2025-11-15
