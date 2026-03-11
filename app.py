import os
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st

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


# Load API key from Streamlit secrets
if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
else:
    st.error("OPENAI_API_KEY not found in Streamlit secrets.")
    st.stop()


# Input field
url = st.text_input("Enter arXiv URL")


if st.button("Evaluate Paper"):

    if url:

        try:

            # Step 1: Download paper
            with st.spinner("Downloading paper from arXiv..."):
                pdf_path = download_pdf(url)

            # Step 2: Extract text
            with st.spinner("Extracting text from PDF..."):
                text = extract_text(pdf_path)

            # Step 3: Split sections
            with st.spinner("Splitting paper into sections..."):
                sections = split_sections(text)

            # Step 4: Initialize LLM
            llm = LLM(model="gpt-4o-mini")

            # Step 5: Run evaluation
            with st.spinner("Running AI agents for evaluation..."):
                result = evaluate_paper(sections, llm)

            # Step 6: Generate report
            report = generate_report(result)

            # Step 7: Display report
            st.subheader("Evaluation Report")
            st.markdown(report)

            # Step 8: Download button
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
