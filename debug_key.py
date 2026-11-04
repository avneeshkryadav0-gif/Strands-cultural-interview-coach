from groq import Groq

MY_GROQ_KEY = "YOUR_API_KEY_HERE" 

print("=== TESTING CORRECT MODEL NAME ===")
try:
    client = Groq(api_key=MY_GROQ_KEY)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Say 'Groq is finally working!'"}],
        model="llama-3.1-70b-versatile" # <-- THIS IS THE FIX
    )
    print(f"\n✅ SUCCESS: {response.choices[0].message.content}")
except Exception as e:
    print(f"\n❌ FAILED: {e}")