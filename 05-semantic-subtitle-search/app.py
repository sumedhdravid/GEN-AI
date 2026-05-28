import streamlit as st
from src.text_chunker import strip_subtitle_timestamp_noise, execute_sliding_window_chunking
import chromadb
from chromadb.utils import embedding_functions

st.set_page_config(page_title="Semantic Search Engine Ingestion Pipeline", layout="wide")
st.title("🔍 Semantic Subtitle Search Engine & Ingestion Pipeline")
st.caption("High-throughput vector collection workflows running inside a persistent local ChromaDB instance.")

# Initialize a persistent client database system inside local file workspace directories
@st.cache_resource
def get_local_persistent_db_client():
    client = chromadb.PersistentClient(path="chroma_db")
    # Initialize a lightweight default local embedding framework
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    collection = client.get_or_create_collection(name="subtitle_vectors_pipeline", embedding_function=emb_fn)
    return collection

db_collection = get_local_persistent_db_client()

# Sample mock subtitle content string layer matching default SRT layout tracks structure
mock_srt = """1
00:00:01,000 --> 00:00:04,500
Welcome back to the deep-tech engineering architecture session.

2
00:00:05,100 --> 00:00:09,800
Today we are implementing highly optimized sovereign multi-model agent routing swarms.

3
00:00:10,200 --> 00:00:15,000
Data privacy metrics dictate that sensitive user records can never touch public cloud endpoints.
"""

uploaded_srt_raw = st.text_area("Input Target SRT / Subtitle Log Document Metadata Stream Source:", value=mock_srt, height=200)

if st.button("Trigger Pipeline Indexing Process Loop"):
    if uploaded_srt_raw.strip():
        with st.spinner("Executing regex cleanup filters, chunk partitioning loops, and database indexing..."):
            try:
                # 1. Strip timestamp noise using regex
                normalized_text = strip_subtitle_timestamp_noise(uploaded_srt_raw)
                
                # 2. Compute text window slices via sliding-window chunking
                text_segments = execute_sliding_window_chunking(normalized_text, window_size_tokens=15, overlap_tokens=5)
                
                # Empty-stream validation guards ensuring database consistency
                if not text_segments or (len(text_segments) == 1 and text_segments[0] == ""):
                    st.error("Pipeline Validation Exception: Ingestion payload stream resulted in empty token segments.")
                else:
                    # 3. Batch insert vector assets into persistent collection storage
                    ids = [f"id_segment_{i}" for i in range(len(text_segments))]
                    metadatas = [{"source_layer_index": i} for i in range(len(text_segments))]
                    
                    db_collection.add(
                        documents=text_segments,
                        metadatas=metadatas,
                        ids=ids
                    )
                    st.success(f"High-throughput collection loop finalized: Embedded {len(text_segments)} documents successfully into ChromaDB storage layers.")
            except Exception as e:
                st.error(f"Ingestion pipeline process failed: {str(e)}")

st.divider()
st.subheader("🎯 Test Conceptual Search Invalidation Layer")
query_search_input = st.text_input("Enter your semantic query concept:", value="data privacy parameters")

if st.button("Query Local Persistent Vector DB"):
    if query_search_input:
        with st.spinner("Calculating similarity vectors..."):
            query_results = db_collection.query(
                query_texts=[query_search_input],
                n_results=2
            )
            
            # Render returned segments mapping context
            if query_results and 'documents' in query_results and query_results['documents'][0]:
                for idx, match_doc in enumerate(query_results['documents'][0]):
                    distance_metric = query_results['distances'][0][idx] if 'distances' in query_results else "N/A"
                    st.info(f"**Matched Result Match Node [{idx+1}]** (Vector Distance Index Score: {distance_metric})")
                    st.write(match_doc)
            else:
                st.warning("No records matched the conceptual parameter input threshold.")
