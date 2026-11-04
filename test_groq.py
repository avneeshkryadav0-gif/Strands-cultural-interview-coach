import os
from strands import Agent
from strands.models import OpenAIModel

print("=== GROQ CONNECTION TEST ===")

# PASTE YOUR NEW KEY EXACTLY HERE. NO SPACES!
MY_GROQ_KEY = "gsk_paste_your_exact_new_key_here" 
MY_BASE_URL = "https://api.groq.com/openai/v1"

print("1. Connecting to Groq via OpenAI Model...")
try:
    os.environ["OPENAI_API_KEY"] = MY_GROQ_KEY
    os.environ["OPENAI_BASE_URL"] = MY_BASE_URL
    
    model = OpenAIModel(
        model_id="llama-3.3-70b-versatile"
    )
    
    agent = Agent(model=model)
    print("2. Sending test message...")
    response = agent("Say 'Groq is connected and working perfectly!'")
    print(f"\n✅ AI RESPONSE: {response}")
    
except Exception as e:
    print(f"\n❌ FAILED: {e}")