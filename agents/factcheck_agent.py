from crewai import Agent


def create_factcheck_agent(llm):

    return Agent(
        role="Scientific Fact Checker",

        goal="""
        Verify formulas, constants, and scientific claims
        mentioned in the research paper. Identify which
        claims appear correct and which require verification.
        """,

        backstory="""
        You are a meticulous research scientist responsible
        for verifying scientific accuracy in academic papers.
        """,

        llm=llm,
        verbose=True,
        allow_delegation=False
    )
