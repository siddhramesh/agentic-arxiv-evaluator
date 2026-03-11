from crewai import Task

def create_consistency_task(agent, methodology, results):

    return Task(

        description=f"""
        Analyze whether this methodology logically supports
        the results.

        Methodology:
        {methodology}

        Results:
        {results}

        Provide a Consistency Score (0-100).
        """,

        agent=agent
    )
