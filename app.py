import os
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["GROQ_DISABLE_TELEMETRY"] = "true"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except (ImportError, KeyError):
    pass

import streamlit as st

st.title("Agentic Research Paper Evaluator")
st.write(
    "Enter an arXiv paper link to automatically evaluate the research paper "
    "using multiple AI agents."
)

# Load API key from Streamlit secrets
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
else:
    st.error("GEMINI_API_KEY not found in Streamlit secrets.")
    st.stop()

# Input field
url = st.text_input("Enter arXiv URL")

if st.button("Evaluate Paper"):
    if url:
        try:
            # Heavy imports only when needed
            from tools.arxiv_scraper import download_pdf, fetch_metadata
            from tools.paper_parser import extract_text, split_sections
            from evaluator.evaluator import evaluate_paper
            from reports.report_generator import generate_report
            from crewai import LLM

            # Step 0: Fetch and display paper metadata
            with st.spinner("Fetching paper details..."):
                metadata = fetch_metadata(url)

            if metadata:
                st.subheader("📄 Paper Details")
                st.markdown(f"**Title:** {metadata['title']}")
                st.markdown(f"**Authors:** {', '.join(metadata['authors'])}")
                st.markdown(f"**Published:** {metadata['published']}")
                with st.expander("Abstract"):
                    st.write(metadata['summary'])
                st.divider()

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
            llm = LLM(
                 model="gemini/gemini-1.5-flash",
                api_key=st.secrets["GEMINI_API_KEY"]
            )

            # Step 5: Run evaluation
            with st.spinner("Running AI agents for evaluation... (this may take 2-3 minutes)"):
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
