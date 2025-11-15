#!/usr/bin/env bash
#
# Claude Code Ultimate Configuration Installer
# Version: 2.1.0
#
# This script installs the complete Claude Code ultimate configuration including:
# - Hooks (session-logger, skill-activation, agent-orchestrator)
# - Skills (gh-logger, spec-kit-orchestrator, repomix-analyzer, agent-orchestrator)
# - Configuration (settings.json, skill-rules.json)
# - Documentation

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Determine Claude home directory
if [[ -n "$CLAUDE_CONFIG_DIR" ]]; then
    CLAUDE_HOME="$CLAUDE_CONFIG_DIR"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    CLAUDE_HOME="$USERPROFILE/.claude"
else
    CLAUDE_HOME="$HOME/.claude"
fi

# Convert to absolute path
CLAUDE_HOME=$(cd "$CLAUDE_HOME" 2>/dev/null && pwd || echo "$CLAUDE_HOME")

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Claude Code Ultimate Configuration Installer v2.1.0${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "Installing to: ${GREEN}$CLAUDE_HOME${NC}"
echo ""

# Backup existing configuration
backup_config() {
    echo -e "${YELLOW}➤ Creating backup...${NC}"
    BACKUP_DIR="$CLAUDE_HOME/backups/pre-ultimate-$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$BACKUP_DIR"

    if [[ -f "$CLAUDE_HOME/settings.json" ]]; then
        cp "$CLAUDE_HOME/settings.json" "$BACKUP_DIR/"
        echo -e "  ${GREEN}✓${NC} Backed up settings.json"
    fi

    if [[ -f "$CLAUDE_HOME/skill-rules.json" ]]; then
        cp "$CLAUDE_HOME/skill-rules.json" "$BACKUP_DIR/"
        echo -e "  ${GREEN}✓${NC} Backed up skill-rules.json"
    fi

    if [[ -d "$CLAUDE_HOME/hooks" ]]; then
        cp -r "$CLAUDE_HOME/hooks" "$BACKUP_DIR/"
        echo -e "  ${GREEN}✓${NC} Backed up hooks/"
    fi

    echo -e "  ${GREEN}✓${NC} Backup created at: $BACKUP_DIR"
    echo ""
}

# Install hooks
install_hooks() {
    echo -e "${YELLOW}➤ Installing hooks...${NC}"
    mkdir -p "$CLAUDE_HOME/hooks"

    cp "$SCRIPT_DIR/hooks/session-logger.py" "$CLAUDE_HOME/hooks/"
    echo -e "  ${GREEN}✓${NC} Installed session-logger.py"

    cp "$SCRIPT_DIR/hooks/skill-activation.py" "$CLAUDE_HOME/hooks/"
    echo -e "  ${GREEN}✓${NC} Installed skill-activation.py"

    cp "$SCRIPT_DIR/hooks/agent-orchestrator.py" "$CLAUDE_HOME/hooks/"
    echo -e "  ${GREEN}✓${NC} Installed agent-orchestrator.py"

    # Set executable permissions on Unix
    if [[ "$OSTYPE" != "msys" && "$OSTYPE" != "win32" ]]; then
        chmod +x "$CLAUDE_HOME/hooks"/*.py
        echo -e "  ${GREEN}✓${NC} Set executable permissions"
    fi

    echo ""
}

# Install skills
install_skills() {
    echo -e "${YELLOW}➤ Installing skills...${NC}"
    mkdir -p "$CLAUDE_HOME/skills"

    cp -r "$SCRIPT_DIR/skills/gh-logger" "$CLAUDE_HOME/skills/"
    echo -e "  ${GREEN}✓${NC} Installed gh-logger skill"

    cp -r "$SCRIPT_DIR/skills/spec-kit-orchestrator" "$CLAUDE_HOME/skills/"
    echo -e "  ${GREEN}✓${NC} Installed spec-kit-orchestrator skill"

    cp -r "$SCRIPT_DIR/skills/repomix-analyzer" "$CLAUDE_HOME/skills/"
    echo -e "  ${GREEN}✓${NC} Installed repomix-analyzer skill"

    cp -r "$SCRIPT_DIR/skills/agent-orchestrator" "$CLAUDE_HOME/skills/"
    echo -e "  ${GREEN}✓${NC} Installed agent-orchestrator skill"

    echo ""
}

# Merge configuration
merge_config() {
    echo -e "${YELLOW}➤ Merging configuration...${NC}"

    # Copy skill-rules.json
    cp "$SCRIPT_DIR/config/skill-rules.json" "$CLAUDE_HOME/skill-rules.json"
    echo -e "  ${GREEN}✓${NC} Installed skill-rules.json"

    # Merge settings.json (requires jq, or manual merge)
    if command -v jq &> /dev/null; then
        echo -e "  ${BLUE}ℹ${NC} Using jq to merge settings.json"

        # Replace {{CLAUDE_HOME}} placeholder
        ESCAPED_HOME=$(echo "$CLAUDE_HOME" | sed 's/[\/&]/\\&/g')
        sed "s|{{CLAUDE_HOME}}|$ESCAPED_HOME|g" "$SCRIPT_DIR/config/settings-template.json" > "/tmp/settings-merged.json"

        if [[ -f "$CLAUDE_HOME/settings.json" ]]; then
            # Merge with existing
            jq -s '.[0] * .[1]' "$CLAUDE_HOME/settings.json" "/tmp/settings-merged.json" > "/tmp/settings-final.json"
            mv "/tmp/settings-final.json" "$CLAUDE_HOME/settings.json"
            echo -e "  ${GREEN}✓${NC} Merged with existing settings.json"
        else
            # New installation
            mv "/tmp/settings-merged.json" "$CLAUDE_HOME/settings.json"
            echo -e "  ${GREEN}✓${NC} Created new settings.json"
        fi

        rm -f "/tmp/settings-merged.json" "/tmp/settings-final.json"
    else
        echo -e "  ${YELLOW}⚠${NC} jq not found - copying template only"
        echo -e "  ${YELLOW}⚠${NC} You may need to manually merge settings.json"

        ESCAPED_HOME=$(echo "$CLAUDE_HOME" | sed 's/[\/&]/\\&/g')
        sed "s|{{CLAUDE_HOME}}|$ESCAPED_HOME|g" "$SCRIPT_DIR/config/settings-template.json" > "$CLAUDE_HOME/settings-template.json"
        echo -e "  ${BLUE}ℹ${NC} Saved template to: $CLAUDE_HOME/settings-template.json"
    fi

    echo ""
}

# Copy documentation
install_docs() {
    echo -e "${YELLOW}➤ Installing documentation...${NC}"

    cp "$SCRIPT_DIR/docs"/*.md "$CLAUDE_HOME/" 2>/dev/null || true
    echo -e "  ${GREEN}✓${NC} Copied documentation files"

    echo ""
}

# Install dependencies
install_dependencies() {
    echo -e "${YELLOW}➤ Checking dependencies...${NC}"

    # Check Python
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        echo -e "  ${GREEN}✓${NC} Python $PYTHON_VERSION found"
    elif command -v python &> /dev/null; then
        PYTHON_VERSION=$(python --version | cut -d' ' -f2)
        echo -e "  ${GREEN}✓${NC} Python $PYTHON_VERSION found"
    else
        echo -e "  ${RED}✗${NC} Python not found (required for hooks)"
        echo -e "  ${YELLOW}⚠${NC} Please install Python >= 3.8"
    fi

    # Check git (optional)
    if command -v git &> /dev/null; then
        echo -e "  ${GREEN}✓${NC} Git found (optional - for status line)"
    else
        echo -e "  ${BLUE}ℹ${NC} Git not found (optional)"
    fi

    # Check gh CLI (optional)
    if command -v gh &> /dev/null; then
        echo -e "  ${GREEN}✓${NC} GitHub CLI found (optional - for logging)"
    else
        echo -e "  ${BLUE}ℹ${NC} GitHub CLI not found (optional)"
        echo -e "      Install: https://cli.github.com/"
    fi

    echo ""
}

# Show next steps
show_next_steps() {
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}  Installation Complete!${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${BLUE}Next Steps:${NC}"
    echo ""
    echo -e "  1. ${YELLOW}Restart Claude Code${NC}"
    echo -e "     Exit your current session and start a new one"
    echo ""
    echo -e "  2. ${YELLOW}Install recommended marketplaces${NC} (optional)"
    echo -e "     /plugin marketplace add https://github.com/simonwisdom/superpowers.git"
    echo -e "     /plugin marketplace add https://github.com/yamadashy/repomix-mcp.git"
    echo ""
    echo -e "  3. ${YELLOW}Install recommended plugins${NC} (optional)"
    echo -e "     /plugin install superpowers@superpowers-marketplace"
    echo -e "     /plugin install repomix-mcp@repomix"
    echo ""
    echo -e "  4. ${YELLOW}Test the configuration${NC}"
    echo -e "     Try: \"I found a bug\" → Should suggest systematic-debugging"
    echo -e "     Try: \"Let's plan\" → Should suggest spec-kit-orchestrator"
    echo ""
    echo -e "${BLUE}Documentation:${NC}"
    echo -e "  - Quick Start: $CLAUDE_HOME/QUICK-START.md"
    echo -e "  - Full Docs:   $CLAUDE_HOME/COMPREHENSIVE-DOCUMENTATION.md"
    echo -e "  - Changelog:   $CLAUDE_HOME/IMPROVEMENTS-APPLIED.md"
    echo ""
    echo -e "${BLUE}Support:${NC}"
    echo -e "  - Issues: https://github.com/nategarelik/claude-config-ultimate/issues"
    echo -e "  - Backup: $BACKUP_DIR"
    echo ""
}

# Main installation flow
main() {
    backup_config
    install_hooks
    install_skills
    merge_config
    install_docs
    install_dependencies
    show_next_steps
}

# Run installation
main
