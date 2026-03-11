import streamlit as st
import os

from tools.arxiv_scraper import download_pdf
from tools.paper_parser import extract_text, split_sections

from evaluator.evaluator import evaluate_paper
from reports.report_generator import generate_report

from crewai import LLM


st.title("Agentic Research Paper Evaluator")

st.write(
    "Enter an arXiv paper link to automatically evaluate the research paper "
    "using multiple AI agents."
)


# Check API key
if "OPENAI_API_KEY" not in os.environ:
    st.error("OPENAI_API_KEY environment variable not set.")
    st.stop()


url = st.text_input("Enter arXiv URL")


if st.button("Evaluate Paper"):

    if url:

        try:

            with st.spinner("Downloading paper from arXiv..."):
                pdf_path = download_pdf(url)

            with st.spinner("Extracting text from PDF..."):
                text = extract_text(pdf_path)

            with st.spinner("Splitting paper into sections..."):
                sections = split_sections(text)

            llm = LLM(model="gpt-4o-mini")

            with st.spinner("Running AI agents for evaluation..."):
                result = evaluate_paper(sections, llm)

            report = generate_report(result)

            st.subheader("Evaluation Report")

            st.markdown(report)

            st.download_button(
                label="Download Report",
                data=report,
                file_name="research_paper_report.md",
                mime="text/markdown"
            )

        except Exception as e:

            st.error(f"Error occurred: {e}")

    else:

        st.warning("Please enter a valid arXiv URL.")
