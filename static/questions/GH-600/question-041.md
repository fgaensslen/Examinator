---
question: |
    You have a GitHub Enterprise Cloud repository that uses the GitHub Copilot coding agent.

    Engineers assign issues to Copilot, and Copilot creates draft pull requests. The engineers start tasks either by assigning issues on github.com or by using GitHub Copilot Chat in an IDE. Reviewers request updates by leaving pull request comments.

    You discover that sometimes, Copilot uses outdated requirements after a reviewer posts an updated instruction in a pull request comment, and, in several cases, Copilot fails to resume work from the comment.

    You need to ensure that iteration requests are applied to the correct pull request session and are processed consistently.

    What should you do?
---

- [x] Ensure that the reviewer has write access to the repository. Instruct the reviewer to mention @copilot in the pull request comments.
- [ ] Ensure that the agent has write access to the repository. Instruct the reviewer to mention @github in the task comments.
- [ ] Ensure that the agent has write access to the repository. Instruct the reviewer to unassign and reassign the original issue to Copilot.
- [ ] Start a new task from Copilot Chat in the IDE. Instruct the reviewer to mention @github in the task comments.