import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize the client with API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_content(messages):
    # Format messages into a single prompt or conversation format
    text_messages = [f"{m['role']}: {m['content']}" for m in messages]
    prompt = "\n".join(text_messages)

    # Use the new API to generate content
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text
