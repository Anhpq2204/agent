from langgraph.graph import StateGraph, START, END
from state import GraphState

# Import nodes
from retriever import retrieve_papers
from analyzer import analyze_papers
from comparator import generate_comparison
from reviewer import generate_review
from compiler import compile_final_report

def build_graph():
    builder = StateGraph(GraphState)
    
    builder.add_node("retrieve_papers", retrieve_papers)
    builder.add_node("analyze_papers", analyze_papers)
    builder.add_node("generate_comparison", generate_comparison)
    builder.add_node("generate_review", generate_review)
    builder.add_node("compile_final_report", compile_final_report)
    
    builder.add_edge(START, "retrieve_papers")
    builder.add_edge("retrieve_papers", "analyze_papers")
    builder.add_edge("analyze_papers", "generate_comparison")
    builder.add_edge("generate_comparison", "generate_review")
    builder.add_edge("generate_review", "compile_final_report")
    builder.add_edge("compile_final_report", END)
    
    return builder.compile()

def main():
    topic = "Gene expression single-cell spatial machine learning"
    print(f"Starting LangGraph Workflow for topic: {topic}")
    
    app = build_graph()
    
    initial_state = {
        "topic": topic,
        "limit": 5, # Demo limit
        "raw_papers": [],
        "analyses": [],
        "comparison_table": "",
        "literature_review": "",
        "research_ideas": [],
        "final_report": ""
    }
    
    final_state = app.invoke(initial_state)
    
    with open("final_report.md", "w", encoding="utf-8") as f:
        f.write(final_state["final_report"])
        
    print("\n[*] LangGraph Workflow complete. Report saved to final_report.md")

if __name__ == "__main__":
    main()
