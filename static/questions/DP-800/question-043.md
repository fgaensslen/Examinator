---
question: |
    You have a database named DB1. The schema is stored in a Git repository as an SDK-style SQL database project.

    You have a GitHub Actions workflow that already runs dotnet build and produces a database artifact.

    You need to add a deployment step that publishes the .dacpac file to an Azure SQL database by using the secrets stored in GitHub repository secrets.    

    ```yaml
    env:
      SQL_CONNECTION_STRING: Server=tcp:myserver.database.windows.net;
      ...
    steps:

    A.
      - name: Publish
        uses: azure/sql-action@v2
        with:
          action: publish
          path: bin/Debug/db1.dacpac
          connection-string: ${{ env.SQL_CONNECTION_STRING }}

    B.
      - name: Publish
        uses: azure/sql-action@v2
        with:
          action: extract
          path: bin/Debug/db1.dacpac
          connection-string: ${{ secrets.SQL_CONNECTION_STRING }}

    C.
      - name: Publish
        uses: azure/sql-action@v2
        with:
          action: publish
          path: bin/Debug/db1.dacpac
          connection-string: ${{ secrets.SQL_CONNECTION_STRING }}

    D.
      - name: Publish
        run: |
          dotnet build db1.sqlproj \
            /p:TargetConnectionString="${{ secrets.SQL_CONNECTION_STRING }}"
    ```
    
    What should you include in the workflow?
---
- [ ]A
- [ ]B
- [x]C
- [ ]D
