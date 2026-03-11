from crewai import Agent

def create_consistency_agent(llm):

    return Agent(
        role="Scientific Consistency Auditor",

        goal="""
        Verify whether methodology logically supports
        the claimed results.
        """,

        backstory="""
        You are an expert peer reviewer specializing in
        identifying logical inconsistencies in scientific papers.
        """,

        llm=llm,
        verbose=True
    )
