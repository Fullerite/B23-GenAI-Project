import os
import re
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from urllib.parse import urljoin, urldefrag


START_URL = "https://v4fire.github.io/Core/modules.html"
BASE_DOMAIN = "v4fire.github.io/Core"
OUTPUT_DIR = "data/docs"
CONCURRENCY_LIMIT = 20
MIN_CONTENT_LENGTH = 50

visited = set()
queue = asyncio.Queue()

def clean_markdown(text):
    if not text:
        return ""
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def parse_and_save(url, html):
    soup = BeautifulSoup(html, "html.parser")

    content_div = soup.find("div", class_="col-8 col-content")
    if not content_div:
        return False

    raw_markdown = md(str(content_div), heading_style="ATX")
    final_content = clean_markdown(raw_markdown)
    
    if len(final_content) < MIN_CONTENT_LENGTH:
        return False

    path_part = url.split(BASE_DOMAIN + "/")[-1]
    clean_name = path_part.replace(".html", "")
    safe_name = clean_name.replace("/", "_").replace("\\", "_").replace(":", "")
    filename = os.path.join(OUTPUT_DIR, f"{safe_name}.md")

    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else safe_name

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n")
            f.write(f"Source: {url}\n\n")
            f.write(final_content)
        return True
    except Exception as e:
        print(f"Error saving {filename}: {e}")
        return False

def extract_links(soup, current_url):
    links = []
    content_div = soup.find("div", class_="col-8 col-content")
    if content_div:
        for a_tag in content_div.find_all("a"):
            href = a_tag.get("href")
            if href and not href.startswith(("mailto:", "tel:", "javascript:", "#")):
                full_url = urljoin(current_url, href)
                clean_url, _ = urldefrag(full_url)
                if BASE_DOMAIN in clean_url and clean_url.endswith(".html"):
                    links.append(clean_url)
    return links

async def fetch(session, url):
    try:
        async with session.get(url, timeout=15) as response:
            if response.status == 200:
                return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

async def worker(session):
    while True:
        try:
            current_url = queue.get_nowait()
        except asyncio.QueueEmpty:
            break

        if current_url in visited:
            queue.task_done()
            continue

        visited.add(current_url)
        html = await fetch(session, current_url)
        
        if html:
            saved = parse_and_save(current_url, html)
            soup = BeautifulSoup(html, "html.parser")
            new_links = extract_links(soup, current_url)
            
            for link in new_links:
                if link not in visited:
                    await queue.put(link)

            if len(visited) % 50 == 0:
                print(f"Processed {len(visited)} pages... (Queue: {queue.qsize()})")

        queue.task_done()


async def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    queue.put_nowait(START_URL)
    
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(worker(session)) for _ in range(CONCURRENCY_LIMIT)]
        await queue.join()
        for task in tasks:
            task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
