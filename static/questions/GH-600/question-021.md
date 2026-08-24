---
question: |
    You have a GitHub Enterprise repository that runs an autonomous agent by using a GitHub Actions workflow. 
    
    The workflow has the following jobs: agent-run that generates trace.json and plan.md review that waits for human approval before continuing deploy that uses the outputs from agent-run

    You need to make the files inspectable in the GitHub Actions UI and ensure that the files are available to the review and deploy jobs.

    What should you do in the workflow?
---

- [ ] Use dependency caching to store trace.json and plan.md.
- [x] Upload trace.json and plan.md as workflow artifacts in agent-run, and download the files inside the jobs.
- [ ] Commit trace.json and plan.md back to the repository from agent-run.
- [ ] Store trace.json and plan.md on a network share and have later jobs retrieve them from the share.