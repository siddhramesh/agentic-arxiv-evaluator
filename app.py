import streamlit as st
from crewai import Crew, Process
from agents.research_agent import research_agent
from agents.methodology_agent import methodology_agent
from agents.evaluation_agent import evaluation_agent
from crewai import Task

st.title("📄 Agentic AI Research Paper Evaluator")

url = st.text_input("Enter arXiv paper URL")

if st.button("Evaluate Paper"):

    if url == "":
        st.warning("Please enter a valid arXiv URL")
    else:

        research_task = Task(
            description=f"Extract key details from this research paper: {url}. Summarize the abstract, problem statement and contributions.",
            agent=research_agent,
            expected_output="Summary of the paper with problem statement and contributions"
        )

        methodology_task = Task(
            description=f"Analyze the methodology used in the paper: {url}. Explain the approach, models, and techniques used.",
            agent=methodology_agent,
            expected_output="Explanation of methodology and techniques"
        )

        evaluation_task = Task(
            description=f"Evaluate the strengths and weaknesses of the research paper: {url}. Provide a critical review.",
            agent=evaluation_agent,
            expected_output="Critical evaluation with strengths and weaknesses"
        )

        crew = Crew(
            agents=[research_agent, methodology_agent, evaluation_agent],
            tasks=[research_task, methodology_task, evaluation_task],
            process=Process.sequential
        )

        result = crew.kickoff()

        st.subheader("Evaluation Report")
        st.write(result)
