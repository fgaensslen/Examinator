---
question: "Which scopes are available to define custom environment variables within a workflow file? (Choose three.)"
documentation: "https://docs.github.com/en/actions/learn-github-actions/variables"
---
- [x] the entire workflow, by using env at the top level of the workflow file
- [ ] all jobs being run on a single Actions runner, by using runner.env at the top of the workflow file
- [ ] the entire stage, by using env at the top of the defined build stage
- [ ] within the run attribute of a job step
- [x] the contents of a job within a workflow, by using jobs.env
- [x] a specific step within a job, by using jobs.<job_id>.steps[*].env
