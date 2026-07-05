import asyncio
import os
from playwright.async_api import async_playwright

INPUT_FILE = r"C:\Users\Florian\Downloads\clean_final.txt"  # Your text file containing the clean URLs
OUTPUT_FILE = r"C:\Users\Florian\Downloads\exam_content.txt"

async def scrape_questions():
    if not os.path.exists(INPUT_FILE):
        print(f"[-] Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"[*] Starting speed-scrape of {len(urls)} questions...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = await context.new_page()

        for idx, url in enumerate(urls, 1):
            print(f"[{idx}/{len(urls)}] Scraping: {url}")
            try:
                # Go to the URL and stop waiting as soon as the DOM tree forms
                await page.goto(url, wait_until="domcontentloaded")
                
                # INSTANT EXTRACTION: Grab the text content before the overlay script fires
                # ExamTopics places the core question text inside the card element
                content = await page.evaluate('''() => {
                    const card = document.querySelector('.exam-question-card') || document.body;
                    return card.innerText;
                }''')
                
                # Append immediately to your text archive
                with open(OUTPUT_FILE, "a", encoding="utf-8") as out:
                    out.write(f"\n\n{'='*40}\nURL: {url}\n{'='*40}\n")
                    out.write(content)
                
                # A very brief rest to keep the browser from crashing, but fast enough to outrun blocks
                await asyncio.sleep(0.5)

            except Exception as e:
                print(f"[-] Failed to scrape {url}: {e}")
                
        await browser.close()
    print(f"[+] Finished! Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(scrape_questions())