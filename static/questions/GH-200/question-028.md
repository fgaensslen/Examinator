---
question: "Which of the following scenarios requires a developer to explicitly use the GITHUB_TOKEN or github.token secret within a workflow? (Choose two.)"
documentation: "https://docs.github.com/en/actions/security-guides/automatic-token-authentication"
---
- [x] passing the GITHUB_TOKEN secret to an action that requires a token as an input
- [x] making an authenticated GitHub API request
- [ ] checking out source code with the actions/checkout@v3 action
- [ ] assigning non-default permissions to the GITHUB_TOKEN
