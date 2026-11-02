import streamlit as st
import json
import datetime
from pathlib import Path

st.set_page_config(page_title="Brahma AI V104", layout="wide")

DATA = Path("data")
DATA.mkdir(exist_ok=True)
CF = DATA / "courses.json"
PF = DATA / "purchases.json"
MH = DATA / ".hash"
AS = DATA / ".sess"
AP = DATA / "apis.json"
QR = DATA / "upi_qr.jpg"
PPT = DATA / "ppts"
PPT.mkdir(exist_ok=True)

def load(p, d):
  try:
    return json.loads(p.read_text())
  except:
    return d

def save(p, d):
  p.write_text(json.dumps(d, indent=2))

TOP25 = ["AI Product Mgmt","AI Project Mgmt","Gen AI Prompt","AI Agents","AI Eng LLM","ML MLOps","AI Strategy","LLM RAG","AI Auto n8n","Data Science","Data Analytics","Data Eng","CyberSec","Cloud AWS","DevOps","FullStack MERN","Python FullStack","Digital Mkt","SEO","FinTech","Blockchain","NoCode","Chatbot","SaaS","Ecom Shopify"]

def sess_ok():
  try:
    d = load(AS, {})
    es = d.get("expiry","")
    if not es:
      return False
    exp = datetime.datetime.fromisoformat(es)
    return datetime.datetime.now() < exp
  except:
    return False

if "admin" not in st.session_state:
  st.session_state.admin = sess_ok()

st.sidebar.title("Brahma AI V104 Pura")

if not MH.exists():
  pw = st.sidebar.text_input("Create Password", type="password")
  if st.sidebar.button("Create Admin"):
    if pw and len(pw) >= 4:
      MH.write_text(pw)
      st.rerun()
  menu = "Browse Courses"
else:
  if not st.session_state.admin:
    menu = st.sidebar.radio("Menu", ["Browse Courses", "My Access"])
    pw = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
      if pw == MH.read_text().strip():
        save(AS, {"expiry": (datetime.datetime.now() + datetime.timedelta(days=7)).isoformat()})
        st.session_state.admin = True
        st.rerun()
      else:
        st.sidebar.error("Wrong")
  else:
    st.sidebar.success("Admin OK V104 Stable No Crash")
    menu = st.sidebar.radio("Admin", ["Dashboard","Price Manager 99","Add New Course","Course Library","UPI QR Setup","API Setup","Brahma Super Agent","Sales","Google Sheet Data"])
    if st.sidebar.button("Logout"):
      AS.unlink(missing_ok=True)
      st.session_state.admin = False
      st.rerun()

def init25():
  d = []
  for i