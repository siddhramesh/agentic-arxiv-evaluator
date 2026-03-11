from crewai import Task

def create_judge_task(agent, previous_results):
    return Task(
        description=f"""
        Review the evaluations provided by the other agents.

        Agent Evaluations:
        {previous_results}

        Provide a final judgement report including ALL of the following
        with exact numeric scores:

        - Executive Summary (2-3 sentences)
        - Pass or Fail Recommendation
        - Consistency Score: a number between 0 and 100
          (100 = methodology perfectly supports results)
        - Grammar Rating: one of High / Medium / Low
        - Novelty Index: a number between 0 and 100
          (100 = completely original contribution)
          followed by a qualitative label (e.g. Highly Novel, Moderately Novel, Incremental)
        - Fact Check Log: list of verified claims and unverified/questionable claims
        - Fabrication Probability: a percentage between 0% and 100%
          (0% = no fabrication risk, 100% = likely fabricated)
        - Key Strengths (bullet points)
        - Major Concerns (bullet points)

        You MUST output each score as an explicit number. Do not use ranges or qualitative
        descriptions in place of numbers for Consistency Score, Novelty Index,
        and Fabrication Probability.
        """,
        expected_output="""
        A structured final research evaluation report in this exact format:

        ## Executive Summary
        <2-3 sentence summary>

        ## Recommendation: PASS or FAIL

        ## Scores
        - Consistency Score: <number 0-100>
        - Grammar Rating: <High / Medium / Low>
        - Novelty Index: <number 0-100> (<qualitative label>)
        - Fabrication Probability: <percentage>%

        ## Fact Check Log
        **Verified Claims:**
        - <claim 1>
        - <claim 2>

        **Unverified / Questionable Claims:**
        - <claim 1>
        - <claim 2>

        ## Key Strengths
        - <strength 1>
        - <strength 2>

        ## Major Concerns
        - <concern 1>
        - <concern 2>
        """,
        agent=agent
    )
