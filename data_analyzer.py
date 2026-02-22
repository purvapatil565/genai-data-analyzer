import pandas as pd
from prompts import EDA_PROMPT, INSIGHTS_PROMPT
from utils import llm, safe_exec

class DataAnalyzer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.file_path = file_path
    
    def get_dataset_info(self):
        info = f"""
        Shape: {self.df.shape}
        Columns: {list(self.df.columns)}
        Sample data:
        {self.df.head(3).to_dict()}
        """
        return info
    
    def generate_eda(self):
        info = self.get_dataset_info()
        prompt = EDA_PROMPT.format(description=info)
        
        response = llm.invoke(prompt)
        code = response.content.strip("```python").strip("```").strip()
        
        result = safe_exec(code)
        return code, result
    
    def generate_insights(self, eda_results):
        prompt = INSIGHTS_PROMPT.format(eda_results=eda_results)
        response = llm.invoke(prompt)
        return response.content
