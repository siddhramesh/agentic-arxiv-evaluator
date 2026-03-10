from crewai import Agent

def create_grammar_agent(llm):

    return Agent(
        role="Academic Language Reviewer",

        goal="Evaluate grammar, clarity, and professional tone.",

        backstory="""
        You are an academic journal editor who evaluates
        language quality, grammar, and readability.
        """,

        verbose=True,
        allow_delegation=False,
        llm=llm
    )
