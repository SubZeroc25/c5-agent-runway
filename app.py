import os
import ccxt
import openai
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from pydantic import BaseModel

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
gate_api_key = os.getenv("GATE_API_KEY")
gate_api_secret = os.getenv("GATE_API_SECRET")

exchange = ccxt.gateio({
    'apiKey': gate_api_key,
    'secret': gate_api_secret,
})

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask_agent")
def ask_agent_endpoint(req: PromptRequest):
    prompt = req.prompt
    if "trade" in prompt.lower():
        return { 'response': trade() }
    return { 'response': "No action taken." }

def trade():
    try:
        balance = exchange.fetch_balance()
        usdt = balance.get('USDT', {}).get('free', 0)
        if usdt and usdt > 10:
            order = exchange.create_market_buy_order('BTC/USDT', 0.001)
            return f"✅ Bought BTC with {usdt} USDT."
        return f"⚠️ Not enough USDT to trade. Current balance: {usdt}"
    except Exception as e:
        return f"❌ Trade error: {str(e)}"

@app.get("/")
def root():
    return {"message": "C5 Agent API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
