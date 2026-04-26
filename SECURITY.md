# Security Policy

## Overview

The security of the Claude How To project is important to us. This document outlines our security practices and describes how to report security vulnerabilities responsibly.

## Supported Versions

We provide security updates for the following versions:

| Version | Status | Support Until |
|---------|--------|---------------|
| Latest (main) | ✅ Active | Current + 6 months |
| 1.x releases | ✅ Active | Until next major version |

**Note**: As an educational guide project, we focus on maintaining current best practices and documentation security rather than traditional version support. Updates are applied directly to the main branch.

## Security Practices

### Code Security

1. **Dependency Management**
   - All Python dependencies are pinned in `requirements.txt`
   - Regular updates via dependabot and manual review
   - Security scanning with Bandit on every commit
   - Pre-commit hooks for security checks

2. **Code Quality**
   - Linting with Ruff catches common issues
   - Type checking with mypy prevents type-related vulnerabilities
   - Pre-commit hooks enforce standards
   - All changes reviewed before merging

3. **Access Control**
   - Branch protection on `main` branch
   - Required reviews before merge
   - Status checks must pass before merge
   - Limited write access to repository

### Documentation Security

1. **No Secrets in Examples**
   - All API keys in examples are placeholders
   - Credentials are never hardcoded
   - `.env.example` files show required variables
   - Clear warnings about secret management

2. **Security Best Practices**
   - Examples demonstrate secure patterns
   - Security warnings highlighted in documentation
   - Links to official security guides
   - Credential handling discussed in relevant sections

3. **Content Review**
   - All documentation reviewed for security issues
   - Security considerations in contributing guidelines
   - Validation of external links and references

### Dependency Security

1. **Scanning**
   - Bandit scans all Python code for vulnerabilities
   - Dependency vulnerability checks via GitHub security alerts
   - Regular manual security audits

2. **Updates**
   - Security patches applied promptly
   - Major versions evaluated carefully
   - Changelog includes security-related updates

3. **Transparency**
   - Security updates documented in commits
   - Vulnerability disclosures handled responsibly
   - Public security advisories when appropriate

## Reporting a Vulnerability

### Security Issues We Care About

We appreciate reports on:
- **Code vulnerabilities** in scripts or examples
- **Dependency vulnerabilities** in Python packages
- **Cryptography issues** in any code examples
- **Authentication/Authorization flaws** in documentation
- **Data exposure risks** in configuration examples
- **Injection vulnerabilities** (SQL, command, etc.)
- **SSRF/XXE/Path traversal** issues

### Security Issues Out of Scope

These are outside the scope of this project:
- Vulnerabilities in Claude Code itself (report to Anthropic)
- Issues with external services or libraries (report to upstream)
- Social engineering or user education (not applicable to this guide)
- Theoretical vulnerabilities without proof of concept
- Vulnerabilities in dependencies reported through official channels

## How to Report

### Private Reporting (Preferred)

**For sensitive security issues, please use GitHub's private vulnerability reporting:**

1. Visit: https://github.com/luongnv89/claude-howto/security/advisories
2. Click "Report a vulnerability"
3. Fill in the vulnerability details
4. Include:
   - Clear description of the vulnerability
   - Affected component (file, section, example)
   - Potential impact
   - Steps to reproduce (if applicable)
   - Suggested fix (if you have one)

**What happens next:**
- We'll acknowledge receipt within 48 hours
- We'll investigate and assess severity
- We'll work with you to develop a fix
- We'll coordinate disclosure timeline
- We'll credit you in the security advisory (unless you prefer anonymity)

### Public Reporting

For non-sensitive issues or those already public:

1. **Open a GitHub Issue** with label `security`
2. Include:
   - Title: `[SECURITY]` followed by brief description
   - Detailed description
   - Affected file or section
   - Potential impact
   - Suggested fix

## Vulnerability Response Process

### Assessment (24 hours)

1. We acknowledge receipt of the report
2. We assess severity using [CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document)
3. We determine if it's in scope
4. We contact you with initial assessment

### Development (1-7 days)

1. We develop a fix
2. We review and test the fix
3. We create a security advisory
4. We prepare release notes

### Disclosure (varies by severity)

**Critical (CVSS 9.0-10.0)**
- Fix released immediately
- Public advisory issued
- 24-hour advance notice to reporters

**High (CVSS 7.0-8.9)**
- Fix released within 48-72 hours
- 5-day advance notice to reporters
- Public advisory on release

**Medium (CVSS 4.0-6.9)**
- Fix released in next regular update
- Public advisory on release

**Low (CVSS 0.1-3.9)**
- Fix included in next regular update
- Advisory on release

### Publication

We publish security advisories that include:
- Description of the vulnerability
- Affected components
- Severity assessment (CVSS score)
- Fix version
- Workarounds (if applicable)
- Credit to reporter (with permission)

## Best Practices for Reporters

### Before Reporting

- **Verify the issue**: Can you reproduce it consistently?
- **Search existing issues**: Is it already reported?
- **Check documentation**: Is there guidance on secure usage?
- **Test the fix**: Does your suggested fix work?

### When Reporting

- **Be specific**: Provide exact file paths and line numbers
- **Include context**: Why is this a security issue?
- **Show impact**: What could an attacker do?
- **Provide steps**: How can we reproduce it?
- **Suggest fixes**: How would you fix it?

### After Reporting

- **Be patient**: We have limited resources
- **Be responsive**: Answer follow-up questions quickly
- **Keep it confidential**: Don't publicly disclose before fix
- **Respect coordination**: Follow our timeline for disclosure

## Security Headers and Configuration

### Repository Security

- **Branch protection**: Main branch requires 2 approvals for changes
- **Status checks**: All CI/CD checks must pass
- **CODEOWNERS**: Designated reviewers for key files
- **Signed commits**: Recommended for contributors

### Development Security

```bash
# Install pre-commit hooks
pre-commit install

# Run security scans locally
bandit -c pyproject.toml -r scripts/
mypy scripts/ --ignore-missing-imports
ruff check scripts/
```

### Dependency Security

```bash
# Check for known vulnerabilities
pip install safety
safety check

# Or use pip-audit
pip install pip-audit
pip-audit
```

## Security Guidelines for Contributors

### When Writing Examples

1. **Never hardcode secrets**
   ```python
   # ❌ Bad
   api_key = "sk-1234567890"

   # ✅ Good
   api_key = os.getenv("API_KEY")
   ```

2. **Warn about security implications**
   ```markdown
   ⚠️ **Security Note**: Never commit `.env` files to git.
   Add to `.gitignore` immediately.
   ```

3. **Use secure defaults**
   - Enable authentication by default
   - Use HTTPS where applicable
   - Validate and sanitize inputs
   - Use parameterized queries

4. **Document security considerations**
   - Explain why security matters
   - Show secure vs. insecure patterns
   - Link to authoritative sources
   - Include warnings prominently

### When Reviewing Contributions

1. **Check for exposed secrets**
   - Scan for common patterns (api_key=, password=)
   - Review configuration files
   - Check environment variables

2. **Verify secure coding practices**
   - No hardcoded credentials
   - Proper input validation
   - Secure authentication/authorization
   - Safe file handling

3. **Test security implications**
   - Can this be misused?
   - What's the worst case?
   - Are there edge cases?

## Security Resources

### Official Standards
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [CVSS Calculator](https://www.first.org/cvss/calculator/3.1)

### Python Security
- [Python Security Advisories](https://www.python.org/dev/security/)
- [PyPI Security](https://pypi.org/help/#security)
- [Bandit Documentation](https://bandit.readthedocs.io/)

### Dependency Management
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [GitHub Security Alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)

### General Security
- [Anthropic Security](https://www.anthropic.com/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

## Security Advisories Archive

Past security advisories are available in the [GitHub Security Advisories](https://github.com/luongnv89/claude-howto/security/advisories) tab.

## Contact

For security-related questions or to discuss security practices:

1. **Private Security Report**: Use GitHub's private vulnerability reporting
2. **General Security Questions**: Open a discussion with `[SECURITY]` tag
3. **Security Policy Feedback**: Create an issue with `security` label

## Acknowledgments

We appreciate the security researchers and community members who help keep this project secure. Contributors who report vulnerabilities responsibly will be acknowledged in our security advisories (unless they prefer anonymity).

## Policy Updates

This security policy is reviewed and updated:
- When new vulnerabilities are discovered
- When security best practices evolve
- When the project scope changes
- Annually as a minimum

**Last Updated**: April 27, 2026
**Next Review**: April 2027

---

Thank you for helping keep Claude How To secure! 🔒
