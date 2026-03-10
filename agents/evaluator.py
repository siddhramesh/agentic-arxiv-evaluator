from crewai import Crew, Task
from crewai import LLM

from agents.consistency_agent import create_consistency_agent
from agents.grammar_agent import create_grammar_agent
from agents.novelty_agent import create_novelty_agent
from agents.factcheck_agent import create_factcheck_agent
from agents.authenticity_agent import create_authenticity_agent

from crewai import Crew, Task
from crewai import LLM

from agents.consistency_agent import create_consistency_agent
from agents.grammar_agent import create_grammar_agent
from agents.novelty_agent import create_novelty_agent
from agents.factcheck_agent import create_factcheck_agent
from agents.authenticity_agent import create_authenticity_agent


def evaluate_paper(paper):

    llm = LLM(model="gpt-4o-mini", temperature=0.2)

    consistency_agent = create_consistency_agent(llm)
    grammar_agent = create_grammar_agent(llm)
    novelty_agent = create_novelty_agent(llm)
    factcheck_agent = create_factcheck_agent(llm)
    authenticity_agent = create_authenticity_agent(llm)

    consistency_task = Task(
        description=f"""
Evaluate if the methodology supports the results.

Methodology:
{paper['methodology']}

Results:
{paper['results']}

Return:
Score (0-100)
Explanation
""",
        agent=consistency_agent
    )

    grammar_task = Task(
        description=f"""
Evaluate grammar and clarity.

Text:
{paper['abstract']}

Return rating: High / Medium / Low.
""",
        agent=grammar_agent
    )

    novelty_task = Task(
        description=f"""
Evaluate novelty of the research.

Abstract:
{paper['abstract']}
""",
        agent=novelty_agent
    )

    factcheck_task = Task(
        description=f"""
Verify factual claims.

Text:
{paper['abstract']}
""",
        agent=factcheck_agent
    )

    authenticity_task = Task(
        description=f"""
Detect possible fabrication.

Text:
{paper['results']}
""",
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
        ],
        process="sequential"
    )

    result = crew.kickoff()

    return {
        "analysis": str(result)
    }
