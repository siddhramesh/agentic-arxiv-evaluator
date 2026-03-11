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
