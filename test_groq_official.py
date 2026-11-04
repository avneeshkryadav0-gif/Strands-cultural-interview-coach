from groq import Groq
import os

print("=== TESTING WITH OFFICIAL GROQ CLIENT ===")

# Get your key from Groq console one more time
MY_GROQ_KEY = "PASTE_YOUR_GROQ_KEY_HERE"

try:
    client = Groq(api_key=MY_GROQ_KEY)
    
    print("1. Sending request to Groq...")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say 'Groq official client is working!'",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    
    print(f"\n✅ SUCCESS: {chat_completion.choices[0].message.content}")
    
except Exception as e:
    print(f"\n❌ FAILED: {e}")
    print("\n Troubleshooting:")
    print("1. Make sure you copied the ENTIRE key (starts with gsk_)")
    print("2. Make sure there are NO spaces before or after the key")
    print("3. Try generating a completely new key at console.groq.com/keys")