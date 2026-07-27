---
question: "You are a DevOps engineer working on deployment workflows. You need to execute the deploy job only if the current branch name is feature branch. Which code snippet will help you to implement the conditional execution of the job?"
documentation: "https://docs.github.com/en/actions/learn-github-actions/contexts#github-context"
---
- [x] jobs: deploy: if: github.ref_name == 'feature-branch' runs-on: ubuntu-latest steps: - uses: actions/checkout@v3
- [ ] jobs: deploy: if: github.branch.name == 'feature-branch' runs-on: ubuntu-latest steps: - uses: actions/checkout@v3
- [ ] jobs: deploy: if: github.ref.name == 'feature-branch' runs-on: ubuntu-latest steps: - uses: actions/checkout@v3
- [ ] jobs: deploy: if: github.branch_name == 'feature-branch' runs-on: ubuntu-latest steps: - uses: actions/checkout@v3
