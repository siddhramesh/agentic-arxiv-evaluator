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
* Powered by **Groq free-tier LLM** (llama-3.3-70b-versatile)
* Streamlit interface for easy interaction
* Automated evaluation report generation
* Downloadable report output

---

## System Architecture

```
User Input (arXiv URL)
↓
Download PDF from arXiv
↓
Extract text from paper
↓
Decompose paper into sections
↓
Run multiple AI agents (CrewAI sequential pipeline)
↓
Generate evaluation report
↓
Display results in Streamlit UI
```

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

### Judge Agent
Synthesizes all agent outputs into a final Judgement Report with pass/fail recommendation.

---

## Evaluation Output

The system generates a **Judgement Report** including:

* Executive Summary (Pass/Fail recommendation)
* Consistency Score (0–100)
* Grammar Rating (High/Medium/Low)
* Novelty Index (qualitative description)
* Fact Check Log (verified vs. unverified claims)
* Fabrication Risk Assessment (percentage-based)

Example output:

```
Executive Summary: PASS
Consistency Score: 82
Grammar Rating: High
Novelty Index: Highly Novel
Fabrication Risk: 5%
```

---

## Project Structure

```
agentic-arxiv-evaluator/
├── app.py                  – Streamlit interface
├── requirements.txt        – project dependencies
├── runtime.txt             – Python version for deployment
├── agents/                 – AI agent definitions
├── tasks/                  – agent task definitions
├── tools/                  – scraping and parsing utilities
├── evaluator/              – CrewAI orchestration
└── reports/                – evaluation report generation
```

---

## Environment Variables

This project uses **Groq** as the free-tier LLM provider.

### Get a Groq API Key

1. Sign up at [console.groq.com](https://console.groq.com)
2. Navigate to **API Keys** in the left sidebar
3. Click **Create API Key**, give it a name, and copy the key (starts with `gsk_`)

### Running Locally

Create a `.env` file in the project root:

```
GROQ_API_KEY=gsk_your_api_key_here
```

Or export it directly:

```bash
export GROQ_API_KEY=gsk_your_api_key_here
```

### Deploying on Streamlit Cloud

In your Streamlit Cloud app settings, go to **Secrets** and add:

```toml
GROQ_API_KEY = "gsk_your_api_key_here"
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/siddhramesh/agentic-arxiv-evaluator.git
cd agentic-arxiv-evaluator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The interface will open in your browser at `http://localhost:8501`.

---

## Streamlit Cloud Deployment

This app is deployed on Streamlit Cloud. To deploy your own instance:

1. Fork the repository
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your GitHub repo
3. Set **Python version to 3.11** in the app settings
4. Add `GROQ_API_KEY` to the app Secrets
5. Deploy

---

## Usage

1. Open the Streamlit interface
2. Enter an arXiv paper URL (e.g. `https://arxiv.org/abs/1706.03762`)
3. Click **Evaluate Paper**
4. The system will:
   * Download and extract the paper
   * Run 6 specialized AI agents sequentially
   * Generate a structured Judgement Report
5. Download the report as a Markdown file

---

## Example Input

```
https://arxiv.org/abs/1706.03762
```

---

## Future Improvements

The following enhancements have been identified and can be implemented in future iterations of this project:

### 1. Real Novelty Search via Semantic Scholar API
Currently the Novelty Agent analyzes the abstract in isolation using LLM reasoning. A future improvement would integrate the free **Semantic Scholar API** (`tools/semantic_scholar.py`) to search for similar existing papers and provide evidence-based novelty scoring rather than relying solely on LLM opinion.

### 2. Citations Verification Agent
A dedicated `citations_agent.py` could be added to the `agents/` directory to verify whether references cited in the paper actually exist, are correctly attributed, and support the claims made. This would significantly strengthen the fact-checking pipeline.

### 3. Per-Agent Progress Bar
The current UI shows a single spinner during the entire 2-3 minute evaluation. A progress bar in `app.py` that updates after each of the 6 agents completes would make the experience more transparent and informative for the user.

### 4. Smart Retry Logic for Rate Limits
The current implementation uses a fixed 20-second sleep between agents to avoid LLM rate limits. A smarter approach using the `tenacity` library in `evaluator/evaluator.py` would implement exponential backoff retries, reducing unnecessary wait time when the API is available.

### 5. PDF Export
The current report is exported as Markdown. A future version could add PDF generation using `fpdf2` in the `reports/` directory, with a dedicated PDF download button in `app.py`, fully satisfying the PDF deliverable format mentioned in the assignment.

### 6. Paper Metadata Display
Before running the evaluation, the app could display the paper's title, authors, and publication date fetched from the arXiv API. This would give users confirmation they entered the correct paper before waiting for the full evaluation to complete.

---

## Technology Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Streamlit | Web interface |
| CrewAI | Multi-agent orchestration |
| Groq (llama-3.3-70b-versatile) | Free-tier LLM provider |
| PyMuPDF | PDF text extraction |
| LiteLLM | LLM provider abstraction |
| Requests | HTTP requests |
| arXiv API | Paper metadata and download |
