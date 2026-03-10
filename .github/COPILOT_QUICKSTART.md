# Quick Start: GitHub Copilot Coding Agent

This guide helps you quickly get started with GitHub Copilot coding agent in the RawanAI repository.

## 🚀 Quick Setup

### Prerequisites
- GitHub Copilot subscription (Pro, Pro+, Business, or Enterprise)
- Write access to the repository (to assign issues)

### How to Use Copilot

1. **Create a clear issue** using one of our templates:
   - [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md)
   - [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md)
   - [Documentation Update](.github/ISSUE_TEMPLATE/documentation.md)

2. **Assign the issue to @copilot**
   - Copilot will automatically create a branch
   - Make the necessary changes
   - Create a pull request

3. **Review the PR**
   - Check the changes carefully
   - Provide feedback in comments
   - Copilot will update based on feedback

4. **Merge when ready**
   - Once satisfied, merge the PR
   - Changes are deployed to main branch

## 📁 Instruction Files Overview

| File | Purpose | Applies To |
|------|---------|------------|
| [copilot-instructions.md](copilot-instructions.md) | General project guidelines | All files |
| [instructions/python.instructions.md](instructions/python.instructions.md) | Python backend guidelines | `**/*.py`, `requirements.txt` |
| [instructions/frontend.instructions.md](instructions/frontend.instructions.md) | Frontend/PWA guidelines | `**/*.html`, `**/*.css`, `**/*.js`, `manifest.json` |
| [agents/my-agent.agent.md](agents/my-agent.agent.md) | Custom full-stack agent | All files (when invoked) |

## 💡 Tips for Good Issues

### ✅ Do This
- Be specific about what needs to change
- Provide clear acceptance criteria
- Include relevant context (bilingual, RTL, character personalities)
- Mention which component is affected (backend/frontend)
- Add screenshots or examples when helpful

### ❌ Avoid This
- Vague descriptions like "make it better"
- Multiple unrelated tasks in one issue
- Missing context about language requirements
- No acceptance criteria
- Overly broad scope

## 🌍 Project-Specific Reminders

When creating issues, remember:

1. **Bilingual Project**: Specify Arabic/English requirements
2. **RTL Support**: Mention if Arabic text alignment matters
3. **Character Personalities**: روان (Jeddah dialect) or مروى (Najdi dialect)
4. **Dark Theme**: Changes must maintain purple dark aesthetic
5. **Mobile-First**: Test on both desktop and mobile
6. **Cultural Context**: Respect Saudi Arabian and Sudanese dialects

## 🎯 Example Issues

### Good Feature Request
```
✨ Add voice input support to RawanAI chatbot

**Description**: Allow users to speak their questions instead of typing

**Acceptance Criteria**:
- [ ] Voice input button appears in chat interface
- [ ] Speech-to-text works for both Arabic and English
- [ ] Maintains RTL support for Arabic transcription
- [ ] Works on mobile devices
- [ ] Matches dark purple theme

**Components**: RawanAI Backend (speech recognition), Frontend (UI)
```

### Good Bug Report
```
🐛 Arabic text not aligned correctly in Lord'Os chat

**Steps to Reproduce**:
1. Open Lord'Os PWA
2. Send a message in Arabic to مروى
3. Observe text alignment

**Expected**: Arabic text should be right-aligned (RTL)
**Actual**: Arabic text appears left-aligned

**Component**: Lord'Os Frontend (CSS)
**Language**: Arabic RTL issue
```

## 🔧 Testing Commands

### Python Backend (RawanAI)
```bash
pip install -r requirements.txt
python app.py
# Access at http://localhost:7860
```

### Frontend PWA (Lord'Os)
```bash
python3 -m http.server 8080
# Access at http://localhost:8080
```

## 📚 Learn More

- [Full Documentation](README.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Validation Checklist](COPILOT_VALIDATION.md)
- [GitHub Copilot Docs](https://docs.github.com/en/copilot/tutorials/coding-agent)

## ❓ Common Questions

**Q: Can Copilot work on any issue?**  
A: Copilot works best on well-scoped, clearly defined issues. Complex or vague issues may need human guidance.

**Q: Will Copilot preserve character personalities?**  
A: Yes! Our instructions emphasize maintaining روان's and مروى's personalities and dialects.

**Q: Does Copilot understand Arabic?**  
A: Yes! Our instructions guide Copilot to properly handle bilingual content, RTL support, and cultural context.

**Q: Can I provide feedback on Copilot's work?**  
A: Absolutely! Leave comments on the PR, and Copilot will iterate based on your feedback.

**Q: What if Copilot makes a mistake?**  
A: Review carefully, provide specific feedback, and request changes. You can also manually edit the PR.

## 🎉 Ready to Start!

Create your first issue and assign it to @copilot to see the magic happen! 🤖

---

**Need Help?** Check the [full documentation](README.md) or open a discussion in the repository.
