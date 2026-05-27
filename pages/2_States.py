import streamlit as st
import pandas as pd
import plotly.express as px

st.title("State-Level Inflation Rankings")
st.caption("Source: NBS CPI State Reports 2024–2025")

states_data = {
    "State": ["Borno","Niger","Bauchi","Kaduna","Plateau","Osun","Kogi","Kano",
              "Zamfara","Abia","Nasarawa","Imo","Edo","Lagos","Rivers","Bayelsa","Akwa Ibom"],
    "Zone": ["North East","North Central","North East","North West","North Central",
             "South West","North Central","North West","North West","South East",
             "North Central","South East","South South","South West","South South","South South","South South"],
    "All-items inflation (%)": [38.9,35.0,34.5,33.3,32.3,32.1,31.8,28.9,29.3,29.2,29.0,28.7,28.3,17.9,17.5,23.8,16.8],
    "Food inflation (%)": [64.4,30.3,38.2,31.1,18.6,22.0,27.4,30.7,28.2,31.9,26.6,25.3,21.9,15.2,14.8,20.1,14.1],
    "Period": ["May 2025","May 2025","2024","Mar 2025","May 2025","Mar 2025","2024",
               "Mar 2025","Feb 2025","Feb 2025","Jul 2025","Mar 2025","Mar 2025","2025","2025","Aug 2025","2025"]
}
df = pd.DataFrame(states_data)

zone_filter = st.multiselect("Filter by zone", df["Zone"].unique(), default=list(df["Zone"].unique()))
filtered = df[df["Zone"].isin(zone_filter)]

sort_col = st.radio("Sort by", ["All-items inflation (%)", "Food inflation (%)"], horizontal=True)
filtered = filtered.sort_values(sort_col, ascending=False)

fig = px.bar(
    filtered, x="State", y=sort_col,
    color="Zone", text=sort_col,
    color_discrete_sequence=px.colors.qualitative.Set2,
    height=450
)
fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
fig.update_layout(xaxis_tickangle=-35)
st.plotly_chart(fig, use_container_width=True)

st.dataframe(filtered.reset_index(drop=True), use_container_width=True)