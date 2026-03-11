from crewai import Task

def create_novelty_task(agent, abstract):

    return Task(

        description=f"""
        Evaluate whether this research idea appears novel.

        Abstract:
        {abstract}

        Provide a short explanation of novelty.
        """,

        agent=agent
    )
