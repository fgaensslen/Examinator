# Pdf Extractor
Im Script `Pdf_Extractor.py` die Pfade zur Quelle und Ziel entsprechend anpassend und einfach ausführen.

# Examtopics.com Extractor
1. Suchen nach der entsprechenden Zertifizierung, zum Beispiel `site:examtopics.com/discussions/microsoft/view "exam dp-800"` oder `site:examtopics.com/discussions/appian/view "exam ACD101"`

2. Auf die Bookmarkleiste des Browsers rechtsklicken > "Seite hinzufügen" > einen Namen eingeben und folgendes Script in die URL-Zeile eintragen. Beim Klicken dieses Bookmarks wird der Source-Code der aktuellen Seite in eine `google_source.txt` Datei heruntergeladen.
```
javascript:(function(){const blob=new Blob([document.documentElement.outerHTML],{type:'text/html'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='google_source.txt';document.body.appendChild(a);a.click();document.body.removeChild(a);})();
```
3. Nun das `Parse_Google_Results.py` Script ausführen. Für alle Suchseiten wiederholen. Am Ende werden alle Links in einer `extracted_links.txt` Datei gespeichert.
4. Ausführen von Script `Examtopic_Extractor.py` und den Content aller Links in eine `exam_content.txt` schreiben und Bilder in einen ``exam_images`` extrahieren
5. Ausführen von Script `Export_to_Markdown.py` um jede Frage aus `exam_content.txt` in eine eigene Markdown-Datei zu extrahieren