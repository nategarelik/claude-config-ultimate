---
description: Use when you need to understand codebase structure, find patterns, or analyze unfamiliar code - leverages Repomix MCP for fast text-based code analysis and search
allowed-tools: [mcp__plugin_repomix-mcp_repomix__pack_codebase, mcp__plugin_repomix-mcp_repomix__grep_repomix_output, mcp__plugin_repomix-mcp_repomix__read_repomix_output, Grep, Glob, Read]
---

# Repomix Analyzer Skill

## Purpose

This skill provides fast, efficient codebase understanding using Repomix MCP server. It's optimized for:

- **Codebase exploration** - Understanding project structure
- **Pattern discovery** - Finding similar code patterns
- **Dependency analysis** - Tracing imports and relationships
- **Documentation generation** - Creating architecture overviews
- **Pre-implementation research** - Understanding existing code before changes

## When to Use

Activate this skill when:
- Starting work in unfamiliar codebase
- Need to understand existing patterns
- Looking for similar implementations
- Analyzing architecture before planning
- Documenting code structure
- Finding all usages of a pattern

## Core Capabilities

### 1. Pack and Analyze Codebase

```bash
# Pack entire codebase
Use mcp__plugin_repomix-mcp_repomix__pack_codebase tool
directory: "/path/to/project"
style: "xml"  # or "markdown", "json", "plain"

# Pack with compression (for large codebases)
compress: true  # Reduces tokens by ~70%

# Focus on specific files
includePatterns: "src/**/*.ts,**/*.tsx"

# Exclude test files
ignorePatterns: "**/*.test.ts,**/*.spec.ts"
```

**Output**: Consolidated view of entire codebase with metrics

### 2. Search for Patterns

```bash
# Find all React components
Use mcp__plugin_repomix-mcp_repomix__grep_repomix_output tool
pattern: "export (default )?function [A-Z]\\w+\\("
contextLines: 5

# Find API endpoints
pattern: "app\\.(get|post|put|delete)\\("

# Find authentication code
pattern: "auth|login|jwt|token"
ignoreCase: true
```

### 3. Read Specific Sections

```bash
# Read file tree section
Use mcp__plugin_repomix-mcp_repomix__read_repomix_output tool
startLine: 1
endLine: 100

# Read specific file from packed output
startLine: 500
endLine: 600
```

### 4. Metrics and Overview

After packing, you get:
- Total files and lines of code
- Language breakdown
- Largest files
- File tree structure
- Token usage estimates

## Typical Workflows

### Workflow 1: Understand New Codebase

```bash
# Step 1: Pack the codebase
Pack codebase: ./my-project

# Step 2: Review file tree
Read lines 1-50 to see directory structure

# Step 3: Find entry points
Grep for: "main\\(|render\\(|app\\.listen"

# Step 4: Understand architecture
Grep for: "import.*from"  # See dependencies
Grep for: "class |interface " # See type definitions

# Step 5: Document findings
Create summary document with:
- Entry points
- Key modules
- Architecture patterns
- External dependencies
```

### Workflow 2: Find Implementation Examples

```bash
# Goal: Implement authentication, find existing examples

# Step 1: Search for auth patterns
Grep: "authenticate|authorization"

# Step 2: Find middleware
Grep: "middleware.*auth"

# Step 3: Find JWT usage
Grep: "jwt\\.sign|jwt\\.verify"

# Step 4: Read relevant files
Read sections around matches

# Step 5: Synthesize approach
Document patterns found and adapt for new implementation
```

### Workflow 3: Pre-Planning Analysis

```bash
# Before using spec-kit-orchestrator, understand codebase

# Step 1: Pack with focus
includePatterns: "src/**"  # Only source code
ignorePatterns: "**/*.test.*,**/node_modules/**"

# Step 2: Analyze structure
Read file tree
Note: monolith vs microservices, layered architecture

# Step 3: Find similar features
Grep for features similar to what you're building

# Step 4: Document constraints
Note: existing patterns you must follow
List: libraries already in use
Identify: testing approach in use

# Step 5: Feed into spec-kit
Use findings to inform Plan phase
Follow existing patterns for consistency
```

### Workflow 4: Refactoring Impact Analysis

```bash
# Goal: Understand what would break if you refactor function X

# Step 1: Find function definition
Grep: "function functionName"

# Step 2: Find all usages
Grep: "functionName\\("

# Step 3: Analyze call sites
Read context around each usage

# Step 4: Find tests
Grep: "describe.*functionName|test.*functionName"

# Step 5: Plan refactoring
Document all affected files
Plan backwards-compatible approach or update strategy
```

## Integration with Other Skills

### With spec-kit-orchestrator

```bash
# Before Phase 2 (Specify):
Use repomix-analyzer to understand existing code

# Before Phase 3 (Plan):
Use repomix-analyzer to find similar implementations
Identify patterns to follow

# During Phase 4 (Tasks):
Use repomix-analyzer to find relevant files to modify
```

### With superpowers:systematic-debugging

```bash
# During debugging:
Use repomix-analyzer to trace data flow
Find all code paths that could trigger error
Identify related code that might have same bug
```

### With episodic-memory

```bash
# After analysis:
Log findings to episodic memory
Record architectural decisions discovered
Document patterns for future reference
```

## Advanced Usage

### Incremental Analysis

```bash
# Start with overview
Pack with compression: true
Review high-level structure

# Deep dive into specific area
Pack again without compression
includePatterns: "src/auth/**"
Get full detail for focused area
```

### Cross-Repository Comparison

```bash
# Pack multiple codebases
Pack: /project-a
Pack: /project-b

# Compare approaches
Grep both for similar features
Document differences
Identify best practices to adopt
```

### Documentation Generation

```bash
# Pack codebase
style: "markdown"

# Generate architecture doc
Read file tree → Document structure
Grep for patterns → Document conventions
Identify entry points → Document user flows
```

### Performance Analysis

```bash
# Find performance hotspots
Grep: "loop|for\\(|while\\(|forEach"
Grep: "setTimeout|setInterval"
Grep: "async|await|Promise"

# Identify inefficiencies
Look for: N+1 queries, nested loops, blocking operations
```

## Best Practices

1. **Start Broad, Then Narrow**
   - Pack full codebase first for overview
   - Use compression for large repos
   - Deep dive into specific areas afterward

2. **Use Appropriate Patterns**
   - Grep uses JavaScript RegExp syntax
   - Escape special characters: `\\(` for `(`
   - Use `ignoreCase: true` for broader matching

3. **Context is Key**
   - Always use `contextLines` in grep
   - 3-5 lines usually sufficient
   - More lines for complex code

4. **Combine with Direct File Access**
   - Use Repomix for search and overview
   - Use Read tool for detailed file analysis
   - Use Edit tool for modifications

5. **Document Findings**
   - Create summary documents
   - Log to episodic memory
   - Share with team via gh-logger

## Performance Tips

### For Large Codebases (>100K LOC)

```bash
# Use compression
compress: true  # ~70% token reduction

# Focus analysis
includePatterns: "src/**"  # Only relevant code
ignorePatterns: "**/*.test.*,**/dist/**,**/node_modules/**"

# Incremental packing
Pack different modules separately
Analyze one module at a time
```

### For Fast Iteration

```bash
# Cache packed output
Pack once, grep multiple times
outputId is reusable across greps

# Use head_limit
grep with head_limit: 20  # First 20 matches only
Saves tokens, faster responses
```

### Token Budget Management

```bash
# Monitor usage
Check Repomix metrics for token counts

# Strategic compression
Compress for overview (signatures only)
No compression for implementation details

# Selective inclusion
Only pack what you need
Use includePatterns liberally
```

## Troubleshooting

**Grep returns no results?**
- Check pattern syntax (JavaScript RegExp)
- Try simpler pattern first
- Use `ignoreCase: true`
- Verify outputId is correct

**Too many results?**
- Use more specific patterns
- Add context to patterns (e.g., `export function` vs just `function`)
- Use head_limit to cap results
- Narrow with includePatterns

**Performance slow?**
- Enable compression
- Reduce scope with includePatterns
- Exclude large files (dist/, node_modules/)
- Pack incrementally

**Missing files in output?**
- Check .gitignore (Repomix respects it)
- Verify includePatterns not too restrictive
- Check file extensions supported

## Related Skills

- **spec-kit-orchestrator** - Use analyzer before planning phase
- **superpowers:systematic-debugging** - Use analyzer to trace bugs
- **episodic-memory:remembering-conversations** - Store analysis findings
- **gh-logger** - Log architectural discoveries

## Comparison to Alternatives

### Repomix vs Serena MCP

| Feature | Repomix (This Skill) | Serena MCP |
|---------|---------------------|------------|
| **Speed** | Very fast | Slower (LSP overhead) |
| **Understanding** | Text-based | Semantic/symbol-level |
| **Best for** | Overview, search, patterns | Refactoring, precise edits |
| **Token usage** | Lower (with compression) | Higher |
| **Setup** | Already installed | Requires additional setup |
| **Strength** | Quick exploration | Deep code intelligence |

**Recommendation**: Use Repomix (this skill) for exploration and overview. Add Serena later if you need semantic code understanding for complex refactoring.

## Notes

This skill leverages your existing Repomix installation and is optimized for:
- Fast codebase onboarding
- Pattern discovery
- Pre-planning research
- Documentation generation

It's designed to work seamlessly with:
- Spec-Kit workflow (analysis before planning)
- Superpowers skills (context for debugging, testing)
- Episodic memory (storing findings)
- GH logger (documenting discoveries)

The skill is **always available** but auto-activates when you use keywords like "codebase", "understand", "explore", "analyze", or "structure" in your prompts.
