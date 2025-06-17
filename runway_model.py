import runway
import os
import ccxt
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
gate_api_key = os.getenv("GATE_API_KEY")
gate_api_secret = os.getenv("GATE_API_SECRET")

exchange = ccxt.gateio({
    'apiKey': gate_api_key,
    'secret': gate_api_secret,
})

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

@runway.command('ask_agent', inputs={ 'prompt': runway.text }, outputs={ 'response': runway.text })
def ask_agent(model, inputs):
    prompt = inputs['prompt']
    if "trade" in prompt.lower():
        return { 'response': trade() }
    return { 'response': "No action taken." }

if __name__ == '__main__':
    runway.run()
