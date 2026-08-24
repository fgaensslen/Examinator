import asyncio
import os
import re
from pathlib import Path
from urllib.parse import urljoin
from playwright.async_api import async_playwright

INPUT_FILE = r"C:\Users\Florian\Downloads\extracted_links.txt"
OUTPUT_FILE = r"C:\Users\Florian\Downloads\exam_content.txt"
IMAGE_DIR = r"C:\Users\Florian\Downloads\exam_images"
SCREENSHOT_DIR = r"C:\Users\Florian\Downloads\exam_screenshots"

async def download_image(request_context, img_url, save_path):
    """Downloads an image using the browser's active session context."""
    try:
        response = await request_context.get(img_url)
        if response.status == 200:
            image_data = await response.body()
            with open(save_path, "wb") as f:
                f.write(image_data)
            return True
    except Exception as e:
        print(f"    [-] Failed downloading image {img_url}: {e}")
    return False

async def scrape_questions():
    if not os.path.exists(INPUT_FILE):
        print(f"[-] Error: {INPUT_FILE} not found.")
        return

    # Ensure output directories exist
    os.makedirs(IMAGE_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"[*] Starting speed-scrape of {len(urls)} questions with images and screenshots...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = await context.new_page()

        for idx, url in enumerate(urls, 1):
            print(f"[{idx}/{len(urls)}] Scraping: {url}")
            try:
                await page.goto(url, wait_until="domcontentloaded")

                # Unique ID prefix based on topic and question numbers from the URL
                match = re.search(r'topic-(\d+)-question-(\d+)', url)
                prefix = f"t{match.group(1)}_q{match.group(2)}" if match else f"q_{idx}"

                # Capture full page or viewport screenshot
                screenshot_filename = f"{prefix}_screenshot.png"
                screenshot_filepath = os.path.join(SCREENSHOT_DIR, screenshot_filename)
                await page.screenshot(path=screenshot_filepath, full_page=True)

                # Extract both text and image URLs from the main question card
                data = await page.evaluate('''() => {
                    const card = document.querySelector('.exam-question-card') || document.body;
                    const images = Array.from(card.querySelectorAll('img')).map(img => img.src);
                    return {
                        text: card.innerText,
                        images: images
                    };
                }''')

                downloaded_image_names = []
                
                # Process and save images
                for img_idx, img_src in enumerate(data['images'], 1):
                    # Filter out base icons/UI badges if any exist
                    if "logo" in img_src.lower() or "avatar" in img_src.lower():
                        continue

                    # Construct full image URL if relative
                    full_img_url = urljoin(url, img_src)
                    
                    # Extract file extension or default to .png
                    ext = Path(full_img_url.split("?")[0]).suffix
                    if not ext or len(ext) > 5:
                        ext = ".png"

                    filename = f"{prefix}_img_{img_idx}{ext}"
                    filepath = os.path.join(IMAGE_DIR, filename)

                    success = await download_image(context.request, full_img_url, filepath)
                    if success:
                        downloaded_image_names.append(filename)

                # Format text content along with image logs
                with open(OUTPUT_FILE, "a", encoding="utf-8") as out:
                    out.write(f"\n\n{'='*40}\nURL: {url}\n{'='*40}\n")
                    out.write(f"[SCREENSHOT: {screenshot_filename}]\n")
                    if downloaded_image_names:
                        out.write(f"[ATTACHED IMAGES: {', '.join(downloaded_image_names)}]\n\n")
                    out.write(data['text'])

                await asyncio.sleep(0.5)

            except Exception as e:
                print(f"[-] Failed to scrape {url}: {e}")

        await browser.close()
    print(f"[+] Finished! Text saved to {OUTPUT_FILE}")
    print(f"[+] Images downloaded to {IMAGE_DIR}")
    print(f"[+] Screenshots saved to {SCREENSHOT_DIR}")

    # Delete all downloaded .webp images
    webp_files = list(Path(IMAGE_DIR).glob("*.webp"))
    for file_path in webp_files:
        try:
            file_path.unlink()
        except Exception as e:
            print(f"[-] Failed to delete {file_path.name}: {e}")
    print(f"[+] Cleaned up {len(webp_files)} .webp image(s).")

if __name__ == "__main__":
    asyncio.run(scrape_questions())