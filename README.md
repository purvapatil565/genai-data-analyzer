# genai-data-analyzer
# 🚀 GenAI Data Analysis Automation

**Upload CSV → AI generates EDA code, insights & reports automatically**

## ✨ **Demo**
Streamlit app running at: http://localhost:8501
Tested with Superstore Sales dataset (9,995 rows)

## 🎯 **Features**
- **CSV Upload** → Instant data preview + metrics
- **AI-Powered EDA** → Auto-generates Pandas/Seaborn analysis code  
- **Business Insights** → GPT extracts actionable recommendations
- **Production Ready** → Error handling, loading states, deployable

## 🛠 **Tech Stack**
Frontend: Streamlit
AI: OpenAI GPT-4o-mini + LangChain
Data: Pandas, Plotly, Seaborn
Deployment: GitHub Codespaces → Hugging Face Spaces


## 🚀 **Quick Start**
```bash
# Clone & run
git clone https://github.com/YOUR_USERNAME/genai-data-analyzer.git
cd genai_data_analyzer
pip install -r requirements.txt
streamlit run app.py
