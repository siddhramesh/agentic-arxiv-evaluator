from crewai import Agent

def create_authenticity_agent(llm):

    return Agent(
        role="Research Integrity Investigator",

        goal="Estimate fabrication probability based on anomalies.",

        backstory="""
        You analyze logical inconsistencies and statistical
        anomalies to detect fabricated research claims.
        """,

        verbose=True,
        allow_delegation=False,
        llm=llm
    )
