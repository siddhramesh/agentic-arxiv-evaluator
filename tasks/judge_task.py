from crewai import Task

def create_judge_task(agent, previous_results):

    return Task(

        description=f"""
        Review the evaluations provided by the other agents.

        Agent Evaluations:
        {previous_results}

        Provide a final judgement report including:

        - Executive Summary
        - Pass or Fail Recommendation
        - Key strengths
        - Major concerns
        """,

        expected_output="""
        A final research evaluation report with a PASS or FAIL
        recommendation and a brief justification.
        """,

        agent=agent
    )
