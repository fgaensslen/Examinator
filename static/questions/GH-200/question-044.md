---
question: "As a DevOps engineer, you are developing workflows to build an application. You have a requirement to create the build targeting multiple node versions. Which code block should you use to define the workflow?"
documentation: "https://docs.github.com/en/actions/learn-github-actions/contexts#github-context"
---
- [x] jobs:
      build-app:
        strategy:
          matrix:
            node-ver: [10, 12, 14]
        steps:
          - uses: actions/setup-node@v3
            with:
              node-version: ${{ matrix.node-ver }}
- [ ] jobs:
      build-app:
        matrix-strategy:
          node-vers: [10, 12, 14]
        steps:
          - uses: actions/setup-node@v3
            with:
              node-version: ${{ matrix-strategy.node-ver }}
- [ ] jobs:
      build-app:
        matrix:
          strategy:
            node-ver: [10, 12, 14]
        steps:
          - uses: actions/setup-node@v3
            with:
              node-version: ${{ matrix.node-ver }}
- [ ] jobs:
      build-app:
        strategy:
          matrix:
            node-vers: [10, 12, 14]
        steps:
          - uses: actions/setup-node@v3
            with:
              node-version: ${{ strategy.matrix.node-ver }}
