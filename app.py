import streamlit as st

from tools.arxiv_scraper import fetch_paper
from agents.evaluator import evaluate_paper
from report.report_formatter import format_report

st.title("Agentic AI Research Paper Evaluator")

url = st.text_input("Enter arXiv paper URL")

if st.button("Evaluate Paper"):

    if not url:
        st.warning("Please enter a URL")

    elif "arxiv.org" not in url:
        st.error("Please enter a valid arXiv link")

    else:
        with st.spinner("Analyzing paper using AI agents..."):

            paper = fetch_paper(url)

            evaluation = evaluate_paper(paper)

            report = format_report(paper["title"], evaluation)

            st.markdown(report)
