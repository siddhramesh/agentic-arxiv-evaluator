from crewai import Agent


def create_novelty_agent(llm):

    return Agent(
        role="Literature Review Specialist",

        goal="""
        Evaluate whether the research contribution appears novel
        compared to existing literature. Provide a qualitative
        novelty assessment.
        """,

        backstory="""
        You are an expert researcher skilled in reviewing scientific
        literature and identifying whether a research idea introduces
        a new contribution or resembles existing work.
        """,

        llm=llm,
        verbose=True,
        allow_delegation=False
    )
