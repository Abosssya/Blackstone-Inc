import streamlit as st
import pandas as pd

# 1. INITIALIZE / READ (The "R" in CRUD)
def initialize_data():
    if 'portfolio' not in st.session_state:
        # Default starting data for the demo
        st.session_state.portfolio = pd.DataFrame([
            {"Ticker": "HLT", "EBITDA ($B)": 2.88, "Multiple": 14.5, "EV ($B)": 41.76},
            {"Ticker": "CQP", "EBITDA ($B)": 4.42, "Multiple": 10.2, "EV ($B)": 45.08}
        ])

def show_crud():
    initialize_data()
    st.subheader("📊 Strategic Portfolio Manager")

    # 2. CREATE (The "C" in CRUD)
    with st.expander("➕ Add New Valuation Entry"):
        with st.form("create_form", clear_on_submit=True):
            ticker = st.text_input("Ticker Symbol (e.g., MAR, ABNB)").upper()
            ebitda = st.number_input("EBITDA ($B)", min_value=0.0, step=0.1)
            multiple = st.number_input("Exit Multiple", min_value=0.0, step=0.1)
            
            if st.form_submit_button("Commit to Pipeline"):
                if ticker:
                    ev = ebitda * multiple
                    new_deal = {"Ticker": ticker, "EBITDA ($B)": ebitda, "Multiple": multiple, "EV ($B)": ev}
                    st.session_state.portfolio = pd.concat([st.session_state.portfolio, pd.DataFrame([new_deal])], ignore_index=True)
                    st.success(f"Deal {ticker} has been added to the global database.")
                    st.rerun()
                else:
                    st.error("Ticker symbol is required.")

    # 3. READ (Displaying the Data)
    st.write("### Active Deal Pipeline")
    st.dataframe(st.session_state.portfolio, use_container_width=True)

    # 4. UPDATE & DELETE (The "U" and "D" in CRUD)
    if not st.session_state.portfolio.empty:
        st.divider()
        st.write("### Manage Existing Records")
        
        # Select target for modification
        target = st.selectbox("Select Asset to Modify or Delete", st.session_state.portfolio["Ticker"])
        idx = st.session_state.portfolio.index[st.session_state.portfolio['Ticker'] == target].tolist()[0]
        current_row = st.session_state.portfolio.iloc[idx]

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Update Logic**")
            new_mult = st.number_input("Adjust Multiple", value=float(current_row["Multiple"]), key="update_mult")
            if st.button("Update Valuation"):
                st.session_state.portfolio.at[idx, "Multiple"] = new_mult
                st.session_state.portfolio.at[idx, "EV ($B)"] = current_row["EBITDA ($B)"] * new_mult
                st.success(f"Valuation for {target} updated.")
                st.rerun()

        with col2:
            st.write("**Removal Logic**")
            st.write(f"Warning: Deleting {target} is permanent.")
            if st.button("Delete Deal", type="primary"):
                st.session_state.portfolio = st.session_state.portfolio.drop(idx).reset_index(drop=True)
                st.warning(f"Record for {target} removed.")
                st.rerun()
