import os
import streamlit as st
from google import genai
from google.genai import types

# Page Config
st.set_page_config(
    page_title="MediRef AI",
    page_icon="🩺",
    layout="centered"
)

# Initialize Gemini Client securely from environment variables
api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API Key not found. Please set it in your environment variables or Streamlit secrets.")
else:
    client = genai.Client(api_key=api_key)

st.title("🩺 MediRef AI")
st.subheader("Automated Research Abstract & Citation Assistant")
st.markdown("Paste a medical research abstract below to instantly extract its PICO framework, study design, key findings, and methodological limitations.")

# Text input for abstract
abstract_text = st.text_area("Paste Research Abstract Here:", height=200, placeholder="Background: ... Methods: ... Results: ... Conclusion: ...")

if st.button("Analyze Abstract", type="primary"):
    if not abstract_text.strip():
        st.warning("Please enter a valid abstract text.")
    else:
        with st.spinner("Analyzing literature through clinical lens..."):
            try:
                system_instruction = (
                    "You are an expert medical research assistant and epidemiologist. "
                    "Analyze the provided research abstract or text and extract the following structured details in valid Markdown: "
                    "1. **PICO Breakdown**: Population, Intervention, Comparison, and Outcome. "
                    "2. **Study Design**: Identify the study design (e.g., RCT, Systematic Review, Observational). "
                    "3. **Key Findings**: Bullet points of primary statistical and clinical results. "
                    "4. **Methodology & Limitations**: Potential biases or limitations evident from the abstract. "
                    "5. **Suggested MeSH Terms**: Relevant keywords for literature indexing. "
                    "Keep the analysis objective, concise, and clinically rigorous."
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=abstract_text,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.2,
                    ),
                )

                st.markdown("---")
                st.markdown("### 📊 Analysis Report")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
