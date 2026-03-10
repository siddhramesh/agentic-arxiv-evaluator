from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_paper(text):

    prompt = f"""
You are an AI research review committee evaluating a research paper.

Simulate five reviewers:

1. Consistency Reviewer
2. Grammar Reviewer
3. Novelty Reviewer
4. Fact Check Reviewer
5. Research Integrity Reviewer

Return structured output.

Paper:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
