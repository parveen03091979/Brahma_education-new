import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
st.set_page_config(page_title="Brahma Retirement", layout="wide")
DATA=Path("data")
PPT_DIR=DATA/"ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)
CF=DATA/"courses.json"
PF=DATA/"purchases.json"
QF=DATA/"upi_qr.jpg"
MH=DATA/".master_hash"
AS=DATA/".admin_session"
UID="parveen39179@okicici"
OWNER="Parveen Kumar"
def load(p,d):
 try:
  if p.exists():
   return json.loads(p.read_text(encoding="utf-8"))
 except:
  pass
 return d
def save(p,d):
 t=p.with_suffix(".tmp")
 t.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
 t.replace(p)
TOP50="AI Product Mgmt,AI Project Mgmt,Gen AI Prompt,AI Agents,AI Eng LLM,ML MLOps,AI Strategy,LLM RAG,AI Auto n8n,Data Science,Data Analytics,Data Eng,CyberSec,Cloud AWS,DevOps,FullStack MERN,Python FullStack,Java FullStack,UI UX,Digital Mkt,SEO,Social Media,Video Edit,Graphic Design,Blockchain,FinTech,Stock Crypto,Product Mgmt,Project Mgmt,Biz Analytics,Robotics,Quantum,IoT,AR VR,Game Dev,Mobile Flutter,NoCode,Chatbot,SaaS,Ecom Shopify,YouTube Auto,Copywriting,Resume Interview,Communication,Leadership,EV Tech,Solar Energy,Digital Health,Bioinfo,Supply Chain,HR Analytics,Tally GST".split(",")
def init50():
 d=[]
 for i,name in enumerate(TOP50):
  d.append({"id":f"BRAHMA{1000+i}","topic":name.strip(),"price":99})
 save(CF,d)
 return d
courses=init50()
purchases=load(PF,[])
MODS="WHAT IS,WHY IMP,WHERE USE,WHEN USE,WHO LEARN,HOW WORKS,TOOLS,EARN MONEY,PRACTICAL,RIGHT WAY,FOUNDATION,CORE,ADVANCED,STEP PROCESS