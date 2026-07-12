---
question: "You installed specific software on a Linux self-hosted runner. You have users with workflows that need to be able to select the runner based on the identified custom software. Which steps should you perform to prepare the runner and your users to run these workflows? (Each correct answer presents part of the solution. Choose two.)"
documentation: "https://docs.github.com/en/actions/hosting-your-own-runners/using-labels-with-self-hosted-runners"
---
- [ ] Configure the webhook and network to enable GitHub to trigger workflow.
- [ ] Create the group custom-software-on-linux and move the runner into the group.
- [x] Inform users to identify the runner with the labels custom-software and linux.
- [ ] Add the label linux to the runner.
- [ ] Inform users to identify the runner based on the group.
- [x] Add the label custom-software to the runner.
