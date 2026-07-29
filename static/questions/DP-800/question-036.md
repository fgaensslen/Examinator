---
question: "You have a database named DB1. The schema is stored in a GitHub repository as an SDK-style SQL database project.


You use a feature branch workflow to deploy changes to DB1.
You need to update the local feature branch with the latest changes to main, and then create a pull request to merge the feature branch into main for review.


How should you complete the GitHub CLI script? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
code_lang: "CODE"
values_pool:
    - "gh pr create"
    - "gh pr merge"
    - "gh pr ready"
    - "git checkout main"
    - "git fetch origin"
    - "git merge origin/main"
    - "git pull origin main"
correct_mapping:
    blank_1: "git fetch origin"
    blank_2: "git merge origin/main"
    blank_3: "gh pr create"
---
git checkout feature/db1-add-staticdata
{blank_1}
{blank_2}
{blank_3} \
--title "Feature Update: DB1" \
--body "Apply latest improvements and updates for review" \
--head feature/db1-add-staticdata \
--base main \
--repo <GitHubOwner>/DB1 \
--web
