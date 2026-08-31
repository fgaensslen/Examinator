# Examinator

Examinator is a local Streamlit application for studying certification questions. It discovers exam collections from Markdown files, lets you run randomized practice exams or browse every question, and provides immediate answer feedback and exam results.

The repository also contains optional utilities for converting question sources into the Markdown format used by the app.

## Features

- Automatically discovers exams under `static/questions/`
- Groups Microsoft and GitHub exams by certification area
- Runs randomized practice exams with a configurable question count
- Provides a study mode for browsing and checking questions individually
- Supports single-answer, multiple-answer, and fill-in/drag-and-drop style questions
- Displays question images, answer images, code blocks, and case studies
- Includes paginated question navigation and answer-status indicators
- Shows a score summary after a practice exam is submitted
- Saves favorite exams in the browser's local storage
- Displays the last update date for each exam collection

## Requirements

- Python 3.10 or newer
- A modern web browser

## Quick Start

1. Clone the repository and open its directory:

	```powershell
	git clone <repository-url>
	cd Examinator
	```

2. Create and activate a virtual environment:

	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	```

3. Install the application dependencies:

	```powershell
	python -m pip install -r requirements.txt
	```

4. Start the app:

	```powershell
	streamlit run app.py
	```

5. Open the local URL printed by Streamlit, usually `http://localhost:8501`.

## Using the App

The dashboard lists every exam folder containing Markdown question files.

- **Start Practice Exam** shuffles the selected exam's questions, limits the session to the number chosen with the slider, and shows results after submission.
- **Browse all questions** keeps the complete collection available and lets you check each answer immediately.
- Select the star on an exam tile to keep that exam at the top of its category. Favorites are stored only in the current browser.
- Use the sidebar during a session to jump between questions or return to the dashboard.

Question order and answer-choice order are randomized when applicable. Session progress is held in Streamlit session state and resets when a new session is started or the browser session is cleared.

## Adding an Exam

Create a directory named after the exam and add one Markdown file per question:

```text
static/questions/
└── AZ-900/
	 ├── question-001.md
	 ├── question-002.md
	 └── question-003.md
```

The folder appears on the dashboard automatically. To show its update date, add an entry to `static/last_update.md`:

```markdown
# AZ-900
31.08.2026
```

### Standard Questions

Use YAML frontmatter for the question and Markdown task-list items for the answers. Mark every correct answer with `[x]`; multiple checked items create a multiple-answer question.

```markdown
---
question: "Which option is correct?"
---

- [ ] A. First option
- [x] B. Second option
- [ ] C. Third option
```

Question text can also be placed in the Markdown body. Relative image paths are resolved from the exam folder. An optional answer image named after the question, such as `question-001_answer.png`, is displayed with the answer feedback.

### Fill-In Questions

Use `question_type: "drag_drop"`, define the available values, and map each placeholder to its correct value:

```markdown
---
question: "Complete the query."
question_type: "drag_drop"
values_pool:
  - "CustomerId"
  - "CreatedAt"
correct_mapping:
  blank_1: "CustomerId"
---

SELECT {blank_1}
FROM Customers;
```

Set `code_lang` in the frontmatter when explicit rendering is needed; 
`code_lang = "SQL"` and `code_lang = "JSON"` can be used for explicit code rendering. Use `code_lang =  "TEXT"` to disable code rendering.

### Case Studies

Case-study files belong in an exam's `case_studies/` directory. The parser uses top-level `#` headings as dialog tabs and can associate the case study with questions through its YAML metadata. Images referenced by the case study should be stored in the same directory.

## Project Structure

```text
Examinator/
├── app.py              # Streamlit views and quiz interactions
├── config.py           # Paths and UI defaults
├── helpers.py          # Shared rendering and answer helpers
├── parsers.py          # Code-language and case-study parsing
├── state.py            # Session state and browser favorites
├── styles.py           # Application CSS
├── utils.py            # Exam discovery and question loading
├── requirements.txt    # Runtime dependencies
├── scripts/            # Optional content-import utilities
└── static/
	 ├── last_update.md
	 └── questions/      # Exam folders and question assets
```

## Content Import Utilities

The scripts in `scripts/` are described below and can be used to extract questions from the Examtopics website.

Some import tools need additional packages:

```powershell
python -m pip install playwright pypdf pillow
python -m playwright install chromium
```

### Web Import Workflow
1. Search for the corresponding certification, for example `site:examtopics.com/discussions/microsoft/view "exam dp-800"` or `site:examtopics.com/discussions/appian/view "exam ACD101"`

2. Right-click on your browser's bookmarks bar > "Add Page" > enter a name and paste the following script into the URL field. When you click this bookmark, the source code of the current page will be downloaded to a `google_source.txt` file.
```
javascript:(function(){const blob=new Blob([document.documentElement.outerHTML],{type:'text/html'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='google_source.txt';document.body.appendChild(a);a.click();document.body.removeChild(a);})();
```
3. Now run the script `1_Parse_Google_Results.py`. Repeat for all search pages. At the end, all links will be saved in an `extracted_links.txt` file.
4. It's possible that some links are not available through the Google search. Therefore, run the script `2_Create_Missing_URLS.py` and the missing links will be added to the existing file.
5. Run script `3_Examtopic_Extractor.py` and write the content of all links to an `exam_content.txt` file and extract images to an `exam_images` folder
6. Run script `Export_to_Markdown.py` to extract each question from `exam_content.txt` into its own Markdown file

Run a script from the repository root with, for example:

```powershell
python .\scripts\1_Parse_Google_Results.py
```

### PDF Import Workflow

`scripts/Pdf_Extractor.py` extracts question text and embedded images from a PDF and packages the generated Markdown files in a ZIP archive. Update the source PDF and destination ZIP paths in its `package_study_materials(...)` call before running it:

```powershell
python .\scripts\Pdf_Extractor.py
```

PDF extraction is format-dependent. Always inspect the generated questions, answer mappings, and image placement before adding them to the app.

## Configuration

Application defaults are defined in `config.py`:

- `ITEMS_PER_PAGE` controls sidebar pagination.
- `DEFAULT_QUESTIONS` controls the initial practice-exam length.
- `MAX_QUESTIONS_LOAD` can limit loaded questions during development when supported by the loader.