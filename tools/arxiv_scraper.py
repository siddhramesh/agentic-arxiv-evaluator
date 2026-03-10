import arxiv

def fetch_paper(url):

    paper_id = url.split("/")[-1]

    search = arxiv.Search(id_list=[paper_id])

    paper = next(search.results())

    return {
        "title": paper.title,
        "abstract": paper.summary
    }
