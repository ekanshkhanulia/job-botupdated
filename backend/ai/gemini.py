import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(prompt: str) -> str:
    """Base function to call Gemini and return raw text response"""
    response = model.generate_content(prompt)
    return response.text

def ask_gemini_json(prompt: str) -> dict:
    """Call Gemini and return parsed JSON response"""
    full_prompt = prompt + "\n\nRespond ONLY with valid JSON. No explanation, no markdown, no code blocks. Just the raw JSON object."
    response = model.generate_content(full_prompt)
    
    # Clean response in case Gemini adds markdown anyway
    raw = response.text.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    
    return json.loads(raw)