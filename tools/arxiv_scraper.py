import requests
import fitz

def download_pdf(arxiv_url):

    paper_id = arxiv_url.split("/")[-1]
    pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"

    response = requests.get(pdf_url)

    with open("paper.pdf", "wb") as f:
        f.write(response.content)

    return "paper.pdf"
