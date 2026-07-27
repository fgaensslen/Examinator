---
question: "How can a workflow deploy mitigate the risk of multiple workflow runs that are deploying to a single cloud environment simultaneously? (Each correct answer presents part of the solution. Choose two.)"
documentation: "https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#concurrency"
---
- [ ] Reference the mutex in the task performing the deployment.
- [ ] Set the concurrency in the deploymentjob to 1.
- [x] Specify a target environment in the deploymentjob.
- [x] Specify a concurrency scope in the workflow.
- [ ] Configure the mutex setting in the environment.
- [ ] Pass the mutex into the deployment job.
