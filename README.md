# Agentic Research Paper Evaluator

## Overview

The **Agentic Research Paper Evaluator** is a multi-agent AI platform that automatically evaluates academic papers from **arXiv**.

Instead of simply summarizing a paper, the system performs a **peer-review style analysis** by coordinating multiple specialized AI agents. Each agent focuses on a different aspect of evaluation such as logical consistency, language quality, factual accuracy, novelty, and authenticity.

The system scrapes an arXiv paper, extracts and decomposes its sections, and runs a coordinated agent pipeline to produce a **Judgement Report**.

---

## Features

* Automatic **arXiv paper scraping**
* PDF text extraction
* Paper decomposition into sections:

  * Abstract
  * Methodology
  * Results
  * Conclusion
* Multi-agent evaluation using **CrewAI**
* Streamlit interface for easy interaction
* Automated evaluation report generation
* Downloadable report output

---

## System Architecture

User Input (arXiv URL)
↓
Download PDF from arXiv
↓
Extract text from paper
↓
Decompose paper into sections
↓
Run multiple AI agents
↓
Generate evaluation report
↓
Display results in Streamlit UI

---

## Agents in the System

### Consistency Agent

Evaluates whether the methodology logically supports the results presented in the paper.

### Grammar & Language Agent

Reviews the academic tone, clarity, and grammatical quality of the paper.

### Novelty Agent

Analyzes whether the research contribution appears novel compared to existing work.

### Fact-Checking Agent

Verifies formulas, constants, and scientific claims mentioned in the paper.

### Authenticity Agent

Estimates the probability of fabricated results or statistical anomalies.

---

## Evaluation Output

The system generates a **Judgement Report** including:

* Executive Summary
* Consistency Score (0–100)
* Grammar Rating
* Novelty Index
* Fact Check Log
* Fabrication Risk Assessment

Example output:

Executive Summary: PASS

Consistency Score: 82

Grammar Rating: High

Novelty Index: Moderately Novel

Fabrication Risk: 18%

---

## Project Structure

agentic-arxiv-evaluator/

app.py – Streamlit interface
requirements.txt – project dependencies
runtime.txt – Python version for deployment

agents/ – AI agent definitions
tasks/ – agent task definitions
tools/ – scraping and parsing utilities
evaluator/ – CrewAI orchestration
reports/ – evaluation report generation

---

## Installation

Clone the repository:

git clone https://github.com/siddhramesh/agentic-arxiv-evaluator.git

cd agentic-arxiv-evaluator

Install dependencies:

pip install -r requirements.txt

---

## Environment Variables

Set your API key before running the application.

For OpenAI:

export OPENAI_API_KEY=your_api_key_here

---

## Running the Application

Start the Streamlit application:

streamlit run app.py

The interface will open in your browser.

---

## Usage

1. Open the Streamlit interface
2. Enter an arXiv paper URL
3. Click **Evaluate Paper**
4. The system will:

   * Download the paper
   * Extract and analyze the content
   * Run multiple AI agents
   * Generate an evaluation report

You can download the generated report directly from the interface.

---

## Example Input

https://arxiv.org/abs/1706.03762

---

## Technology Stack

Python
Streamlit
CrewAI
PyMuPDF
Requests
OpenAI API

---

## Future Improvements

* Semantic Scholar integration for deeper novelty detection
* Retrieval-augmented fact verification
* Parallel agent execution
* Visualization dashboards for evaluation metrics
* Support for additional research repositories

---

## License

This project is for educational and research purposes.

---

## Author

Siddhramesh Diksanggi
