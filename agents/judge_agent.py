from crewai import Agent

def create_judge_agent(llm):

    return Agent(
        role="Chief Research Reviewer",

        goal="""
        Review the analysis produced by other agents and provide
        a final evaluation of the research paper.
        """,

        backstory="""
        You are the head of a research peer-review committee.
        You synthesize the findings from multiple reviewers
        and provide a final judgement on the research paper.
        """,

        llm=llm,
        verbose=True,
        allow_delegation=False
    )
