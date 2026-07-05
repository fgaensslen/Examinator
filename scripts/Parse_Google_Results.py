import re

def extract_links_from_file(filename="google_source.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"[-] Error: Could not find the file '{filename}'. Please ensure you saved your Google page source to this location.")
        return

    # Regex targeting ExamTopics discussion paths hidden within Google's HTML source structure
    raw_matches = re.findall(r'https://www\.examtopics\.com/discussions/microsoft/view/[^"\'\s&>]+', html_content)
    
    discovered_urls = set()
    for url in raw_matches:
        # Strip any trailing characters that aren't part of the direct URL format
        clean_url = url.split("?")[0].split(")")[0].split("\\")[0]
        if "exam-gh-300" in clean_url.lower():
            # Standardize domain scheme
            if not clean_url.endswith('/'):
                clean_url += '/'
            discovered_urls.add(clean_url)
            
    print("\n" + "="*60)
    print(f"SUCCESS: EXTRACTED {len(discovered_urls)} UNIQUE QUESTION LINKS")
    print("="*60)
    
    # Sort the final output cleanly by Topic and Question numbers
    def sort_key(url):
        topic_match = re.search(r'topic-(\d+)', url)
        question_match = re.search(r'question-(\d+)', url)
        t = int(topic_match.group(1)) if topic_match else 0
        q = int(question_match.group(1)) if question_match else 0
        return (t, q)
        
    for url in sorted(list(discovered_urls), key=sort_key):
        print(url)

if __name__ == "__main__":
    extract_links_from_file()