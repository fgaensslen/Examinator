---
question: "As a developer, which of the following snippets will enable you to run the commands npm ci and npm run build as part of a workflow?"
documentation: "https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsrun"
---
- [x] - run: |
        npm ci
        npm run build
- [ ] - shell:
        npm ci
        npm run build
- [ ] - run: |
        npm ci
        npm run build
      shell: nodejs
- [ ] - run:
        npm ci
        npm run build
- [ ] - shell: |
        npm ci
        npm run build
