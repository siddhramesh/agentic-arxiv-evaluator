import streamlit as st

from tools.arxiv_scraper import download_pdf
from tools.paper_parser import extract_text, split_sections

from evaluator.evaluator import evaluate_paper


st.title("Agentic Research Paper Evaluator")

url = st.text_input("Enter arXiv URL")


if st.button("Evaluate Paper"):

    if url:

        st.write("Downloading paper...")

        pdf_path = download_pdf(url)

        st.write("Extracting text...")

        text = extract_text(pdf_path)

        st.write("Decomposing paper sections...")

        sections = split_sections(text)

        abstract = sections["abstract"]
        methodology = sections["methodology"]
        results = sections["results"]
        conclusion = sections["conclusion"]

        st.write("Running AI evaluation agents...")

        result = evaluate_paper(sections)

        st.subheader("Evaluation Report")

        st.write(result)

    else:
        st.warning("Please enter a valid arXiv URL")
