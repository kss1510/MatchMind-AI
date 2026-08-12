import streamlit as st
import sys
import os

# Add parent directory to sys.path so we can import from core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.matchmind_engine import MatchMindEngine

def main():
    st.set_page_config(page_title="MatchMind AI", page_icon="🏏", layout="wide")

    st.title("MatchMind AI")
    st.subheader("Multi-Agent Cricket Intelligence Platform")

    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.write("### Configuration")
        match_id_input = st.text_input("Enter Cricbuzz Match ID", value="40381")
        
        analyze_btn = st.button("Analyze Match", type="primary")

    if analyze_btn:
        try:
            match_id = int(match_id_input)
        except ValueError:
            st.error("Invalid Match ID. Please enter a valid number.")
            return

        st.markdown("---")
        
        with st.spinner("Initializing MatchMind AI Engine..."):
            engine = MatchMindEngine()
            
        with st.spinner("Fetching data, parsing scorecard, and running specialist agents (this may take a few minutes)..."):
            result = engine.process_match(match_id)

        if not result.get("success"):
            st.error(f"Execution Failed: {result.get('error')}")
            return

        st.success("Match analysis completed successfully!")

        match_context = result["match_context"]
        
        # Display Match Overview
        st.write("### Match Overview")
        st.write(f"**Teams:** {match_context.team} vs {match_context.opponent}")
        st.write(f"**Format:** {match_context.format}")
        st.write(f"**Venue:** {match_context.venue}")
        st.write(f"**Date:** {match_context.match_date}")
        
        with st.expander("View Scorecard Summary"):
            st.json(match_context.scorecard)
            
        with st.expander("View Agent Execution Status"):
            selected = [agent["agent"] for agent in result["selected_agents"]]
            st.write(f"**Selected Agents:** {', '.join(selected)}")
            for res in result["agent_results"]:
                if res["agent"] != "Report Generator Agent":
                    st.write(f"✅ {res['agent']} completed.")

        st.markdown("---")
        st.write("### Final MatchMind AI Report")
        st.markdown(result["final_report"])


if __name__ == "__main__":
    main()
