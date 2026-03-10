from crewai import Agent, Task, Crew

def evaluate_paper(abstract):

    research_agent = Agent(
        role="Research Analyst",
        goal="Analyze research paper abstracts and determine their novelty and clarity",
        backstory="An AI trained to evaluate academic research quality.",
        verbose=True
    )

    evaluation_task = Task(
        description=f"""
        Analyze the following research abstract and provide:
        - Executive summary (pass/fail)
        - Consistency score (0-100)
        - Grammar rating
        - Novelty assessment

        Abstract:
        {abstract}
        """,
        agent=research_agent
    )

    crew = Crew(
        agents=[research_agent],
        tasks=[evaluation_task]
    )

    result = crew.kickoff()

    return {"analysis": result}
