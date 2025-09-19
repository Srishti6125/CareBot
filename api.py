# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import carebot_reply  # <-- importing from chatbot.py

app = FastAPI(title="CareBot API", version="1.0")

# Input model
class ChatRequest(BaseModel):
    message: str

# Output model
class ChatResponse(BaseModel):
    reply: str
    emotion: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply, emotion = carebot_reply(request.message)
    return ChatResponse(reply=reply, emotion=emotion)

@app.get("/")
def root():
    return {"message": "CareBot API is running!"}
