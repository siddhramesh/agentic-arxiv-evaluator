from crewai import Task


def create_authenticity_task(agent, results):

    return Task(

        description=f"""
        Analyze whether the research results show signs of
        fabricated data, statistical anomalies, or unrealistic claims.

        Results:
        {results}

        Estimate the probability that the results may be fabricated.
        """,

        expected_output="""
        A short explanation of potential anomalies and a final
        Fabrication Probability percentage (0–100%).
        """,

        agent=agent
    )
