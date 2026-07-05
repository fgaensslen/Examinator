---
question: "Which step is using the dbserver environment variable correctly?"
documentation: "https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsenv"
---
- [ ] steps: - name: Hello world run: echo $dbserver variables: dbserver: orgserver1
- [ ] steps: - name: Hello world run: echo $dbserver env: - name: dbserver value: orgserver1
- [ ] steps: - name: Hello world run: echo $dbserver environment: dbserver: orgserver1
- [x] steps: - name: Hello world run: echo $dbserver env: dbserver: orgserver1
