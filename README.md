# Examtopics.com Extractor
1. Search for the corresponding certification, for example `site:examtopics.com/discussions/microsoft/view "exam dp-800"` or `site:examtopics.com/discussions/appian/view "exam ACD101"`

2. Right-click on your browser's bookmarks bar > "Add Page" > enter a name and paste the following script into the URL field. When you click this bookmark, the source code of the current page will be downloaded to a `google_source.txt` file.
```
javascript:(function(){const blob=new Blob([document.documentElement.outerHTML],{type:'text/html'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='google_source.txt';document.body.appendChild(a);a.click();document.body.removeChild(a);})();
```
3. Now run the script `1_Parse_Google_Results.py`. Repeat for all search pages. At the end, all links will be saved in an `extracted_links.txt` file.
4. It's possible that some links are not available through the Google search. Therefore, run the script `2_Create_Missing_URLS.py` and the missing links will be added to the existing file.
5. Run script `3_Examtopic_Extractor.py` and write the content of all links to an `exam_content.txt` file and extract images to an `exam_images` folder
6. Run script `Export_to_Markdown.py` to extract each question from `exam_content.txt` into its own Markdown file

# PDF Extractor
In the script `Pdf_Extractor.py`, adjust the paths for source and destination accordingly and simply execute it