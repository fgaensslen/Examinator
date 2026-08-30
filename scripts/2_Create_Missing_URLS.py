import re

# Input file path
EXTRACTED_FILE = r"C:\Users\Florian\Downloads\extracted_links.txt"
OUTPUT_FILE = r"C:\Users\Florian\Downloads\extracted_links.txt"

# Set the expected total number of questions for the exam (e.g., GH-600)
EXPECTED_QUESTION_COUNT = 0 # <<<<< CHECK EXAMTOPICS AND WRITE THE NUMBER OF EXPECTED QUESTIONS HERE (e.g., 58 for GH-600) >>>>>>

def fill_missing_links():
    # 1. Read existing links
    try:
        with open(EXTRACTED_FILE, "r", encoding="utf-8") as f:
            existing_links = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[-] File not found: {EXTRACTED_FILE}")
        return

    actual_count = len(existing_links)
    print(f"[*] Found {actual_count} extracted links. Expected target: {EXPECTED_QUESTION_COUNT}.")

    if actual_count == EXPECTED_QUESTION_COUNT:
        print("[+] Link count matches expected questions! No action needed.")
        return

    print("[!] Count mismatch detected. Generating missing links...\n")

    # 2. Extract discussion IDs and mapped metadata (topic, question) from existing URLs
    # Pattern to capture: (ID, Topic, Question)
    pattern = re.compile(r'/view/(\d+)-exam-.*?topic-(\d+)-question-(\d+)-discussion')

    id_to_link = {}
    found_ids = []

    for link in existing_links:
        match = pattern.search(link)
        if match:
            disc_id = int(match.group(1))
            found_ids.append(disc_id)
            id_to_link[disc_id] = link

    if not found_ids:
        print("[-] Could not parse discussion IDs from the input links. Please check the URL structures.")
        return

    found_ids.sort()
    min_id = min(found_ids)
    
    # 3. Detect ID sequential range
    # Since examtopics IDs are sequential, we project the range from min_id up to min_id + EXPECTED_QUESTION_COUNT - 1
    expected_ids = set(range(min_id, min_id + EXPECTED_QUESTION_COUNT))
    existing_id_set = set(found_ids)
    missing_ids = expected_ids - existing_id_set

    # 4. Generate candidate URLs for missing IDs based on template structure of known links
    # Extract template format from the first known link
    sample_link = existing_links[0]
    
    # Identify the base URL domain and trail pattern
    # e.g., https://www.examtopics.com/discussions/microsoft/view/
    complete_links = list(existing_links)
    generated_links = []

    for missing_id in sorted(missing_ids):
        # We construct generic replacement URLs for missing IDs
        # Note: Examtopics will automatically redirect any valid discussion ID to its correct URL title
        gen_url = f"https://www.examtopics.com/discussions/microsoft/view/{missing_id}-exam-gh-600-discussion/"
        generated_links.append(gen_url)
        complete_links.append(gen_url)

    print(f"[+] Successfully generated {len(generated_links)} missing links.")

    # 5. Save output to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for link in complete_links:
            f.write(f"{link}\n")

    print(f"[+] Complete list of {len(complete_links)} links saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    fill_missing_links()