---
question: "Which command can you include in your workflow file to set the output parameter for an action?"
documentation: "https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-environment-variable"
---
- [ ] echo "action_color=purple" >> $GITHUB_ENV
- [ ] echo "::debug::action_color=purple"
- [ ] echo "::add-mask::$ACTI0N_C0L0R"
- [x] echo "action_color=purple" >> $GITHUB_OUTPUT
