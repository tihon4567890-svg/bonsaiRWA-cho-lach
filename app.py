import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="127 Cay Mai Vang RWA", layout="wide")
st.title("🌱 Global Peace Map - 127 Cay Mai Vang RWA")
st.caption("Cho Lach, Ben Tre - Tech-Zen | 127 cay")

df = pd.read_csv("data.csv", encoding="utf-8", on_bad_lines="skip")

# Tu dong tao du 127 cay neu moi co 5 cay
if len(df) < 127:
    st.warning(f"Ban moi co {len(df)} cay, dang tao mau du 127 cay de test...")
    import random
    all_data = []
    for i in range(1, 128):
        hang = chr(65 + (i-1)//10)  # A, B, C...
        cot = (i-1)%10 + 1
        all_data.append([i, hang, cot, f"Mai Vang {i}", random.randint(70,98), 5, 15000000, "Khoe"])
    df = pd.DataFrame(all_data, columns=["ID","Hang","Cot","TenCay","DoAm","Tuoi","GiaTri","TrangThai"])

tab1, tab2, tab3 = st.tabs(["🗺️ Ban Do Nhiet", "🚨 Canh Bao", "🔍 Chi Tiet"])

with tab1:
    st.subheader(f"So do do am {len(df)} cay")
    # Mau Do = Kho, Xanh = Uot
    fig = px.density_heatmap(df, x="Cot", y="Hang", z="DoAm", 
                             color_continuous_scale="RdYlGn",
                             range_color=[0,100],
                             title="Xanh=Du Nuoc, Do=Thieu Nuoc")
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)
    stimport streamlit as st
import pandas as pd
import plotly.express as px
import qrcode
from PIL import Image
import io
import random

st.set_page_config(page_title="127 Cay Mai Vang RWA - Full", layout="wide")
st.title("🌱 Global Peace Map - 127 Cay Mai Vang RWA")
st.caption("Cho Lach, Ben Tre - Tech-Zen | QR + Cho RWA + IoT")

# Doc data
try:
    df = pd.read_csv("data.csv", encoding="utf-8", on_bad_lines="skip")
except:
    df = pd.DataFrame()

# Tu dong tao 127 cay neu chua du
if len(df) < 127:
    all_data = []
    for i in range(1, 128):
        hang = chr(65 + (i-1)//10)
        cot = (i-1)%10 + 1
        all_data.append([i, hang, cot, f"Mai Vang {i}", random.randint(65,98), random.randint(3,8), random.choice([8000000,12000000,15000000,20000000]), random.choice(["Khoe","Can Tuoi","Dang Hoa"]), f"0x{i:03d}...RWA", random.choice(["Trong","Da Ban","Dang Ban"])])
    df = pd.DataFrame(all_data, columns=["ID","Hang","Cot","TenCay","DoAm","Tuoi","GiaTri","TrangThai","TokenID","RWAStatus"])

def make_qr(url):
    qr = qrcode.make(url)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    return buf.getvalue()

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🗺️ Ban Do", "🚨 Canh Bao", "🔍 QR Cay", "🛒 Cho RWA", "📡 IoT Cam Bien"])

with tab1:
    st.subheader(f"So do {len(df)} cay - Do=Kho, Xanh=Uot")
    fig = px.density_heatmap(df, x="Cot", y="Hang", z="DoAm", color_continuous_scale="RdYlGn", range_color=[0,100])
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    kho = df[df["DoAm"] < 80]
    if len(kho) > 0:
        st.error(f"Co {len(kho)} cay can tuoi ngay!")
        st.dataframe(kho)
    else:
        st.success("Ca vuon du nuoc!")

with tab3:
    st.subheader("A) QR Code cho tung cay")
    cay = st.selectbox("Chon cay de tao QR", df["TenCay"], key="qr")
    tt = df[df["TenCay"]==cay].iloc[0]
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Do Am", f"{tt['DoAm']}%")
        st.metric("Gia Tri", f"{tt['GiaTri']:,} VND")
        st.write(f"Token: {tt['TokenID']}")
        link_cay = f"https://bonsai-cho-lach-127.streamlit.app/?cay={tt['ID']}"
        st.write(f"Link: {link_cay}")
        qr_bytes = make_qr(link_cay)
        st.image(qr_bytes, caption=f"QR {cay}")
    with col2:
        st.info("Khach quet QR nay se thay thong tin cay, lich su cham soc, va nut Mua RWA")
        st.download_button("Tai QR PNG", qr_bytes, f"QR_{cay}.png", "image/png")

with tab4:
    st.subheader("B) Cho RWA - Mua Ban Cay Mai Vang Token")
    st.write("Moi cay la 1 NFT RWA tren Blockchain")
    filter_status = st.selectbox("Loc", ["Tat Ca","Dang Ban","Da Ban","Trong"])
    df_show = df if filter_status=="Tat Ca" else df[df["RWAStatus"]==filter_status]
    for idx, row in df_show.head(20).iterrows():
        with st.container(border=True):
            c1, c2, c3, c4 = st.columns([2,2,2,1])
            c1.write(f"**{row['TenCay']}** - {row['TokenID']}")
            c2.write(f"{row['GiaTri']:,} VND - {row['TrangThai']}")
            c3.write(f"DoAm {row['DoAm']}% - {row['RWAStatus']}")
            if c4.button("Mua", key=f"buy_{row['ID']}"):
                st.success(f"Da dat mua {row['TenCay']}! Lien he Zalo Chợ Lách!")

with tab5:
    st.subheader("C) IoT Cam Bien That - Huong dan ket noi")
    st.markdown("""
    **De cam bien ngoai vuon tu cap nhat len app:**
    1. Mua bo **ESP32 + Cam bien do am dat capacitive**
    2. ESP32 se gui so lieu moi 15 phut qua WiFi
    3. Code ESP32 se goi API: `https://api.thingspeak.com` hoac Google Sheet
    4. App Streamlit se doc tu Google Sheet tu dong
    
    **Mau Google Sheet:** Tao sheet co cot: ID, DoAm, NhietDo, ThoiGian
    Sau do vao app.py thay dong `pd.read_csv` thanh `pd.read_csv("https://docs.google.com/spreadsheets/d/ID/export?format=csv")`
    """)
    st.code("""
# Code mau cho ESP32 (Arduino)
# gui len ThingSpeak
import urequests
urequests.get(f"https://api.thingspeak.com/update?api_key=XXX&field1={do_am}")
    """, language="python")
    st.warning("Can toi viet code chi tiet cho ESP32 thi gui anh bo cam bien ong dang dung nhe!")

st.download_button("Tai full data 127 cay CSV", df.to_csv(index=False).encode('utf-8'), "127_cay_full_RWA_QR_IoT.csv", "text/csv")
