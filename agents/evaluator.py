from crewai import Crew, Task
from crewai import LLM

from agents.consistency_agent import create_consistency_agent
from agents.grammar_agent import create_grammar_agent
from agents.novelty_agent import create_novelty_agent
from agents.factcheck_agent import create_factcheck_agent
from agents.authenticity_agent import create_authenticity_agent


def evaluate_paper(text):

    llm = LLM(model="gpt-3.5-turbo")

    consistency_agent = create_consistency_agent(llm)
    grammar_agent = create_grammar_agent(llm)
    novelty_agent = create_novelty_agent(llm)
    factcheck_agent = create_factcheck_agent(llm)
    authenticity_agent = create_authenticity_agent(llm)

    consistency_task = Task(
        description=f"Evaluate if methodology supports results:\n{text}",
        agent=consistency_agent
    )

    grammar_task = Task(
        description=f"Evaluate grammar and language quality:\n{text}",
        agent=grammar_agent
    )

    novelty_task = Task(
        description=f"Evaluate novelty of the research:\n{text}",
        agent=novelty_agent
    )

    factcheck_task = Task(
        description=f"Fact-check scientific claims:\n{text}",
        agent=factcheck_agent
    )

    authenticity_task = Task(
        description=f"Estimate fabrication probability:\n{text}",
        agent=authenticity_agent
    )

    crew = Crew(
        agents=[
            consistency_agent,
            grammar_agent,
            novelty_agent,
            factcheck_agent,
            authenticity_agent
        ],
        tasks=[
            consistency_task,
            grammar_task,
            novelty_task,
            factcheck_task,
            authenticity_task
        ]
    )

    return crew.kickoff()
