---
question: "You are a DevOps engineer working on custom Actions development. You need to handle the errors or exceptions as part of the JavaScript based action code. What should be added to the following code block to handle errors? const core = require('@actions/core'); try { // action code } catch (error) { << insert snippet here >> }"
documentation: "https://docs.github.com/en/actions/creating-actions/creating-a-javascript-action"
---
- [ ] core.setException(error.message);
- [ ] action.setError(error.message);
- [x] core.setFailed(error.message);
- [ ] core.action.setException(error.message);
