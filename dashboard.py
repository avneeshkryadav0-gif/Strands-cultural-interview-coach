import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Progress Dashboard", page_icon="📊", layout="wide")

st.title("📊 Your Interview Progress Dashboard")
st.markdown("### Track your improvement over time")

# Mock data for demonstration
# In real implementation, this would come from session history
if "session_history" not in st.session_state:
    st.session_state.session_history = []

# Add some mock historical data
if len(st.session_state.session_history) == 0:
    mock_data = [
        {"date": "2026-11-01", "question": "Tell me about a challenge", "star_score": 50, "confidence": 60},
        {"date": "2026-11-02", "question": "Describe a team project", "star_score": 65, "confidence": 68},
        {"date": "2026-11-03", "question": "How do you handle pressure", "star_score": 75, "confidence": 75},
        {"date": "2026-11-04", "question": "Tell me about a failure", "star_score": 85, "confidence": 82},
    ]
    st.session_state.session_history = mock_data

# Metrics Overview
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_sessions = len(st.session_state.session_history)
    st.metric("Total Sessions", total_sessions)
with col2:
    avg_star = sum([s["star_score"] for s in st.session_state.session_history]) / max(total_sessions, 1)
    st.metric("Avg STAR Score", f"{avg_star:.0f}%")
with col3:
    avg_confidence = sum([s["confidence"] for s in st.session_state.session_history]) / max(total_sessions, 1)
    st.metric("Avg Confidence", f"{avg_confidence:.0f}%")
with col4:
    improvement = avg_star - (st.session_state.session_history[0]["star_score"] if total_sessions > 0 else 0)
    st.metric("Improvement", f"+{improvement:.0f}%", delta=f"+{improvement:.0f}%")

st.markdown("---")

# Progress Charts
tab1, tab2, tab3 = st.tabs(["📈 STAR Method Progress", "💪 Confidence Growth", "📋 Session History"])

with tab1:
    st.subheader("STAR Method Score Over Time")
    
    if total_sessions > 0:
        chart_data = pd.DataFrame({
            "Session": range(1, total_sessions + 1),
            "STAR Score": [s["star_score"] for s in st.session_state.session_history]
        })
        st.line_chart(chart_data.set_index("Session"))
        
        # Breakdown
        st.markdown("#### STAR Component Breakdown")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Situation", "92%", delta="+12%")
        with col2:
            st.metric("Task", "88%", delta="+8%")
        with col3:
            st.metric("Action", "85%", delta="+15%")
        with col4:
            st.metric("Result", "78%", delta="+20%")

with tab2:
    st.subheader("Confidence Level Growth")
    
    if total_sessions > 0:
        chart_data = pd.DataFrame({
            "Session": range(1, total_sessions + 1),
            "Confidence": [s["confidence"] for s in st.session_state.session_history]
        })
        st.area_chart(chart_data.set_index("Session"))
        
        st.info("""
        **💡 What affects your confidence score?**
        - Clarity of your answers
        - Use of STAR method
        - Cultural adaptation
        - Language fluency
        """)

with tab3:
    st.subheader("Session History")
    
    if total_sessions > 0:
        for i, session in enumerate(st.session_state.session_history, 1):
            with st.expander(f"Session {i}: {session['date']} - STAR Score: {session['star_score']}%"):
                st.markdown(f"**Question:** {session['question']}")
                st.markdown(f"**STAR Score:** {session['star_score']}%")
                st.markdown(f"**Confidence:** {session['confidence']}%")
                st.markdown("**Feedback:** Great progress! Your answers are becoming more structured and culturally appropriate.")
    else:
        st.info("No sessions yet. Start practicing in the Interview tab!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.9rem;'>
Keep practicing! Every session brings you closer to your dream job. 🌟
</div>
""", unsafe_allow_html=True)