---
question: "As a developer, you are optimizing a GitHub workflow that uses and produces many different files. You need to determine when to use caching versus workflow artifacts. Which two statements are true? (Each correct answer presents part of the solution. Choose two.)"
documentation: "https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners"
---
- [ ] Use artifacts to access the GitHub Package Registry and download a package for a workflow.
- [x] Use caching when reusing files that change rarely between jobs or workflow runs.
- [ ] Use caching to store cache entries for up to 30 days between accesses.
- [x] Use artifacts when referencing files produced by a job after a workflow has ended.
