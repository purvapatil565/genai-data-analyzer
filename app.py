import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

st.title("🚀 GenAI Data Analyzer")
st.markdown("Upload CSV → AI Analysis in 1 click")

# File upload
uploaded_file = st.file_uploader("Choose CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data loaded:", df.shape)
    st.dataframe(df.head())
    
    if st.button("🔍 Analyze Data"):
        st.write("✅ **Analysis Complete!**")
        st.write("**Key Metrics:**")
        st.write(f"- Rows: {len(df)}")
        st.write(f"- Columns: {len(df.columns)}")
        st.write(f"- Missing values: {df.isnull().sum().sum()}")
