---
question: "As a DevOps engineer, you need to execute a deployment to different environments like development and testing based on the labels added to a pull request. The deployment should use the releases branch and trigger only when there is a change in the files under ‘apps’ folder. Which code block should be used to define the deployment workflow trigger?"
documentation: "https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows"
---
- [ ] on:
      pull_request_label:
        branches:
          - 'releases'
        paths:
          - 'apps/**'
- [ ] on:
      pull_request:
        types: [labeled]
        branches:
          - 'releases/**'
        paths:
          - 'apps'
- [x] on:
      pull_request:
        types: [labeled]
        branches:
          - 'releases'
        paths:
          - 'apps/**'
- [ ] on:
      pull_request_review:
        types: [labeled]
        branches:
          - 'releases'
        paths:
          - 'apps/**'
