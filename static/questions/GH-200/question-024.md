---
question: "You are a DevOps engineer in ABC Corp. You need to schedule your deployment workflow twice a week at 7:45 UTC every Wednesday and Saturday. What is the appropriate YAML structure?"
documentation: "https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule"
---
- [ ] on:
      cron: '45 7 * * 3,6'
- [ ] on:
      cron:
        - schedule: '45 7 * * 3,6'
- [x] on:
      schedule:
        - cron: '45 7 * * 3,6'
- [ ] on:
      schedule: '45 7 * * 3,6'
