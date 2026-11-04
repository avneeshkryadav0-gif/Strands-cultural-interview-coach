import streamlit as st
import time

st.set_page_config(page_title="Demo Mode", page_icon="🎬", layout="wide")

st.title("🎬 Demo Mode - Pre-recorded Conversation")
st.info("This is a scripted demo conversation for your hackathon video. Click 'Next' to advance through the conversation.")

# Scripted conversation
demo_script = [
    {
        "role": "assistant",
        "content": "Hello! I'm your interview coach. Let's practice a behavioral question. Tell me about a time you faced a difficult challenge at work or school and how you overcame it."
    },
    {
        "role": "user",
        "content": "Yes, we had a project deadline. We worked very hard and my team fixed the bug. It was good."
    },
    {
        "role": "assistant",
        "content": """
**🔍 STAR Evaluation:**
- ✅ Situation: Project deadline mentioned
- ⚠️ Task: Unclear what YOUR specific role was
- ⚠️ Action: "We worked hard" is too vague
- ❌ Result: "It was good" is not measurable

**🌍 Cultural Translation (Hindi):**
आपने अच्छा किया, लेकिन अमेरिकी इंटरव्यू में 'We' की जगह 'I' का उपयोग करें। व्यक्तिगत योगदान स्पष्ट करें।

**💡 Pro Tip:**
Instead of "We fixed the bug", say: "I identified the root cause in the database query and implemented a fix that reduced load time by 40%."

**🎯 Confidence Boost:**
Your technical understanding is clear! Just focus on stating your individual contribution with specific metrics.
"""
    },
    {
        "role": "user",
        "content": "I was working on a web application. I found a bug in the database query. I fixed it and reduced load time by 40%. The team was happy."
    },
    {
        "role": "assistant",
        "content": """
**🔍 STAR Evaluation:**
- ✅ Situation: Web application project
- ✅ Task: Found bug in database query
- ✅ Action: Fixed the bug
- ✅ Result: Reduced load time by 40%

**STAR Status: COMPLETE** ✨

**🌍 Cultural Translation (Hindi):**
बहुत बढ़िया! अब आपका जवाब अमेरिकी इंटरव्यू के लिए perfect है। आपने 'I' का उपयोग किया और specific result बताया।

**💡 Pro Tip:**
Perfect! You used "I" to show individual contribution and included a measurable result (40%). This is exactly what US interviewers want to hear.

**🎯 Confidence Boost:**
Excellent improvement! Your answer is now structured, specific, and culturally appropriate. You're ready for real interviews! 🌟
"""
    }
]

# Initialize demo state
if "demo_step" not in st.session_state:
    st.session_state.demo_step = 0

if "demo_messages" not in st.session_state:
    st.session_state.demo_messages = []

# Display current messages
for message in st.session_state.demo_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⏮️ Reset"):
        st.session_state.demo_step = 0
        st.session_state.demo_messages = []
        st.rerun()

with col2:
    if st.session_state.demo_step < len(demo_script):
        if st.button("▶️ Next Message", type="primary"):
            # Add next message
            next_msg = demo_script[st.session_state.demo_step]
            st.session_state.demo_messages.append(next_msg)
            st.session_state.demo_step += 1
            
            # Simulate typing delay
            if next_msg["role"] == "assistant":
                time.sleep(0.5)
            
            st.rerun()
    else:
        st.success("🎉 Demo complete! This is perfect for your hackathon video.")

with col3:
    st.caption(f"Step {st.session_state.demo_step}/{len(demo_script)}")

# Instructions
st.markdown("---")
st.markdown("""
### 📹 Recording Tips for Your Video:
1. **Start with the main page** - Show the mission and configuration
2. **Click through Demo Mode** - This shows the multi-agent system in action
3. **Highlight the STAR evaluation** - Show how it improves
4. **Show the cultural translation** - This is your unique selling point
5. **End with the confidence boost** - Show the social impact

**Total time: 2-3 minutes** (perfect for the hackathon requirement!)
""")