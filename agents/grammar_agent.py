from crewai import Agent

def create_grammar_agent(llm):

    return Agent(
        role="Academic Language Reviewer",

        goal="Evaluate grammar, syntax and professional tone.",

        backstory="Expert editor of scientific journals.",

        llm=llm
    )
