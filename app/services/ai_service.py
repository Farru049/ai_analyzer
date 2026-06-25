from click import prompt
from groq import Groq
from app.config import settings
import json

client = Groq(api_key = settings.GROQ_API_KEY)

def analyze_jd(job_description:str):
    prompt = f"""Analyze the job description and extract:
1. Required Skills (list out them)
2.Experience level (junior/mid/senior)
3.Key Responsibilities (bullet points)
4.Salary range if mentioned
Job Description:
{job_description}
Return as JSON format"""

    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {"role": "user", "content": prompt}
        ],
        max_tokens = 500
    )
    return response.choices[0].message.content