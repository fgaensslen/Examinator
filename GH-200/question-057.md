---
question: "You are a DevOps engineer working on a custom action. You want to conditionally run a script at the start of the action, before the main entrypoint. Which code block should be used to define the metadata file for your custom action?"
documentation: "https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions"
---
- [ ] runs:
      using: 'node16'
      pre-if: github.event_name == 'push' then 'start.js'
      main: 'index.js'
- [x] runs:
      using: 'node16'
      pre: 'start.js'
      pre-if: github.event_name == 'push'
      main: 'index.js'
- [ ] runs:
      using: 'node16'
      start: 'start.js'
      start-if: github.event_name == 'push'
      main: 'index.js'
- [ ] runs:
      using: 'node16'
      before: 'start.js'
      before-if: github.event_name == 'push'
      main: 'index.js'
