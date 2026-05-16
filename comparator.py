from state import GraphState
from llm_service import call_llm_classify_tasks

def generate_comparison(state: GraphState) -> GraphState:
    print("[*] Node: generate_comparison...")
    analyses = state["analyses"]
    
    table = "| Title | Data Type | Modeling Approach | Task Type | Dataset/Complexity |\n"
    table += "|---|---|---|---|---|\n"
    
    task_types = call_llm_classify_tasks(analyses)

    for i, a in enumerate(analyses):
        title_short = a['title']
        data_type = a['data_type'].replace("|", "/")
        model_method = a['model_method'].replace("|", "/")
        task = str(task_types[i]).replace("|", "/")
        dataset = a['datasets'].replace("|", "/")
        table += f"| {title_short} | {data_type} | {model_method} | {task} | {dataset} |\n"
        
    return {"comparison_table": table}
