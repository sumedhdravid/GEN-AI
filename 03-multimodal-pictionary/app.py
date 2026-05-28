import streamlit as st
import json
from streamlit_drawable_canvas import st_canvas
from src.canvas_processor import normalize_canvas_image_layers
import google.generativeai as genai

st.set_page_config(page_title="Multimodal Pictionary Clone", layout="centered")
st.title("🎨 Interactive Multimodal Pictionary Game Clone")
st.caption("Powered by google-genai-sdk integration tracking strict canvas token validation layouts.")

# Collect API validation keys from local sidebar UI component
gemini_key = st.sidebar.text_input("Google Gemini API Key:", type="password")

target_words = ["Microscope", "Space Rocket", "Server Rack", "Network Topology Diagram", "Database Architecture Diagram"]
if "current_word_index" not in st.session_state:
    st.session_state.current_word_index = 0

secret_target = target_words[st.session_state.current_word_index]

st.info(f"Draw this concept clearly on the workspace below: **{secret_target}**")

# Establish web design workspace dimension matrices
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 1)",
    stroke_width=4,
    stroke_color="#000000",
    background_color="#ffffff",
    height=320,
    width=480,
    drawing_mode="freedraw",
    key="canvas_instance"
)

if canvas_result.image_data is not None:
    # Check if user has drawn anything to prevent processing blanks
    if np.any(canvas_result.image_data[:, :, 3] > 0):
        if not gemini_key:
            st.warning("Please insert your Gemini API Key inside the sidebar dashboard panel configuration.")
        elif st.button("Submit Sketch for AI Inspection"):
            with st.spinner("Processing drawing arrays and running multimodal guess loops..."):
                try:
                    # Clean input array matrix allocations
                    processed_sketch = normalize_canvas_image_layers(canvas_result.image_data)
                    
                    # Target endpoint client configuration
                    genai.configure(api_key=gemini_key)
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    spatial_system_prompt = (
                        "Analyze this image token data array representing an engineering or technical sketch clone grid.\n"
                        "Identify what structural geometric concepts the user is drawing.\n"
                        "Enforce strict API constraints: return raw structural application/json JSON strings.\n"
                        "Structure format payload matching exactly: "
                        "{'ai_guess': 'String', 'confidence_metric_percentage': Float, 'geometric_analysis_notes': 'String'}"
                    )
                    
                    response = model.generate_content(
                        contents=[processed_sketch, spatial_system_prompt],
                        generation_config=genai.GenerationConfig(
                            response_mime_type="application/json",
                            temperature=0.2
                        )
                    )
                    
                    # Parse structural outputs smoothly
                    output_payload = json.loads(response.text)
                    
                    st.subheader("🤖 Multimodal AI Model Analysis Verdict")
                    st.write(f"Model Guess: **{output_payload.get('ai_guess')}**")
                    st.write(f"Confidence Index: **{output_payload.get('confidence_metric_percentage')}%**")
                    st.info(f"Structural Notes: {output_payload.get('geometric_analysis_notes')}")
                    
                    # Game victory logic calculations
                    guess = output_payload.get('ai_guess', '').lower()
                    if secret_target.lower() in guess or guess in secret_target.lower():
                        st.success("Victory! The AI correctly interpreted your sketch design layout.")
                        if st.button("Proceed to Next Technical Concept Blueprint"):
                            st.session_state.current_word_index = (st.session_state.current_word_index + 1) % len(target_words)
                            st.rerun()
                    else:
                        st.error("The AI failed to recognize the drawing context. Adjust geometry tracking strokes and retry.")
                        
                except Exception as ex:
                    st.error(f"Pipeline boundary exception error: {str(ex)}")
