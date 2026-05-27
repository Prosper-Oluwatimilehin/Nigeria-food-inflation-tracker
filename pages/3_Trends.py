import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Year-on-Year Inflation Trend")
st.caption("Source: NBS CPI monthly reports 2023–2025. Note: NBS rebased CPI from 2009 → 2024 in early 2025.")

months = ["Jan 23","Apr 23","Jul 23","Oct 23","Jan 24","Apr 24","Jun 24",
          "Sep 24","Dec 24","Feb 25*","May 25","Jul 25","Oct 25","Dec 25"]

series = {
    "Food (all)":    [18.4, 24.3, 26.5, 29.8, 35.4, 40.9, 40.9, 39.8, 39.8, 23.5, 21.1, 22.7, 13.1, 10.8],
    "Cereals/bread": [17.1, 22.1, 24.3, 28.1, 33.2, 38.5, 38.5, 37.9, 37.6, 21.8, 20.4, 21.6, 12.8, 10.2],
    "Oils & fats":   [22.0, 30.1, 32.4, 34.8, 41.2, 46.2, 46.2, 42.7, 41.0, 24.1, 21.8, 23.1, 14.2, 11.5],
    "Tubers & veg":  [16.2, 21.8, 23.9, 27.1, 36.1, 43.6, 43.6, 40.1, 39.8, 22.4, 20.6, 22.1, 12.6, 10.0],
}

selected = st.multiselect("Select categories", list(series.keys()), default=list(series.keys()))

fig = go.Figure()
colors = ["#C0390F", "#D95C26", "#E98E55", "#1D9E75"]
for i, cat in enumerate(selected):
    fig.add_trace(go.Scatter(
        x=months, y=series[cat], name=cat,
        line=dict(color=colors[i % len(colors)], width=2),
        mode="lines+markers"
    ))

fig.add_annotation(
    x="Feb 25*", y=1, xref="x", yref="paper",
    text="⬆ CPI rebase", showarrow=False,
    font=dict(size=11, color="gray"),
    bgcolor="white", bordercolor="gray", borderwidth=1
)
fig.update_layout(
    yaxis_title="YoY food inflation (%)",
    yaxis_ticksuffix="%", height=420,
    legend=dict(orientation="h", yanchor="bottom", y=1.02)
)
st.plotly_chart(fig, use_container_width=True)
st.caption("* Feb 2025 onwards uses rebased CPI (base year 2024). Sharp drop partly reflects methodology change, not just real price relief.")