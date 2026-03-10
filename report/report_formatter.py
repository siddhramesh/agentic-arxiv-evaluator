def format_report(title, evaluation):

    report = f"""
# Judgement Report

## Paper Title
{title}

## Executive Summary
{evaluation['executive_summary']}

## Detailed Scores

**Consistency Score:** {evaluation['consistency_score']} / 100

**Grammar Rating:** {evaluation['grammar_rating']}

**Novelty Index**
{evaluation['novelty_index']}

**Accuracy / Fabrication Risk**
{evaluation['fabrication_risk']}

## Fact Check Log
"""

    for item in evaluation["fact_check_log"]:
        report += f"- {item}\n"

    return report
