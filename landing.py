import streamlit as st

def show_landing():
    # 1. Professional Header & Branding
    st.title("🏢 Blackstone Beacon: Strategic ERP Portfolio")
    st.markdown("""
    **Transforming Global Private Equity Operations** The Beacon is an institutional-grade platform designed to centralize deal flow between the **New York** and **London** offices. 
    By standardizing LBO valuation logic, we eliminate "Excel Bias" and reporting silos.
    """)

    st.divider()

    # 2. Key Objectives (Professional Presentation)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("### ⚡ Efficiency")
        st.write("Reducing manual reporting for assets like **Hilton ($HLT$)** from 4 hours to 60 minutes.")
    with col2:
        st.write("### 🛡️ Integrity")
        st.write("Unified MySQL-backed valuations to prevent multi-million dollar spreadsheet errors.")
    with col3:
        st.write("### 🌐 Collaboration")
        st.write("Real-time synchronization across global investment committees.")

    st.divider()

    # 3. INTERACTIVE FORM (Requirement: "Includes an interactive form")
    st.subheader("📬 Stakeholder System Inquiry")
    st.write("Request access to specific modules or report a data discrepancy.")
    
    with st.form("landing_inquiry_form"):
        user_email = st.text_input("Corporate Email Address")
        inquiry_type = st.selectbox("Inquiry Type", ["Module Access Request", "Data Variance Report", "General Feedback"])
        message = st.text_area("Detailed Message")
        
        # Form submission logic
        submitted = st.form_submit_button("Submit Inquiry")
        if submitted:
            if user_email and message:
                st.success(f"Thank you. Your {inquiry_type} has been logged and routed to the IT Operations team.")
                # In a real app, this would save to a 'Messages' table in MySQL
            else:
                st.error("Please fill out all fields before submitting.")

    # 4. Project Roadmap Visualization (Extra Professional Touch)
    st.write("---")
    st.caption("Beacon Roadmap: Q2 - Database Migration | Q3 - UAT Testing | Q4 - Global Go-Live 2026")
