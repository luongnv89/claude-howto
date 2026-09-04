# Security Vulnerability Reporting

This file explains how to report security vulnerabilities to the Claude How To project.

## Quick Links

- **Private Reporting**: https://github.com/luongnv89/claude-howto/security/advisories
- **Security Policy**: [SECURITY.md](../SECURITY.md)
- **Report Template**: See below

## Report a Vulnerability

### Option 1: GitHub Private Vulnerability Report (RECOMMENDED)

This is the preferred method for reporting security vulnerabilities.

**Steps:**
1. Go to: https://github.com/luongnv89/claude-howto/security/advisories
2. Click "Report a vulnerability"
3. Fill in the details (use template below)
4. Submit

**Advantages:**
- Keeps vulnerability private until fix is released
- Automatic notifications to maintainers
- Built-in collaboration features
- Integrated with GitHub security tools

### Option 2: GitHub Security Alert (For Dependencies)

If you discover a vulnerability in a dependency:

1. Go to: https://github.com/luongnv89/claude-howto/security/advisories
2. Review the alert
3. Create a pull request with the fix
4. Tag with `security` label

### Option 3: Private Email (If GitHub unavailable)

If you cannot use GitHub's reporting system:

**Coming soon**: Security contact email will be added here

For now, use GitHub's private vulnerability reporting as described above.

## Vulnerability Report Template

Use this template when reporting a vulnerability:

```
**Title**: [Brief description of vulnerability]

**Severity**: [Critical/High/Medium/Low]
Estimated CVSS Score: [0-10]

**Type**: [Code/Documentation/Dependency/Configuration]

**Affected Component**:
- File: [path/to/file.py]
- Section: [Section name if documentation]
- Version: [latest/specific version]

**Description**:
[Clear explanation of what the vulnerability is]

**Potential Impact**:
[What could an attacker do with this vulnerability?]
[Who could be affected?]

**Steps to Reproduce**:
1. [First step]
2. [Second step]
3. [Third step]
[Expected result vs actual result]

**Proof of Concept** (if available):
[Code or steps to demonstrate the vulnerability]

**Suggested Fix**:
[Your recommended solution, if you have one]

**Additional Context**:
[Any other relevant information]

**Your Information**:
- Name: [Your name or anonymous]
- Email: [Your email]
- Credit: [How you'd like to be credited, if at all]
```

## What Happens After You Report

### Timeline

1. **Immediate (< 1 hour)**
   - Automatic notification sent to project maintainers

2. **Within 24 hours**
   - Initial assessment of the report
   - Confirmation that we received it
   - Preliminary severity assessment

3. **Within 48 hours**
   - Detailed response from security team
   - Questions for clarification (if needed)
   - Timeline for fix (if vulnerability confirmed)

4. **Within 1-7 days** (depends on severity)
   - Fix developed and tested
   - Security advisory prepared
   - Fix released and public advisory published

### Communication

We will keep you informed through:
- GitHub private vulnerability discussion
- Email (if provided)
- Updates in the discussion thread

You can:
- Ask clarifying questions
- Provide additional information
- Suggest improvements to the fix
- Request timeline adjustments

### Disclosure Timeline

**Critical Issues (CVSS 9.0-10.0)**
- Fix: Released immediately (within 24 hours)
- Disclosure: Public advisory issued same day
- Notice: 24 hours advance notice to reporter

**High Issues (CVSS 7.0-8.9)**
- Fix: Released within 48-72 hours
- Disclosure: Public advisory on release
- Notice: 5 days advance notice to reporter

**Medium Issues (CVSS 4.0-6.9)**
- Fix: Included in next regular update
- Disclosure: Public advisory on release
- Notice: Coordinated timing

**Low Issues (CVSS 0.1-3.9)**
- Fix: Included in next regular update
- Disclosure: Advisory on release
- Notice: Same day as release

## Security Vulnerability Criteria

### In Scope

We accept reports on:

- **Code Vulnerabilities**
  - Injection attacks (command, SQL, etc.)
  - Cross-site scripting (XSS) in examples
  - Authentication/authorization flaws
  - Path traversal vulnerabilities
  - Cryptography issues

- **Documentation Security**
  - Exposed secrets or credentials
  - Insecure code patterns
  - Security anti-patterns
  - Misleading security claims

- **Dependency Vulnerabilities**
  - Known CVEs in dependencies
  - Supply chain attacks
  - Malicious dependencies

- **Configuration Issues**
  - Insecure defaults
  - Missing security headers
  - Credential exposure in examples

### Out of Scope

We do NOT accept reports on:

- Vulnerabilities in Claude Code itself (contact Anthropic)
- Vulnerabilities in external services
- Theoretical vulnerabilities without proof
- Issues already reported to upstream projects
- Social engineering or phishing
- User education/training issues

## Responsible Disclosure Guidelines

### Do's ✅

- **Report privately** before public disclosure
- **Be specific** with file paths and line numbers
- **Provide proof** of the vulnerability
- **Give us time** to fix (coordinated disclosure)
- **Update** if you discover more details
- **Be professional** in all communications
- **Respect confidentiality** until we publish

### Don'ts ❌

- **Don't publicly disclose** before we fix
- **Don't exploit** the vulnerability beyond testing
- **Don't modify** other users' data
- **Don't demand** payment or favors
- **Don't share** the vulnerability with others
- **Don't use** it in any harmful way
- **Don't spam** with non-security related issues

## Coordinated Disclosure

We practice responsible disclosure:

1. **Private Report**: You report to us privately
2. **Our Assessment**: We evaluate and assess severity
3. **Fix Development**: We develop and test a fix
4. **Advance Notice**: We give you advance notice before public disclosure
5. **Public Release**: We release fix and advisory together
6. **Your Credit**: We acknowledge your contribution (if desired)

**Timeline varies based on severity** (see section above)

## After the Fix is Released

### Public Advisory

A public security advisory will include:
- Description of the vulnerability
- Affected versions
- Severity (CVSS score)
- Steps to remediate
- Link to the fix
- Credit to reporter (with permission)

### Your Recognition

If you wish to be credited:
- Your name/handle in the advisory
- Link to your profile/website
- Mention in release notes
- Addition to hall of fame (if created)

### No Compensation

Please note:
- This is a volunteer-run open-source project
- We cannot offer financial rewards
- We do offer recognition and credit
- Your contribution helps the community

## Security Research

If you're conducting security research:

1. **Get Permission**: Contact maintainers first
2. **Define Scope**: Agree on what you'll test
3. **Report Findings**: Use this process
4. **Respect Timeline**: Allow time for fixes
5. **Publish Responsibly**: Coordinate with us

## Questions?

For questions about this process:

1. Check [SECURITY.md](../SECURITY.md) for detailed policy
2. Look at [FAQ](#faq) section below
3. Open a discussion with `[SECURITY]` label
4. Use private vulnerability reporting for sensitive questions

## FAQ

**Q: Will my report be kept confidential?**
A: Yes, until the fix is released. We only share details with those working on the fix.

**Q: How long do I need to wait before public disclosure?**
A: We follow responsible disclosure timelines based on severity (24 hours to 7 days). You can agree to extend this if needed.

**Q: Will I get credit?**
A: Yes, in the security advisory and release notes (unless you prefer anonymity).

**Q: What if the vulnerability is minor?**
A: All legitimate security issues are taken seriously. Even minor fixes will be acknowledged.

**Q: Can I report vulnerabilities in documentation only?**
A: Yes! Documentation security is important too. Examples with insecure patterns are in scope.

**Q: What if I'm not sure if something is a security issue?**
A: Report it anyway! If it's not a security issue, we'll let you know. False positives are fine.

**Q: Can I publicly discuss the vulnerability after reporting?**
A: No, please keep it private until we publish the advisory. Premature disclosure could put users at risk.

**Q: How do I know you received my report?**
A: GitHub will send an automatic notification, and we'll follow up within 24 hours.

**Q: What if I don't hear back?**
A: Check GitHub security advisories page. If you still don't see a response, you can follow up with a comment on the private report.

## Resources

- [SECURITY.md](../SECURITY.md) - Full security policy
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contributing guidelines
- [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) - Community standards
- [OWASP Vulnerability Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html) - Responsible disclosure best practices
- [Coordinated Vulnerability Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html)

---

Thank you for helping keep this project secure! 🔒
