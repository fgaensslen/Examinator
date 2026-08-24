---
question: |
    You have a GitHub repository that contains an agent named Orchestrator.Orchestrator delegates work to the following specialized subagents:

    - Planner reviews issues and creates a plan of action.
    - Implementer writes code based on the plan of action.
    - Reviewer reviews the code.

    You create a new agent named Summarizer that produces a concise summary of the work performed by the other agents.

    You need to ensure that Orchestrator can invoke Summarizer as part of its workflow.

    What should you do?
---

- [ ] In the YAML frontmatter of the Reviewer agent, add a handoffs entry that points to the Summarizer agent.
- [ ] In the YAML frontmatter of the Reviewer agent, add Summarizer to the agents list.
- [ ] In the YAML frontmatter of the Orchestrator agent, add Summarizer to the tools list.
- [x] In the YAML frontmatter of the Orchestrator agent, add Summarizer to the agents list.