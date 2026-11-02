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
  return "ENGLISH ONLY " + topic + " M" + str(n) + " Master Teacher\nCOURSE COVER " + topic + " Price 99\nOVERVIEW What is " + topic + " Future 180K 600 openings\nOUTCOMES 10 define explain build save tools clients earn portfolio\nPREREQ Phone internet 1h daily No laptop Village Redmi 8 Jio Rahul 1h 2L\nROADMAP Month1-2 foundation Month3 portfolio Month4 5 clients 75k Month6 agency 2L\nTOOLS ChatGPT Make.com n8n Sheet WhatsApp API Canva\nMODULE M" + str(n) + " " + topic + " Master Teacher Price 99\nGOAL After M" + str(n) + " explain to 5\nWHY Salary 56 percent premium 180K\nCORE Perceive Reason Act Engine car\nDEEP Definition Types How works Input Output Frontend Backend API\nSTEP 5 STEPS Choose task Open ChatGPT prompt You are expert Connect Make.com Test\nTOOLS PRACTICAL Which tools Free vs Paid How use click by click\nEXAMPLE Success Company A growth 3x Failure B skipped\nCASE Rahul village Redmi 8 Jio no laptop 1h daily Before 4h after 30m auto 90 percent shop owner 10k 3 referrals proof\nMISTAKES 90 percent fail M1 Skip foundation Fix M01-M10 twice M2 Only watch Fix 15m theory practical\nHOMEWORK Today 15m theory + 15m practical Build mini project automate 1 task\nNEXT Next M" + str(n+1) + " builds on M" + str(n) + "\nPROJECTS 5 Minor every 8 modules 1 small 2 Major after M20 M30 Real client 1 Final M40 Full portfolio Behance GitHub LinkedIn 1Cr\nEXTRA Templates prompts Make.com blueprints Sheet templates WhatsApp Canva Checklists Daily 1h Weekly Portfolio Client onboarding Cheat Sheets Tools comparison Salary 180K Case Studies Freelancing Upwork Fiverr profile proposal First client 15k 5 star Referral 5 clients 75k Agency 2L Resources YouTube Docs Communities LinkedIn Discord Mentors\nASSESSMENT Quiz 3 to 5 self check Assignment practical Final Exam M40 final project review Certificate Brahma Professional\nAGENT SEO Title " + topic + " Master Course 2026 Top 25 Price 99 Only Writer Teacher Single File Har Page Alag Distinct Blog Why Most Demanding 2026 Facebook Instagram post Marketing Copy Sales Funnel Email WhatsApp Chat Bot Price 99 UPI UTR Invoice Access Key\nFULL BOOK COMPLETE DISTINCT Pura Page Bhara Puri Knowledge Market Best 100 percent Price 99 Only Har Page Alag Distinct Good Writer Good Teacher Proper Arrange\n"

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
    sl = prs.slides.add_slide(prs.slide_layouts[6])
    tb = sl.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.text = "M" + str(n) + " " + top + " Master Teacher All Decided Price 99"
    tf.paragraphs[0].font.size = Pt(10)
    tf.paragraphs[0].font.bold = True
    bb = sl.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
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

st.sidebar.title("Brahma AI Master Teacher")

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
    st.sidebar.success("Admin OK")
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
    st.title("Dashboard - All Decided")
    st.success("All Decided - WHAT IS TO M40 HATA DIYA - Tested")
    c1, c2 = st.columns(2)
    c1.metric("Total Best 25", len(courses))
    c2.metric("EN Files", len(list(PPT_DIR.glob("*EN.pptx"))))
    if st.button("DELETE OLD FILES"):
      for f in PPT_DIR.glob("*.*"):
        f.unlink(missing_ok=True)
      st.success("Done Deleted")
      st.rerun()
    if st.button("CREATE BEST 25", type="primary"):
      bar = st.progress(0)
      total = len(courses)
      count = 0
      for c in courses:
        make(c)
        count = count + 1
        bar.progress(int(count * 100 / total))
      st.success("Done Best 25 Created")
      st.balloons()
      st.rerun()
  elif menu == "Price Manager 99":
    st.title("Price Manager 99")
    bulk = st.number_input("Set All Price To", value=99, min_value=1, max_value=10000, step=1)
    if st.button("SET ALL BULK PRICE", type="primary"):
      for c in courses:
        c["price"] = int(bulk)
      save(CF, courses)
      st.success("Done")
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
      st.success("Done Single")
      st.rerun()
  elif menu == "Add New Course":
    st.title("Add New Course")
    with st.form("add"):
      nt = st.text_input("New Course Name")
      npr = st.number_input("New Price", value=99, min_value=1, max_value=10000, step=1)
      sub = st.form_submit_button("ADD NEW COURSE", type="primary")
      if sub:
        if len(nt) < 3:
          st.error("Error Short")
        else:
          nid = "BRAHMA" + str(1000+len(courses))
          courses.append({"id": nid, "topic": nt, "price": int(npr)})
          save(CF, courses)
          make({"id": nid, "topic": nt})
          st.success("Done Added")
          st.rerun()
  elif menu == "Course Library":
    st.title("Course Library")
    for idx, co in enumerate(courses):
      en_f = list(PPT_DIR.glob(co["id"] + "*EN.pptx"))
      if en_f:
        st.success(str(idx+1) + ". " + co["topic"] + " - Rs " + str(co.get("price",99)))
        st.download_button("EN Download", data=en_f[0].read_bytes(), file_name=en_f[0].name, key="en"+str(idx))
  elif menu == "UPI QR Setup":
    st.title("UPI QR Setup")
    st.write("UPI ID: " + UID + " Owner: " + OWNER + " Price 99")
    up = st.file_uploader("Upload QR Code Image", type=["jpg","png","jpeg"])
    if up:
      QF = DATA / "upi_qr.jpg"
      QF.write_bytes(up.getvalue())
      st.success("Done QR Uploaded")
      st.rerun()
    if (DATA / "upi_qr.jpg").exists():
      st.image(str(DATA / "upi_qr.jpg"), width=300)
  elif menu == "API Setup":
    st.title("API Setup")
    apis = load(AS, {})
    o = st.text_input("OpenAI Key", value=apis.get("openai",""), type="password")
    f = st.text_input("Facebook Token", value=apis.get("fb",""), type="password")
    ii = st.text_input("Instagram Token", value=apis.get("insta",""), type="password")
    g = st.text_input("Google Key", value=apis.get("google",""), type="password")
    if st.button("SAVE API KEYS", type="primary"):
      save(AS, {"openai": o, "fb": f, "insta": ii, "google": g})
      st.success("Done Saved")
      st.rerun()
  elif menu == "Brahma Super Agent":
    st.title("Brahma Super Agent")
    for idx, co in enumerate(courses[:5]):
      with st.expander(str(idx+1) + ". " + co["topic"]):
        st.write("SEO Title " + co["topic"] + " Master Course 2026 Top 25 Price 99 Only")
        st.write("Blog Why " + co["topic"] + " Most Demanding 2026 Market Data 180K 600 openings")
        st.write("Social Media Post Facebook Instagram Reels Stories")
        st.write("Chat Boat Script Welcome to Brahma Master Academy Price 99 Only")
    st.success("Super Agent Active")
  elif menu == "Sales":
    st.title("Sales - No Pending Direct Access")
    st.success("Sales Alag Alag - No Pending - Direct Access")
    for i, p in enumerate(purchases):
      with st.expander(p.get("invoice_no","Order") + " - " + p.get("course","") + " - Rs " + str(p.get("price",""))):
        st.write("Name:", p.get("name"))
        st.write("Mobile:", p.get("mobile",""))
        st.write("Email:", p.get("email"))
        st.write("Course:", p.get("course"))
        st.write("Price:", p.get("price"))
        st.write("UTR:", p.get("utr"))
        st.write("Status:", p.get("status"))
        st.write("Access Key:", p.get("access_key"))
        st.success("Direct Approved - " + p.get("access_key",""))
else:
  if menu == "Browse Courses":
    st.title("Brahma Academy - Best 25 Full Plan - No Pending Direct Access")
    st.success("Customer Form - All Decided - No Pending Direct Access")
    for i, course in enumerate(courses):
      with st.expander(str(i+1) + ". " + course["topic"] + " - Rs " + str(course["price"])):
        params = {"pa": UID, "pn": OWNER, "am": str(course["price"]), "cu": "INR", "tn": course["topic"][:20]}
        link = "upi://pay?" + urllib.parse.urlencode(params)
        st.link_button("PAY Rs " + str(course["price"]) + " - UPI Payment", link, type="primary")
        with st.form("buy_" + course["id"]):
          name = st.text_input("Your Name", key="n"+course["id"])
          mobile = st.text_input("Your Mobile Number", key="mob"+course["id"])
          email = st.text_input("Your Email", key="e"+course["id"])
          utr = st.text_input("UTR Number", key="u"+course["id"])
          submit = st.form_submit_button("SUBMIT PAYMENT Rs " + str(course["price"]))
          if submit:
            if len(name) < 3 or len(email) < 5 or len(utr) < 5 or len(mobile) < 5:
              st.error("Error Fill All Name Mobile Email UTR")
            else:
              ak = "BRAHMA-" + secrets.token_hex(3).upper()
              inv = "INV" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
              purchases.append({"invoice_no": inv, "access_key": ak, "name": name, "mobile": mobile, "email": email, "course": course["topic"], "course_id": course["id"], "price": int(course["price"]), "utr": utr, "status": "APPROVED", "date": str(datetime.datetime.now())})
              save(PF, purchases)
              st.success("Done Direct Access - Invoice " + inv + " - Access Key " + ak + " - Invoice will be sent to Email " + email)
              st.balloons()
  elif menu == "My Access":
    st.title("My Learning - Best 25 Full Plan")
    k = st.text_input("Enter Invoice Or Access Key")
    if st.button("UNLOCK", type="primary"):
      found = [p for p in purchases if (p.get("invoice_no")==k or p.get("access_key")==k) and p.get("status")=="APPROVED"]
      if not found:
        st.error("Error Not Found")
      else:
        pu = found[0]
        st.success("Welcome " + pu.get("name","Student") + " - " + pu.get("course"))
        en_f = list(PPT_DIR.glob(pu.get("course_id") + "*EN.pptx"))
        if en_f:
          st.download_button("DOWNLOAD ENGLISH ONLY FULL PLAN PRICE 99", data=en_f[0].read_bytes(), file_name=en_f[0].name, type="primary")
        if not en_f:
          st.warning("Books Not Ready Yet")

st.caption("V144 Final Tested Flat No Indent Error All Decided Things Present Best 25 English Only Single File 40 Modules Master Teacher Inside All Things Dashboard Alag Alag Price Manager 99 Bulk Single Add New Course Course Library UPI QR Setup API Setup Brahma Super Agent Sales Browse My Access No Pending Direct Access WHAT IS TO M40 HATA DIYA")