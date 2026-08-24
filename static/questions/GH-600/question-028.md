---
question: |
    You have a GitHub Copilot coding agent named Orchestrator that runs a multi-phase workflow by using the following subagents:

    - Explorer gathers context by using read-only tools.
    Modifier applies focused edits.
    - You are adding a new agent named Summarizer that generates a concise summary after modifications are complete. Summarizer includes the following YAML frontmatter.
    ![](question-028.png)

    The Orchestrator agent lists all three agents in its agents property.

    After adding the Summarizer agent, Orchestrator successfully runs Explorer and Modifier but fails to run Summarizer.

    What is a possible cause of the failure?
---

- [ ] Summarizer cannot be invoked as a subagent because disable-model-invocation is set to true.
- [x] Orchestrator is missing a handoff entry to trigger Summarizer.
- [ ] Orchestrator cannot call Summarizer because user-invocable is set to false.
- [ ] Summarizer is missing the editing tools required to complete the workflow.