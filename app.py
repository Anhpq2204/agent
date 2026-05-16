import streamlit as st
import os
from main import build_graph
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Research Agent Demo", page_icon="🧬", layout="wide")

st.title("🧬 Autonomous Research Agent")
st.markdown("A full-cycle research agent using LangGraph and Gemini to perform comprehensive literature reviews.")

with st.sidebar:
    st.header("⚙️ Configuration")
    topic = st.text_area("Research Topic", value="Gene expression single-cell spatial machine learning", height=100)
    limit = st.slider("Number of Papers", min_value=1, max_value=15, value=5, help="More papers will take longer to process.")
    
    st.markdown("---")
    api_key_input = st.text_input("Gemini API Key (Optional if set in .env)", type="password")

if st.button("Run Research Pipeline", type="primary"):
    if api_key_input:
        os.environ["GEMINI_API_KEY"] = api_key_input
        # We need to re-configure if the user just provided it
        import google.generativeai as genai
        genai.configure(api_key=api_key_input)
        
    if not os.getenv("GEMINI_API_KEY"):
        st.error("Please provide a Gemini API Key either in the sidebar or in your .env file.")
        st.stop()
        
    # Re-import to ensure config uses the new env var if it was just set
    # Actually, config.py is already evaluated, so we might need to be careful.
    # But since we update os.environ before importing build_graph (which we did at top), it might be too late for config.py.
    # Let's manually reconfigure just in case
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    st.info(f"Starting research on: **{topic}**")
    
    app = build_graph()
    
    initial_state = {
        "topic": topic,
        "limit": limit,
        "raw_papers": [],
        "analyses": [],
        "comparison_table": "",
        "literature_review": "",
        "research_ideas": [],
        "final_report": ""
    }
    
    # We use st.status to show a collapsible progress container
    with st.status("Agent Workflow Running...", expanded=True) as status:
        st.write("Initializing graph...")
        # We can step through the stream to show progress dynamically
        for output in app.stream(initial_state):
            for node_name, state_update in output.items():
                st.write(f"✅ Finished node: `{node_name}`")
                
                # We save the latest state
                final_state = state_update
        
        status.update(label="Research Complete!", state="complete", expanded=False)
    
    st.success("Successfully generated the literature review!")
    
    # Display the final report
    st.markdown("---")
    
    # If final_report is in the last updated state
    report_content = final_state.get("final_report", "Error: Report generation failed.")
    st.markdown(report_content)
    
    st.download_button(
        label="Download Report as Markdown",
        data=report_content,
        file_name="literature_review.md",
        mime="text/markdown"
    )
