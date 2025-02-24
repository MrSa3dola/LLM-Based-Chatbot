from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from gemini import generate_content

app = FastAPI()


# Pydantic models to validate incoming requests and outgoing responses.
class Message(BaseModel):
    role: str
    content: str


class QueryRequest(BaseModel):
    messages: List[Message]


class QueryResponse(BaseModel):
    response: str


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    # Convert Pydantic objects into simple dicts.
    messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]

    # Initialize an empty response string.
    full_response = ""

    # Call generate_content (which streams responses)
    # Note: If generate_content is blocking, consider offloading this work with FastAPI's run_in_threadpool.
    for chunk in generate_content(messages):
        if chunk.text:
            full_response += chunk.text

    # Return the complete response as JSON.
    return {"response": full_response}
