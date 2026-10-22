import streamlit as st
import pandas as pd
import plotly.express as px
import qrcode, io, random
from web3 import Web3

QUICKNODE_URL = "https://quick-soft-forest.matic.quiknode.pro/84fc0c23521d03a382a4840796c8ba2b36a1b52b/"
w3 = Web3(Web3.HTTPProvider(QUICKNODE_URL))

st.set_page_config(page_title='BONSAIRWA V10 GOLDEN', layout="wide", page_icon="🌳")

# TIEU DE 1: LOGO LUC SAC
st.markdown("""
<div style="background:#0a0a0a; padding:20px; border-radius:15px; border:3px solid #FFD700; text-align:center;">
    <h1 style="color:#FFD700; font-size:42px; margin:0;">BONSAIRWA</h1>
    <h2 style="color:white; font-size:28px; margin:5px;">V10 GOLDEN - LUC SAC DOC BAN</h2>
    <p style="color:#F9A8D4; font-size:16px;">Vang • Tim • Xanh da troi • Xanh ma non • Trang • Hong lot</p>
    <p style="color:#A3E635; font-size:14px;">Doc ban CEO Thanh Thai Nguyen - Cho Lach!</p>
</div>
""", unsafe_allow_html=True)

# TIEU DE 2: CAY ME
st.markdown("""
<div style="background: linear-gradient(90deg, #8B5CF6 0%, #38BDF8 50%, #FFD700 100%); padding:15px; border-radius:10px; margin-top:15px; text-align:center;">
    <h2 style="color:white; font-size:22px; margin:0;">BONSAIRWA-000 | MAI XU ME - BAU VAT</h2>
    <p style="color:black; font-weight:bold; font-size:16px; margin:5px; background:white; padding:5px; border-radius:5px;">
        HOANH 90 • CAO 3M • TRUC QUAN TU • DAU VOI DUOI CHUOT • XU CHAY • 500 TRIEU
    </p>
    <p style="color:white; font-size:13px;">Mai Vang 6 Canh Nguyen Thuy - Khong Ghep - Cay Me 127 Cay</p>
</div>
""", unsafe_allow_html=True)

# TIEU DE 3: BLOCKCHAIN - SACH KHONG CO CHU LA
col1, col2, col3 = st.columns(3)
with col1:
    if w3.is_connected():
        st.success(f"Da ket noi MATIC - Block: {w3.eth.block_number}")
    else:
        st.error("Chua ket noi MATIC")
with col2:
    st.info(f"Block Cay Me: 95777687 | BONSAIRWA-000-XU-90-3M")
with col3:
    st.warning(f"QuickNode: Rung Mem Nhanh - Free 10M")

st.markdown("---")
