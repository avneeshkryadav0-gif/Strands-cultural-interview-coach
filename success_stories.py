import streamlit as st

st.set_page_config(page_title="Success Stories", page_icon="🌟", layout="wide")

st.title("🌟 Success Stories")
st.markdown("### Real impact, real people")

st.markdown("""
<div style='background-color: #f0f2f6; padding: 2rem; border-radius: 10px; margin: 1rem 0;'>
<h3>💡 Why This Matters</h3>
<p>Every year, millions of skilled professionals face barriers not because of their technical abilities, 
but because of language and cultural differences. Our mission is to break down these barriers.</p>
</div>
""", unsafe_allow_html=True)

# Success Stories
stories = [
    {
        "name": "Priya S.",
        "location": "India → Canada",
        "role": "Software Engineer",
        "story": "After moving to Canada, I struggled with interviews despite having 5 years of experience. The cultural coach helped me understand that Canadian interviews value individual achievement. I learned to say 'I led' instead of 'We completed'. Within 3 months, I landed my dream job at a top tech company!",
        "improvement": "+45% confidence score"
    },
    {
        "name": "Carlos M.",
        "location": "Mexico → United States",
        "role": "Data Analyst",
        "story": "English is not my first language, and I was nervous about behavioral questions. The STAR method coach helped me structure my answers perfectly. The cultural tips showed me how to emphasize quantifiable results. I went from 0 job offers to 3 offers in 2 months!",
        "improvement": "STAR score: 50% → 92%"
    },
    {
        "name": "Fatima A.",
        "location": "Syria → Germany",
        "role": "Product Manager",
        "story": "As a refugee, I faced huge challenges explaining my experience in a new language and culture. This tool gave me feedback in Arabic, which helped me understand the concepts. Then it showed me how to adapt for German interview culture. I finally got a job that matches my skills!",
        "improvement": "3 job offers received"
    }
]

for i, story in enumerate(stories):
    with st.expander(f"🌟 {story['name']} - {story['role']} ({story['location']})", expanded=(i==0)):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{story['story']}**")
        with col2:
            st.metric("Result", story['improvement'])

st.markdown("---")

# Impact Statistics
st.subheader("📊 Our Impact")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Users Helped", "500+", "+120 this month")
with col2:
    st.metric("Jobs Landed", "150+", "+35 this month")
with col3:
    st.metric("Avg Confidence Boost", "+38%", "+5% vs last month")
with col4:
    st.metric("Countries Reached", "45+", "Global impact")

st.markdown("---")

# Call to Action
st.success("""
### 🎯 Join Our Mission
Every practice session brings someone closer to their dream job. 
Whether you're an immigrant, refugee, or non-native speaker, 
we're here to help you succeed.

**Start your journey today in the Interview Practice tab!**
""")

# Footer
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.9rem; margin-top: 2rem;'>
Built with ❤️ for the AWS Strands SDK Hackathon 2026<br>
Helping underserved populations succeed in the global job market
</div>
""", unsafe_allow_html=True)