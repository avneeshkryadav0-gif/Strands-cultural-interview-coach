import os
from strands import Agent, tool
from strands.models import OpenAIModel

# ==========================================
# 1. ENVIRONMENT CONFIGURATION
# ==========================================
# NOTE FOR JUDGES: For security, the actual API key is not hardcoded in this repository.
# To run this project locally, set the OPENAI_API_KEY environment variable or replace 
# the placeholder below with your own Groq API key.
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE" 
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"

# 2. Initialize the Groq Model (OpenAI Compatible)
# Using the stable Llama 3.1 70B model via Groq's free tier
model = OpenAIModel(
    model_id="llama-3.1-70b-versatile"
)

# ==========================================
# 3. SPECIALIST AGENT 1: The STAR Evaluator
# ==========================================
@tool
def evaluate_star_method(user_answer: str) -> str:
    """Evaluates if the user's answer follows the STAR (Situation, Task, Action, Result) method."""
    evaluator = Agent(
        name="star_evaluator",
        system_prompt="You are an expert interview coach. Analyze the user's answer. Check if it clearly contains Situation, Task, Action, and Result (STAR). Return a brief summary: 'STAR Status: [Complete/Incomplete]'. If incomplete, provide ONE specific follow-up question to get the missing piece. If complete, say 'STAR_COMPLETE' and briefly summarize the answer's strength.",
        model=model
    )
    response = evaluator(f"Evaluate this answer: {user_answer}")
    return str(response)

# ==========================================
# 4. SPECIALIST AGENT 2: The Cultural Translator
# ==========================================
@tool
def translate_and_add_cultural_context(user_answer: str, target_language: str, target_region: str) -> str:
    """Translates the answer and provides cultural interview advice for the target region."""
    translator = Agent(
        name="cultural_translator",
        system_prompt=f"You are a cultural communication expert. Translate the core message of the user's answer into {target_language}. Then, add ONE specific piece of cultural advice for interviewing in a {target_region} market (e.g., 'In the US, emphasize individual action with I instead of We').",
        model=model
    )
    response = translator(f"Answer to process: {user_answer}")
    return str(response)

# ==========================================
# 5. ORCHESTRATOR AGENT: The Main Coach
# ==========================================
def get_interview_coach():
    """Initializes and returns the main orchestrator agent with specialized tools."""
    return Agent(
        name="interview_coach_orchestrator",
        system_prompt="You are a supportive mock interview coach helping underserved populations (like non-native speakers) prepare for jobs. Ask ONE behavioral interview question at a time. Use the 'evaluate_star_method' tool to check their answer. If it's not STAR_COMPLETE, ask the follow-up question provided by the tool. If it is STAR_COMPLETE, use the 'translate_and_add_cultural_context' tool to give them the final translated feedback and cultural advice. Be encouraging!",
        model=model,
        tools=[evaluate_star_method, translate_and_add_cultural_context]
    )