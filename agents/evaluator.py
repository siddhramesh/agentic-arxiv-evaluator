from crewai import Crew, Task, LLM, Process

from agents.consistency_agent import create_consistency_agent
from agents.grammar_agent import create_grammar_agent
from agents.novelty_agent import create_novelty_agent
from agents.factcheck_agent import create_factcheck_agent
from agents.authenticity_agent import create_authenticity_agent


def evaluate_paper(paper):
    """
    Runs multi-agent evaluation of a research paper.
    """

    # Initialize LLM
    llm = LLM(
        model="gpt-4o-mini",
        temperature=0.2
    )

    # Create agents
    consistency_agent = create_consistency_agent(llm)
    grammar_agent = create_grammar_agent(llm)
    novelty_agent = create_novelty_agent(llm)
    factcheck_agent = create_factcheck_agent(llm)
    authenticity_agent = create_authenticity_agent(llm)

    # Safely extract paper sections
    abstract = paper.get("abstract", "Not available")
    methodology = paper.get("methodology", "Not available")
    results = paper.get("results", "Not available")

    # Task 1: Methodology vs Results Consistency
    consistency_task = Task(
        description=f"""
Evaluate whether the methodology logically supports the results.

Methodology:
{methodology}

Results:
{results}

Return:
1. Score (0-100)
2. Short explanation
""",
        agent=consistency_agent
    )

    # Task 2: Grammar & clarity
    grammar_task = Task(
        description=f"""
Evaluate grammar quality and clarity of the abstract.

Text:
{abstract}

Return:
Rating: High / Medium / Low
Short explanation
""",
        agent=grammar_agent
    )

    # Task 3: Research novelty
    novelty_task = Task(
        description=f"""
Evaluate novelty of this research.

Abstract:
{abstract}

Return:
1. Novelty rating (High / Medium / Low)
2. Explanation
""",
        agent=novelty_agent
    )

    # Task 4: Fact checking
    factcheck_task = Task(
        description=f"""
Verify factual plausibility of claims.

Text:
{abstract}

Return:
1. Possible factual concerns
2. Explanation
""",
        agent=factcheck_agent
    )

    # Task 5: Fabrication detection
    authenticity_task = Task(
        description=f"""
Analyze whether results appear fabricated or statistically suspicious.

Results:
{results}

Return:
1. Fabrication probability (Low / Medium / High)
2. Explanation
""",
        agent=authenticity_agent
    )

    # Crew setup
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
        process=Process.sequential,
        verbose=False
    )

    # Run evaluation
    crew.kickoff()

    # Structured results (better for Streamlit UI)
    results = {
        "consistency_analysis": str(consistency_task.output),
        "grammar_analysis": str(grammar_task.output),
        "novelty_analysis": str(novelty_task.output),
        "factcheck_analysis": str(factcheck_task.output),
        "authenticity_analysis": str(authenticity_task.output)
    }

    return results
```
