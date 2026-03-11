from crewai import Task


def create_factcheck_task(agent, methodology):

    return Task(

        description=f"""
        Examine the methodology section and determine whether
        formulas, constants, or scientific claims appear valid.

        Methodology:
        {methodology}

        Identify claims that appear correct and those that
        may require verification.
        """,

        expected_output="""
        A fact-check log containing two lists:
        1. Verified claims
        2. Questionable or unverified claims
        """,

        agent=agent
    )
