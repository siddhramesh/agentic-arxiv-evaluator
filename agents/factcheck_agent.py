from crewai import Agent

def create_factcheck_agent(llm):

    return Agent(
        role="Scientific Fact Checker",

        goal="Verify formulas, references, and factual claims.",

        backstory="""
        You are responsible for verifying scientific accuracy
        and identifying unsupported claims in research papers.
        """,

        verbose=True,
        allow_delegation=False,
        llm=llm
    )
