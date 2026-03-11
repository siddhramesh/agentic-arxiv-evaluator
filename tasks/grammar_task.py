from crewai import Task

def create_grammar_task(agent, abstract):

    return Task(

        description=f"""
        Review the grammar, clarity and professional tone
        of the following abstract.

        Abstract:
        {abstract}

        Rate grammar quality as High, Medium, or Low.
        """,

        agent=agent
    )
