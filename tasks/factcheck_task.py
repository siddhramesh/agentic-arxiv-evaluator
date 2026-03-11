from crewai import Task

def create_factcheck_task(agent, methodology):

    return Task(

        description=f"""
        Check whether formulas, constants or claims in the
        methodology appear correct.

        Methodology:
        {methodology}

        List verified and questionable claims.
        """,

        agent=agent
    )
