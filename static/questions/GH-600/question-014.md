---
question: |
    You use a GitHub Actions workflow to orchestrate a multi-agent draft-review process for pull requests. The workflow uploads a single combined review-package artifact at the end of each run.

    You discover that the review-package artifact is occasionally missing from the workflow run history, and you suspect that a user deleted it.

    You need to identify which user manually deleted a workflow run artifact and when the deletion occurred.

    What should you use?
---

- [ ] the checks.delete_logs audit log event
- [ ] the pull request description and comment history
- [ ] the merge commit history
- [x] the artifact.destroy audit log event