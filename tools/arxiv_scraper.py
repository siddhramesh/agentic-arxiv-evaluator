import arxiv
import requests

def fetch_paper(url):

    paper_id = url.split("/")[-1]

    search = arxiv.Search(id_list=[paper_id])
    paper = next(search.results())

    abstract = paper.summary

    # Basic section placeholders (since arxiv API gives only abstract)
    # Agents will simulate analysis based on abstract
    paper_data = {
        "title": paper.title,
        "abstract": abstract,
        "methodology": abstract,
        "results": abstract,
        "conclusion": abstract
    }

    return paper_data
