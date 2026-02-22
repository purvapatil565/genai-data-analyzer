EDA_PROMPT = """
You are an expert data analyst. Given this dataset description: {description}
Generate Python code to perform comprehensive EDA. Include:
1. Data summary (shape, types, missing values)
2. Key statistics by category
3. Correlation analysis
4. Top trends and insights
Return ONLY executable Python code using pandas, matplotlib, seaborn.
"""

INSIGHTS_PROMPT = """
Analyze these EDA results: {eda_results}
Extract 3-5 key business insights and recommendations.
Format as markdown with bullet points.
"""
