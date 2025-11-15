---
description: Use when starting new features or major implementation work - orchestrates spec-driven development workflow (Constitution→Specify→Plan→Tasks→Implement) integrated with Superpowers quality gates
allowed-tools: [Bash, Read, Write, Edit, SlashCommand, Skill, Task]
---

# Spec-Kit Orchestrator Skill

## Purpose

This skill orchestrates the complete spec-driven development workflow, combining GitHub Spec-Kit's structured approach with Superpowers' quality gates (TDD, code review, systematic debugging).

## When to Use

Activate this skill when:
- Starting new features or major implementations
- User requests structured planning
- Working in projects with `.specify/` directory
- Need to break down complex work into tasks
- Want quality gates and verification throughout development

## Workflow Phases

### Phase 1: Constitution (Project Setup)

Establish development principles and standards.

```bash
# Initialize spec-kit in project
cd /path/to/project
specify init project-name --ai claude

# This creates:
# .specify/memory/constitution.md
# Slash commands: /speckit.constitution, /speckit.specify, etc.
```

**Constitution should include:**
- Coding standards
- Testing requirements
- Security policies
- Performance targets
- Documentation standards

### Phase 2: Specify (Requirements)

Define WHAT needs to be built and WHY.

**Use slash command:**
```
/speckit.specify
```

**This will prompt you to define:**
- Feature description and user stories
- Success criteria
- Constraints and assumptions
- Edge cases
- Non-functional requirements

**Output:** `.specify/memory/specs/feature-name.md`

**Superpowers Integration:** Use `superpowers:brainstorming` skill before finalizing spec to explore alternatives.

### Phase 3: Plan (Technical Design)

Define HOW to implement the specification.

**Use slash command:**
```
/speckit.plan
```

**This will guide you through:**
- Architecture decisions
- Tech stack selection
- Data models and schemas
- API contracts
- External dependencies
- Risk assessment

**Output:** `.specify/memory/plans/feature-name-plan.md`

**Superpowers Integration:** Use `superpowers:writing-plans` for detailed task breakdown.

### Phase 4: Tasks (Implementation Checklist)

Break plan into executable tasks.

**Use slash command:**
```
/speckit.tasks
```

**Creates checklist of:**
- [ ] Setup/infrastructure tasks
- [ ] Core implementation tasks
- [ ] Testing tasks
- [ ] Documentation tasks
- [ ] Verification tasks

**Output:** `.specify/memory/tasks/feature-name-tasks.md`

**Superpowers Integration:** Each task follows TDD workflow via `superpowers:test-driven-development`.

### Phase 5: Implement (Execution with Quality Gates)

Execute tasks with Superpowers quality gates.

**For each task:**

1. **Write Test First** (TDD)
   ```
   Use superpowers:test-driven-development skill
   - Write failing test
   - Implement minimum code to pass
   - Refactor
   ```

2. **Implement Feature**
   - Follow plan exactly
   - Document as you go
   - Handle edge cases from spec

3. **Code Review** (After Logical Chunk)
   ```
   Use superpowers:requesting-code-review skill
   - Verify against spec and plan
   - Check test coverage
   - Validate edge cases
   ```

4. **Debug If Needed**
   ```
   Use superpowers:systematic-debugging skill
   - Root cause analysis
   - Pattern identification
   - Fix verification
   ```

5. **Verify Completion**
   ```
   Use superpowers:verification-before-completion skill
   - All tests passing
   - Coverage thresholds met
   - Documentation complete
   ```

## Example End-to-End Workflow

```bash
# 1. Initialize project with spec-kit
cd my-app
specify init my-app --ai claude

# 2. Create constitution
/speckit.constitution
# Define: TDD mandatory, 80% coverage, TypeScript strict mode

# 3. Specify feature
/speckit.specify
# Feature: User authentication with OAuth
# Success: Users can login via Google/GitHub
# Constraints: GDPR compliant, <500ms response

# 4. Plan implementation
/speckit.plan
# Tech: Passport.js + JWT
# Data: Users table with oauth_provider field
# API: POST /auth/login, GET /auth/callback

# 5. Generate tasks
/speckit.tasks
# Output: 12 tasks covering setup → implementation → testing

# 6. Execute with quality gates
# Task 1: Setup Passport.js
Use superpowers:test-driven-development
# - Write test for /auth/login endpoint
# - Implement route
# - Pass test

# Task 2-11: Continue with TDD
# ...

# Task 12: Final verification
Use superpowers:verification-before-completion
# - All tests pass ✓
# - Coverage 85% ✓
# - Docs updated ✓

# 7. Request code review
Use superpowers:requesting-code-review
# Review against original spec and plan

# 8. Merge
Use superpowers:finishing-a-development-branch
# Create PR, merge, cleanup
```

## Integration with episodic-memory

The orchestrator automatically stores:
- Specifications in `.specify/memory/specs/`
- Plans in `.specify/memory/plans/`
- Tasks in `.specify/memory/tasks/`

Use `episodic-memory:remembering-conversations` to recall decisions made during specification phase.

## Repomix Integration

Before starting Phase 2 (Specify), use `repomix-analyzer` skill to:
- Understand existing codebase structure
- Identify similar patterns to follow
- Find related code that might be affected

```bash
# Analyze codebase before planning
Use repomix-analyzer skill
# "Show me authentication-related code"
# "What's the current architecture?"
```

## Configuration

**Project-Level Setup** (`.claude/settings.json`):

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "cat .specify/memory/constitution.md 2>/dev/null || echo 'No constitution yet'"
          }
        ]
      }
    ]
  }
}
```

This displays project constitution at session start as a reminder.

## Best Practices

1. **Always Start with Constitution**: Define standards before coding
2. **Spec First, Code Later**: Resist urge to jump to implementation
3. **Use Brainstorming**: Explore alternatives during Specify phase
4. **Detailed Plans**: More detail = better task breakdown
5. **Small Tasks**: Each task should be <2 hours of work
6. **TDD Everything**: Write test first for every task
7. **Review Per Chunk**: Don't wait until end for code review
8. **Update Spec if Needed**: Specifications can evolve during implementation
9. **Document Decisions**: Log why you deviated from plan

## Troubleshooting

**Spec-kit commands not available?**
- Run `specify init` in project root
- Verify `.specify/` directory exists
- Check slash commands with `/help`

**Tasks too vague?**
- Use `superpowers:writing-plans` for more detail
- Break tasks into subtasks
- Add acceptance criteria to each task

**Spec conflicts with plan?**
- Spec is source of truth
- Update plan to match spec
- If spec is wrong, update spec first, then plan

**Quality gates failing?**
- Review constitution requirements
- Check test coverage
- Verify against original spec

## Advanced Usage

### Custom Quality Gates

Add project-specific gates in constitution:

```markdown
## Quality Gates

1. All PRs require 2 approvals
2. Performance: All API endpoints <200ms
3. Security: OWASP top 10 checks pass
4. Accessibility: WCAG 2.1 AA compliance
5. Bundle size: <500KB gzipped
```

### Multi-Agent Orchestration

For large features, use subagents per phase:

```bash
# Use Task tool to parallelize
Task: Implement auth system spec
- Subagent 1: OAuth integration (Google)
- Subagent 2: OAuth integration (GitHub)
- Subagent 3: Session management
- Subagent 4: Tests for all flows

# Each subagent follows full TDD workflow
```

### Integration with CI/CD

```bash
# Pre-commit hook: Verify against constitution
.git/hooks/pre-commit:
#!/bin/bash
claude --prompt "Verify this commit follows constitution" \
  --context .specify/memory/constitution.md

# Pre-push hook: Verify spec compliance
.git/hooks/pre-push:
#!/bin/bash
claude --prompt "Verify implementation matches spec" \
  --context .specify/memory/specs/*.md
```

## Related Skills

- **superpowers:brainstorming** - Design exploration before specification
- **superpowers:writing-plans** - Detailed implementation planning
- **superpowers:test-driven-development** - TDD workflow per task
- **superpowers:requesting-code-review** - Quality gates after chunks
- **superpowers:systematic-debugging** - Debug failures during implementation
- **superpowers:verification-before-completion** - Final verification before merge
- **repomix-analyzer** - Codebase understanding before planning
- **episodic-memory:remembering-conversations** - Recall past decisions

## Notes

This skill enforces a disciplined development workflow that:
- Reduces bugs through upfront thinking
- Improves code quality via quality gates
- Creates documentation automatically (specs, plans, tasks)
- Enables team collaboration (clear handoffs)
- Facilitates debugging (clear chain of decisions)

The overhead of specification pays dividends in:
- Fewer rewrites
- Better test coverage
- Clearer documentation
- Easier onboarding
- Maintainable codebase
