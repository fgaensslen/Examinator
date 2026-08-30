# Examtopics.com Extractor
1. Suchen nach der entsprechenden Zertifizierung, zum Beispiel `site:examtopics.com/discussions/microsoft/view "exam dp-800"` oder `site:examtopics.com/discussions/appian/view "exam ACD101"`

2. Auf die Bookmarkleiste des Browsers rechtsklicken > "Seite hinzufügen" > einen Namen eingeben und folgendes Script in die URL-Zeile eintragen. Beim Klicken dieses Bookmarks wird der Source-Code der aktuellen Seite in eine `google_source.txt` Datei heruntergeladen.
```
javascript:(function(){const blob=new Blob([document.documentElement.outerHTML],{type:'text/html'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='google_source.txt';document.body.appendChild(a);a.click();document.body.removeChild(a);})();
```
3. Nun das Script `1_Parse_Google_Results.py` ausführen. Für alle Suchseiten wiederholen. Am Ende werden alle Links in einer `extracted_links.txt` Datei gespeichert.
4. Unter Umständen kann es sein, dass einige Links nicht über die Google-Suche verfügbar sind. Deshalb das Script `2_Create_Missing_URLS.py` ausführen und die fehlenden Links werden in der vorhandenen Datei ergänzt.
5. Ausführen von Script `3_Examtopic_Extractor.py` und den Content aller Links in eine `exam_content.txt` schreiben und Bilder in einen `exam_images` extrahieren
6. Ausführen von Script `Export_to_Markdown.py` um jede Frage aus `exam_content.txt` in eine eigene Markdown-Datei zu extrahieren

# Pdf Extractor
Im Script `Pdf_Extractor.py` die Pfade zur Quelle und Ziel entsprechend anpassend und einfach ausführen