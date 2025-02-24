import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generate_content(messages):
    model = genai.GenerativeModel("gemini-1.5-flash")

    text_messages = [f"{m['role']}: {m['content']}" for m in messages]

    response = model.generate_content(text_messages, stream=True)

    return response
