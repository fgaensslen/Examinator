---
question: |
    You have a private GitHub repository that has Copilot memory enabled.

    Several developers who have write access to the repository make changes across multiple branches, including creating some pull requests that are later closed without merging.

    Your team needs to understand how GitHub Copilot ensures that only task-relevant, up-to-date information influences code suggestions, even when older memories exist.

    How does Copilot manage memories?
---

- [x] Copilot validates each memory's citations against the current branch before using the memory, and ignores the memory if the referenced code no longer exists.
- [ ] Copilot stores memories per user, ensuring that only the developer who created a memory can trigger the memory in future sessions.
- [ ] Copilot stores memories indefinitely until a repository administrator deletes them manually.
- [ ] Copilot automatically blocks memory creation from pull requests that are closed without merging, to prevent outdated information from being stored.