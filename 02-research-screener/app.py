import streamlit as st
import os
from src.ingestion import convert_pdf_to_clean_tokens
from src.gateway import AuditEvaluationSchema
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

st.set_page_config(page_title="AI Research Screener", layout="wide")
st.title("🔬 AI Research Paper Screener & Candidate Auditor")
st.caption("FAISS-driven semantic indexing platform backed by defensive JSON gateway execution constraints.")

# Ensure localized API access token exists safely before execution
os.environ["OPENAI_API_KEY"] = st.sidebar.text_input("OpenAI API Key:", type="password")

uploaded_file = st.file_uploader("Upload High-Density Unstructured Academic Literature (PDF)", type=["pdf"])
target_criteria = st.text_area("Target Candidate Match/Role Criteria:", value="Expertise in high-throughput vector processing pipelines, sliding window token logic, and localized model orchestration.")

if uploaded_file and target_criteria:
    if not os.environ.get("OPENAI_API_KEY"):
        st.error("Please provide your OpenAI API access key in the sidebar panel.")
    elif st.button("Run Semantic Pipeline & Audit Evaluation"):
        with st.spinner("Extracting stream sequences, mapping vector layers, and initializing gateway validation..."):
            try:
                # 1. Parsing raw file tokens
                clean_text = convert_pdf_to_clean_tokens(uploaded_file)
                
                # 2. In-Memory database instantiation & Cosine similarity ranking mapping
                embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")
                # Split raw document chunks safely for local store index ingestion
                chunks = [clean_text[i:i+1500] for i in range(0, len(clean_text), 1200)]
                
                vector_db = FAISS.from_texts(chunks, embeddings_model)
                retriever = vector_db.as_retriever(search_kwargs={"k": 3})
                matched_docs = retriever.get_relevant_documents(target_criteria)
                context_payload = "\n---\n".join([doc.page_content for doc in matched_docs])
                
                # 3. Constructing low-temperature model gateway architecture
                parser = JsonOutputParser(pydantic_object=AuditEvaluationSchema)
                
                system_prompt = (
                    "You are a strict, objective technical auditor code system checking incoming research payloads.\n"
                    "Evaluate the text payload below cleanly against target requirements metrics.\n"
                    "Enforce strict constraints: Clamped Temperature (0.1). No human prose or chat introductory statements.\n"
                    "Output payload MUST strictly align into explicit target schema mapping constraints.\n\n"
                    "Format Instructions:\n{format_instructions}\n\n"
                    "Context Source Payload Material:\n{context}\n\n"
                    "Target Metrics Evaluation Criteria:\n{criteria}"
                )
                
                prompt_template = ChatPromptTemplate.from_template(system_prompt)
                model = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
                
                # Wire execution pipeline chain layout
                chain = prompt_template | model | parser
                
                evaluation_results = chain.invoke({
                    "format_instructions": parser.get_format_instructions(),
                    "context": context_payload,
                    "criteria": target_criteria
                })
                
                # Render structured metrics
                st.success("Semantic extraction loop validated successfully.")
                
                score = evaluation_results["candidate_relevancy_percentage"]
                st.metric(label="Calculated Automated Relevancy Index Match", value=f"{score}%")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("💡 Detected Technical Breakthroughs")
                    for item in evaluation_results["matched_breakthroughs"]:
                        st.write(f"- {item}")
                with col2:
                    st.subheader("⚠️ Missing Competency Signals")
                    for item in evaluation_results["missing_technical_competencies"]:
                        st.write(f"- {item}")
                        
                st.subheader("🔍 Structured Audit Breakdown Justification")
                st.info(evaluation_results["justification_summary"])
                
            except Exception as ex:
                st.error(f"Execution boundary error encountered: {str(ex)}")
