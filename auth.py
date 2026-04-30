import streamlit as st

def login():
    # Blackstone Styling for the Login Box
    st.markdown("""
        <style>
        .login-box {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            border: 1px solid #e0e0e0;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Blackstone_Logo.svg/1200px-Blackstone_Logo.svg.png", width=250)
        st.title("🛡️ Beacon Access Portal")
        st.write("Institutional Equity Reporting & Valuation System")
        
        # Simulated User Entry Fields
        username = st.text_input("Credential ID (Try: Ayden or Mason)")
        password = st.text_input("Access Token", type="password", help="For this simulation, any password works.")

        if st.button("Authenticate"):
            # The logic check
            if username.lower() in ["ayden", "mason"]:
                st.session_state.authenticated = True
                st.session_state.user_role = username.capitalize()
                st.success(f"Identity Verified. Welcome, {st.session_state.user_role}.")
                st.rerun() # Refresh to unlock the main ERP
            else:
                st.error("Authentication Failed: User ID not recognized in global directory.")
