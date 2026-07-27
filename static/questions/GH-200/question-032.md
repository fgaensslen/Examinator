---
question: "You need to make a script to retrieve workflow run logs via the API. Which is the correct API to download a workflow run log?"
documentation: "https://docs.github.com/en/rest/actions/workflow-runs#download-workflow-run-logs"
---
- [ ] POST /repos/:owner/:repo/actions/runs/:run_id/logs
- [x] GET /repos/:owner/:repo/actions/runs/:run_id/logs
- [ ] POST /repos/:owner/:repo/actions/runs/:run_id
- [ ] GET /repos/:owner/:repo/actions/artifacts/logs
