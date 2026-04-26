import streamlit as st
from datetime import datetime
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Blackstone Beacon ERP", page_icon="🛡️", layout="wide")

# Custom CSS for Blackstone Branding
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { background-color: #002D62; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Blackstone Beacon: Investment Management System")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Blackstone_logo.svg/1200px-Blackstone_logo.svg.png", width=200)

# Sidebar Navigation
menu = st.sidebar.selectbox("Module Selection", ["Valuation Entry & Record Gen", "Pipeline Dashboard"])

if menu == "Valuation Entry & Record Gen":
    st.header("Module: Strategic Deal Entry")
    st.caption("Authenticated as: Ayden Shaw | Location: New York Office")

    with st.container():
        st.subheader("Target Asset Details")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            ticker = st.selectbox("Select Target Ticker", ["HLT", "CQP", "NEW_TARGET"])
            if ticker == "NEW_TARGET":
                ticker = st.text_input("Enter New Ticker")
        with col2:
            ebitda = st.number_input("Projected 2026 EBITDA ($)", value=2880000000.0, step=1000000.0)
        with col3:
            multiple = st.slider("Exit Multiple (EV/EBITDA)", 5.0, 20.0, 9.5)

    # ERP Logic Calculations
    enterprise_value = ebitda * multiple
    net_debt = 3200000000.0 # Standardized debt for this demo
    equity_value = enterprise_value - net_debt

    st.divider()

    # The Automation Trigger
    if st.button("Finalize Valuation & Generate IC Memo"):
        # 1. Simulate Database Commitment
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tx_id = f"BST-2026-{ticker}-001"
        
        st.success("✅ Deal Committed to Global Database.")
        
        # 2. THE AUTOMATED RECORD GENERATION (The "Invoice" logic)
        st.markdown("### 📄 AUTOMATED DEAL SUMMARY (IC MEMO)")
        st.info(f"**Transaction ID:** {tx_id} | **Generated On:** {timestamp}")
        
        memo_col1, memo_col2 = st.columns(2)
        with memo_col1:
            st.write(f"**Target Asset:** {ticker}")
            st.write(f"**Lead Analyst:** Ayden Shaw")
            st.write(f"**Valuation Method:** Standardized LBO/Exit Multiple")
        with memo_col2:
            st.write(f"**Implied Enterprise Value:** ${enterprise_value:,.2f}")
            st.write(f"**Implied Equity Value:** ${equity_value:,.2f}")
            st.write(f"**Tax Status:** Jurisdictional Compliance Verified")
            
        st.write("---")
        st.warning(f"**Workflow Automation:** This record has been routed to **Mason Mount (Managing Director)** for final commitment signature.")

elif menu == "Pipeline Dashboard":
    st.header("Executive Dashboard")
    st.caption("Authenticated as: Mason Mount | Location: London Office")
    
    # Simple table to show data flow
    df = pd.DataFrame({
        "Deal Name": ["Hilton (HLT)", "Cheniere (CQP)"],
        "Status": ["Awaiting Signature", "Active Portfolio"],
        "Value ($B)": [27.36, 64.20],
        "Lead": ["Ayden Shaw", "Mason Mount"]
    })
    st.table(df)

