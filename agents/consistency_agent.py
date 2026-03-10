from crewai import Agent

def create_consistency_agent(llm):

    return Agent(
        role="Consistency Auditor",

        goal="Check if the methodology logically supports the results.",

        backstory="""
        You are an experienced peer reviewer for AI conferences.
        You verify whether experimental design and methodology
        justify the results presented in the research paper.
        """,

        verbose=True,
        allow_delegation=False,
        llm=llm
    )
