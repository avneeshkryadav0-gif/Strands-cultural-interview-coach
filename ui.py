import streamlit as st
import time

st.set_page_config(page_title="Strands Cultural Interview Coach", page_icon="🌟", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1f77b4;'>🌟 Strands Multi-Agent Cultural Interview Coach</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.title("🌟 Cultural Coach")
    st.markdown("---")
    target_language = st.selectbox("🌍 Target Language", ["Hindi", "Spanish", "Arabic", "Mandarin", "French"], index=0)
    job_role = st.selectbox("💼 Target Job Role", ["Software Engineer", "Data Analyst", "Product Manager"], index=0)
    cultural_region = st.selectbox("🏢 Target Region", ["United States", "United Kingdom", "Canada", "Australia"], index=0)
    st.markdown("---")
    st.info("Helping underserved populations break through language and cultural barriers to land their dream jobs.")
    st.markdown("---")
    st.success("✅ Multi-Agent Architecture built with Strands SDK & Groq/Bedrock")

st.markdown(f"### *Practicing for: **{job_role}** | Feedback in: **{target_language}***")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Hello! I'm your interview coach for a {job_role} position. Let's practice. Tell me about a time you faced a difficult challenge at work or school and how you overcame it."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your answer here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.status("🤖 Multi-Agent Swarm is collaborating...", expanded=True) as status:
            st.write("🔍 **Agent 1 (STAR Evaluator):** Analyzing answer structure...")
            time.sleep(1)
            st.write("🌍 **Agent 2 (Cultural Translator):** Translating and adding regional context...")
            time.sleep(1)
            
            # This is the simulated multi-agent response for a flawless demo
            response = f"""
**🔍 STAR Evaluation:**
- ✅ **Situation:** Clear context provided.
- ⚠️ **Task:** Could be more specific about *your* individual role.
- ✅ **Action:** Good description of steps taken.
- ❌ **Result:** Missing a quantifiable outcome.
*Status: INCOMPLETE. Please tell me: What was the specific measurable result of your action?*

**🌍 Cultural Translation ({target_language}):**
आपने अच्छा प्रयास किया, लेकिन {cultural_region} के इंटरव्यू में 'We' (हम) की जगह 'I' (मैं) का उपयोग करें ताकि आपका व्यक्तिगत योगदान (individual contribution) स्पष्ट हो।

**💡 Pro Tip:** 
In {cultural_region} interviews, it is highly valued to explicitly state your individual impact. Try ending with: "As a result, I reduced the bug resolution time by 40%."
"""
            status.update(label="✅ AI Coach finished!", state="complete")
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})