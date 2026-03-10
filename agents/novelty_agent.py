from crewai import Agent

def create_novelty_agent(llm):

    return Agent(
        role="Research Novelty Analyst",

        goal="Evaluate whether the research introduces new ideas.",

        backstory="""
        You specialize in literature review and identifying
        whether research contributions are truly novel.
        """,

        verbose=True,
        allow_delegation=False,
        llm=llm
    )
