---
question: |
    You have a GitHub repository that uses the GitHub Copilot coding agent.

    Your company restricts GitHub Actions secrets.

    Developers need the Copilot coding agent to call an internal dependency-scanning API during its run. The API requires an access token.

    You need to ensure that the Copilot coding agent can use the token during execution without accessing the repository's Actions secrets and variables. The solution must prevent exposing the token in plaintext.

    What should you do?
---

- [ ] Add the token as an Actions repository secret.
- [x] Add the token as a secret in the Copilot environment.
- [ ] Store the token in a repository custom instructions file.
- [ ] Store the token in the agent configuration file.