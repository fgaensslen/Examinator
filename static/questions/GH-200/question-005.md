---
question: "As a developer, you need to leverage Redis in your workflow. What is the best way to use Redis on a self-hosted Linux runner without affecting future workflow runs?"
documentation: "https://docs.github.com/en/actions/using-containerized-jobs/about-service-containers"
---
- [ ] Install Redis on the hosted runner image and place it in a runner group. Specify label: in your job to target the runner group.
- [ ] Set up Redis on a separate machine and reference that instance from your job.
- [x] Specify container and services: in your job definition to leverage a Redis service container.
- [ ] Add a run step to your workflow, which dynamically installs and configures Redis as part of your job.
