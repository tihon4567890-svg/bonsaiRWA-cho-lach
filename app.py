
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="127 Cay Mai Vang RWA", layout="wide")
st.title("🌱 Global Peace Map - 127 Cay Mai Vang RWA")
st.caption("Cho Lach, Ben Tre - Tech-Zen")

df = pd.read_csv("data.csv")

tab1, tab2 = st.tabs(["🗺️ So Do Vuon", "🔍 Chi Tiet"])

with tab1:
    st.subheader(f"Ban do do am {len(df)} o cay")
    fig = px.density_heatmap(df, x="Cot", y="Hang", z="DoAm", color_continuous_scale="Greens", range_color=[0,100])
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

with tab2:
    cay = st.selectbox("Chon cay", df["TenCay"])
    tt = df[df["TenCay"]==cay].iloc[0]
    st.metric("Do Am", f"{tt['DoAm']}%")
    st.metric("Tuoi", f"{tt['Tuoi']} nam")
    st.metric("Gia Tri", f"{tt['GiaTri']:,} VND")
    st.write(f"Trang Thai: {tt['TrangThai']}")
