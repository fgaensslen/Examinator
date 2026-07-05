import os
import re

INPUT_FILE = r"C:\Users\Florian\Downloads\exam_content.txt"
OUTPUT_DIR = r"C:\Users\Florian\Downloads\GH-300_Quiz_Files"

def parse_sequentially():
    if not os.path.exists(INPUT_FILE):
        print(f"[-] Error: '{INPUT_FILE}' not found.")
        return
        
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Read and normalize all line endings to prevent OS rendering mismatches
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        full_text = f.read().replace('\r\n', '\n')
        
    # Isolate blocks using the distinct URL boundary strings
    sections = re.split(r'={40}\nURL: .*?\n={40}', full_text)
    urls = re.findall(r'={40}\nURL: (.*?)\n={40}', full_text)
    
    if len(sections) > len(urls):
        sections = sections[1:]
        
    print(f"[*] Processing {len(sections)} text dumps into unique files...")
    
    saved_count = 0
    # Use a strict sequential counter (1 to 113) so filenames never overwrite each other
    for sequential_id, (url, content) in enumerate(zip(urls, sections), 1):
        content = content.strip()
        if not content:
            continue
            
        # Format filename directly from the absolute index placement (question-001.md through question-113.md)
        filename = f"question-{str(sequential_id).zfill(3)}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Isolate question body text safely
        question_text = ""
        q_block_match = re.search(r'\[All GH-300 Questions\]\s*\n(.*?)\n\s*A\.', content, re.DOTALL)
        if not q_block_match:
            q_block_match = re.search(r'Question #:\s*\d+\s*\nTopic #:\s*\d+\s*\n(.*?)\n\s*A\.', content, re.DOTALL)
            
        if q_block_match:
            question_text = q_block_match.group(1).strip().replace('"', '\\"')
        else:
            question_text = "Context extraction placeholder"
            
        # Extract multiple choices cleanly (handles both 4-choice and 5-choice profiles)
        choices = []
        for letter in ['A', 'B', 'C', 'D', 'E']:
            choice_match = re.search(rf'^\s*{letter}\.\s*(.*?)$', content, re.MULTILINE)
            if choice_match:
                choices.append((letter, choice_match.group(1).strip()))
                
        # Calculate community vote alignment 
        votes = re.findall(r'Selected Answer:\s*([A-Ea-e]+)', content)
        clean_votes = []
        for v in votes:
            clean_votes.extend([char.upper() for char in v if char.upper() in 'ABCDE'])
            
        if clean_votes:
            correct_letter = max(set(clean_votes), key=clean_votes.count)
        else:
            correct_letter = "B" # Safe base default fallback if a question has no replies
            
        # Map perfectly to your Front Matter Markdown structure
        md_lines = [
            "---",
            f'question: "{question_text}"',
            'documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"',
            "---\n"
        ]
        
        for letter, text in choices:
            is_checked = "x" if letter == correct_letter else " "
            md_lines.append(f"- [{is_checked}] {letter}. {text}")
            
        with open(filepath, "w", encoding="utf-8") as out_f:
            out_f.write("\n".join(md_lines))
            
        saved_count += 1

    print("=" * 60)
    print(f"SUCCESS: Generated {saved_count} unique files inside '{OUTPUT_DIR}/'")
    print("=" * 60)

if __name__ == '__main__':
    parse_sequentially()