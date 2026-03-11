def create_factcheck_agent(llm):

    return Agent(
        role="Scientific Fact Checker",

        goal="Verify formulas, constants and scientific claims.",

        backstory="Research scientist verifying claims.",

        llm=llm
    )
