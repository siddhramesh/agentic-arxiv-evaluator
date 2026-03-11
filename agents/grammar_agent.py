from crewai import Agent


def create_grammar_agent(llm):

    return Agent(
        role="Academic Language Reviewer",

        goal="""
        Evaluate the grammar, clarity, readability, and
        professional academic tone of the research text.
        Provide a rating: High, Medium, or Low.
        """,

        backstory="""
        You are an experienced editor for top scientific journals,
        specializing in improving academic writing quality and clarity.
        """,

        llm=llm,
        verbose=True,
        allow_delegation=False
    )
