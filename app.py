import streamlit as st
import pandas as pd
import plotly.express as px
import qrcode, io, random
from web3 import Web3

# ===== BONSAIRWA V10 - QUICKNODE POLYGON MAINNET - DUONG ONG VANG =====
QUICKNODE_URL = "https://quick-soft-forest.matic.quiknode.pro/84fc0c23521d03a382a4840796c8ba2b36a1b52b/"
w3 = Web3(Web3.HTTPProvider(QUICKNODE_URL))
# ===== HET PHAN QUICKNODE =====

st.set_page_config(page_title='127 Cay Mai', layout="wide")
st.title('127 Cay Mai Vang RWA')
st.caption('Cho Lach - QR + Cho RWA + IoT')
try:
 df = pd.read_csv('data.csv', encoding='utf-8', on_bad_lines='skip')
except:
 df = pd.DataFrame()
if len(df) < 127:
 all_data = []
 for i in range(1,128):
  hang = chr(65+(i-1)//10)
  cot = (i-1)%10+1
  stt = random.choice(['Ban','DaBan','Trong'])
  all_data.append([i,hang,cot,f'Mai {i}',random.randint(65,98),5,15000000,'Khoe',f'0x{i:03d}',stt])
 df = pd.DataFrame(all_data, columns=['ID','Hang','Cot','TenCay','DoAm','Tuoi','GiaTri','TrangThai','TokenID','RWAStatus'])
def make_qr(url):
 qr=qrcode.make(url)
 buf=io.BytesIO()
 qr.save(buf, format='PNG')
 return buf.getvalue()
t1,t2,t3,t4,t5 = st.tabs(['Ban Do','Canh Bao','QR Cay','Cho RWA','IoT'])
with t1:
 st.subheader(f'So do {len(df)} cay')
 fig=px.density_heatmap(df,x='Cot',y='Hang',z='DoAm',color_continuous_scale='RdYlGn',range_color=[0,100])
 fig.update_yaxes(autorange='reversed')
 st.plotly_chart(fig,use_container_width=True)
 st.dataframe(df)
with t2:
 kho=df[df['DoAm']<80]
 if len(kho)>0:
  st.error(f'Co {len(kho)} cay can tuoi!')
  st.dataframe(kho)
 else:
  st.success('Vuon du nuoc!')
with t3:
 st.subheader('QR cho tung cay')
 cay=st.selectbox('Chon cay',df['TenCay'],key='qr')
 tt=df[df['TenCay']==cay].iloc[0]
 c1,c2=st.columns(2)
 with c1:
  st.metric('Do Am',f"{tt['DoAm']}%")
  link=f"https://bonsai-cho-lach-127.streamlit.app/?cay={tt['ID']}"
  qr_bytes=make_qr(link)
  st.image(qr_bytes,caption=f'QR {cay}')
 with c2:
  st.info('Quet QR de xem cay va mua RWA')
  st.download_button('Tai QR',qr_bytes,f"QR_{cay}.png",'image/png')
with t4:
 st.subheader('Cho RWA')
 loc=st.selectbox('Loc',['Tat Ca','Ban','DaBan','Trong'])
 show=df if loc=='Tat Ca' else df[df['RWAStatus']==loc]
 for _,r in show.head(20).iterrows():
  with st.container(border=True):
   a,b,c,d=st.columns([2,2,2,1])
   a.write(f"**{r['TenCay']}** {r['TokenID']}")
   b.write(f"{r['GiaTri']:,} VND")
   c.write(f"{r['RWAStatus']} {r['DoAm']}%")
   if d.button('Mua',key=f"buy_{r['ID']}"):
    st.success(f"Dat mua {r['TenCay']}!")
with t5:
 st.subheader('IoT Cam Bien')
 st.write('ESP32 gui DoAm qua ThingSpeak')
 st.code('GET https://api.thingspeak.com/update?api_key=XXX&field1=DoAm')
st.download_button('Tai CSV 127 cay',df.to_csv(index=False).encode('utf-8'),'127_cay.csv','text/csv')
