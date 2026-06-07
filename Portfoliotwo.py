import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tumelo Rakabe | Portfolio", page_icon="🚀", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #00d4ff !important; }
    .skill-tag {
        background-color: #1e2130;
        border: 1px solid #00d4ff;
        border-radius: 15px;
        padding: 5px 15px;
        margin: 5px;
        display: inline-block;
        font-size: 0.8rem;
    }
    .cert-card {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #00d4ff;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Tumelo J. Rakabe")
    st.write("📍 Pretoria, South Africa")
    st.write("📧 Tumelorakabe55@gmail.com")
    st.write("📞 +27 69 384 8379")
    st.divider()
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/tumelo-rakabe)")
    st.markdown("[💻 GitHub](https://github.com/578025tumi)")
    st.divider()
    st.success("Specializing in GenAI & Data Ops")

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Software Developer & AI/Data Engineer")
    st.subheader("Automating Business Intelligence with Generative AI & Data Pipelines")
    st.write("""
    I build 'Intelligence Engines.' With a deep background in **Generative AI (LLMs)**, **Data Engineering**, and **Predictive Analytics**, 
    I help businesses stop 'leaking' capital and start making data-driven decisions.
    """)

st.divider()

# --- TABS ---
tab_projects, tab_certs, tab_skills, tab_contact = st.tabs(["📂 Projects", "📜 Certifications", "🛠 Tech Stack", "✉️ Contact Me"])

# --- PROJECTS TAB ---
with tab_projects:
    st.header("High-Impact Solutions")
    
    # Project 1: ApexMine
    with st.expander("🛠 ApexMine Command Center", expanded=True):
        c1, c2 = st.columns([1, 2])
        c1.metric("Asset Recovery", "$185k/yr")
        c2.write("**Mining Asset Preservation:** GPS 'Stop-Verification' engine preventing copper shrinkage via real-time WhatsApp webhooks.")

    # Project 2: ESG Tracker
    with st.expander("🤖 AI-Driven ESG Tracker"):
        st.write("**Distributed AI Auditing:** Using FastAPI, Redis, and GPT-4o to audit global news for corporate ethics violations.")

# --- CERTIFICATIONS TAB ---
with tab_certs:
    st.header("Professional Certifications")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("🤖 AI & Generative AI")
        ai_certs = ["Generative AI with LLMs", "Intro to Generative AI", "Generative AI Assistance", "AI Essentials", "AI on Microsoft Azure", "Python for Data Science, AI & Development"]
        for cert in ai_certs:
            st.markdown(f'<div class="cert-card">{cert}</div>', unsafe_allow_html=True)

    with c2:
        st.subheader("📊 Data Engineering & Analytics")
        data_certs = ["Intro to Data Engineering", "Engineering and Management", "Acquisition and Preparation", "Predictive Analysis and Forecasting", "Data Transformation and Manipulation", "Analytics and Exploration"]
        for cert in data_certs:
            st.markdown(f'<div class="cert-card">{cert}</div>', unsafe_allow_html=True)

# --- SKILLS TAB ---
with tab_skills:
    st.header("Technical Stack")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Data Ops**")
        for s in ["FastAPI", "PostgreSQL", "Redis", "Data Pipelines"]: st.markdown(f'<div class="skill-tag">{s}</div>', unsafe_allow_html=True)
    with col2:
        st.write("**AI/ML**")
        for s in ["GPT-4o", "LLM Integration", "Predictive Modeling", "Azure AI"]: st.markdown(f'<div class="skill-tag">{s}</div>', unsafe_allow_html=True)
    with col3:
        st.write("**Languages**")
        for s in ["Python", "TypeScript", "SQL"]: st.markdown(f'<div class="skill-tag">{s}</div>', unsafe_allow_html=True)

# --- CONTACT TAB ---
with tab_contact:
    st.header("Get In Touch")
    st.write("Have a project in mind? Let's discuss how I can help your business.")

    # CONTACT FORM USING FORMSUBMIT (FREE)
    contact_form = f"""
    <form action="https://formsubmit.co/Tumelorakabe55@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #00d4ff; background: #161b22; color: white;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #00d4ff; background: #161b22; color: white;">
        <textarea name="message" placeholder="Your message here" style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #00d4ff; background: #161b22; color: white; height: 150px;"></textarea>
        <button type="submit" style="background-color: #00d4ff; color: black; padding: 10px 25px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
st.caption("© 2024 Tumelo Rakabe | Built with Streamlit")