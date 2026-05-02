import streamlit as st
import google.generativeai as genai

# Brain Connection (Gemini Setup)
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
except:
    st.error("API Key ki settings mein kuch gadbad hai bhai!")

# Dashboard Look (CRED Theme)
st.set_page_config(page_title="Ledger Pro", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1f2937; padding: 20px; border-radius: 15px; border-left: 5px solid #00ff41; }
    div[data-testid="stMetricValue"] { color: #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("💰 Ledger Pro")
st.write("Welcome, Palak Rathi. Zero effort finance tracking starts here.")

# Balance Metric
st.metric(label="Current Balance (March 2026)", value="₹1,937.10")

# Input Section
st.subheader("Update Your Ledger")
user_input = st.text_area("Paste statement text here...", height=150)

if st.button("Process & Update"):
    if user_input:
        with st.spinner("Gemini is thinking..."):
            prompt = f"Analyze this bank statement text and provide a summary of total income, total expenses, and a clean table of transactions: {user_input}"
            response = model.generate_content(prompt)
            
            st.markdown("### 📊 Analysis Result")
            st.write(response.text)
            st.balloons()
    else:
        st.warning("Pehle text toh paste karo!")
