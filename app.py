import streamlit as st
from openai import OpenAI
from tools.arxiv_scraper import fetch_paper
from agents.evaluator import evaluate_paper
from report.report_formatter import format_report

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(
    page_title="Agentic Research Paper Evaluator",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Agentic Research Paper Evaluator")
st.write("Multi-agent AI system that evaluates research papers from arXiv.")

st.divider()

# Input section
arxiv_url = st.text_input(
    "Enter arXiv Paper URL",
    placeholder="https://arxiv.org/abs/1706.03762"
)

if st.button("Evaluate Paper") and arxiv_url:

    if not arxiv_url:
        st.warning("Please enter a valid arXiv URL.")
        st.stop()

    with st.spinner("Fetching paper from arXiv..."):

        try:
            paper = fetch_paper(arxiv_url)

        except Exception as e:
            st.error(f"Failed to fetch paper: {e}")
            st.stop()

    st.success("Paper fetched successfully")

    st.subheader("Paper Title")
    st.write(paper["title"])

    with st.expander("Abstract"):
        st.write(paper["abstract"])

    st.divider()

    with st.spinner("Running multi-agent evaluation..."):

        try:
            evaluation = evaluate_paper(paper)

        except Exception as e:
            st.error(f"Evaluation failed: {e}")
            st.stop()

    st.success("Evaluation complete")

    report = format_report(paper["title"], evaluation)

    st.subheader("Evaluation Report")

    st.markdown(report)

    st.download_button(
        label="Download Report",
        data=report,
        file_name="evaluation_report.md",
        mime="text/markdown"
    )
