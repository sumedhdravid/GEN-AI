from pydantic import BaseModel, Field
from typing import List, Optional

class AgentState(BaseModel):
    """Centralized Pydantic data model serving as the single source of truth."""
    raw_query: str = Field(description="The primary user search topic or query.")
    papers_metadata: List[dict] = Field(default=[], description="Extracted raw metadata streams from literature.")
    summaries: List[str] = Field(default=[], description="Automated two-sentence context summaries.")
    trends: str = Field(default="", description="Cross-paper trend synthesis payload.")
    blog_markdown: str = Field(default="", description="The fully generated draft markdown content.")
    seo_metadata: dict = Field(default={}, description="Appended custom SEO YAML front-matter maps.")
    current_node: str = Field(default="", description="Tracking flag for current graph telemetry status.")
