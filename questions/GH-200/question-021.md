---
question: "Your organization is managing secrets using GitHub encrypted secrets, including a secret named SuperSecret. As a developer, you need to create a version of that secret that contains a different value for use in a workflow that is scoped to a specific repository named MyRepo. How should you store the secret to access your specific version within your workflow?"
documentation: "https://docs.github.com/en/actions/security-guides/encrypted-secrets"
---
- [ ] Create MyRepo_SuperSecret in GitHub encrypted secrets to specify the scope to MyRepo.
- [ ] Create a duplicate entry for SuperSecret in the encrypted secret store and specify MyRepo as the scope.
- [ ] Create a file with the SuperSecret information in the .github/secrets folder in MyRepo.
- [x] Create and access SuperSecret from the secrets store in MyRepo.