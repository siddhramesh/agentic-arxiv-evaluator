from crewai import Crew, Process

from agents.consistency_agent import create_consistency_agent
from agents.grammar_agent import create_grammar_agent
from agents.novelty_agent import create_novelty_agent
from agents.factcheck_agent import create_factcheck_agent
from agents.authenticity_agent import create_authenticity_agent

from tasks.consistency_task import create_consistency_task
from tasks.grammar_task import create_grammar_task
from tasks.novelty_task import create_novelty_task
from tasks.factcheck_task import create_factcheck_task
from tasks.authenticity_task import create_authenticity_task


def evaluate_paper(sections, llm):

    abstract = sections["abstract"]
    methodology = sections["methodology"]
    results = sections["results"]
    conclusion = sections["conclusion"]

    # Create agents
    consistency_agent = create_consistency_agent(llm)
    grammar_agent = create_grammar_agent(llm)
    novelty_agent = create_novelty_agent(llm)
    factcheck_agent = create_factcheck_agent(llm)
    authenticity_agent = create_authenticity_agent(llm)

    # Create tasks
    consistency_task = create_consistency_task(consistency_agent, methodology, results)
    grammar_task = create_grammar_task(grammar_agent, abstract)
    novelty_task = create_novelty_task(novelty_agent, abstract)
    factcheck_task = create_factcheck_task(factcheck_agent, methodology)
    authenticity_task = create_authenticity_task(authenticity_agent, results)

    tasks = [
        consistency_task,
        grammar_task,
        novelty_task,
        factcheck_task,
        authenticity_task
    ]

    crew = Crew(
        agents=[
            consistency_agent,
            grammar_agent,
            novelty_agent,
            factcheck_agent,
            authenticity_agent
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return result
