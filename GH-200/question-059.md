---
question: "As a developer, your Actions workflow often reuses the same outputs or downloaded dependencies from one run to another. To cache dependencies for a job, you are using the GitHub cache action. Which input parameters are required for this action? (Each correct answer presents part of the solution. Choose two.)"
documentation: "https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners"
---
- [x] path: the file path on the runner to cache or restore
- [ ] dependency: the name and version of a package to cache or restore
- [x] key: the key created when saving a cache and the key used to search for a cache
- [ ] restore-keys: the copy action key used with cache parameter to cache the data
- [ ] cache-hit: the copy action key used with restore parameter to restore the data from the cache
- [ ] ref: the ref name of the branch to access and restore a cache created
