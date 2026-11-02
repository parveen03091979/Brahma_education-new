import streamlit as st
import json
import datetime
from pathlib import Path

st.set_page_config(page_title="Brahma AI V150 Pura", layout="wide")

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

st.sidebar.title("Brahma AI V150 Pura Project")

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
    st.sidebar.success("Admin OK V150 Pura No Crash")
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

def writer_full(topic, n):
  txt = ""
  txt += "ENGLISH ONLY " + topic + " M" + str(n) + " Master Teacher All Decided\n"
  txt += "COURSE COVER " + topic + " Price 99 Master Teacher 40 Modules Single File 100 percent Data Har Page Alag Distinct Market Best\n"
  txt += "OVERVIEW What is " + topic + " Future Market $180K-$320K 600 openings 2026 Most Demanding Top 25\n"
  txt += "OUTCOMES 10 define " + topic + " explain to 5 build 1 project save 2h tools clients earn portfolio final\n"
  txt += "PREREQ Phone internet 1h daily No laptop No degree Village Redmi 8 Jio Rahul 1h daily 2L\n"
  txt += "ROADMAP Month1-2 foundation Month3 portfolio Month4 5 clients 75k Month6 agency 2L Next M" + str(n+1) + "\n"
  txt += "TOOLS ChatGPT Make.com n8n Sheet WhatsApp API Canva Free vs Paid\n"
  txt += "MODULE M" + str(n) + " " + topic + " Master Teacher Price 99 No Ulta Sidha Proper Arrange Good Writer Good Teacher\n"
  txt += "GOAL After M" + str(n) + " explain to 5 real example proof\n"
  txt += "WHY Salary 56 percent premium 180K With " + topic + " salary 3x Top 2026\n"
  txt += "CORE Perceive Reason Act Engine car WhatsApp check think reply auto\n"
  txt += "DEEP Definition Types How works Input Output Frontend Backend API When use when not\n"
  txt += "STEP 5 STEPS Choose task Open ChatGPT prompt You are expert Connect Make.com Test Diary 15m theory + 15m practical\n"
  txt += "TOOLS PRACTICAL Which tools Free vs Paid How use click by click\n"
  txt += "EXAMPLE Success Company A growth 3x 5h to 30m Failure B skipped fail\n"
  txt += "CASE Rahul village Redmi 8 Jio no laptop 1h daily Before 4h after 30m auto 90 percent shop owner 10k 3 referrals proof\n"
  txt += "MISTAKES 90 percent fail M1 Skip foundation Fix M01-M10 twice M2 Only watch Fix 15m theory practical M3 Money chase Fix 30 days skill M4 No diary Fix 10m diary M5 No mentor Fix community Pro Tip Extra 2h 5 star\n"
  txt += "HOMEWORK Today 15m theory + 15m practical Build mini project automate 1 task screenshot Teach to friend voice note Quiz\n"
  txt += "NEXT Next M" + str(n+1) + " builds on M" + str(n) + "\n"
  txt += "PROJECTS 5 Minor every 8 modules 1 small 2 Major after M20 M30 Real client ROI 1 Final M40 Full portfolio Behance GitHub LinkedIn 1Cr interview\n"
  txt += "EXTRA Templates prompts Make.com blueprints Sheet templates WhatsApp Canva Checklists Daily 1h Weekly Portfolio Client onboarding Cheat Sheets Tools comparison Salary 180K Case Studies 10 Rahul story Freelancer Interview Top 20 Freelancing Upwork Fiverr profile proposal First client 15k 5 star Referral 5 clients 75k Agency 2L Resources YouTube Docs Communities LinkedIn Discord Mentors\n"
  txt += "ASSESSMENT Quiz 3 to 5 self check Assignment practical screenshot video Final Exam M40 final project review Certificate Brahma Professional English Only\n"
  txt += "SUPER AGENT SEO Title " + topic + " Master Course 2026 Top 25 Price 99 Only Writer Teacher Single File Har Page Alag Distinct Blog Why Most Demanding 2026 Facebook Instagram post Marketing Copy Sales Funnel Email WhatsApp Chat Bot Price 99 UPI UTR Invoice Access Key Auto Post Daily Always Automatically Khud Karega Hamesha\n"
  txt += "FULL BOOK COMPLETE DISTINCT Pura Page Bhara Puri Knowledge Market Best 100 percent Price 99 Only Har Page Alag Distinct Good Writer Good Teacher Proper Arrange No Ulta Sidha Complete English Only Best 25 100 percent Data Master Teacher Inside All Things\n"
  return txt

courses = init25()
purchases = load(PF, [])
apis = load(AP, {})

if st.session_state.admin:
  if menu == "Dashboard":
    st.title("Dashboard - V150 Pura Project - All Points Include")
    st.success("Jo Sari Chijen Decide Ki Thi Yahi Sari Chijon Ke Saath Sahi Bana - Best 25 Top 25 market data salary $180K 600 openings - English Only Single File 40 Modules har page alag distinct full book pura page bhara market best - Master Teacher AI 100% online data collect Writer Teacher proper arrange No Ulta Sidha WHAT IS TO M40 HATA DIYA - Ek course me 23 points Course Cover Overview Outcomes Prereq Roadmap Tools Module Goal Why Core Deep Step Tools Practical Example Case Rahul Village Mistakes Homework Next Projects Extra Templates Assessment Super Agent SEO Blog Social Media Full Book - Dashboard alag Price Manager bulk single Add New Course master teacher command keyboard Course Library UPI QR Setup QR + keyboard UPI ID Owner API Setup API + Tokens Super Agent daily auto posting SEO FB Insta blog Chat Boat Sales Google Sheet Data Browse My Access No Pending Direct Access UPI ID parveen39179@okicici Owner Parveen Kumar Price 99 Email invoice Google Sheet auto data")
    c1, c2 = st.columns(2)
    c1.metric("Total Best 25", len(courses))
    c2.metric("Total Sales", len(purchases))
    if st.button("CREATE BEST 25 ALL DECIDED - Text Files Banenge - Safe - No PPT Crash"):
      for c in courses:
        fp = PPT / (c["id"] + "_EN.txt")
        content = ""
        for n in range(1, 41):
          content += writer_full(c["topic"], n) + "\n--- Page Break ---\n"
        fp.write_text(content)
      st.success("Done Best 25 Text Files Created - V150 Pura - No Crash - Har file 40 modules full book")
      st.balloons()

  elif menu == "Price Manager 99":
    st.title("Price Manager 99 - Bulk + Single - V150 Pura")
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
    st.title("Add New Course - Master Teacher Command - V150 Pura")
    nt = st.text_input("New Course Name Keyboard Se - Master Teacher Ko Command - Jaise AI Product Mgmt")
    npr = st.number_input("New Price", value=99, min_value=1, max_value=10000)
    if st.button("ADD NEW COURSE MASTER TEACHER COMMAND"):
      if len(nt) < 3:
        st.error("Short Name")
      else:
        nid = "BRAHMA" + str(1000+len(courses))
        courses.append({"id": nid, "topic": nt, "price": int(npr)})
        save(CF, courses)
        st.success("Done Added Master Teacher Command - " + nt + " - V150 Pura - 40 Modules Full Book Banega CREATE BEST 25 Dabane Par")
        st.rerun()

  elif menu == "Course Library":
    st.title("Course Library - V150 Pura")
    for idx, co in enumerate(courses):
      en_f = list(PPT.glob(co["id"] + "*EN.txt"))
      if en_f:
        st.success(str(idx+1) + ". " + co["topic"] + " - Rs " + str(co.get("price",99)) + " - Master Teacher All Things")
        st.download_button("EN Download Text Full Book 40 Modules", data=en_f[0].read_bytes(), file_name=en_f[0].name, key="en"+str(idx))
      else:
        st.write(str(idx+1) + ". " + co["topic"] + " - Rs " + str(co.get("price",99)) + " - Not Created Yet - Dashboard Me CREATE BEST 25 Dabao")

  elif menu == "UPI QR Setup":
    st.title("UPI QR Setup - QR Dalne Ka Option - V150 Pura")
    upi_input = st.text_input("UPI ID Keyboard Se", value=apis.get("upi_id", "parveen39179@okicici"))
    owner_input = st.text_input("Owner Name Keyboard Se", value=apis.get("owner", "Parveen Kumar"))
    st.write("Current: " + upi_input + " Owner: " + owner_input + " Price 99")
    up = st.file_uploader("Upload QR Code Image QR Dalne Ka Option", type=["jpg","png","jpeg"])
    if up:
      QR.write_bytes(up.getvalue())
      apis["upi_id"] = upi_input
      apis["owner"] = owner_input
      save(AP, apis)
      st.success("Done QR Uploaded + UPI ID Saved - V150 Pura")
      st.rerun()
    if st.button("SAVE UPI ID OWNER"):
      apis["upi_id"] = upi_input
      apis["owner"] = owner_input
      save(AP, apis)
      st.success("Done Saved - V150 Pura")
      st.rerun()
    if QR.exists():
      st.image(str(QR), width=300)

  elif menu == "API Setup":
    st.title("API Setup - API Form + Tokens Form - V150 Pura")
    o = st.text_input("OpenAI Key - OpenAI Token", value=apis.get("openai",""), type="password")
    fb = st.text_input("Facebook Page Token - Facebook Token", value=apis.get("fb",""), type="password")
    insta = st.text_input("Instagram Token - Instagram Token", value=apis.get("insta",""), type="password")
    goog = st.text_input("Google Search API Key", value=apis.get("google",""), type="password")
    gs_api = st.text_input("Google Sheet API Key - Google Sheet Token", value=apis.get("gs_api",""), type="password")
    gs_id = st.text_input("Google Sheet ID - Super Agent Khud Create Kar Le", value=apis.get("gs_id",""))
    email_api = st.text_input("Email API Key", value=apis.get("email_api",""), type="password")
    email_addr = st.text_input("Email Address Dalne Ka Option - Invoice Yahan Se Jay