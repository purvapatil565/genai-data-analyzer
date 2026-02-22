import pandas as pd
import openai
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def safe_exec(code):
    """Safely execute generated code"""
    try:
        exec_globals = {"pd": pd, "import pandas as pd", "import matplotlib.pyplot as plt", "import seaborn as sns"}
        exec(code, exec_globals)
        return "Code executed successfully"
    except Exception as e:
        return f"Error: {str(e)}"
