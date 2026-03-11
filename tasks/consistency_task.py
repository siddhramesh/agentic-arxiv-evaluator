from crewai import Task


def create_consistency_task(agent, methodology, results):

    return Task(

        description=f"""
        Evaluate whether the research methodology logically
        supports the reported results.

        Methodology:
        {methodology}

        Results:
        {results}

        Provide a detailed explanation and a Consistency Score
        between 0 and 100.
        """,

        expected_output="""
        A short explanation of whether the methodology supports
        the results and a final Consistency Score (0-100).
        """,

        agent=agent
    )
