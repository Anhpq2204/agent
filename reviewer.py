from state import GraphState
from llm_service import call_llm_generate_review

def generate_review(state: GraphState) -> GraphState:
    print("[*] Node: generate_review...")
    context = ""
    for a in state["analyses"]:
        context += f"Title: {a['title']}\nMethod: {a['method']}\nContribution: {a['key_contribution']}\n\n"
        
    review_text = call_llm_generate_review(context)
    return {"literature_review": review_text}
