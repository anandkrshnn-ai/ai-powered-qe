# Prompt Template: AI-Driven Security Vulnerability Scan

Use this prompt to identify potential security gaps in code or infrastructure manifests.

---

## The Prompt

**System Role:** You are a senior Security Engineer and Pen-tester. Your goal is to identify vulnerabilities before they reach production.

**User Input:** Analyze the following [Code/Manifest] for security vulnerabilities:
```[Language/Type]
[Paste Content Here]
```

**Requirements:**
1.  Check for common OWASP Top 10 vulnerabilities (SQLi, XSS, CSRF, etc.).
2.  Review for insecure configurations (hardcoded secrets, open ports, missing encryption).
3.  Evaluate IAM policies for over-privileged permissions.
4.  Suggest specific code or configuration changes to mitigate each risk found.

**Output Format:**
- **Vulnerability Name:**
- **Severity (Low/Medium/High/Critical):**
- **Description:**
- **Recommended Mitigation:**

---

## Tips for Success
-   **Narrow the Scope:** If analyzing a large file, tell the AI to focus on specific areas like "authentication logic" or "database queries".
-   **False Positives:** Instruct the AI to provide a "confidence score" for each finding.
