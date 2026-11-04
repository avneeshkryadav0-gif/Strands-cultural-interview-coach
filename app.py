import os
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models import BedrockModel

# Load environment variables from .env
load_dotenv()

# Initialize the Amazon Bedrock Model (Claude 3.5 Sonnet)
model = BedrockModel(
    model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1")
)

# ==========================================
# SPECIALIST AGENT 1: The STAR Evaluator
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
# SPECIALIST AGENT 2: The Cultural Translator
# ==========================================
@tool
def translate_and_add_cultural_context(user_answer: str, target_language: str) -> str:
    """Translates the answer and provides cultural interview advice for the target region."""
    translator = Agent(
        name="cultural_translator",
        system_prompt="You are a cultural communication expert. Translate the core message of the user's answer into the target language. Then, add ONE specific piece of cultural advice for interviewing in a Western/US market (e.g., 'In the US, emphasize individual action with I instead of We to show leadership').",
        model=model
    )
    response = translator(f"Answer to process: {user_answer}\nTarget Language: {target_language}")
    return str(response)

# ==========================================
# ORCHESTRATOR AGENT: The Main Coach
# ==========================================
orchestrator = Agent(
    name="interview_coach_orchestrator",
    system_prompt="You are a supportive mock interview coach helping underserved populations (like non-native speakers) prepare for jobs. Ask ONE behavioral interview question at a time. Use the 'evaluate_star_method' tool to check their answer. If it's not STAR_COMPLETE, ask the follow-up question provided by the tool. If it is STAR_COMPLETE, use the 'translate_and_add_cultural_context' tool to give them the final translated feedback and cultural advice. Be encouraging!",
    model=model,
    tools=[evaluate_star_method, translate_and_add_cultural_context]
)

# ==========================================
# MAIN EXECUTION LOOP
# ==========================================
def main():
    print("=== 🌟 Strands Multi-Agent Cultural Interview Coach ===")
    print("Helping underserved populations break language and cultural barriers.\n")
    
    target_language = input("1. Enter your target language for feedback (e.g., Spanish, Hindi, Arabic): ")
    job_role = input("2. Enter your target job role (e.g., Software Engineer, Data Analyst): ")
    
    print(f"\n🤖 Coach: Hello! I am your interview coach for a {job_role} role.")
    print("🤖 Coach: Let's practice. Tell me about a time you faced a difficult challenge at work or school and how you overcame it.\n")
    
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("🤖 Coach: Great job practicing today! Good luck with your interviews!")
            break
            
        print("\n⏳ [Multi-Agent Swarm is collaborating and evaluating...]")
        
        # Pass the user input and target language to the orchestrator
        prompt = f"User answered: '{user_input}'. Target language: {target_language}. Process this answer using your tools and respond to the user."
        response = orchestrator(prompt)
        
        print(f"\n🤖 Coach: {response}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()