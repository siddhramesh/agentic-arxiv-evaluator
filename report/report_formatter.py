def format_report(title, evaluation):

    report = f"""
# Judgement Report

## Paper Title
{title}

## AI Evaluation

{evaluation['analysis']}
"""

    return report
