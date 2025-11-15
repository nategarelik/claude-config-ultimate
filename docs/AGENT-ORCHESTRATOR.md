# Agent Orchestrator - Complete Guide

## What Is This?

The **Agent Orchestrator** is an intelligent system that automatically:
1. Analyzes your project requirements when you start planning
2. Searches the entire wshobson/agents catalog (85+ expert agents)
3. Selects the perfect combination of specialists for your project
4. Installs them automatically
5. Prompts you to restart Claude Code (or does it automatically with confirmation)

## How It Works

### Automatic Activation

The orchestrator activates automatically when you say:
- "Let's **plan** a new project"
- "I want to **build** an application"
- "**Design** a system architecture"
- "**Create** a web app with..."
- "**Develop** a Python backend"
- Any planning/architecture discussion

### The Process

```
You: "Let's build a full-stack web app with React, Node.js, and PostgreSQL"
           ↓
[Agent Orchestrator Hook Activates]
           ↓
Analyzes: React → frontend-expert
         Node.js → javascript-expert, backend-expert
         PostgreSQL → database-expert
         Web app → security-expert (always recommended)
           ↓
Displays recommendation:
🤖 Agent Orchestrator Analysis

Detected project requirements:
languages, domains, data, security

📦 Recommended Agents (4):
1. frontend-expert - React, Vue, UI/UX, responsive design
2. backend-expert - Backend APIs, microservices, server architecture
3. database-expert - Schema design, optimization, SQL/NoSQL
4. security-expert - OWASP, vulnerability scanning, secure coding

💡 Token overhead: ~2600 tokens

Would you like me to:
1. Install these agents automatically
2. Customize the selection
3. Skip agent orchestration
           ↓
You: "1" (Install automatically)
           ↓
Orchestrator: Installing agents...
/plugin install frontend-expert@wshobson
/plugin install backend-expert@wshobson
/plugin install database-expert@wshobson
/plugin install security-expert@wshobson
           ↓
✅ Agents installed
📝 Updated ~/.claude/settings.json
📋 Created ~/.claude/AGENT-GUIDE.md
           ↓
🔄 Restart Claude Code now? [Y/n]: Y
           ↓
[Session ends, prompts restart]
           ↓
[New session starts with agents active]
           ↓
You can now use: /frontend-expert, /backend-expert, etc.
```

## The Intelligence

### Requirements Detection

The orchestrator understands:

**Languages:**
- Python, JavaScript/TypeScript, Java/Kotlin, Rust, C/C++, Go
- Bash, PowerShell, Haskell, Elixir
- Embedded/IoT languages

**Domains:**
- Frontend (React, Vue, Angular)
- Backend (APIs, microservices)
- Mobile (React Native, Flutter)
- AI/ML (LLMs, RAG, MLOps)
- Blockchain/DeFi/Web3
- Gaming, Finance, SEO

**Infrastructure:**
- Kubernetes, Docker, CI/CD
- AWS, Azure, GCP
- Terraform, IaC

**Data:**
- PostgreSQL, MySQL, MongoDB
- ETL pipelines, data lakes
- Schema design, migrations

**Security:**
- Authentication, authorization
- OWASP, vulnerability scanning
- Compliance (GDPR, SOC2)
- Mobile security

**Quality:**
- Testing, TDD
- Code review
- Performance optimization

### Smart Selection Algorithm

```
Score = (Language Match × 40%) +
        (Domain Match × 30%) +
        (Infrastructure × 15%) +
        (Security Needs × 10%) +
        (Special Features × 5%)

Top 6 agents selected by score
Conflicts removed (overlapping capabilities)
Token budget verified (~650 tokens per agent)
```

### Intelligent Recommendations

**Lightweight Projects** (2-3 agents):
- Simple apps, scripts, prototypes
- Example: Python script → python-expert, scripting-expert

**Medium Projects** (4-5 agents):
- Production web apps, APIs
- Example: REST API → backend-expert, database-expert, security-expert, testing-expert

**Complex Projects** (6+ agents):
- Microservices, ML pipelines, enterprise systems
- Example: ML platform → python-expert, llm-expert, mlops-expert, kubernetes-expert, data-engineering-expert, operations-expert

## Available Agents (85+)

### Development Experts
- `backend-expert` - APIs, microservices, databases
- `frontend-expert` - React, Vue, UI/UX
- `debugging-expert` - Complex debugging, profiling
- `multi-platform-expert` - Mobile, cross-platform

### Language Specialists
- `python-expert` - Python, Django, Flask
- `javascript-expert` - JS/TS, Node.js, React
- `jvm-expert` - Java, Kotlin, Scala
- `systems-expert` - C/C++, Rust, Go
- `scripting-expert` - Bash, PowerShell
- `functional-expert` - Haskell, Elixir
- `embedded-expert` - IoT, firmware

### Infrastructure & DevOps
- `kubernetes-expert` - K8s, Helm, orchestration
- `cloud-expert` - AWS/Azure/GCP
- `deployment-expert` - CI/CD, releases
- `infrastructure-expert` - Terraform, IaC
- `cicd-expert` - GitHub Actions, Jenkins

### Security Specialists
- `security-expert` - OWASP, pentesting
- `compliance-expert` - GDPR, SOC2
- `api-security-expert` - API auth, rate limiting
- `mobile-security-expert` - Mobile app security

### AI & ML
- `llm-expert` - LangChain, RAG, prompts
- `agent-expert` - Multi-agent orchestration
- `context-expert` - Vector DB, memory systems
- `mlops-expert` - ML pipelines, deployment

### Data & Database
- `database-expert` - Schema design, SQL/NoSQL
- `migration-expert` - Database migrations
- `data-engineering-expert` - ETL, data lakes
- `data-validation-expert` - Schema validation

### Quality & Testing
- `testing-expert` - Unit/integration tests
- `tdd-expert` - Test-driven development
- `code-review-expert` - Code quality
- `quality-expert` - Static analysis
- `performance-expert` - Optimization, profiling

### Operations
- `operations-expert` - Incident response, monitoring
- `diagnostics-expert` - Debugging, troubleshooting

### Specialized Domains
- `blockchain-expert` - Smart contracts, DeFi
- `finance-expert` - Quantitative trading
- `payments-expert` - Stripe, PayPal, billing
- `seo-expert` - SEO content, optimization
- `analytics-expert` - Business intelligence
- `gaming-expert` - Game development

[See full catalog: https://github.com/wshobson/agents]

## Usage Examples

### Example 1: React + Node.js Web App

```
You: "Build a web app with React frontend and Node.js backend"

Orchestrator recommends:
- frontend-expert (React)
- javascript-expert (Node.js)
- backend-expert (APIs)
- security-expert (Always)

Result: 4 agents, ~2600 tokens
```

### Example 2: Python ML Pipeline

```
You: "Create an ML pipeline with LLMs and vector database"

Orchestrator recommends:
- python-expert (Python)
- llm-expert (LLMs, RAG)
- context-expert (Vector DB)
- mlops-expert (Pipelines)
- data-engineering-expert (Data processing)

Result: 5 agents, ~3250 tokens
```

### Example 3: Microservices on Kubernetes

```
You: "Design microservices architecture deployed on Kubernetes"

Orchestrator recommends:
- backend-expert (Microservices)
- kubernetes-expert (K8s)
- deployment-expert (CI/CD)
- operations-expert (Monitoring)
- security-expert (Security)

Result: 5 agents, ~3250 tokens
```

### Example 4: Mobile App with Payments

```
You: "Create iOS/Android app with payment integration"

Orchestrator recommends:
- multi-platform-expert (Mobile)
- payments-expert (Stripe/PayPal)
- mobile-security-expert (Security)
- backend-expert (API for payments)

Result: 4 agents, ~2600 tokens
```

## Integration with Spec-Kit

**Optimal workflow:**

```
1. /speckit.constitution
   Define project standards, coding practices

2. /speckit.specify
   Define requirements: "Build web app with React, Node, PostgreSQL"

3. [AGENT ORCHESTRATOR ACTIVATES]
   Automatically analyzes spec
   Recommends: frontend-expert, backend-expert, database-expert, security-expert
   Installs agents

4. Restart Claude Code
   New session with expert team ready

5. /speckit.plan
   Create technical plan WITH agents providing expertise
   /frontend-expert helps with React architecture
   /backend-expert helps with API design
   /database-expert helps with schema

6. /speckit.tasks
   Generate task breakdown
   Agents help identify specialized tasks

7. Implementation
   Use agents for each specialized task:
   - /frontend-expert "Create responsive navbar"
   - /backend-expert "Design user authentication API"
   - /database-expert "Optimize user query performance"
```

## Token Budget Management

### Understanding Overhead

Each agent adds ~500-800 tokens of context:
- Agent description and capabilities
- Available commands
- Configuration

**Estimates:**
- 2 agents = ~1300 tokens
- 4 agents = ~2600 tokens
- 6 agents = ~3900 tokens

### Budget Recommendations

**Tight budget (<100k tokens):**
- Install 2-3 core agents
- Use Superpowers for general tasks
- Add specialists only when needed

**Medium budget (100-150k tokens):**
- Install 4-5 agents
- Cover main project areas
- Balance core + specialists

**Large budget (>150k tokens):**
- Install 6+ agents
- Full expert team
- Maximum capability

### Optimization Strategies

1. **Phased Installation**
   - Start with core 2-3 agents
   - Add specialists during implementation

2. **Project-Specific**
   - Install agents per project
   - Different projects = different agents

3. **Remove Unused**
   - Uninstall agents not actively used
   - Keep configuration in git for re-install

## Manual Control

### Skip Auto-Installation

```
Orchestrator: Would you like me to:
1. Install these agents automatically
2. Customize the selection
3. Skip agent orchestration

You: 3 (Skip)

Result: Continue without agents, use Superpowers only
```

### Customize Selection

```
Orchestrator: Recommended agents: A, B, C, D

You: 2 (Customize)

Orchestrator: Which agents to install?
- [ ] A
- [ ] B
- [x] C
- [x] D

You: Just C and D

Result: Installs only selected agents
```

### Manual Installation Later

```bash
# Install specific agent manually
/plugin install backend-expert@wshobson

# Or use script
~/.claude/scripts/install-agents.sh backend-expert database-expert
```

## Troubleshooting

### Orchestrator Not Activating

**Check:** Skill rules configured
```bash
cat ~/.claude/skill-rules.json | grep agent-orchestrator
```

**Fix:** Should see agent-orchestrator rule with priority 10

### Installation Failing

**Check:** Plugin marketplace accessible
```bash
/plugin list wshobson
```

**Fix:** Verify network, marketplace configuration

### Agents Not Working After Restart

**Check:** Agents in settings.json
```bash
jq '.enabledPlugins' ~/.claude/settings.json
```

**Fix:** Should show `"agent-name@wshobson": true`

### Too Many Agents Suggested

**Solution:** Choose option 2 (Customize) and deselect some

### Token Budget Exceeded

**Solution:** Install core agents only, skip specialists

## Advanced Usage

### Team Configuration

Share agent configuration with team:

```bash
# Add agents to project settings
cat > .claude/settings.json <<EOF
{
  "enabledPlugins": {
    "backend-expert@wshobson": true,
    "database-expert@wshobson": true,
    "security-expert@wshobson": true
  }
}
EOF

git add .claude/settings.json
git commit -m "Configure project agents"
git push
```

Team members automatically get same agents when they trust the folder.

### Incremental Agent Addition

Start small, add later:

```
Session 1: Install backend-expert, database-expert
        ↓
Implement core API
        ↓
Session 2: Need payment integration
        ↓
Say: "Add payment integration"
        ↓
Orchestrator: Recommends payments-expert
        ↓
Install payments-expert
        ↓
Continue with full team
```

### Agent Replacement

Switch technologies:

```
Current: Express.js → backend-expert configured for Express
Change: Switch to FastAPI
        ↓
Orchestrator detects change
        ↓
Recommends: python-expert + reconfigure backend-expert
        ↓
Updates configuration
        ↓
Restart with new setup
```

## Files Created

After orchestration, you'll have:

```
~/.claude/
├── settings.json          ← Updated with new agents
├── AGENT-GUIDE.md         ← Reference guide for installed agents
├── hooks/
│   └── agent-orchestrator.py  ← The orchestrator hook
├── skills/
│   └── agent-orchestrator/
│       └── SKILL.md       ← This skill
└── scripts/
    └── install-agents.sh  ← Manual installer script
```

## Best Practices

1. **Let It Run Automatically**
   - Don't skip orchestration
   - Trust the recommendations
   - Customize only if needed

2. **Install Before Planning**
   - Spec → Agents → Plan (correct)
   - Not: Spec → Plan → Agents (wrong)

3. **Start Conservative**
   - Install 2-4 core agents
   - Add specialists incrementally
   - Monitor token usage

4. **Use Agent Guide**
   - Read `~/.claude/AGENT-GUIDE.md`
   - Learn agent capabilities
   - Know when to invoke each

5. **Share with Team**
   - Commit `.claude/settings.json`
   - Everyone gets same agents
   - Consistent development environment

## Summary

The Agent Orchestrator is your **project intelligence**:

- ✅ **Automatic** - Activates during planning
- 🧠 **Intelligent** - Analyzes 85+ agents, picks perfect combination
- 📦 **Effortless** - One confirmation, handles rest
- 🔄 **Seamless** - Prompts restart when ready
- 👥 **Team-Ready** - Share configuration via git
- 📊 **Budget-Aware** - Optimizes for token constraints

**You never have to:**
- Browse agent catalog manually
- Guess which agents to use
- Install agents one by one
- Configure settings manually
- Remember to restart

**The orchestrator:**
- Analyzes your requirements automatically
- Selects optimal agents intelligently
- Installs everything automatically
- Prepares perfect development environment
- Prompts restart at right time

**Result:** You start planning with the perfect expert team already assembled.

---

**Next Steps:**
1. Start a new project: "Let's build a web app with..."
2. Watch orchestrator activate and recommend agents
3. Confirm installation
4. Restart Claude Code
5. Continue with expert team ready

**Welcome to orchestrated development! 🤖**
