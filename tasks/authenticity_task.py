from crewai import Task

def create_authenticity_task(agent, results):

    return Task(

        description=f"""
        Analyze whether the results show signs of fabricated
        data or statistical anomalies.

        Results:
        {results}

        Provide a Fabrication Probability percentage.
        """,

        agent=agent
    )
