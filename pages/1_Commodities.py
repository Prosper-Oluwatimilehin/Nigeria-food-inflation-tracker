import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Commodity Price Changes")
st.caption("Source: NBS Selected Food Prices Watch, Dec 2024 & Oct 2025")

df = pd.read_csv("data/nbs_data.csv")

st.subheader("Year-on-year price change: Dec 2023 → Dec 2024")
fig = px.bar(
    df.sort_values("yoy_2024_pct", ascending=True),
    x="yoy_2024_pct", y="commodity",
    orientation="h",
    color="yoy_2024_pct",
    color_continuous_scale="Reds",
    labels={"yoy_2024_pct": "% Change", "commodity": ""},
    text="yoy_2024_pct"
)
fig.update_traces(texttemplate="+%{text:.1f}%", textposition="outside")
fig.update_layout(coloraxis_showscale=False, height=420)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Actual prices in naira (₦)")
display_df = df[["commodity", "unit", "dec_2023", "dec_2024", "oct_2025", "yoy_2024_pct"]].copy()
display_df.columns = ["Commodity", "Unit", "Dec 2023 (₦)", "Dec 2024 (₦)", "Oct 2025 (₦)", "YoY Change (%)"]
st.dataframe(display_df, use_container_width=True)