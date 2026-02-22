import streamlit as st
from data_analyzer import DataAnalyzer
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="GenAI Data Analyzer", layout="wide")

st.title("🚀 GenAI-Powered Data Analysis Automation")
st.markdown("Upload CSV → Get instant EDA, insights & reports")

# File upload
uploaded_file = st.file_uploader("Choose CSV file", type="csv")

if uploaded_file is not None:
    # Save uploaded file
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())
    
    # Initialize analyzer
    analyzer = DataAnalyzer(uploaded_file)
    
    if st.button("🔍 Run AI Analysis", type="primary"):
        with st.spinner("AI is analyzing your data..."):
            # Generate EDA code
            eda_code, exec_result = analyzer.generate_eda()
            st.code(eda_code, language="python")
            
            # Generate insights
            insights = analyzer.generate_insights(f"EDA complete: {exec_result}")
            st.markdown("### 📊 Key Insights & Recommendations")
            st.markdown(insights)
            
            # Download report
            report = f"# Data Analysis Report\n\n{insights}"
            st.download_button("📥 Download Report", report, "data_analysis_report.md")
