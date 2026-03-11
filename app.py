import os
2os.environ["OTEL_SDK_DISABLED"] = "true"
3os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
4
5__import__('pysqlite3')
6import sys
7sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
8
9import streamlit as st
10from tools.arxiv_scraper import download_pdf
11from tools.paper_parser import extract_text, split_sections
12from evaluator.evaluator import evaluate_paper
13from reports.report_generator import generate_report
14from crewai import LLM
15
16st.title("Agentic Research Paper Evaluator")
17st.write(
18    "Enter an arXiv paper link to automatically evaluate the research paper "
19    "using multiple AI agents."
20)
21
22# Load API key from Streamlit secrets
23if "GROQ_API_KEY" in st.secrets:
24    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
25else:
26    st.error("GROQ_API_KEY not found in Streamlit secrets.")
27    st.stop()
28
29# Input field
30url = st.text_input("Enter arXiv URL")
31
32if st.button("Evaluate Paper"):
33    if url:
34        try:
35            # Step 1: Download paper
36            with st.spinner("Downloading paper from arXiv..."):
37                pdf_path = download_pdf(url)
38
39            # Step 2: Extract text
40            with st.spinner("Extracting text from PDF..."):
41                text = extract_text(pdf_path)
42
43            # Step 3: Split sections
44            with st.spinner("Splitting paper into sections..."):
45                sections = split_sections(text)
46
47            # Step 4: Initialize LLM
48            llm = LLM(
49                model="groq/llama-3.1-8b-instant",
50                api_key=st.secrets["GROQ_API_KEY"]
51            )
52
53            # Step 5: Run evaluation
54            with st.spinner("Running AI agents for evaluation..."):
55                result = evaluate_paper(sections, llm)
56
57            # Step 6: Generate report
58            report = generate_report(result)
59
60            # Step 7: Display report
61            st.subheader("Evaluation Report")
62            st.markdown(report)
63
64            # Step 8: Download button
65            st.download_button(
66                label="Download Report",
67                data=report,
68                file_name="research_paper_report.md",
69                mime="text/markdown"
70            )
71
72        except Exception as e:
73            st.error(f"Error occurred: {e}")
74    else:
75        st.warning("Please enter a valid arXiv URL.")
76
