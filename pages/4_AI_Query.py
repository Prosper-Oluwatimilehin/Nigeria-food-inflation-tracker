import streamlit as st
import pandas as pd
from utils.ai_query import get_ai_answer
from utils.export import to_csv, to_excel

st.title("Ask the Data")
st.caption("Powered by Claude — ask questions about Nigeria food price inflation")

df = pd.read_csv("data/nbs_data.csv")
context = df.to_string()

question = st.text_input("Ask a question", placeholder="Which commodity inflated the most in 2024?")

if st.button("Ask ↗") and question:
    with st.spinner("Thinking..."):
        answer = get_ai_answer(question, context)
    st.markdown(f"**Answer:** {answer}")

st.markdown("---")
st.subheader("Download the data")
col1, col2 = st.columns(2)
col1.download_button("Download CSV", to_csv(df), "nbs_food_prices.csv", "text/csv")
col2.download_button("Download Excel", to_excel(df), "nbs_food_prices.xlsx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")