import streamlit as st

from tools.arxiv_scraper import fetch_paper
from report.evaluator import evaluate_paper
from report.report_formatter import format_report

st.title("Agentic AI Research Paper Evaluator")

st.write("Paste an arXiv paper link to generate a judgement report.")

url = st.text_input("Enter arXiv URL")

if st.button("Evaluate Paper"):

    paper = fetch_paper(url)

    evaluation = evaluate_paper(paper["abstract"])

    report = format_report(paper["title"], evaluation)

    st.markdown(report)
