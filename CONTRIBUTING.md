# Contributing to OctoPrint PSU Control Tapo P110

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the OctoPrint PSU Control Tapo P110 plugin.

## 🎯 Project Focus

This plugin is specifically designed for:
- **Tapo P110 Smart Plugs** (not P100 or other models)
- **Firmware 1.1.3+** (Build 240523 Rel.175054 and newer)
- **Python 3.11+** compatibility
- **OctoPrint integration** via PSU Control

## 🐛 Reporting Issues

Before creating an issue, please:

1. **Check existing issues** to avoid duplicates
2. **Test with the latest version** of the plugin
3. **Verify your setup**:
   - Confirm you have a P110 (not P100)
   - Check your firmware version
   - Ensure Python 3.11+ is being used

### Issue Template

When reporting issues, please include:

```
**Device Information:**
- Model: P110
- Firmware Version: [e.g., 1.1.3 Build 240523 Rel.175054]
- IP Address: [e.g., 192.168.1.100]

**Environment:**
- OctoPrint Version: [e.g., 1.9.3]
- Python Version: [e.g., 3.11.5]
- Operating System: [e.g., Raspberry Pi OS, Ubuntu 22.04]

**Plugin Information:**
- Plugin Version: [e.g., 1.0.0]
- PSU Control Version: [e.g., 1.1.2]

**Problem Description:**
[Clear description of the issue]

**Steps to Reproduce:**
1. [First step]
2. [Second step]
3. [And so on...]

**Expected Behavior:**
[What you expected to happen]

**Actual Behavior:**
[What actually happened]

**Logs:**
[Relevant OctoPrint logs - please use code blocks]
```

## 🔧 Development Setup

### Prerequisites
- Python 3.11 or newer
- Git
- A Tapo P110 device for testing

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/OctoPrint-PSUControl-Tapo-P110.git
   cd OctoPrint-PSUControl-Tapo-P110
   ```

2. **Create a virtual environment:**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests:**
   ```bash
   python test_plugin.py
   ```

## 🧪 Testing

### Test Script
Use the included test script to verify functionality:
```bash
python test_plugin.py
```

### Manual Testing
1. Install the plugin in a test OctoPrint instance
2. Configure with your P110 credentials
3. Test power on/off functionality
4. Verify energy monitoring (if enabled)
5. Check logs for any errors

## 📝 Code Style

### Python Code
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep lines under 100 characters when possible

### Comments
- Use clear, concise comments
- Explain "why" not just "what"
- Update comments when code changes

## 🔄 Pull Request Process

1. **Fork the repository** and create a feature branch
2. **Make your changes** following the code style guidelines
3. **Test thoroughly** with a real P110 device
4. **Update documentation** if needed
5. **Create a pull request** with:
   - Clear description of changes
   - Reference to any related issues
   - Test results

### Pull Request Template

```
**Description:**
[Brief description of changes]

**Type of Change:**
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

**Testing:**
- [ ] Tested with P110 device
- [ ] Test script passes
- [ ] Manual testing completed

**Checklist:**
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated (if applicable)
- [ ] No breaking changes (or clearly documented)

**Related Issues:**
Fixes #[issue number]
```

## 🚀 Release Process

Releases are handled by the maintainers and follow semantic versioning:
- **Major** (X.0.0): Breaking changes
- **Minor** (0.X.0): New features, backward compatible
- **Patch** (0.0.X): Bug fixes, backward compatible

## 📄 License

By contributing, you agree that your contributions will be licensed under the AGPLv3 License.

## 🤝 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain a welcoming environment

## 📞 Getting Help

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Discussions**: Use GitHub Discussions for questions and general discussion
- **Community**: Join the OctoPrint Community Forums

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

Thank you for helping make this plugin better! 🎉
