import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="BonsaiRWA Cho Lach", page_icon="🌱", layout="wide")
st.title("🌱 Global Peace Map - 127 Cay Mai Vang RWA")
st.caption("Cho Lach, Ben Tre - Tech-Zen")
rows=[]
for i in range(1,128):
    rows.append({"ID":f"O-{i:03d}","Ten":f"Mai Vang #{i}","Hang":chr(65+(i//32)),"Cot":i%32+1,"DoAm":85+i%11,"Hoanh":25+i%30,"Gia":(15+i%20)*1000000})
df=pd.DataFrame(rows)
tab1,tab2=st.tabs(["🗺️ So Do Vuon","🔍 Chi Tiet"])
with tab1:
    fig=px.scatter(df,x="Cot",y="Hang",color="DoAm",hover_data=["ID","Hoanh"],color_continuous_scale="Greens",title="Ban do do am 127 o cay")
    fig.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig,use_container_width=True)
with tab2:
    sel=st.selectbox("Chon o cay:",df["ID"])
    c=df[df["ID"]==sel].iloc[0]
    st.success(f"**{c['Ten']}** - Hang {c['Hang']} Cot {c['Cot']} | Do am {c['DoAm']}% | Hoanh {c['Hoanh']}cm | Gia {c['Gia']:,} VND")
    if st.button("🔔 Thinh Chuong Tinh Thuc"):
        st.toast(f"Da kich hoat tan so cho {c['Ten']}!")
        st.balloons()
