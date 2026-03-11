import fitz


def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


def split_sections(text):

    text_lower = text.lower()

    sections = {
        "abstract": "",
        "methodology": "",
        "results": "",
        "conclusion": ""
    }

    # Abstract
    if "abstract" in text_lower:
        start = text_lower.find("abstract")
        sections["abstract"] = text[start:start+2000]

    # Methodology
    if "method" in text_lower:
        start = text_lower.find("method")
        sections["methodology"] = text[start:start+4000]

    # Results
    if "result" in text_lower:
        start = text_lower.find("result")
        sections["results"] = text[start:start+4000]

    # Conclusion
    if "conclusion" in text_lower:
        start = text_lower.find("conclusion")
        sections["conclusion"] = text[start:start+2000]

    return sections
