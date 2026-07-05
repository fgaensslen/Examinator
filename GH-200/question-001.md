---
question: "How should you print a debug message in your workflow?"
documentation: "https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-a-debug-message"
---
- [x] echo "::debug::Set variable myVariable to true"
- [ ] echo "Set variable MyVariable to true" >> $DEBUG_MESSAGE
- [ ] echo "::add-mask::Set variable myVariable to true"
- [ ] echo "debug_message=Set variable myVariable to true" >> &GITHUB_OUTPUT
