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

    # Call generate_content with the new API (returns text directly)
    response_text = generate_content(messages)

    # Return the complete response as JSON.
    return {"response": response_text}
