def create_novelty_agent(llm):

    return Agent(
        role="Literature Review Specialist",

        goal="Determine whether the research idea is novel.",

        backstory="Expert in surveying scientific literature.",

        llm=llm
    )
