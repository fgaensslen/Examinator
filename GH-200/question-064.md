---
question: "In the following workflow file, line 5 interprets lines 3 and 4 as Python. Which of the following is a valid option to complete line 5? 1 steps: 2 - run: | 3 import os 4 print(os.environ['PATH']) 5"
documentation: "https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsrun"
---
- [x] shell: python
- [ ] working-directory: .github/python
- [ ] shell: bash
- [ ] with: python
