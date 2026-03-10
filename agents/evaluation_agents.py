from crewai import Agent, Task, Crew

def evaluate_paper(abstract):

    consistency_agent = Agent(
        role="Consistency Analyst",
        goal="Check if the methodology logically supports the results claimed",
        backstory="Expert reviewer specialized in research methodology."
    )

    grammar_agent = Agent(
        role="Language Reviewer",
        goal="Evaluate grammar, clarity, and academic tone",
        backstory="Professional editor for academic publications."
    )

    novelty_agent = Agent(
        role="Novelty Researcher",
        goal="Determine if the research idea appears unique compared to existing literature",
        backstory="AI trained to detect originality in research."
    )

    fact_checker_agent = Agent(
        role="Fact Checker",
        goal="Verify claims and constants mentioned in the abstract",
        backstory="Analyst verifying scientific claims."
    )

    authenticity_agent = Agent(
        role="Authenticity Auditor",
        goal="Estimate probability of fabricated or unsupported results",
        backstory="AI auditor detecting statistical anomalies."
    )

    consistency_task = Task(
        description=f"Evaluate logical consistency of the following abstract:\n{abstract}",
        agent=consistency_agent
    )

    grammar_task = Task(
        description=f"Evaluate grammar quality and academic tone:\n{abstract}",
        agent=grammar_agent
    )

    novelty_task = Task(
        description=f"Assess novelty of the research idea:\n{abstract}",
        agent=novelty_agent
    )

    fact_task = Task(
        description=f"Fact-check scientific claims in this abstract:\n{abstract}",
        agent=fact_checker_agent
    )

    authenticity_task = Task(
        description=f"Estimate fabrication probability for this research abstract:\n{abstract}",
        agent=authenticity_agent
    )

    crew = Crew(
        agents=[
            consistency_agent,
            grammar_agent,
            novelty_agent,
            fact_checker_agent,
            authenticity_agent
        ],
        tasks=[
            consistency_task,
            grammar_task,
            novelty_task,
            fact_task,
            authenticity_task
        ]
    )

    result = crew.kickoff()

    return {"analysis": result}
