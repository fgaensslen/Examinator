import os
import re
import glob

exam_name = "" # <<<<< WRITE YOUR EXAM NAME HERE, LIKE "AZ-900" or "SC-900" etc.>>>>>
downloads_dir = r"C:\Users\Florian\Downloads"
output_file = r"C:\Users\Florian\Downloads\extracted_links.txt"

def get_latest_google_source(directory):
    # Search for google_source.txt, google_source (1).txt, etc.
    pattern = os.path.join(directory, "google_source*.txt")
    files = glob.glob(pattern)
    if not files:
        return None
    # Find the most recently created or modified file
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def extract_links_from_file(output_filename=output_file):
    input_file = get_latest_google_source(downloads_dir)
    
    if not input_file:
        print(f"[-] Error: Could not find any 'google_source*.txt' files in {downloads_dir}")
        return

    print(f"[+] Processing file: {input_file}")

    with open(input_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Load existing links to ensure global deduplication
    discovered_urls = set()
    if os.path.exists(output_filename):
        with open(output_filename, "r", encoding="utf-8") as out_f:
            existing_links = {line.strip() for line in out_f if line.strip()}
            discovered_urls.update(existing_links)

    # Extract new URLs
    raw_matches = re.findall(r'https://www\.examtopics\.com/discussions/microsoft/view/[^"\'\s&>]+', html_content)
    
    for url in raw_matches:
        clean_url = url.split("?")[0].split("%")[0].split(")")[0].split("\\")[0]
        if f"exam-{exam_name}" in clean_url.lower():
            if not clean_url.endswith('/'):
                clean_url += '/'
            discovered_urls.add(clean_url)
            
    # Sort by Topic and Question numbers
    def sort_key(url):
        topic_match = re.search(r'topic-(\d+)', url)
        question_match = re.search(r'question-(\d+)', url)
        t = int(topic_match.group(1)) if topic_match else 0
        q = int(question_match.group(1)) if question_match else 0
        return (t, q)
        
    sorted_urls = sorted(list(discovered_urls), key=sort_key)

    # Save to output file
    with open(output_filename, "w", encoding="utf-8") as out_f:
        for url in sorted_urls:
            out_f.write(url + "\n")

    # Clean up processed file to prevent duplicate downloads clutter
    try:
        os.remove(input_file)
        print(f"[+] Cleaned up: Removed {os.path.basename(input_file)}")
    except OSError as e:
        print(f"[-] Warning: Couldn't delete {input_file}: {e}")

    print("\n" + "="*60)
    print(f"SUCCESS: TOTAL UNIQUE QUESTION LINKS IN FILE: {len(sorted_urls)}")
    print(f"UPDATED: {output_filename}")
    print("="*60)

if __name__ == "__main__":
    extract_links_from_file()