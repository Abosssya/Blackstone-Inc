import streamlit as st
from datetime import datetime
import pandas as pd

# 1. IMPORT YOUR MODULES
from auth import login
from crud import show_crud
from landing import show_landing

# 2. PAGE CONFIGURATION (Must be the very first Streamlit command)
st.set_page_config(page_title="Blackstone Beacon ERP", page_icon="🛡️", layout="wide")

# 3. CUSTOM CSS BRANDING
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { background-color: #002D62; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 4. AUTHENTICATION (The Gatekeeper)
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login()
    st.stop() # Stops the rest of the app from loading until login is successful

# 5. SIDEBAR BRANDING & NAVIGATION
st.sidebar.image("https://findvectorlogo.com/blackstone-products-vector-logo-svg/", width=200)

# Single Navigation Menu
menu = st.sidebar.selectbox("Module Selection", 
    ["Home", "Valuation Entry & Record Gen", "Portfolio Manager", "Pipeline Dashboard"])

# Logout Button
if st.sidebar.button("Logout"):
    st.session_state.authenticated = False
    st.rerun()

# 6. PAGE ROUTING LOGIC (This is where you place the Home logic)
# ------------------------------------------------------------------

if menu == "Home":
    # --- COMPONENT 3: Fully Functional Landing Page ---
    show_landing()

elif menu == "Valuation Entry & Record Gen":
    st.header("Module: Strategic Deal Entry")
    st.caption(f"Authenticated as: {st.session_state.get('user_role', 'Ayden Shaw')} | Location: New York Office")

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
    net_debt = 3200000000.0 
    equity_value = enterprise_value - net_debt

    st.divider()

    if st.button("Finalize Valuation & Generate IC Memo"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tx_id = f"BST-2026-{ticker}-001"
        st.success("✅ Deal Committed to Global Database.")
        
        st.markdown("### 📄 AUTOMATED DEAL SUMMARY (IC MEMO)")
        st.info(f"**Transaction ID:** {tx_id} | **Generated On:** {timestamp}")
        
        memo_col1, memo_col2 = st.columns(2)
        with memo_col1:
            st.write(f"**Target Asset:** {ticker}")
            st.write(f"**Lead Analyst:** {st.session_state.get('user_role', 'Ayden Shaw')}")
            st.write(f"**Valuation Method:** Standardized LBO/Exit Multiple")
        with memo_col2:
            st.write(f"**Implied Enterprise Value:** ${enterprise_value:,.2f}")
            st.write(f"**Implied Equity Value:** ${equity_value:,.2f}")
            st.write(f"**Tax Status:** Jurisdictional Compliance Verified")
            
        st.write("---")
        st.warning("**Workflow Automation:** This record has been routed to Mason Mount for signature.")

elif menu == "Portfolio Manager":
    # --- COMPONENT 2: Basic CRUD Module ---
    show_crud()

elif menu == "Pipeline Dashboard":
    st.header("Executive Dashboard")
    st.caption("Authenticated as: Mason Mount | Location: London Office")
    
    df = pd.DataFrame({
        "Deal Name": ["Hilton (HLT)", "Cheniere (CQP)"],
        "Status": ["Awaiting Signature", "Active Portfolio"],
        "Value ($B)": [27.36, 64.20],
        "Lead": ["Ayden Shaw", "Mason Mount"]
    })
    st.table(df)
