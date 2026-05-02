import streamlit as st

# Dashboard ki premium settings
st.set_page_config(page_title="Ledger Pro", layout="centered")

# Custom CSS for CRED Dark Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1f2937; padding: 20px; border-radius: 15px; border-left: 5px solid #00ff41; }
    div[data-testid="stMetricValue"] { color: #00ff41; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.title("💰 Ledger Pro")
st.write("Welcome, Palak Rathi. Your financial intelligence is ready.")

# Current Balance (Placeholder based on your March data)
st.metric(label="Total Balance (March 2026)", value="₹1,937.10")

# The Magic Input Area
st.subheader("Update Your Ledger")
user_input = st.text_area("Paste bank statement text here...", height=150, placeholder="Copy text from your bank and paste here. No manual entry needed.")

if st.button("Process & Update"):
    if user_input:
        st.success("Data received! Connecting to Gemini Brain...")
    else:
        st.warning("Pehle kuch paste toh kar lo bhai!")
