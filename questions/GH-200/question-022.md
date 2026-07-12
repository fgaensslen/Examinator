---
question: "As a developer, one of your workflows will require XCode version 11.2 hosted on macOS Catalina (i.e., v10.15). You’ve already created and configured a self-hosted runner to conform to those requirements and registered it with your organization. What else should you do to ensure that the workflow accesses the correct runner instance? (Each answer presents a complete solution. Choose three.)"
documentation: "https://docs.github.com/en/actions/hosting-your-own-runners/using-labels-with-self-hosted-runners"
---
- [ ] Add your runner to the appropriate runner groups.
- [ ] In the workflow, specify: runs-on: [ ${{groups.macos-10.15}}, ${{groups.xcode-11.2}} ].
- [x] Create custom runner labels for macos-10.15 and xcode-11.2.
- [ ] Create runner groups named macos-10.15 and xcode-11.2.
- [x] In the workflow, specify: runs-on: [self-hosted, macos-10.15, xcode-11.2].
- [x] Assign the custom labels to the self-hosted runner.
