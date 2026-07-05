---
question: "Which syntax correctly accesses a job output (output1) of an upstream job (job1) from a dependent job within a workflow?"
documentation: "https://docs.github.com/en/actions/learn-github-actions/contexts"
---
- [x] ${{needs.job1.outputs.output1}}
- [ ] ${{needs.job1.output1}}
- [ ] ${{depends.job1.output1}}
- [ ] ${{job1.outputs.output1}}
