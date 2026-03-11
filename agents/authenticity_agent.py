def create_authenticity_agent(llm):

    return Agent(
        role="Research Integrity Investigator",

        goal="Estimate fabrication probability.",

        backstory="""
        You detect statistical anomalies,
        fabricated datasets and logical gaps.
        """,

        llm=llm
    )
