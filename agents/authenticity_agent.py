from crewai import Agent


def create_authenticity_agent(llm):

    return Agent(
        role="Research Integrity Investigator",

        goal="""
        Analyze whether the results show signs of fabricated
        data, statistical anomalies, or logical inconsistencies.
        Provide a fabrication probability percentage.
        """,

        backstory="""
        You are a research integrity expert skilled at detecting
        fabricated datasets, statistical irregularities, and
        suspicious research claims.
        """,

        llm=llm,
        verbose=True,
        allow_delegation=False
    )
