---
question: |
    You need to resolve the issue of the agents generating conflicting output. The solution must meet the implementation guidelines.

    What should you do?
---

- [ ] Add shared/config.yaml to a CODEOWNERS file that requires SG_Review approval before any changes can be merged.
- [x] Configure each agent to work on a separate branch and add a required status check that detects file-level overlap before either pull request can be merged.
- [ ] Configure tools: ['read', 'search'] in both agent profiles to prevent either agent from writing files.
- [ ] Configure a concurrency group on both agent workflows so that only one workflow runs at a time.