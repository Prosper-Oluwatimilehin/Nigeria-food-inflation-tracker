import streamlit as st
import pandas as pd
from utils.export import to_csv, to_excel

st.title("Download the Data")
st.caption("AI query feature coming soon")

df = pd.read_csv("data/nbs_data.csv")

st.dataframe(df, use_container_width=True)

st.subheader("Download")
col1, col2 = st.columns(2)
col1.download_button("Download CSV", to_csv(df), "nbs_food_prices.csv", "text/csv")
col2.download_button("Download Excel", to_excel(df), "nbs_food_prices.xlsx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")