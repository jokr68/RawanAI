# GitHub Copilot Configuration

This directory contains configuration for GitHub Copilot coding agent, including custom instructions and agents.

## 📁 Structure

```
.github/
├── README.md                          # This file
├── CONTRIBUTING.md                    # Contribution guidelines
├── copilot-instructions.md           # Repository-wide instructions
├── instructions/                      # Scoped instructions by file type
│   ├── python.instructions.md        # Python backend guidelines
│   └── frontend.instructions.md      # Frontend/PWA guidelines
└── agents/                            # Custom Copilot agents
    └── my-agent.agent.md             # RawanAI Development Agent
```

## 🤖 What is GitHub Copilot Coding Agent?

GitHub Copilot coding agent is an AI assistant that can autonomously work on GitHub issues when assigned. It:
- Creates branches and pull requests
- Makes code changes following your instructions
- Responds to review feedback
- Follows best practices defined in your repository

## 📋 Instruction Files

### 1. Repository-Wide Instructions (`copilot-instructions.md`)

General guidelines that apply to the entire repository:
- Project overview and structure
- Language and communication guidelines (bilingual Arabic/English)
- Code style conventions
- Testing and validation procedures
- Deployment targets
- Key features to preserve (character personalities, RTL support, dark theme)
- Boundaries (what not to modify)
- Common tasks and workflows
- Build and run commands

### 2. Scoped Instructions (`instructions/*.instructions.md`)

Path-specific guidelines that apply only to certain file types:

#### **python.instructions.md**
Applies to: `**/*.py`, `requirements.txt`

Covers:
- Python/Gradio backend conventions
- Model configuration (Phi-3-Mini)
- System prompts and روان's personality
- Gradio interface guidelines
- Dependencies and performance optimization
- Testing and debugging procedures
- Security considerations

#### **frontend.instructions.md**
Applies to: `**/*.html`, `**/*.css`, `**/*.js`, `manifest.json`

Covers:
- PWA architecture and design patterns
- Dark mode + Glassmorphism styling
- RTL support for Arabic text
- Responsive design (mobile-first)
- JavaScript best practices
- مروى's AI character logic
- PWA configuration and testing
- Security and performance optimization

### 3. Custom Agents (`agents/*.agent.md`)

Specialized AI agents with domain-specific expertise:

#### **my-agent.agent.md** - RawanAI Development Agent

A full-stack developer agent specialized in:
- Python/Gradio backends
- PWA frontends
- Bilingual (Arabic/English) development
- AI/ML model integration
- Cultural context (Saudi Arabian and Sudanese dialects)

## 🎯 How Copilot Uses These Instructions

1. **General Context**: Copilot reads `copilot-instructions.md` for overall project understanding
2. **File-Specific Guidance**: When working on specific files, it applies relevant scoped instructions
3. **Custom Agents**: Can invoke the custom agent for specialized tasks
4. **Iterative Learning**: Follows feedback in PR reviews to improve

## ✍️ Writing Good Instructions

Based on [GitHub best practices](https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/):

### Do's ✅
- **Be specific**: Provide concrete examples and patterns
- **Include context**: Explain *why* certain practices are important
- **Show examples**: Code snippets demonstrate better than descriptions
- **Set boundaries**: Clearly state what should never change
- **Document commands**: Include exact commands for testing/building
- **Cover edge cases**: Mention common pitfalls and how to avoid them

### Don'ts ❌
- **Avoid vague guidance**: "Write good code" is not helpful
- **Don't contradict**: Ensure instructions don't conflict across files
- **Don't assume knowledge**: Explain project-specific concepts
- **Don't over-constrain**: Give Copilot flexibility to solve creatively
- **Don't forget examples**: Abstract rules without examples are hard to follow

## 🔧 Modifying Instructions

When updating instructions:

1. **Test changes**: Assign a simple issue to Copilot to verify it follows updated guidance
2. **Be consistent**: Update all relevant instruction files if a practice changes
3. **Document rationale**: Explain *why* a guideline exists
4. **Get feedback**: If Copilot misinterprets instructions, refine them
5. **Version control**: Instructions are part of the repo, so changes are tracked

## 📝 YAML Frontmatter

Scoped instruction files use YAML frontmatter to specify which files they apply to:

```markdown
---
applies_to:
  - "**/*.py"        # All Python files
  - "requirements.txt"
---

# Your instructions here...
```

Agent files use different frontmatter:

```markdown
---
name: Agent Name
description: Brief description of the agent's expertise
---

# Your agent instructions here...
```

## 🚀 Using with Copilot Coding Agent

### In GitHub Issues
1. Create a clear, well-scoped issue
2. Assign it to `@copilot` (requires write access)
3. Copilot will create a PR following these instructions
4. Review and provide feedback

### In VS Code
The same instructions guide Copilot's code suggestions in your IDE when you have Copilot enabled.

## 🌍 Project-Specific Considerations

### Bilingual Development
This project requires special attention to:
- **RTL (Right-to-Left) text** for Arabic
- **Character personalities** (روان and مروى) with specific dialects
- **Cultural sensitivity** in language and interactions
- **Dark theme** aesthetic throughout

### Key Technologies
- **Backend**: Python, Gradio, HuggingFace Transformers
- **Frontend**: Pure HTML/CSS/JS (no frameworks)
- **Design**: Dark mode + Glassmorphism
- **Deployment**: Hugging Face Spaces (backend), Netlify/Vercel (frontend)

### Testing Requirements
- **Python**: Run `python app.py` and test manually
- **PWA**: Serve with `python3 -m http.server 8080`
- **Always verify**: Arabic RTL rendering, character consistency, mobile responsiveness

## 📚 Further Reading

- [GitHub Copilot Coding Agent Documentation](https://docs.github.com/en/copilot/tutorials/coding-agent)
- [GitHub Copilot Instructions Guide](https://design.dev/guides/copilot-instructions/)
- [Setting up Copilot for Success (GitHub Blog)](https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-copilot-coding-agent-for-success/)
- [Custom Instructions Deep Dive](https://www.nathannellans.com/post/all-about-github-copilot-custom-instructions)

## 🤝 Contributing to Instructions

If you notice instructions are:
- **Outdated**: Update them to reflect current practices
- **Unclear**: Add examples or clarification
- **Missing**: Add new guidelines as the project evolves
- **Conflicting**: Resolve contradictions

See [CONTRIBUTING.md](CONTRIBUTING.md) for general contribution guidelines.

---

**Last Updated**: 2026-02-12  
**Maintained By**: Project Contributors
