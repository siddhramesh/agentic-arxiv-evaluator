import streamlit as st

from tools.arxiv_scraper import download_pdf
from tools.paper_parser import extract_text
from evaluator.evaluator import evaluate_paper

st.title("Agentic Research Paper Evaluator")

url = st.text_input("Enter arXiv URL")

if st.button("Evaluate"):

    pdf = download_pdf(url)

    text = extract_text(pdf)

    st.write("Paper processed.")

    result = evaluate_paper(text)

    st.write(result)
