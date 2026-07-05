---
question: "A single secret must be accessed by workflows in specific repositories. What is the best way to create the secret?"
documentation: "https://docs.github.com/en/actions/security-guides/encrypted-secrets"
---
- [ ] Create an environment secret at the organization level and leverage that environment in each of the specified repositories.
- [x] Create an organization secret, specify Selected repositories as the Repository access, and select the required repositories.
- [ ] Create the secret in one of the repositories, check the Share secret option, and select the required repositories.
- [ ] Store the secret in a supported external key vault. Configure OpenID Connect (OIDC) to allow access to the external vault and link the secret from the external key vault in each of the specific repositories.
