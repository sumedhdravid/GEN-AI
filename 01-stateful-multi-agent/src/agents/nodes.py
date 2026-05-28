import json
from ..state import AgentState

def metadata_extractor_node(state: AgentState) -> dict:
    """Node 1: Simulates extracting structured metadata tokens from literature."""
    query = state.raw_query
    # Mocking ingestion pipeline for high-density papers matching the query
    mocked_papers = [
        {"title": f"Advanced Foundations in {query}", "authors": "S. Dravid et al.", "year": 2026},
        {"title": f"Stateful Architectural Paradigms of {query}", "authors": "Alpha Swarm Labs", "year": 2025}
    ]
    return {"papers_metadata": mocked_papers, "current_node": "metadata_extractor"}

def summarizer_node(state: AgentState) -> dict:
    """Node 2: Generates clean, localized summaries from paper metadata."""
    summaries = []
    for paper in state.papers_metadata:
        summaries.append(f"Analysis of '{paper['title']}' highlights critical methodologies deployed by {paper['authors']} in {paper['year']}.")
    return {"summaries": summaries, "current_node": "summarizer"}

def trend_analyzer_node(state: AgentState) -> dict:
    """Node 3: Executes cross-paper synthesis processing loops."""
    combined_context = " ".join(state.summaries)
    synthesized_trend = f"Synthesized Core Trend: Convergence of production patterns suggests a shift toward zero-latency executions within fields relating to '{state.raw_query}'."
    return {"trends": synthesized_trend, "current_node": "trend_analyzer"}

def markdown_generator_node(state: AgentState) -> dict:
    """Node 4: Compiles contextual elements into structural Markdown."""
    markdown = f"# Deep-Dive Research Report on {state.raw_query}\n\n"
    markdown += f"## Executive Synthesis\n{state.trends}\n\n"
    markdown += "## Analyzed Literature Foundations\n"
    for summary in state.summaries:
        markdown += f"* {summary}\n"
    return {"blog_markdown": markdown, "current_node": "markdown_generator"}

def seo_optimizer_node(state: AgentState) -> dict:
    """Node 5: Appends structured SEO metadata mapping directly onto the payload object."""
    seo_map = {
        "title": f"Unlocking {state.raw_query} - Architectural Insights",
        "meta_description": f"An expert technical analysis exploring the latest breakthroughs and trends in {state.raw_query}.",
        "keywords": [state.raw_query, "AI Engineering", "Stateful Architecture", "Tech Trends"]
    }
    return {"seo_metadata": seo_map, "current_node": "seo_optimizer"}
