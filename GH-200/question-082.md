---
question: "A workflow that had been working now stalls in a waiting state until failing. The workflow file process-ml.yaml has not changed and contains jobs specifying runs-on: [gpu ]. Which of the following steps would troubleshoot the issue? (Each answer presents a complete solution. Choose two.)"
documentation: "https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners"
---
- [x] Review the contents of the Runner_*.log files in the _diag folder.
- [ ] Increase the usage limits for the GitHub-hosted runners.
- [x] Check the “Set up job” step for the logs of the last successful run to determine the runner.
- [ ] Update the org settings to enable GPU-based GitHub-hosted runners.
- [ ] Rotate the GITHUB_TOKEN secret for the appropriate runners.
