import streamlit as st

st.set_page_config(
    page_title="Nigeria Food Price Inflation Tracker",
    page_icon="🇳🇬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🇳🇬 Nigeria Food Price Inflation Tracker")
st.markdown("""
Track how food prices changed across Nigerian states from 2022–2025,  
using data from the **National Bureau of Statistics (NBS)**.

Use the sidebar to navigate between sections.
""")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Food inflation peak", "40.87%", "June 2024 (NBS)")
col2.metric("Dec 2025 food inflation", "10.84%", "-29% from Dec 2024")
col3.metric("Worst commodity 2024", "Garri +200%", "Dec 2023 → Dec 2024")
col4.metric("Most-hit state", "Borno", "64.4% food inflation")

st.markdown("---")
st.caption("Sources: NBS CPI Reports 2022–2025 · NBS Selected Food Prices Watch · NISER CPI Rebasing Brief 2025")