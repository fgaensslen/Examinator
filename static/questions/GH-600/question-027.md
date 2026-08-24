---
question: |
    You have a multi-agent GitHub Actions workflow that uploads review artifacts for each run.

    You discover that some workflow run artifacts are being deleted manually.
    
    You need to use your organization's audit log data to identify which user deleted the artifacts.

    Which audit log search filter should you use?
---

- [ ] repo:<org>/<repo>
- [ ] action:workflows.run
- [ ] operation:remove
- [x] action:artifact.destroy