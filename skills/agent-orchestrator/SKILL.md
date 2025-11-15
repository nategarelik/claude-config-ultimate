---
description: ALWAYS USE WHEN PLANNING - Automatically analyzes project requirements and intelligently selects the perfect agents from wshobson/agents marketplace (85+ specialized experts), installs them, and prepares your development environment with the optimal toolset
allowed-tools: [Bash, Read, Write, Edit, WebFetch, Grep, Glob, Task, AskUserQuestion]
---

# Intelligent Agent Orchestrator

## Purpose

This skill is your **project planning intelligence layer**. It automatically:

1. **Analyzes** your project requirements, tech stack, and architecture
2. **Searches** the entire wshobson/agents catalog (85+ agents, 63 plugins)
3. **Selects** the perfect combination of specialized agents for your specific needs
4. **Installs** them automatically via `/plugin install`
5. **Prepares** your environment for optimal development
6. **Prompts restart** when ready (or restarts automatically with confirmation)

## When to Use

**ALWAYS USE** when:
- Starting new project planning (before `/speckit.plan`)
- User says "plan", "design", "architecture", "build", "create project"
- Beginning spec-kit workflow (right after `/speckit.specify`)
- Switching to new tech stack or domain
- Need specialized expertise for complex implementation

**Auto-activates** via skill-rules.json when planning detected.

## How It Works

### Phase 1: Requirements Analysis

Analyzes your project to determine:
- **Tech stack**: Languages, frameworks, databases
- **Domain**: Web app, API, ML, blockchain, mobile, etc.
- **Infrastructure**: Cloud provider, CI/CD, containerization
- **Security needs**: Authentication, compliance, vulnerability scanning
- **Special requirements**: Performance, testing, documentation

### Phase 2: Intelligent Agent Selection

Searches wshobson catalog and selects optimal agents from:

**Development Agents:**
- `backend-expert` - Backend APIs, microservices, databases
- `frontend-expert` - React, Vue, UI/UX, responsive design
- `debugging-expert` - Complex bug investigation, profiling
- `multi-platform-expert` - Cross-platform development

**Language Specialists:**
- `python-expert` - Python, Django, Flask, data science
- `javascript-expert` - JS/TS, Node.js, React, Vue
- `systems-expert` - C/C++, Rust, low-level programming
- `jvm-expert` - Java, Kotlin, Scala, Spring
- `scripting-expert` - Bash, PowerShell, automation
- `functional-expert` - Haskell, Elixir, functional patterns
- `embedded-expert` - IoT, firmware, hardware integration

**Infrastructure & DevOps:**
- `deployment-expert` - CI/CD, releases, rollbacks
- `kubernetes-expert` - K8s, Helm, orchestration
- `cloud-expert` - AWS/Azure/GCP architecture
- `infrastructure-expert` - Terraform, IaC, provisioning
- `cicd-expert` - GitHub Actions, Jenkins, pipelines

**Security:**
- `security-expert` - Vulnerability scanning, OWASP, pentesting
- `compliance-expert` - GDPR, SOC2, security audits
- `api-security-expert` - API authentication, rate limiting
- `mobile-security-expert` - Mobile app security, MASVS

**AI & ML:**
- `llm-expert` - LangChain, RAG, prompt engineering
- `agent-expert` - Multi-agent orchestration, workflows
- `context-expert` - Context management, memory systems
- `mlops-expert` - ML pipelines, model deployment

**Testing & Quality:**
- `testing-expert` - Unit/integration testing, TDD
- `tdd-expert` - Test-driven development workflows
- `code-review-expert` - Code quality, best practices
- `quality-expert` - Static analysis, linting, standards
- `performance-expert` - Profiling, optimization, benchmarking

**Data & Database:**
- `database-expert` - Schema design, optimization, indexing
- `migration-expert` - Database migrations, data modeling
- `data-engineering-expert` - ETL pipelines, data lakes
- `data-validation-expert` - Schema validation, data quality

**Specialized Domains:**
- `blockchain-expert` - Smart contracts, DeFi, Web3
- `finance-expert` - Quantitative trading, risk management
- `payments-expert` - Stripe, PayPal, billing systems
- `seo-expert` - SEO content, technical optimization
- `analytics-expert` - Business intelligence, metrics
- `operations-expert` - Incident response, on-call, diagnostics

### Phase 3: Smart Installation Strategy

**Intelligent Batching:**
- Groups related agents (e.g., `backend-expert` + `database-expert` + `api-security-expert`)
- Installs in optimal order (infrastructure → core → specialized)
- Minimizes restarts (batch installs, single restart)

**Conflict Detection:**
- Checks for overlapping capabilities
- Warns if too many agents (token budget)
- Suggests alternatives if conflicts found

**Token Budget Awareness:**
- Estimates token overhead per agent
- Recommends core agents + 2-3 specialists max
- Offers lightweight alternatives for large projects

### Phase 4: Installation Execution

Automatically executes:

```bash
# For each selected agent/plugin:
/plugin install backend-expert@wshobson
/plugin install database-expert@wshobson
/plugin install security-expert@wshobson
# ... etc

# Updates project settings
# Adds to .claude/settings.json for team sharing
```

### Phase 5: Environment Preparation

Prepares your project:
- ✅ Updates `.claude/settings.json` with new plugins
- ✅ Creates project-specific skill rules
- ✅ Generates agent usage guide
- ✅ Sets up constitution with agent recommendations
- ✅ Configures optimal tool permissions

### Phase 6: Smart Restart

**Option A - Automatic (with confirmation):**
```
📦 Installed 3 agents: backend-expert, database-expert, security-expert
🔄 Ready to restart Claude Code to activate agents

Restart now? [Y/n]: _
```

**Option B - Manual prompt:**
```
✅ All agents installed successfully!

To activate new agents, please restart Claude Code:
- Exit this session (Ctrl+D or 'exit')
- Start new Claude Code session
- Agents will be available immediately

Would you like me to prepare a restart command? [Y/n]: _
```

## Usage Examples

### Example 1: Web Application

**User input:**
```
"Let's build a full-stack web app with React frontend, Node.js backend, PostgreSQL database, and deploy to AWS"
```

**Orchestrator analysis:**
```
📊 Project Analysis:
- Frontend: React, TypeScript
- Backend: Node.js, Express
- Database: PostgreSQL
- Cloud: AWS
- Security: Authentication, API security

🤖 Recommended Agents (5):
1. frontend-expert - React/TypeScript UI development
2. backend-expert - Node.js API architecture
3. database-expert - PostgreSQL schema design
4. cloud-expert - AWS deployment strategy
5. security-expert - Auth, API security, OWASP

📦 Installation Plan:
- Core: frontend-expert, backend-expert (restart 1)
- Supporting: database-expert, cloud-expert, security-expert (restart 2)

Optimize to single restart? [Y/n]: Y

🔄 Installing all 5 agents...
✅ Installed: frontend-expert@wshobson
✅ Installed: backend-expert@wshobson
✅ Installed: database-expert@wshobson
✅ Installed: cloud-expert@wshobson
✅ Installed: security-expert@wshobson

📝 Updated .claude/settings.json
🎯 Created project agent guide
📋 Ready to restart

Restart Claude Code now? [Y/n]: _
```

### Example 2: Machine Learning Pipeline

**User input:**
```
"Design an ML pipeline for training and deploying LLM-based chatbot with RAG, using Python, LangChain, vector DB, and Kubernetes deployment"
```

**Orchestrator analysis:**
```
📊 Project Analysis:
- Language: Python
- Domain: ML, LLMs, RAG
- Infrastructure: Kubernetes
- Data: Vector database
- DevOps: ML pipelines, deployment

🤖 Recommended Agents (6):
1. python-expert - Python development
2. llm-expert - LangChain, RAG, prompt engineering
3. context-expert - Vector DB, memory systems
4. mlops-expert - ML pipeline deployment
5. kubernetes-expert - K8s orchestration
6. data-engineering-expert - Data pipelines

⚠️ Token Budget Warning:
6 agents = ~3500 tokens overhead

Options:
A. Install all 6 (recommended for complex ML projects)
B. Install core 4: python-expert, llm-expert, mlops-expert, kubernetes-expert
C. Custom selection

Choice [A/B/C]: A

🔄 Installing 6 agents...
[... installation output ...]

✅ All agents installed
📝 Project configuration updated
🎯 Agent usage guide: .claude/AGENT-GUIDE.md

Restart to activate? [Y/n]: _
```

### Example 3: Mobile App with Backend

**User input:**
```
"Create a mobile app (iOS/Android) with real-time chat, push notifications, and payment integration"
```

**Orchestrator analysis:**
```
📊 Project Analysis:
- Platform: Mobile (cross-platform)
- Features: Real-time, payments
- Backend: API, WebSocket
- Infrastructure: Push notifications, payment gateway

🤖 Recommended Agents (5):
1. multi-platform-expert - React Native/Flutter
2. backend-expert - API + WebSocket server
3. mobile-security-expert - Mobile app security
4. payments-expert - Stripe/PayPal integration
5. operations-expert - Monitoring, incident response

💡 Alternative lightweight approach:
- Core: multi-platform-expert, backend-expert
- Use built-in Superpowers for: security, payments guidance

Choose approach:
A. Full agent suite (5 agents)
B. Lightweight (2 core agents)

Choice [A/B]: B

🔄 Installing core agents...
✅ Installed: multi-platform-expert@wshobson
✅ Installed: backend-expert@wshobson

📋 Note: For payments/security, using:
- superpowers:systematic-debugging (built-in)
- Security best practices from constitution

Restart now? [Y/n]: _
```

## Integration with Spec-Kit Workflow

**Optimal timing:**

```
Constitution → Specify → **AGENT ORCHESTRATOR** → Plan → Tasks → Implement
                                    ↓
                         Installs perfect agents
                         Before technical planning
```

**Why here?**
- After requirements defined (Specify)
- Before technical decisions (Plan)
- Agents available for entire implementation

**Workflow:**

```bash
# 1. Define what you're building
/speckit.specify
# Output: Requirements, constraints, success criteria

# 2. AUTOMATICALLY TRIGGERS: agent-orchestrator skill
# Analyzes requirements → Selects agents → Installs → Prepares restart

# 3. Restart Claude Code
# New session with perfect agent team

# 4. Create technical plan (with agents available)
/speckit.plan
# Agents provide specialized expertise during planning

# 5. Generate tasks
/speckit.tasks
# Agents help break down into specialized tasks

# 6. Implement with expert agents
# Each task uses relevant specialist agent
```

## Smart Selection Logic

### Priority Matrix

The orchestrator uses weighted scoring:

| Factor | Weight | Examples |
|--------|--------|----------|
| **Language match** | 40% | Python project → python-expert |
| **Domain match** | 30% | ML project → llm-expert, mlops-expert |
| **Infrastructure** | 15% | K8s deployment → kubernetes-expert |
| **Security needs** | 10% | Auth required → security-expert |
| **Special features** | 5% | Payments → payments-expert |

### Selection Algorithm

```python
def select_agents(requirements):
    candidates = analyze_catalog()

    # Score each agent
    for agent in candidates:
        score = 0
        score += language_match(agent, requirements) * 0.40
        score += domain_match(agent, requirements) * 0.30
        score += infrastructure_match(agent, requirements) * 0.15
        score += security_match(agent, requirements) * 0.10
        score += feature_match(agent, requirements) * 0.05

        agent.score = score

    # Select top N agents
    selected = top_agents(candidates, max=6)

    # Check for conflicts/overlap
    selected = remove_conflicts(selected)

    # Verify token budget
    if estimate_tokens(selected) > budget:
        selected = optimize_for_budget(selected)

    return selected
```

### Conflict Resolution

**Overlapping capabilities:**
- `backend-expert` + `api-security-expert` → Keep both (complementary)
- `python-expert` + `scripting-expert` → Keep python-expert (more specific)
- `testing-expert` + `tdd-expert` → Keep tdd-expert (superset)

**Token budget exceeded:**
1. Prioritize by score
2. Offer lightweight alternatives
3. Suggest phased installation (install more later)

## Configuration

### Auto-Activation Rule

Already added to `~/.claude/skill-rules.json`:

```json
{
  "skill": "agent-orchestrator",
  "priority": 10,
  "keywords": ["plan", "build", "create", "design", "architecture", "new project"],
  "file_patterns": [".specify/", "spec.md"],
  "reason": "Project planning detected - agent orchestration recommended"
}
```

### Settings Integration

The orchestrator automatically updates `.claude/settings.json`:

```json
{
  "enabledPlugins": {
    "superpowers@superpowers-marketplace": true,
    "backend-expert@wshobson": true,
    "database-expert@wshobson": true,
    "security-expert@wshobson": true
  },
  "pluginConfigs": {
    "backend-expert@wshobson": {
      "preferredFramework": "express",
      "language": "typescript"
    }
  }
}
```

### Project-Level Agent Guide

Creates `.claude/AGENT-GUIDE.md`:

```markdown
# Project Agents

## Installed Agents

### backend-expert
**Use for:** API design, database integration, backend architecture
**Invoke:** `/backend-expert <task>`
**Skills:** REST APIs, GraphQL, microservices, authentication

### database-expert
**Use for:** Schema design, migrations, query optimization
**Invoke:** `/database-expert <task>`
**Skills:** PostgreSQL, schema modeling, indexing, performance

### security-expert
**Use for:** Security review, vulnerability scanning, auth implementation
**Invoke:** `/security-expert <task>`
**Skills:** OWASP, penetration testing, secure coding, compliance

## Usage Examples

### Design API endpoint
`/backend-expert Design RESTful API for user management with CRUD operations`

### Optimize query
`/database-expert Optimize this query for user search with pagination`

### Security review
`/security-expert Review authentication implementation for vulnerabilities`
```

## Advanced Features

### Incremental Agent Addition

After initial setup, add more agents:

```
"I need to add payment integration"

Agent Orchestrator: Analyzing new requirement...
Recommended: payments-expert@wshobson

Install now? [Y/n]: Y
```

### Agent Replacement

```
"Switch from Express to FastAPI"

Agent Orchestrator: Detected framework change
- Current: backend-expert (configured for Express)
- New recommendation: python-expert + backend-expert (reconfigure for FastAPI)

Update configuration? [Y/n]: Y
```

### Team Sharing

Automatically commits agent configuration:

```bash
git add .claude/settings.json
git add .claude/AGENT-GUIDE.md
git commit -m "Add project agents: backend, database, security"
git push

# Team members auto-install when they trust the folder
```

## Best Practices

### 1. Let It Run Before Planning

❌ **Don't:**
```
/speckit.specify
/speckit.plan  # No agents selected yet!
```

✅ **Do:**
```
/speckit.specify
# Wait for agent-orchestrator to activate
# Install recommended agents
# Restart Claude Code
/speckit.plan  # Now with perfect agent team
```

### 2. Trust the Recommendations

The orchestrator analyzes:
- 85+ available agents
- Your specific requirements
- Token budget constraints
- Capability overlaps
- Industry best practices

Unless you have specific needs, accept the recommendations.

### 3. Install Core Agents First

Start with 2-4 core agents:
- Language specialist (python, javascript, etc.)
- Domain expert (backend, frontend, ml, etc.)
- Security expert (always recommended)

Add specialists later as needed.

### 4. Review Generated Guide

After installation, read `.claude/AGENT-GUIDE.md`:
- Learn agent capabilities
- Understand when to use each
- See example invocations
- Note configuration options

### 5. Share with Team

Commit `.claude/settings.json`:
- Team gets same agents
- Consistent development environment
- Knowledge sharing built-in

## Troubleshooting

### "Too many agents selected"

**Problem:** Orchestrator suggests 8+ agents, token overhead too high
**Solution:**
1. Choose "optimize for budget" option
2. Install core 2-3 agents now
3. Add specialists later as needed

### "Agent not activating after restart"

**Problem:** Installed agent but can't invoke
**Check:**
```bash
# Verify installation
jq '.enabledPlugins' ~/.claude/settings.json

# Should show:
# "agent-name@wshobson": true
```

**Fix:** Run `/plugin install <agent>@wshobson` again

### "Orchestrator not activating during planning"

**Problem:** Said "let's plan" but agent-orchestrator didn't activate
**Check:** `~/.claude/skill-rules.json` has agent-orchestrator rule
**Test:**
```bash
echo '{"prompt": "lets plan this project"}' | python ~/.claude/hooks/skill-activation.py
# Should suggest: agent-orchestrator
```

### "Installation failed"

**Problem:** `/plugin install` returned error
**Common causes:**
- Network issue (retry)
- Plugin name typo (check spelling)
- Marketplace not accessible (check wshobson marketplace config)

**Fix:**
```bash
# Verify marketplace accessible
/plugin list wshobson

# Retry installation
/plugin install <agent>@wshobson
```

## Token Budget Guidelines

### Lightweight (< 2000 tokens overhead)
- 2-3 core agents
- Ideal for: Simple apps, scripts, prototypes

### Medium (2000-4000 tokens)
- 4-5 specialized agents
- Ideal for: Production apps, APIs, web services

### Heavy (4000-6000 tokens)
- 6-8 expert agents
- Ideal for: Complex systems, ML pipelines, enterprise

**Recommendation:** Start lightweight, add specialists later.

## Related Skills

- **spec-kit-orchestrator** - Workflow orchestration (used after agent selection)
- **repomix-analyzer** - Codebase analysis (before agent selection)
- **superpowers:writing-plans** - Detailed planning (with agents available)
- **episodic-memory** - Remember agent selections for future projects

## Notes

This skill is **game-changing** because:

1. **Zero Manual Search** - No browsing wshobson catalog manually
2. **Intelligent Selection** - Analyzes 85+ agents, picks perfect combination
3. **Automatic Installation** - One confirmation, handles rest
4. **Optimized Environment** - Best possible toolset for your project
5. **Team Consistency** - Same agents for entire team
6. **Progressive Enhancement** - Start light, add specialists later

The orchestrator is your **AI architect** - it knows every available expert, understands your needs, and assembles the perfect team before you even start planning.

**Always let it run before technical planning.**
