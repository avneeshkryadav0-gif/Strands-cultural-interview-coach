# 🌟 Strands Multi-Agent Cultural Interview Coach

## 🎯 The Problem
Millions of skilled immigrants and non-native speakers fail technical interviews not because they lack skills, but due to language barriers and unfamiliarity with Western interview norms (like the STAR method).

## 💡 The Solution
A multi-agent AI swarm built with the **Strands Agents SDK** and **Amazon Bedrock** that provides:
1. **Real-time STAR Method Coaching**: Evaluates answers for Situation, Task, Action, and Result.
2. **Cultural Context Translation**: Adapts feedback for specific target regions (e.g., advising when to use "I" vs "We").
3. **Native Language Support**: Builds confidence by explaining concepts in the user's first language.

## 🏗️ Technical Architecture
- **Orchestrator Agent**: Manages the conversation flow and delegates tasks.
- **STAR Evaluator Tool**: A specialized agent that analyzes answer structure.
- **Cultural Translator Tool**: A specialized agent that translates and adds regional interview advice.
- **Frontend**: Streamlit for a responsive, accessible web interface.

## 🚀 How to Run Locally
1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Mac/Linux) or `.\venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your AWS credentials: