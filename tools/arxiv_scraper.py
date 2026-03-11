import requests

def download_pdf(arxiv_url):
    paper_id = arxiv_url.split("/")[-1]
    pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"
    response = requests.get(pdf_url)
    if response.status_code != 200:
        raise Exception("Failed to download paper from arXiv.")
    file_path = "arxiv_paper.pdf"
    with open(file_path, "wb") as f:
        f.write(response.content)
    return file_path


def fetch_metadata(arxiv_url):
    paper_id = arxiv_url.split("/")[-1]
    api_url = f"https://export.arxiv.org/api/query?id_list={paper_id}"
    response = requests.get(api_url)
    if response.status_code != 200:
        return None

    # Parse the Atom XML response
    content = response.text
    def extract(tag, text):
        try:
            start = text.index(f"<{tag}") + len(f"<{tag}")
            start = text.index(">", start) + 1
            end = text.index(f"</{tag}>", start)
            return text[start:end].strip()
        except ValueError:
            return "N/A"

    def extract_all(tag, text):
        results = []
        remaining = text
        while f"<{tag}" in remaining:
            try:
                start = remaining.index(f"<{tag}") + len(f"<{tag}")
                start = remaining.index(">", start) + 1
                end = remaining.index(f"</{tag}>", start)
                results.append(remaining[start:end].strip())
                remaining = remaining[end:]
            except ValueError:
                break
        return results

    title = extract("title", content.split("<entry>")[-1])
    summary = extract("summary", content)
    published = extract("published", content)[:10]  # just the date part

    # Extract author names
    author_blocks = content.split("<author>")[1:]
    authors = []
    for block in author_blocks:
        try:
            end = block.index("</author>")
            name_start = block.index("<name>") + len("<name>")
            name_end = block.index("</name>")
            authors.append(block[name_start:name_end].strip())
        except ValueError:
            continue

    return {
        "title": title,
        "authors": authors,
        "published": published,
        "summary": summary
    }
