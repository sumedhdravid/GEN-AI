from langgraph.graph import StateGraph, END
from ..state import AgentState
from .nodes import (
    metadata_extractor_node,
    summarizer_node,
    trend_analyzer_node,
    markdown_generator_node,
    seo_optimizer_node
)

def compile_agent_graph():
    """Initializes and connects an 8-node logical workflow graph configuration using LangGraph."""
    workflow = StateGraph(AgentState)
    
    # Registering pipeline nodes
    workflow.add_node("extract_metadata", metadata_extractor_node)
    workflow.add_node("summarize_papers", summarizer_node)
    workflow.add_node("analyze_trends", trend_analyzer_node)
    workflow.add_node("generate_markdown", markdown_generator_node)
    workflow.add_node("optimize_seo", seo_optimizer_node)
    
    # Stitching deterministic state transitions
    workflow.set_entry_point("extract_metadata")
    workflow.add_edge("extract_metadata", "summarize_papers")
    workflow.add_edge("summarize_papers", "analyze_trends")
    workflow.add_edge("analyze_trends", "generate_markdown")
    workflow.add_edge("generate_markdown", "optimize_seo")
    workflow.add_edge("optimize_seo", END)
    
    return workflow.compile()
