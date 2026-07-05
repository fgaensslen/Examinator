1. Suchen nach der entsprechenden Zertifizierung, zum Beispiel site:examtopics.com/discussions/microsoft/view "exam dp-800" oder site:examtopics.com/discussions/appian/view "exam ACD101"
2. Den Source-Code der Suchseiten einzeln durchgehen und den Inhalt jedes Mal in eine google_source.txt kopieren. Dann das "Parse_Google_Results.py" Script ausführen. Für alle Suchseiten wiederholen
3. Die erzeugte links.txt Datei enthält evtl. strings, welche nach "-discussion/" bereinigt werden müssen. Dafür auf RegEx umstellen, Suchen nach "(-discussion/).*" und Replace "$1"
4. Bereinigen von Duplikaten mit diesem PowerShell command: Get-Content links.txt | Select-Object -Unique | Set-Content clean_links.txt
5. Ausführen von Script "Examtopic_Extractor.py" und den Content aller Links in eine exam_content.txt schreiben
6. Ausführen von Scripts "Export_to_Markdown.py" um jede Frage aus exam_content.txt in eine eigene Markdown-Datei zu extrahieren