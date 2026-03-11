from crewai import Agent


def create_consistency_agent(llm):

    return Agent(
        role="Scientific Consistency Auditor",

        goal="""
        Evaluate whether the research methodology logically
        supports the reported results and conclusions.
        Provide a clear consistency assessment.
        """,

        backstory="""
        You are an experienced academic peer reviewer with expertise
        in evaluating research methodologies and detecting logical
        inconsistencies in scientific publications.
        """,

        llm=llm,
        verbose=True,
        allow_delegation=False
    )
