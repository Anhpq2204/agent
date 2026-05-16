# 🧬 Autonomous Gene Expression Research Agent

An intelligent, full-cycle research agent built with **LangGraph** and the **Gemini API** (Google Generative AI). This agent autonomously performs comprehensive literature reviews on computational biology and gene expression topics.

## 🚀 Features

- **Automated Paper Retrieval:** Uses the Europe PMC API to fetch real, verifiable academic papers (including PubMed links).
- **Intelligent Summarization & Extraction:** Leverages Gemini to extract the core problem, methodology, key contributions, biological insights, and structured data (datasets, models, baselines).
- **Methodology Comparison:** Automatically categorizes tasks and builds a comprehensive comparison table.
- **Synthesized Literature Review:** Generates a structured review chronicling the evolution of methods, trends, and agreements/disagreements with exact inline citations.
- **Streamlit Web UI:** An interactive web application for easy configuration and real-time execution tracking.

## 🏗️ Architecture

The pipeline is orchestrated as a directed graph using **LangGraph**. The workflow progresses sequentially through specific nodes:

1. `retriever.py`: Fetches papers dynamically.
2. `analyzer.py`: Extracts Summaries and Structured Extractions.
3. `comparator.py`: Generates a comparison table.
4. `reviewer.py`: Writes the literature review.
5. `compiler.py`: Formats everything into a finalized Markdown report.
6. `llm_service.py`: Centralized service handling all Gemini API calls and Pydantic schemas.

## 💻 Local Setup

1. Clone the repository and navigate into it:
   ```bash
   git clone <your-repo-url>
   cd agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Gemini API Key:
   - Create a `.env` file in the root directory.
   - Add your key: `GEMINI_API_KEY=your_api_key_here`
   - *(Alternatively, you can paste the key directly into the Streamlit sidebar).*

4. Run the Streamlit Application:
   ```bash
   streamlit run app.py
   ```

## ☁️ Deployment

This app is ready to be deployed to **Streamlit Community Cloud**. 
Just connect your GitHub repository and ensure you add your `GEMINI_API_KEY` to the Streamlit **Advanced Settings > Secrets** before deploying.
