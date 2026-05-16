from typing import List, Dict, Any, TypedDict

class GraphState(TypedDict):
    topic: str
    limit: int
    raw_papers: List[Dict[str, str]]
    analyses: List[Dict[str, Any]]
    comparison_table: str
    literature_review: str
    research_ideas: List[Dict[str, str]]
    final_report: str
