def format_report(title, evaluation):

    report = f"""
# Judgement Report

## Paper Title
{title}

## Executive Summary
This paper was evaluated using a multi-agent AI peer review system.

## Detailed Evaluation

### Consistency Score
Evaluates whether methodology logically supports results.

### Grammar Rating
Evaluation of language clarity and professional tone.

### Novelty Index
Assessment of originality and uniqueness.

### Fact Check Log
Verification of claims and referenced data.

### Fabrication Probability
Likelihood of fabricated or inconsistent results.

---

## Agent Analysis
{evaluation['analysis']}
"""

    return report
