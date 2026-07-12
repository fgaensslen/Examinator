---
question: "As a developer, you are authoring a workflow that will deploy to both DevCloud and TestCloud resources. Each cloud resource is accessed with a different deployment key. Which approach best allows you to use the same reusable workflow in separate jobs to target the different cloud resources?"
documentation: "https://docs.github.com/en/actions/security-guides/encrypted-secrets"
---
- [ ] Populate a DEPLOY_KEY repository secret with a JSON object containing DevCloud and TestCloud properties. Then specify DEPLOY_KEY.DevCloud in the secrets sections of the reusable workflow.
- [ ] Use a marketplace action to conditionally parse the DEPLOY_KEY repository secret based on the cloud resource name.
- [x] Store the different keys in a DEPLOY_KEY environment secret in the DevCloud and TestCloud environments. Specify DEPLOY_KEY in the secrets section of the reusable workflow.
- [ ] Create repository secrets named DevCloud.DEPLOY_KEY and TestCloud.DEPLOY_KEY so that the workflow targets different cloud resources.
