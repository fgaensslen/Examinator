---
question: "As a developer, you need to use GitHub Actions to deploy a microservice that requires runtime access to a secure token. This token is used by a variety of other microservices managed by different teams in different repos. To minimize management overhead and ensure the token is secure, which mechanisms should you use to store and access the token? (Each correct answer presents a complete solution. Choose two.)"
documentation: "https://docs.github.com/en/actions/security-guides/encrypted-secrets"
---
- [ ]  Store the token as a GitHub encrypted secret in the same repo as the code. During deployment, use GitHub Actions to store the secret in an
environment variable that can be accessed at runtime.
- [x] Use a corporate non-GitHub secret store (e.g., HashiCorp Vault) to store the token. During deployment, use GitHub Actions to store the
secret in an environment variable that can be accessed at runtime.
- [x] Store the token as an organizational-level encrypted secret in GitHub. During deployment, use GitHub Actions to store the secret in an
environment variable that can be accessed at runtime.
- [] Store the token as a GitHub encrypted secret in the same repo as the code. Create a reusable custom GitHub Action to access the token by
the microservice at runtime.
- [] Store the token in a configuration file in a private repository. Use GitHub Actions to deploy the configuration file to the runtime environment.