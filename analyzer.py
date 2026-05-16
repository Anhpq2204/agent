import time
from state import GraphState
from llm_service import call_llm_analyze_paper

def analyze_papers(state: GraphState) -> GraphState:
    print("[*] Node: analyze_papers (Summarization & Extraction)...")
    analyses = []
    
    for paper in state["raw_papers"]:
        print(f"    - Analyzing: {paper['title']}")
        
        result = call_llm_analyze_paper(paper['title'], paper['year'], paper['abstract'])
        
        analyses.append({
            "title": result.summary.title,
            "problem": result.summary.problem,
            "method": result.summary.method,
            "key_contribution": result.summary.key_contribution,
            "main_biological_insight": result.summary.main_biological_insight,
            "datasets": result.extraction.datasets,
            "data_type": result.extraction.data_type,
            "model_method": result.extraction.model_method,
            "evaluation_metrics": result.extraction.evaluation_metrics,
            "baselines": result.extraction.baselines
        })
        time.sleep(1) # Rate limit
        
    return {"analyses": analyses}
