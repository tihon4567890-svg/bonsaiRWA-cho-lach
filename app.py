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
    st.dataframe(df, use_container_width=True)

with tab2:
    kho = df[df["DoAm"] < 80]
    if len(kho) > 0:
        st.error(f"Co {len(kho)} cay can tuoi nuoc ngay!")
        st.dataframe(kho[["TenCay","Hang","Cot","DoAm"]])
    else:
        st.success("Ca vuon du nuoc! Tuyet voi!")

with tab3:
    cay = st.selectbox("Chon cay", df["TenCay"])
    tt = df[df["TenCay"]==cay].iloc[0]
    col1, col2, col3 = st.columns(3)
    col1.metric("Do Am", f"{tt['DoAm']}%", delta=f"{tt['DoAm']-80}%")
    col2.metric("Tuoi", f"{tt['Tuoi']} nam")
    col3.metric("Gia Tri", f"{tt['GiaTri']:,} VND")
    st.write(f"Trang thai: **{tt['TrangThai']}** - Hang {tt['Hang']} Cot {tt['Cot']}")

st.download_button("Tai file 127 cay mau CSV", df.to_csv(index=False).encode('utf-8'), "127_cay_mau.csv", "text/csv")
