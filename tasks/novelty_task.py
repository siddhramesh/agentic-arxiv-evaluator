from crewai import Task


def create_novelty_task(agent, abstract):

    return Task(

        description=f"""
        Evaluate whether the research idea described in the
        abstract appears novel compared to typical work in
        the same research area.

        Abstract:
        {abstract}

        Provide an explanation of whether the idea appears
        original or similar to existing research.
        """,

        expected_output="""
        A short explanation describing the level of novelty,
        such as Highly Novel, Moderately Novel, or Not Novel.
        """,

        agent=agent
    )
