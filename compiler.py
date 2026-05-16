from state import GraphState

def compile_final_report(state: GraphState) -> GraphState:
    print("[*] Node: compile_final_report...")
    report = "# Comprehensive Literature Review on Gene Expression\n\n"
    
    report += "## 1. Paper List\n\n"
    for p in state["raw_papers"]:
        url_link = f" - [Link]({p['url']})" if p.get("url") else ""
        report += f"- {p['title']} ({p['year']}){url_link}\n"
        
    report += "\n## 2. Paper Summaries\n\n"
    for a in state["analyses"]:
        report += f"**{a['title']}**\n"
        report += f"- **Problem:** {a['problem']}\n"
        report += f"- **Method:** {a['method']}\n"
        report += f"- **Key Contribution:** {a['key_contribution']}\n"
        report += f"- **Main Biological Insight:** {a['main_biological_insight']}\n\n"
        
    report += "## 3. Comparison Table\n\n"
    report += state["comparison_table"] + "\n\n"
    
    report += "## 4. Literature Review\n\n"
    report += state["literature_review"] + "\n\n"
    
    return {"final_report": report}
