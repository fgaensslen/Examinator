import os
import re
import zipfile
import pypdf
from PIL import Image
import io
import shutil

def get_documentation_url(question_text):
    """Basic keyword-based mapping for documentation links."""
    mappings = {
        "AI": "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai",
        "JSON": "https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server",
        "T-SQL": "https://learn.microsoft.com/en-us/sql/t-sql/language-elements/try-catch-transact-sql",
        "GitHub": "https://docs.github.com/en/actions"
    }
    for keyword, url in mappings.items():
        if keyword in question_text:
            return url
    return "https://learn.microsoft.com/en-us/azure/"

def extract_content(pdf_path, temp_dir):
    """
    Parses questions with a robust regex to capture all 59+ items.
    """
    reader = pypdf.PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    # Regex captures variations of "Question #X" or "Topic X Question #X"
    pattern = r'(?i)(?:Question\s+#\s*\d+|Topic\s+\d+\s*Question\s+#\s*\d+)'
    parts = re.split(pattern, full_text)
    headers = re.findall(pattern, full_text)
    
    questions = []
    # Skip the first element if it contains only pre-amble text
    for i, content in enumerate(parts[1:]):
        lines = [l.strip() for l in content.split('\n') if l.strip()]
        
        suggested = ""
        final_lines = []
        for line in lines:
            if "Suggested Answer:" in line:
                suggested = re.sub(r'.*Suggested Answer:', '', line).strip()
            else:
                final_lines.append(line)
        
        q_body = []
        options = []
        for line in final_lines:
            # Matches A., B., C., etc.
            if re.match(r'^[A-E]\.\s+', line):
                options.append(line)
            else:
                q_body.append(line)
        
        questions.append({
            "id": headers[i] if i < len(headers) else f"Question #{i+1}",
            "question": " ".join(q_body).strip(),
            "options": options,
            "answer": suggested
        })

    # Image Extraction
    for page_num, page in enumerate(reader.pages):
        if "/XObject" in page.get("/Resources", {}):
            xObject = page["/Resources"]["/XObject"].get_object()
            for obj in xObject:
                if xObject[obj].get("/Subtype") == "/Image":
                    try:
                        data = xObject[obj].get_data()
                        img = Image.open(io.BytesIO(data))
                        img.save(os.path.join(temp_dir, f"page_{page_num+1}_img_{obj[1:]}.png"))
                    except Exception: 
                        continue
                    
    return questions

def package_study_materials(pdf_path, output_zip_path):
    temp_dir = "temp_study_pack"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir, exist_ok=True)
    
    questions = extract_content(pdf_path, temp_dir)
    
    for q in questions:
        # Create sanitized filename
        file_name = f"{q['id'].replace(' ', '_').replace('#', '').replace(':', '')}.md"
        with open(os.path.join(temp_dir, file_name), "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f'question: "{q["question"]}"\n')
            f.write(f'documentation: "{get_documentation_url(q["question"])}"\n')
            f.write("---\n\n")
            
            # Write Options with formatting
            for opt in q['options']:
                # Extract the letter (e.g., 'A') to check correctness
                letter = opt[0]
                is_correct = letter in q['answer']
                f.write(f"- [{'x' if is_correct else ' '}] {opt}\n")
            
    # Zip everything
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)
                
    shutil.rmtree(temp_dir)
    print(f"Success! Created {len(questions)} question files in: {output_zip_path}")

if __name__ == "__main__":
    package_study_materials(
        r"C:\Users\Florian\OneDrive\Braindumps Zertifizierungen\DP-800\DP-800_Answers.pdf", 
        r"C:\Users\Florian\Downloads\Final_Study_Pack.zip"
    )