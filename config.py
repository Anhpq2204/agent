import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Warning: GEMINI_API_KEY not found in environment variables. Please set it in .env before running.")
    sys.exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3.1-flash-lite")
