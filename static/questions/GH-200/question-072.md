---
question: "While writing a custom action, some behavior within the runner must be changed. Which workflow commands would set an error message in the runner’s output? (Each correct answer presents a complete solution. Choose two.)"
documentation: "https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions"
---
- [x] echo "::error file=main.py,line=10,col=15::There was an error"
- [ ] echo "::error=There was an error::"
- [x] echo "::error::There was an error"
- [ ] echo "::error message=There was an error::"
