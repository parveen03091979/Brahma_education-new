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
AP = DATA / "apis.json"

UID_DEFAULT = "parveen39179@okicici"
OWNER_DEFAULT = "Parveen Kumar"

def load(p, d):
  try:
    return json.loads(p.read_text())
  except:
    return d

def save(p, d):
  p.write_text(json.dumps(d, indent=2))

TOP25 = ["AI Product Mgmt","AI Project Mgmt","Gen AI Prompt","AI Agents","AI Eng LLM","ML MLOps","AI Strategy","LLM RAG","AI Auto n8n","Data Science","Data Analytics","Data Eng","CyberSec","Cloud AWS","DevOps","FullStack MERN","Python FullStack","Digital Mkt","SEO","FinTech","Blockchain","NoCode","Chatbot","SaaS","Ecom Shopify"]

def writer(topic, n):
  txt = "ENGLISH ONLY " + topic + " M" + str(n) + " Master Teacher All Decided\n"
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
    tb =