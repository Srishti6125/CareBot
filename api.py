# api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import carebot_reply  # <-- importing from chatbot.py

app = FastAPI(title="CareBot API", version="1.0")

# ------------------ CORS Setup ------------------
origins = [
    "http://localhost:3000",       # React dev server
    "http://127.0.0.1:3000",
    "https://carebot-fe1t.onrender.com",  # backend itself
    # Add your deployed frontend URL here, e.g.:
    # "https://your-frontend.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow everything (safe for dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -------------------------------------------------

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
