---
question: "Which of the following commands will set the $FOO environment variable within a script, so that it may be used in subsequent workflow job steps?"
documentation: "https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-environment-variable"
---
- [ ] run: echo "::set-env name=FOO::bar"
- [x] run: echo "FOO=bar" >> $GITHUB_ENV
- [ ] run: echo ${{ $FOO=bar }}
- [ ] run: export FOO=bar
