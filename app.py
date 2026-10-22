import streamlit as st
import pandas as pd
import plotly.express as px
import qrcode, io, random
from web3 import Web3

# ===== BONSAIRWA V10 GOLDEN - 3 TIEU DE DOC BAN =====
QUICKNODE_URL = "https://quick-soft-forest.matic.quiknode.pro/84fc0c23521d03a382a4840796c8ba2b36a1b52b/"
w3 = Web3(Web3.HTTPProvider(QUICKNODE_URL))

st.set_page_config(page_title='BONSAIRWA V10 GOLDEN', layout="wide", page_icon="🌳")

# ===== TIEU DE 1: LOGO LUC SAC DOC BAN =====
st.markdown("""
<div style="background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%); padding:20px; border-radius:15px; border:3px solid #FFD700; text-align:center;">
    <h1 style="color:#FFD700; font-size:42px; margin:0;">BONSAIRWA</h1>
    <h2 style="color:white; font-size:28px; margin:5px;">V10 GOLDEN - LUC SAC DOC BAN</h2>
    <p style="color:#F9A8D4; font-size:16px; margin:5px;">Vang • Tim • Xanh da troi • Xanh ma non • Trang • Hong lot</p>
    <p style="color:#A3E635; font-size:14px;">Doc ban cua CEO Thanh Thai Nguyen - Cho Lach!</p>
</div>
""", unsafe_allow_html=True)

# ===== TIEU DE 2: CAY ME HOANH 90 =====
st.markdown("""
<div style="background: linear-gradient(90deg, #8B5CF6 0%, #38BDF8 50%, #FFD700 100%); padding:15px; border-radius:10px; margin-top:15px; text-align:center;">
    <h2 style="color:white; font-size:22px; margin:0;">🌳 BONSAIRWA-000 | MAI XU ME - BAU VAT</h2>
    <p style="color:black; font-weight:bold; font-size:16px; margin:5px; background:white; padding:5px; border-radius:5px;">
        HOANH 90 • CAO 3M • TRUC QUAN TU • DAU VOI DUOI CHUOT • XU CHAY • 500 TRIEU
    </p>
    <p style="color:white; font-size:13px;">Mai Vang 6 Canh Nguyen Thuy - Khong Ghep - Gen Quy Hiem - Cay Me Cua 127 Cay</p>
</div>
""", unsafe_allow_html=True)

# ===== TIEU DE 3: 【entity-POLYGON¦canonical_name=Polygon】 BLOCK =====
col1, col2, col3 = st.columns(3)
with col1:
    if w3.is_connected():
        st.success(f"✅ 【entity-Polygon¦canonical_name=Polygon】 - Block: {w3.eth.block_number}")
    else:
        st.error("❌ Chua ket noi 【entity-Polygon¦canonical_name=Polygon】")
with col2:
    st.info(f"🔗 Block Cay Me: 95777687 | BONSAIRWA-000-XU-90-3M")
with col3:
    st.warning(f"⚡ QuickNode: Rung Mem Nhanh - Free 10M")

st.markdown("---")
st.title('127 Cay Mai Vang RWA')
st.caption('Cho Lach - QR + Cho RWA + IoT - V10 GOLDEN')

try:
    df = pd.read_csv('data.csv', encoding='utf-8', on_bad_lines='skip')
    df = df.sort_values(by='ID', ascending=True)
    st.write(f"Tong {len(df)} cay - Tong gia tri: {df['GiaTri'].sum():,} VND")
    mother = df[df['ID']==0]
    if not mother.empty:
        st.markdown("### 🌟 CAY ME BONSAIRWA-000 - HOANH 90")
        st.dataframe(mother, use_container_width=True)
    t1,t2,t3,t4,t5 = st.tabs(['Ban Do','Canh Bao','QR Cay','Cho RWA','IoT'])
    with t1:
        st.subheader(f"So do {len(df)} cay")
        fig = px.density_heatmap(df, x='Cot', y='Hang', z='DoAm', color_continuous_scale='RdYlGn')
        st.plotly_chart(fig, use_container_width=True)
    with t2:
        kho = df[df['DoAm']<80]
        st.write(f"Cay can tuoi: {len(kho)} cay")
        st.dataframe(kho)
    with t3:
        st.write("QR cho tung cay - BONSAIRWA-000")
    with t4:
        st.write("Cho RWA - Ban cay")
    with t5:
        st.write("ESP32 gui DoAm qua ThingSpeak")
    st.dataframe(df)
except Exception as e:
    st.error(f"Loi: {e}")
