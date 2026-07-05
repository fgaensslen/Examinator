---
question: "As a developer, you need to add the correct syntax to allow the following workflow file to be triggered by multiple types of events. Which two code blocks should you add starting at line 5? (Each correct answer presents a complete solution. Choose two.)"
documentation: "https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows"
---
- [x] on: [push, pull_request]
- [ ] on:
      branches:
        - 'main'
        - 'dev'
- [ ] on:
      schedule:
        - cron: '*/15 * * * *'
      initiate:
        - 'main'
- [ ] on: [push, commit]
- [x] on:
      push:
        branches:
          - main
      release:
        types:
          - created
- [ ] on:
      env:
        - 'prod'
        - 'qa'
        - 'test'
