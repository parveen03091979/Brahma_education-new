import streamlit as st
import json
import datetime
from pathlib import Path

st.set_page_config(page_title="Brahma AI V149 Safe", layout="wide")

DATA = Path("data")
DATA.mkdir(exist_ok=True)
CF = DATA / "courses.json"
PF = DATA / "purchases.json"
MH = DATA / ".hash"
AS = DATA / ".sess"
AP = DATA / "apis.json"

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

st.sidebar.title("Brahma AI V149 Safe No Crash")

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
    st.sidebar.success("Admin OK V149 Safe")
    menu = st.sidebar.radio("Admin", ["Dashboard","Price Manager 99","Add New Course","Course Library","UPI QR Setup","API Setup","Brahma Super Agent","Sales","Google Sheet Data"])
    if st.sidebar.button("Logout"):
      AS.unlink(missing_ok=True)
      st.session_state.admin = False
      st.rerun()

def init25():
  d = []
  for i, name in enumerate(TOP25):
    d.append({"id": "BRAHMA" + str(1000+i), "topic": name.strip(), "price": 99})
  save(CF, d)
  return d

courses = init25()
purchases = load(PF, [])
apis = load(AP, {})

# ADMIN
if st.session_state.admin:
  if menu == "Dashboard":
    st.title("Dashboard - V149 Safe No Crash - All Points Include")
    st.success("Jo Sari Chijen Decide Ki Thi Yahi Sari Chijon Ke Saath Sahi Bana - Best 25 Top 25 market data salary $180K 600 openings - English Only Single File 40 Modules har page alag distinct full book pura page bhara market best - Master Teacher AI 100% online data collect Writer Teacher proper arrange No Ulta Sidha WHAT IS TO M40 HATA DIYA - Ek course me 23 points Course Cover Overview Outcomes Prereq Roadmap Tools Module Goal Why Core Deep Step Tools Practical Example Case Rahul Village Mistakes Homework Next Projects Extra Templates Assessment Super Agent SEO Blog Social Media Full Book - Dashboard alag Price Manager bulk single Add New Course master teacher command keyboard Course Library UPI QR Setup QR + keyboard UPI ID Owner API Setup API + Tokens Super Agent daily auto posting SEO FB Insta blog Chat Boat Sales Google Sheet Data Browse My Access No Pending Direct Access UPI ID parveen39179@okicici Owner Parveen Kumar Price 99 Email invoice Google Sheet auto data")
    st.metric("Total Best 25", len(courses))
    st.metric("Total Sales", len(purchases))
    st.info("V149 Minimal Safe - PPT heavy hata diya - App halka - Guarantee chalega - Paisa kamao - Pure din ka loss cover hoga")

  elif menu == "Price Manager 99":
    st.title("Price Manager 99 - Bulk + Single - V149 Safe")
    bulk = st.number_input("Set All Price To Bulk Sabhi Ka Ek Bar Mein Change", value=99, min_value=1, max_value=10000)
    if st.button("SET ALL BULK PRICE Sabhi Ka Ek Bar Mein Change"):
      for c in courses:
        c["price"] = int(bulk)
      save(CF, courses)
      st.success("Done Bulk " + str(bulk))
      st.rerun()
    if st.button("SET ALL TO 99 ONLY"):
      for c in courses:
        c["price"] = 99
      save(CF, courses)
      st.success("Done 99")
      st.rerun()
    sel = st.selectbox("Select Course For Single Price Change Ek-Ek Ka Change", [c["topic"] + " - " + c["id"] + " - Rs " + str(c.get("price",99)) for c in courses])
    sid = sel.split(" - ")[1]
    curr = 99
    for c in courses:
      if c["id"] == sid:
        curr = c.get("price",99)
    np = st.number_input("New Price Single Course Ek-Ek Ka Change", value=int(curr), min_value=1, max_value=10000)
    if st.button("UPDATE SINGLE COURSE PRICE Ek-Ek Ka Change"):
      for c in courses:
        if c["id"] == sid:
          c["price"] = int(np)
          break
      save(CF, courses)
      st.success("Done Single " + str(np))
      st.rerun()

  elif menu == "Add New Course":
    st.title("Add New Course - Master Teacher Command - V149 Safe")
    nt = st.text_input("New Course Name Keyboard Se - Master Teacher Ko Command")
    npr = st.number_input("New Price", value=99, min_value=1, max_value=10000)
    if st.button("ADD NEW COURSE MASTER TEACHER COMMAND"):
      if len(nt) < 3:
        st.error("Short Name")
      else:
        nid = "BRAHMA" + str(1000+len(courses