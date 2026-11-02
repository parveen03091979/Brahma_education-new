import streamlit as st
import json
import secrets
import datetime
import urllib.parse
from pathlib import Path

st.set_page_config(page_title="Brahma AI", layout="wide")

DATA = Path("data")
PPT_DIR = DATA / "ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

CF = DATA / "courses.json"
PF = DATA / "purchases.json"
MH = DATA / ".hash"
AS = DATA / ".sess"

UID = "parveen39179@okicici"
OWNER = "Parveen Kumar"

def load(p, d):
  try:
    return json.loads(p.read_text())
  except:
    return d

def save(p, d):
  p.write_text(json.dumps(d, indent=2))

TOP25 = ["AI Product Mgmt","AI Project Mgmt","Gen AI Prompt","AI Agents","AI Eng LLM","ML MLOps","AI Strategy","LLM RAG","AI Auto n8n","Data Science","Data Analytics","Data Eng","CyberSec","Cloud AWS","DevOps","FullStack MERN","Python FullStack","Digital Mkt","SEO","FinTech","Blockchain","NoCode","Chatbot","SaaS","Ecom Shopify"]

def writer(topic, n):
  a = "ENGLISH ONLY " + topic + " M" + str(n) + "\n"
  b = "COURSE COVER " + topic + " Price 99 Master Teacher 40 Modules\n"
  c = "OVERVIEW What is " + topic + " Future 180K 600 openings 2026 Top 25\n"
  d = "OUTCOMES 10 define " + topic + " explain to 5 build 1 project save 2h tools clients earn portfolio final\n"
  e = "PREREQ Phone internet 1h daily No laptop No degree Village Redmi 8 Jio Rahul 1h daily 2L\n"
  f = "ROADMAP Month1-2 foundation " + topic + " Month3 portfolio Month4 5 clients 75k Month6 agency 2L Next M" + str(n+1) + "\n"
  g = "TOOLS ChatGPT Make.com n8n Sheet WhatsApp API Canva Free vs Paid\n"
  h = "MODULE M" + str(n) + " " + topic + " Master Teacher Price 99 No Ulta Sidha\n"
  i = "GOAL After M" + str(n) + " explain to 5 real example proof\n"
  j = "WHY Salary 56 percent premium 180K With " + topic + " salary 3x Top 2026\n"
  k = "CORE " + topic + " simple Perceive Reason Act Engine car WhatsApp check think reply\n"
  l = "DEEP Definition Types How " + topic + " works Input Output Frontend Backend API When use when not\n"
  m = "STEP 5 STEPS Choose task " + topic + " Open ChatGPT prompt You are expert Connect Make.com Test Diary\n"
  n2 = "TOOLS PRACTICAL Which tools " + topic + " Free vs Paid How use click by click\n"
  o = "EXAMPLE Success Company A used " + topic + " growth 3x 5h to 30m Failure B skipped fail\n"
  p = "CASE Rahul village Redmi 8 Jio no laptop 1h daily " + topic + " Before 4h after 30m auto 90 percent shop owner 10k 3 referrals proof\n"
  q = "MISTAKES 90 percent fail M1 Skip foundation Fix M01-M10 twice M2 Only watch Fix 15m theory practical M3 Money chase Fix 30 days skill M4 No diary Fix 10m diary M5 No mentor Fix community Pro Tip Extra value 2h extra 5 star\n"
  r = "HOMEWORK Today 15m theory + 15m practical Build mini project " + topic + " automate 1 task screenshot Teach to friend voice note Quiz\n"
  s = "NEXT Next M" + str(n+1) + " builds on M" + str(n) + "\n"
  t2 = "PROJECTS 5 Minor every 8 modules 1 small project 2 Major after M20 M30 Real client ROI 1 Final M40 Full portfolio Behance GitHub LinkedIn 1Cr interview\n"
  u = "EXTRA Templates prompts Make.com blueprints Sheet templates WhatsApp Canva Checklists Daily 1h Weekly Portfolio Client onboarding Cheat Sheets Tools comparison Free Paid Pricing Salary 180K Case Studies 10 Rahul story Freelancer Interview Top 20 Freelancing Upwork Fiverr profile proposal First client 15k 5 star Referral 5 clients 75k Agency 2L Resources YouTube Docs Communities LinkedIn Discord Mentors\n"
  v = "ASSESSMENT Quiz 3 to 5 self check Assignment practical screenshot video Final Exam M40 final project review Certificate Brahma Professional English Only\n"
  w = "AGENT SEO Title " + topic + " Master Course 2026 Top 25 Price 99 Only Writer Teacher Single File Har Page Alag Distinct Blog Why " + topic + " Most Demanding 2026 Facebook Instagram post Marketing Copy Sales Funnel Email WhatsApp Chat Bot Price 99 UPI UTR Invoice Access Key\n"
  x = "FULL BOOK COMPLETE DISTINCT Pura Page Bhara Puri Knowledge Market Best 100 percent Price 99 Only Har Page Alag Distinct Good Writer Good Teacher Proper Arrange No Ulta Sidha Complete English Only Best 25 100 percent Data Master Teacher Inside All Things\n"
  return a+b+c+d+e+f+g+h+i+j+k+l+m+n2+o+p+q+r+s+t2+u+v+w+x

def make(c):
  from pptx import Presentation
  from pptx.util import Inches, Pt
  cid = c["id"]
  top = c["topic"]
  en_p = PPT_DIR / (cid + "_EN.pptx")
  prs = Presentation()
  prs.slide_width = Inches(13.33)
  prs.slide_height = Inches(7.5)
  for n in range(1, 41):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    tb = s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.text = "M" + str(n) + " " + top + " Master Teacher All Decided Price 99"
    tf.paragraphs[0].font.size = Pt(10)
    tf.paragraphs[0].font.bold = True
    bb = s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
    bf = bb.text_frame
    bf.word_wrap = True
    bf.text = writer(top, n)
    bf.paragraphs[0].font.size = Pt(6)
  prs.save(str(en_p))
  return en_p

def sess_ok():
  try:
    d = load(AS, {})
    exp = datetime.datetime.fromisoformat(d["expiry"])
    return datetime.datetime.now() < exp
  except:
    return False

if "admin" not in st.session_state:
  st.session_state.admin = sess_ok()

st.sidebar.title("Brahma AI Master Teacher All Decided")

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
      stored = MH.read_text().strip()
      if pw == stored:
        exp = datetime.datetime.now() + datetime.timedelta(days=7)
        save(AS, {"expiry": exp.isoformat()})
        st.session_state.admin = True
        st.rerun()
      else:
        st.sidebar.error("Wrong")
  else:
    st.sidebar.success("Admin OK All Decided No Pending Dashboard Alag")
    menu = st.sidebar.radio("Admin", ["Dashboard","Price Manager 99","Add New Course","Course Library","UPI QR Setup","API Setup","Brahma Super Agent","Sales"])
    if st.sidebar.button("Logout"):
      st.session_state.admin = False
      AS.unlink(missing_ok=True)
      st.rerun()

def init25():
  d = []
  for i, name in enumerate(TOP25):
    d.append({"id": "BRAHMA" + str(1000+i), "topic": name.strip(), "price": 99})
  save(CF, d)
  return d

courses = init25()
purchases = load(PF, [])

if st.session_state.admin:
  if menu == "Dashboard":
    st.title("Dashboard - All Decided - Master Teacher All Things")
    st.success("Dashboard Alag Alag - All Decided Things - WHAT IS TO M40 HATA DIYA - 100 Checked No Indent Error")
    c1, c2 = st.columns(2)
    c1.metric("Total Best 25", len(courses))
    c2.metric("EN Writer Teacher", len(list(PPT_DIR.glob("*EN.pptx"))))
    if st.button("DELETE OLD FILES"):
      for f in PPT_DIR.glob("*.*"):
        f.unlink(missing_ok=True)
      st.success("Done Deleted")
      st.rerun()
    if st.button("CREATE BEST 25 ALL DECIDED THINGS", type="primary"):
      bar = st.progress(0)
      for idx, c in enumerate(courses):
        make(c)
        bar.progress(int((idx+1)/len(courses)*100))
      st.success("Done Best 25 All Decided Things Master Teacher All Things 100 Checked No Indent Error")
      st.balloons()
      st.rerun()
  elif menu == "Price Manager 99":
    st.title("Price Manager 99 - Alag Alag Price Change - All Decided")
    st.success("Price Change Alag Alag - Bulk + Single - All Decided - 100 Checked")
    bulk = st.number_input("Set All Price To", value=99, min_value=1, max_value=10000, step=1)
    if st.button("SET ALL BULK PRICE", type="primary"):
      for c in courses:
        c["price"] = int(bulk)
      save(CF, courses)
      st.success("Done " + str(bulk))
      st.rerun()
    if st.button("SET ALL TO 99 ONLY", type="primary"):
      for c in courses:
        c["price"] = 99
      save(CF, courses)
      st.success("Done 99")
      st.rerun()
    sel = st.selectbox("Select Course For Single Price Change", [c["topic"] + " - " + c["id"] + " - Rs " + str(c.get("price",99)) for c in courses])
    sid = sel.split(" - ")[1]
    curr = 99
    for c in courses:
      if c["id"] == sid:
        curr = c.get("price",99)
    np = st.number_input("New Price Single Course", value=int(curr), min_value=1, max_value=10000, step=1)
    if st.button("UPDATE SINGLE COURSE PRICE", type="primary"):
      for c in courses:
        if c["id"] == sid:
          c["price"] = int(np)
          break
      save(CF, courses)
      st.success("Done Single " + str(np))
      st.rerun()
  elif menu == "Add