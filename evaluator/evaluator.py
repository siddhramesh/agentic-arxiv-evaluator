from crewai import Crew, Process

def evaluate_paper(tasks):

    crew = Crew(
        agents=[task.agent for task in tasks],
        tasks=tasks,
        process=Process.sequential
    )

    result = crew.kickoff()

    return result
