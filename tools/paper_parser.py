import fitz

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text

def split_sections(text):

    sections = {
        "abstract": "",
        "methodology": "",
        "results": "",
        "conclusion": ""
    }

    text_lower = text.lower()

    if "abstract" in text_lower:
        sections["abstract"] = text.split("abstract")[1][:2000]

    if "method" in text_lower:
        sections["methodology"] = text.split("method")[1][:4000]

    if "result" in text_lower:
        sections["results"] = text.split("result")[1][:4000]

    if "conclusion" in text_lower:
        sections["conclusion"] = text.split("conclusion")[1][:2000]

    return sections
