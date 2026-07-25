# MediRef AI

## a. App Name, What It Does & Real Problem
* **App Name:** MediRef AI
* **What it does:** An automated research analysis tool that parses medical abstracts to instantly extract PICO frameworks, study designs, statistical results, and methodological limitations.
* **Real Problem & Audience:** Medical students, junior researchers, and clinicians spend excessive hours screening dense literature and formatting clinical reviews. MediRef AI accelerates literature appraisal and reference preparation.

## b. Live Deployed URL
[https://mediref-ai.streamlit.app](https://mediref-ai.streamlit.app) *(Replace with your actual deployed Streamlit link)*

## c. Features List
* Instant abstract text parsing.
* Automated PICO (Population, Intervention, Comparison, Outcome) extraction.
* Clinical study design identification.
* Methodological bias and limitation scanner.
* MeSH keyword generator for indexing.

## d. AI Feature & System Prompt
* **Model:** Google Gemini API (`gemini-2.5-flash`).
* **System Prompt / Instructions:**
  > "You are an expert medical research assistant and epidemiologist. Analyze the provided research abstract or text and extract the following structured details in valid Markdown: 1. **PICO Breakdown**: Population, Intervention, Comparison, and Outcome. 2. **Study Design**: Identify the study design (e.g., RCT, Systematic Review, Observational). 3. **Key Findings**: Bullet points of primary statistical and clinical results. 4. **Methodology & Limitations**: Potential biases or limitations evident from the abstract. 5. **Suggested MeSH Terms**: Relevant keywords for literature indexing. Keep the analysis objective, concise, and clinically rigorous."

## e. Tools, Services, and Models Used
* **Frontend/Backend:** Streamlit (Python framework)
* **AI Model:** Google Gemini API via `google-genai` SDK
* **Hosting:** Streamlit Community Cloud
* **Version Control:** Git & GitHub

## f. Screenshots
*(Make sure to upload 3 screenshots of your app showing the input text area, loading state, and generated analysis report, then reference them here)*
1. **App Interface & Input Box:** ![Input Screen](screenshot1.png)
2. **Analysis Loading State:** ![Loading State](screenshot2.png)
3. **Generated PICO & Clinical Report:** ![Report Output](screenshot3.png)

## g. How to Run the Project Locally
1. Clone the repository: 
   `git clone https://github.com/rida61214-cpu/mediref-ai.git`
2. Install dependencies: 
   `pip install -r requirements.txt`
3. Set your API key in a local `.env` file: 
   `GEMINI_API_KEY=your_actual_api_key_here`
4. Run the app: 
   `streamlit run app.py`
