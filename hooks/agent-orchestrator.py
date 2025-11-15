#!/usr/bin/env python3
"""
Intelligent Agent Orchestrator Hook
Analyzes projects and automatically selects/installs optimal agents from wshobson marketplace
"""

import sys
import json
import os
import re
from pathlib import Path

# Agent catalog - maps capabilities to wshobson agents
AGENT_CATALOG = {
    "languages": {
        "python": ["python-expert"],
        "javascript": ["javascript-expert"],
        "typescript": ["javascript-expert"],
        "java": ["jvm-expert"],
        "kotlin": ["jvm-expert"],
        "scala": ["jvm-expert"],
        "rust": ["systems-expert"],
        "c": ["systems-expert"],
        "cpp": ["systems-expert"],
        "go": ["systems-expert"],
        "bash": ["scripting-expert"],
        "powershell": ["scripting-expert"],
        "haskell": ["functional-expert"],
        "elixir": ["functional-expert"],
        "embedded": ["embedded-expert"]
    },
    "domains": {
        "backend": ["backend-expert"],
        "frontend": ["frontend-expert"],
        "api": ["backend-expert"],
        "web": ["frontend-expert", "backend-expert"],
        "mobile": ["multi-platform-expert"],
        "ml": ["llm-expert", "mlops-expert"],
        "ai": ["llm-expert", "agent-expert"],
        "llm": ["llm-expert", "context-expert"],
        "blockchain": ["blockchain-expert"],
        "defi": ["blockchain-expert"],
        "web3": ["blockchain-expert"],
        "fintech": ["finance-expert", "payments-expert"],
        "trading": ["finance-expert"],
        "payments": ["payments-expert"],
        "seo": ["seo-expert"],
        "analytics": ["analytics-expert"],
        "gaming": ["gaming-expert"]
    },
    "infrastructure": {
        "kubernetes": ["kubernetes-expert"],
        "k8s": ["kubernetes-expert"],
        "docker": ["deployment-expert"],
        "cicd": ["cicd-expert"],
        "ci/cd": ["cicd-expert"],
        "aws": ["cloud-expert"],
        "azure": ["cloud-expert"],
        "gcp": ["cloud-expert"],
        "cloud": ["cloud-expert"],
        "terraform": ["infrastructure-expert"],
        "deployment": ["deployment-expert"]
    },
    "data": {
        "database": ["database-expert"],
        "postgres": ["database-expert"],
        "mysql": ["database-expert"],
        "mongodb": ["database-expert"],
        "sql": ["database-expert"],
        "migration": ["migration-expert"],
        "etl": ["data-engineering-expert"],
        "pipeline": ["data-engineering-expert"],
        "data": ["data-engineering-expert", "data-validation-expert"]
    },
    "security": {
        "security": ["security-expert"],
        "auth": ["security-expert", "api-security-expert"],
        "authentication": ["security-expert"],
        "compliance": ["compliance-expert"],
        "gdpr": ["compliance-expert"],
        "vulnerability": ["security-expert"],
        "mobile-security": ["mobile-security-expert"]
    },
    "quality": {
        "testing": ["testing-expert"],
        "tdd": ["tdd-expert"],
        "test": ["testing-expert"],
        "quality": ["quality-expert"],
        "review": ["code-review-expert"],
        "performance": ["performance-expert"],
        "optimization": ["performance-expert"]
    },
    "operations": {
        "monitoring": ["operations-expert"],
        "incident": ["operations-expert"],
        "debugging": ["debugging-expert"],
        "diagnostics": ["operations-expert"],
        "observability": ["operations-expert"]
    }
}

# Agent descriptions for user display
AGENT_INFO = {
    "python-expert": "Python development, Django, Flask, data science",
    "javascript-expert": "JS/TS, Node.js, React, Vue, modern frameworks",
    "jvm-expert": "Java, Kotlin, Scala, Spring ecosystem",
    "systems-expert": "C/C++, Rust, Go, low-level programming",
    "scripting-expert": "Bash, PowerShell, automation scripts",
    "functional-expert": "Haskell, Elixir, functional programming",
    "embedded-expert": "IoT, firmware, hardware integration",
    "backend-expert": "Backend APIs, microservices, server architecture",
    "frontend-expert": "React, Vue, UI/UX, responsive design",
    "multi-platform-expert": "React Native, Flutter, cross-platform",
    "llm-expert": "LangChain, RAG, prompt engineering, LLMs",
    "agent-expert": "Multi-agent systems, orchestration",
    "context-expert": "Vector DB, memory systems, context management",
    "mlops-expert": "ML pipelines, model deployment, MLOps",
    "blockchain-expert": "Smart contracts, DeFi, Web3 protocols",
    "finance-expert": "Quantitative trading, risk management",
    "payments-expert": "Stripe, PayPal, billing integration",
    "kubernetes-expert": "K8s, Helm, container orchestration",
    "cloud-expert": "AWS/Azure/GCP architecture, cloud services",
    "deployment-expert": "CI/CD, releases, deployment automation",
    "infrastructure-expert": "Terraform, IaC, infrastructure provisioning",
    "cicd-expert": "GitHub Actions, Jenkins, CI/CD pipelines",
    "database-expert": "Schema design, optimization, SQL/NoSQL",
    "migration-expert": "Database migrations, data modeling",
    "data-engineering-expert": "ETL pipelines, data lakes, big data",
    "data-validation-expert": "Schema validation, data quality",
    "security-expert": "OWASP, vulnerability scanning, secure coding",
    "compliance-expert": "GDPR, SOC2, security compliance",
    "api-security-expert": "API auth, rate limiting, security",
    "mobile-security-expert": "Mobile app security, MASVS standards",
    "testing-expert": "Unit/integration testing, test automation",
    "tdd-expert": "Test-driven development workflows",
    "quality-expert": "Code quality, static analysis, standards",
    "code-review-expert": "Code review best practices, patterns",
    "performance-expert": "Profiling, optimization, benchmarking",
    "operations-expert": "Incident response, monitoring, on-call",
    "debugging-expert": "Complex debugging, profiling, diagnostics",
    "seo-expert": "SEO content, technical optimization",
    "analytics-expert": "Business intelligence, metrics, dashboards",
    "gaming-expert": "Game development, engines, multiplayer"
}

def analyze_requirements(text):
    """Extract project requirements from text"""
    text_lower = text.lower()

    detected = {
        "languages": set(),
        "domains": set(),
        "infrastructure": set(),
        "data": set(),
        "security": set(),
        "quality": set(),
        "operations": set()
    }

    # Check each category
    for category, keyword_dict in AGENT_CATALOG.items():
        for keyword, agents in keyword_dict.items():
            if keyword in text_lower:
                detected[category].update(agents)

    return detected

def score_agents(detected):
    """Score agents based on detected requirements"""
    scores = {}

    weights = {
        "languages": 0.40,
        "domains": 0.30,
        "infrastructure": 0.15,
        "data": 0.10,
        "security": 0.10,
        "quality": 0.05,
        "operations": 0.05
    }

    for category, agents in detected.items():
        weight = weights.get(category, 0.05)
        for agent in agents:
            scores[agent] = scores.get(agent, 0) + weight

    return scores

def select_top_agents(scores, max_agents=6):
    """Select top N agents by score"""
    sorted_agents = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [agent for agent, score in sorted_agents[:max_agents]]

def estimate_token_overhead(agents):
    """Estimate token overhead for agents"""
    # Rough estimate: 500-800 tokens per agent
    return len(agents) * 650

def generate_installation_plan(agents):
    """Generate installation commands"""
    commands = []
    for agent in agents:
        commands.append(f"/plugin install {agent}@wshobson")
    return commands

def generate_report(agents, requirements_text):
    """Generate analysis report for user"""
    report = {
        "analysis": {
            "requirements_detected": requirements_text[:200],
            "agents_recommended": len(agents),
            "estimated_token_overhead": estimate_token_overhead(agents)
        },
        "agents": [
            {
                "name": agent,
                "description": AGENT_INFO.get(agent, "Specialized expert agent"),
                "install_command": f"/plugin install {agent}@wshobson"
            }
            for agent in agents
        ],
        "next_steps": [
            "Review recommended agents above",
            "Confirm installation (agents will be installed automatically)",
            "Restart Claude Code when prompted",
            "Continue with /speckit.plan with expert agents available"
        ]
    }

    return report

def main():
    """Main orchestrator logic"""
    try:
        # Read stdin for hook data
        hook_input = sys.stdin.read()
        if not hook_input:
            print(json.dumps({}))
            sys.exit(0)

        hook_data = json.loads(hook_input)
        prompt = hook_data.get("prompt", "")

        # Check if this is a planning prompt (minimum length check)
        if len(prompt.strip()) < 20:
            print(json.dumps({}))
            sys.exit(0)

        planning_keywords = ["plan", "build", "create", "design", "architecture", "implement", "develop"]
        if not any(kw in prompt.lower() for kw in planning_keywords):
            print(json.dumps({}))
            sys.exit(0)

        # Analyze requirements
        detected = analyze_requirements(prompt)

        # Score and select agents
        scores = score_agents(detected)
        if not scores:
            # No agents recommended
            print(json.dumps({}))
            sys.exit(0)

        selected_agents = select_top_agents(scores, max_agents=6)

        # Generate report
        report = generate_report(selected_agents, prompt)

        # Build context message
        context_msg = f"""

🤖 **Agent Orchestrator Analysis**

Detected project requirements:
{', '.join([cat for cat, agents in detected.items() if agents])}

📦 Recommended Agents ({len(selected_agents)}):
"""
        for i, agent in enumerate(selected_agents, 1):
            desc = AGENT_INFO.get(agent, "Expert agent")
            context_msg += f"\n{i}. **{agent}** - {desc}"

        context_msg += f"""

💡 Token overhead: ~{estimate_token_overhead(selected_agents)} tokens

Would you like me to:
1. Install these agents automatically
2. Customize the selection
3. Skip agent orchestration

Note: After installation, you'll need to restart Claude Code to activate agents.
"""

        output = {
            "hookSpecificOutput": {
                "additionalContext": context_msg
            }
        }

        print(json.dumps(output))

    except (json.JSONDecodeError, KeyError, ValueError) as e:
        # Don't block on errors
        sys.stderr.write(f"Agent orchestrator error: {e}\n")
        print(json.dumps({}))
    except Exception as e:
        # Unexpected error - log but don't block
        sys.stderr.write(f"Agent orchestrator unexpected error: {e}\n")
        print(json.dumps({}))

    sys.exit(0)

if __name__ == "__main__":
    main()
