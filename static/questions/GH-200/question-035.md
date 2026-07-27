---
question: "What is the proper syntax to reference the system-provided run number variable?"
documentation: "https://docs.github.com/en/actions/learn-github-actions/contexts"
---
- [ ] ${{var.GITHUB_RUN_NUMBER}}
- [ ] ${{env.GITHUB_RUN_NUMBER}}
- [ ] $GITHUB_RUN_NUMBER
- [x] ${{GITHUB_RUN_NUMBER}}
- [ ] $github.run_number
