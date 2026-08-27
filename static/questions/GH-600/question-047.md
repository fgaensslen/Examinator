---
question: |
    You need to resolve the scoping issue associated to agent1.

    What should you do?
---

- [ ] To the profile of agent1, add a custom instruction specifying that the agent must NOT access billing-service or infra-terraform.
- [ ] Add a permissions block to the agent1 workflow in product-api.
- [x] Create a fine-grained personal access token (PAT) scoped to product-api and store the PAT as a GitHub Actions secret for agent1 to use.
- [ ] Create a ruleset for billing-service and infra-terraform that blocks push access from the github-actions bot account.