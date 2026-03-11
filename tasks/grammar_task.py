from crewai import Task


def create_grammar_task(agent, abstract):

    return Task(

        description=f"""
        Review the grammar, clarity, readability, and professional
        tone of the following research abstract.

        Abstract:
        {abstract}

        Provide a grammar quality rating.
        """,

        expected_output="""
        A short explanation of writing quality and a final rating:
        High, Medium, or Low.
        """,

        agent=agent
    )
