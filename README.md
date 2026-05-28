# Generative AI & Advanced LLM Engineering Portfolio

Welcome to my core Generative AI repository. This monorepo consolidates 5 production-grade AI applications, focusing on stateful multi-agent systems, secure LLM gateway architectures, high-throughput vector pipelines, and multimodal data extraction.

## 🚀 Repository Directory

### [01. Stateful Multi-Agent Research Blog Assistant](./01-stateful-multi-agent)
Architected and compiled an 8-node stateful multi-agent system using LangGraph to automate the discovery, summarization, and transformation of dense research literature into technical blogs. 
* **Key Specs:** LangGraph, LangChain (LCEL), OpenAI GPT-4o-mini, Pydantic State Management, Streamlit.
* **Core Highlight:** Replaced linear chains with a cyclic graph using a centralized `AgentState` data model to pass context securely across independent agent nodes.

### [02. AI Research Paper Screener & Candidate Auditor](./02-research-screener)
Engineered an automated document screening pipeline that ingests high-density, unstructured academic literature PDFs and converts raw text streams into clean tokens.
* **Key Specs:** FAISS Vector DB, OpenAI Embeddings (`text-embedding-3-small`), GPT-4o-mini, PyPDF.
* **Core Highlight:** Features a semantic search layer evaluating complex criteria against a local vector store, backed by strict JSON enforcement and low-temperature gateway controls (0.1).

### [03. Interactive Multimodal Pictionary Game Clone](./03-multimodal-pictionary)
Developed a real-time, interactive drawing application where users sketch geometric concepts and a multimodal vision AI model processes the stroke data to predict intent dynamically.
* **Key Specs:** Google GenAI SDK (`gemini-2.5-flash`), Streamlit-Drawable-Canvas, Pillow (PIL).
* **Core Highlight:** Programmatically strips alpha-channel transparency stream noise from canvas array coordinates and uses structured JSON mode boundaries to handle victory states deterministically.

### [04. AI Python Code Auditor Pro / Structured Data Gateway](./04-code-auditor-pro)
Engineered an interactive developer dashboard to execute deterministic structural, semantic, and syntactic analysis on complex Python source code blocks.
* **Key Specs:** OpenAI API, Python Abstract Syntax Tree (AST) Parsing, Structural JSON Schema Validation.
* **Core Highlight:** Hardens LLM gateway security architectures to neutralize adversarial prompt injections while utilizing explicit JSON exception-handling wrappers to eliminate application crashes from malformed payloads.

### [05. Semantic Subtitle Search Engine & Ingestion Pipeline](./05-semantic-subtitle-search)
Designed an end-to-end semantic document indexing, vectorization, and retrieval pipeline enabling high-accuracy conceptual search functionalities over standard string matching.
* **Key Specs:** ChromaDB (Vector Database), Sentence-Transformers, Regular Expressions (RegEx).
* **Core Highlight:** Implements a dynamic sliding-window text chunking algorithm with token overlaps to preserve semantic context while using RegEx preprocessing filters to reduce physical vector storage footprints by over 40%.

---

## 🛠️ Global Technical Core
* **Languages:** Python, JavaScript, SQL
* **Architectures:** Retrieval-Augmented Generation (RAG), Multi-Agent Swarms, Sovereign & Local AI Routing, Static Code Analysis
* **Data Security:** Strict JSON Schema Enforcement, Defensive System Prompts, Low-Temperature Clamping

Each project directory contains its own localized environment setup instructions, isolated source files, and detailed architectural maps.
