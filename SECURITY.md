# Security Policy

## Supported Versions

We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest (main branch) | :white_check_mark: |
| Older releases       | :x:                |

## Reporting a Vulnerability

We take the security of Zero to AI seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do NOT Create a Public Issue

Please **do not** create a public GitHub issue for security vulnerabilities. This could put users at risk.

### 2. Report Privately

Send a detailed report to:
- **GitHub Security Advisories**: [Report a vulnerability](https://github.com/PavanMudigondaTR/zero-to-ai/security/advisories/new)
- **Email**: Create a private issue or use GitHub's security advisory feature

### 3. Include in Your Report

- **Description**: Clear description of the vulnerability
- **Impact**: Potential impact and severity
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Affected Components**: Which notebooks, scripts, or dependencies are affected
- **Suggested Fix**: If you have ideas for fixing the issue
- **Your Contact Info**: How we can reach you for follow-up

## What Qualifies as a Security Vulnerability?

In the context of this educational repository:

### ✅ Valid Security Concerns
- Malicious code injection in notebooks
- Dependencies with known security vulnerabilities
- Scripts that could expose sensitive information
- Unsafe code patterns that could harm users' systems
- Security misconfigurations in setup scripts

### ❌ Not Security Vulnerabilities
- General bugs or errors in notebooks
- Outdated package versions (unless they have CVEs)
- Missing features or enhancements
- Documentation errors
- Performance issues

## Security Best Practices for Users

### When Using This Repository

1. **Virtual Environments**: Always use virtual environments to isolate dependencies
   ```bash
   conda env create -f environment.yml
   # or
   python -m venv .venv
   ```

2. **Review Code**: Review notebooks before running, especially those involving:
   - File system operations
   - Network requests
   - API calls
   - System commands

3. **API Keys**: Never commit API keys or sensitive credentials
   - Use environment variables
   - Add `.env` files to `.gitignore`
   - Use `.env.example` as a template

4. **Dependencies**: Keep dependencies updated
   ```bash
   pip list --outdated
   pip install --upgrade package-name
   ```

5. **Data Privacy**: Don't upload sensitive or personal data to public notebooks

### API Key Security

When working with AI/ML APIs (OpenAI, HuggingFace, etc.):

```python
# ✅ GOOD - Use environment variables
import os
api_key = os.getenv('OPENAI_API_KEY')

# ❌ BAD - Never hardcode keys
api_key = "sk-..." # NEVER DO THIS
```

### Notebook Security

When sharing notebooks:
1. **Clear Outputs**: Clear all cell outputs before committing
2. **Remove Credentials**: Check for accidentally committed keys/tokens
3. **Sanitize Data**: Remove or anonymize any personal/sensitive data
4. **Review Imports**: Be cautious with unfamiliar packages

## Dependency Security

### Checking for Vulnerabilities

We use automated tools to scan for dependency vulnerabilities:

```bash
# Using pip-audit
pip install pip-audit
pip-audit

# Using safety
pip install safety
safety check
```

### Reporting Dependency Issues

If you discover a vulnerable dependency:
1. Check if it's already reported in [GitHub Issues](https://github.com/PavanMudigondaTR/zero-to-ai/issues)
2. If not, create a security advisory or private issue
3. Include the CVE number if available
4. Suggest an updated/alternative package if possible

## Our Commitment

When you report a security vulnerability:

1. **Acknowledgment**: We'll acknowledge receipt within 48 hours
2. **Assessment**: We'll assess the severity and impact
3. **Fix**: We'll work on a fix and test it thoroughly
4. **Disclosure**: We'll coordinate disclosure timing with you
5. **Credit**: We'll credit you in the security advisory (unless you prefer anonymity)

## Security Updates

We will:
- Monitor dependencies for known vulnerabilities
- Update affected packages promptly
- Notify users of critical security issues
- Maintain a security changelog

## Resources

### Security Tools
- [pip-audit](https://github.com/pypa/pip-audit) - Python dependency scanner
- [safety](https://github.com/pyupio/safety) - Checks for known vulnerabilities
- [bandit](https://github.com/PyCQA/bandit) - Python code security analyzer

### Learning Resources
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/latest/library/security_warnings.html)
- [Secure Coding in Python](https://wiki.python.org/moin/SecurityAdvisories)

## Scope

This security policy applies to:
- All code in this repository
- Dependencies listed in `requirements.txt` and `environment.yml`
- Setup scripts and configuration files
- Documentation that includes code examples

## Questions?

If you have questions about this security policy:
- Open a [GitHub Discussion](https://github.com/PavanMudigondaTR/zero-to-ai/discussions)
- Create a non-sensitive issue for policy clarifications

---

**Thank you for helping keep Zero to AI secure!**

Last Updated: December 2025
