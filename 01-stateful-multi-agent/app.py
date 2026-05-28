import streamlit as st
import yaml
from src.agents.graph import compile_agent_graph
from src.state import AgentState

st.set_page_config(page_title="Stateful Multi-Agent Assistant", layout="wide")
st.title("🤖 Stateful Multi-Agent Research Blog Assistant")
st.caption("Architecture built on LangGraph & centralized Pydantic state tracking")

query_input = st.text_input("Enter your core technical research domain:", value="Sovereign AI Systems")

if st.button("Execute Autonomous Multi-Agent Loop"):
    if query_input:
        with st.spinner("Compiling workflow graph and coordinating agent nodes..."):
            # Initialize empty state dictionary maps
            initial_state = AgentState(raw_query=query_input)
            app_graph = compile_agent_graph()
            
            # Execute graph iteration
            final_output = app_graph.invoke(initial_state.model_dump())
            
            st.success("State graph loop complete!")
            
            # Display UI panels
            col1, col2 = st.columns([2, 1])
            with col1:
                st.subheader("📝 Generated Technical Documentation")
                st.markdown(final_output["blog_markdown"])
            
            with col2:
                st.subheader("⚙️ Injected SEO YAML Front-Matter")
                yaml_string = yaml.dump(final_output["seo_metadata"], default_flow_style=False)
                st.code(yaml_string, language="yaml")
                
                st.subheader("📊 Graph Telemetry Logs")
                st.json({
                    "final_node_reached": final_output["current_node"],
                    "total_ingested_metadata_records": len(final_output["papers_metadata"]),
                    "summary_strings_compiled": len(final_output["summaries"])
                })
    else:
        st.warning("Please supply an execution target query.")
