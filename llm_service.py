import json
import google.generativeai as genai
from config import model
from schemas import PaperAnalysis, ResearchIdeas, PaperSummary, StructuredExtraction

def call_llm_analyze_paper(title: str, year: str, abstract: str) -> PaperAnalysis:
    prompt = f"""
    You are an expert computational biologist. Analyze the following academic paper abstract:
    
    Title: {title}
    Year: {year}
    Abstract: {abstract}
    
    Task: Extract the summary and structured features exactly as specified in the schema.
    If information is missing, write "insufficient evidence".
    Do not hallucinate any information.
    """
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=PaperAnalysis,
            ),
        )
        return PaperAnalysis.model_validate_json(response.text)
    except Exception as e:
        print(f"      Error analyzing {title}: {e}")
        # Return fallback
        fallback_summary = PaperSummary(
            title=title, problem="Error", method="Error", key_contribution="Error", main_biological_insight="Error"
        )
        fallback_ext = StructuredExtraction(
            datasets="Error", data_type="Error", model_method="Error", evaluation_metrics="Error", baselines="Error"
        )
        return PaperAnalysis(summary=fallback_summary, extraction=fallback_ext)

def call_llm_classify_tasks(analyses: list) -> list:
    prompt = "Given the following paper methods and problems, classify the 'Task type' (e.g., DE analysis, clustering, imputation, spatial mapping, GRN inference) in 1-3 words.\n\n"
    for i, a in enumerate(analyses):
        prompt += f"Paper {i}: {a['title']}\nProblem: {a['problem']}\nMethod: {a['method']}\n\n"
        
    prompt += "Return the classifications as a strict JSON list of strings in the exact same order."
    
    try:
        response = model.generate_content(prompt, generation_config=genai.GenerationConfig(response_mime_type="application/json"))
        task_types_res = json.loads(response.text)
        if isinstance(task_types_res, list) and len(task_types_res) == len(analyses):
            return task_types_res
    except Exception as e:
        print(f"Error classifying task types: {e}")
    return ["insufficient evidence"] * len(analyses)

def call_llm_generate_review(context: str) -> str:
    prompt = f"""
    Write a structured literature review on Gene Expression analysis using ONLY the provided papers.
    
    Requirements:
    - Group papers by methodology.
    - Explain the evolution of gene expression analysis methods based on these papers.
    - Highlight key trends and breakthroughs.
    - Identify agreements and disagreements among the papers.
    - Use EXACT paper titles as inline citations (e.g., "As seen in [Title]"). Do NOT use fake citations.
    
    Papers Context:
    {context}
    """
    response = model.generate_content(prompt)
    return response.text

def call_llm_generate_ideas(review: str) -> list:
    prompt = f"""
    Based on the following literature review and paper analyses on Gene Expression, identify limitations such as noise in scRNA-seq, batch effects, low spatial resolution, poor interpretability of deep models, or lack of cross-dataset generalization.
    
    Propose 3-7 novel research ideas. For each idea, you MUST provide the following fields exactly:
    - problem_motivation
    - proposed_method
    - expected_contribution
    - possible_dataset
    
    Literature Review:
    {review}
    """
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=ResearchIdeas,
            ),
        )
        ideas_obj = ResearchIdeas.model_validate_json(response.text)
        return [idea.model_dump() for idea in ideas_obj.ideas]
    except Exception as e:
        print(f"Error generating research ideas: {e}")
        return []
