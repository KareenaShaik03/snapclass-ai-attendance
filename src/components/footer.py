import streamlit as st


def footer_home():

    st.markdown(f"""
        <div style="display:flex; align-items:center;justify-content:center; margin-top:2rem; gap:6px;">
        <p style="font-weight:bold; color: white;"> Created with ❤️ by Kareena Shaik </p>
        </div>

                """,unsafe_allow_html=True)
    
def footer_dashboard():

    st.markdown(f"""
        <div style="display:flex; align-items:center;justify-content:center; margin-top:2rem; gap:6px;">
        <p style="font-weight:bold; color: black;"> Created with ❤️ by Kareena Shaik </p>
        </div>

                """,unsafe_allow_html=True)