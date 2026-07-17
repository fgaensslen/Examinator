---
question: "When can GitHub Copilot still use content that was excluded using content exclusion?"
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---
- [ ]When the user prompts with @workspace.
- [ ]When the repository level settings allow overrides by the user.
- [ ]If the content exclusion was configured at the enterprise level, and is overwritten at the organization level.
- [x]If the contents of an excluded file are referenced in code that is not excluded, for example function calls.