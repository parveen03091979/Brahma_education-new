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
  a = "ENGLISH ONLY " + topic + " M" + str(n) + " Master Teacher All Decided\n"
  b = "COURSE COVER " + topic + " Price 99 Master Teacher 40 Modules Single File 100 percent Data Har Page Alag Distinct Market Best\n"
  c = "OVERVIEW What is " + topic + " Future Market $180K-$320K 600 openings 2026 Most Demanding Top 25\n"
  d = "LEARNING OUTCOMES 10 define " + topic + " explain to 5 real persons build 1 project save 2h daily tools list clients handling earn money portfolio final exam certificate\n"
  e = "PREREQUISITES Phone internet 1h daily No laptop No degree Needed Village Student Redmi 8 Jio Rahul Example 1h daily 2L per month Possible\n"
  f = "ROADMAP Month1-2 foundation " + topic + " Month3 portfolio building Month4 5 clients 75k per month Month6 agency 2L per month Next M" + str(n+1) + " builds on M" + str(n) + "\n"
  g = "TOOLS LIST ChatGPT OpenAI Make.com n8n Google Sheet WhatsApp API Canva Free vs Paid Tools Comparison\n"
  h = "MODULE TITLE M" + str(n) + " " + topic + " Master Teacher ENGLISH ONLY Writer Teacher Price 99 No Ulta Sidha Proper Arrange Good Writer Good Teacher\n"
  i = "GOAL After M" + str(n) + " in " + topic + " student can explain to 5 persons with real example with proof\n"
  j = "WHY IMPORTANT Salary 56 percent premium $180K Without " + topic + " fail With " + topic + " salary 3x $50 per hour Top 25 Most Demanding 2026 Future Proof\n"
  k = "CORE CONCEPT " + topic + " simple Perceive Reason Act Engine Example Car Engine Petrol Air Move Same AI WhatsApp check think reply auto\n"
  l = "DEEP DIVE Definition Types How " + topic + " works Input Output Frontend Backend API When use When not use Difference\n"
  m = "STEP BY STEP 5 STEPS Choose 1 task in " + topic + " Open ChatGPT prompt You are " + topic + " expert 10 years experience Connect Make.com n8n Test Diary Maintain 15m theory + 15m practical daily\n"
  n2 = "TOOLS PRACTICAL Which tools for " + topic + " Free vs Paid How to use click by click 15m each tool practical demo\n"
  o = "REAL EXAMPLES Success Company A used " + topic + " growth 3x time 5h to 30m Failure Company B skipped " + topic + " fail loss Note why fail why success\n"
  p = "CASE STUDY Rahul Village Redmi 8 Jio No Laptop 1h Daily " + topic + " Before Manual 4h daily After Auto 30m daily Auto 90 percent Shop Owner Client 10k per month 3 referrals proof screenshot\n"
  q = "MISTAKES PRO TIPS 90 percent fail in " + topic + " M1 Skip foundation Fix M01-M10 twice M2 Only watch no practical Fix 15m theory + 15m practical M3 Money chase Fix 30 days skill build M4 No diary Fix 10m daily diary M5 No mentor Fix community join Pro Tip Extra value give 2h extra work 5 star rating shortcut 6 months journey\n"
  r = "HOMEWORK QUIZ Today 15m theory + 15m practical Build mini project in " + topic + " automate 1 daily task screenshot proof Teach " + topic + " to 1 friend voice note 2m Quiz 3 questions What is " + topic + " When use Which tools\n"
  s = "NEXT STEPS Next M" + str(n+1) + " builds on M" + str(n) + " Previous M" + str(n-1) + " Revision Previous Homework\n"
  t2 = "PROJECTS 5 Minor every 8 modules 1 small project in " + topic + " 2 Major after M20 M30 Real client work with ROI proof 1 Final M40 Full portfolio Problem Identify Plan Build Test Result 10x Portfolio Behance GitHub LinkedIn This is 1Cr interview portfolio\n"
  u = "EXTRA TEMPLATES prompts ChatGPT prompts Make.com blueprints Google Sheet templates WhatsApp templates Canva templates Checklists Daily 1h routine Weekly portfolio checklist Client onboarding template Cheat Sheets Tools comparison Free Paid Pricing Salary $180K Case Studies 10 Rahul story Shop owner Ecom owner YouTuber Freelancer Interview Q Top 20 Freelancing Upwork Fiverr profile proposal template 20 proposals 19 reject 1 accept First client 15k 5 star Referral 5 clients 75k Agency 2L Resources YouTube Docs Communities LinkedIn Discord Mentors list\n"
  v = "ASSESSMENT CERTIFICATION Quiz 3 to 5 questions self check Assignment practical screenshot video proof Final Exam M40 final project review by Master Teacher Certificate Brahma Professional English Only Price 99 Only\n"
  w = "SUPER AGENT SEO BLOG SOCIAL MEDIA SEO Title " + topic + " Master Course 2026 Top 25 Demanding Price 99 Only Writer Teacher English Only Single File 100 percent Data Har Page Alag Distinct Blog Why " + topic + " is Most Demanding 2026 Market Data $180K 600 openings Facebook Post Instagram Post Reels Stories Marketing Copy Sales Funnel Email WhatsApp Chat Bot Script Price 99 UPI UTR Invoice Access Key Auto Post with API Daily Posting Always Automatically Khud Karega Hamesha\n"
  x = "FULL BOOK COMPLETE DISTINCT Pura Page Bhara Puri Knowledge Market Best 100 percent Price 99 Only Har Page Alag Distinct Good Writer Good Teacher Proper Arrange No Ulta Sidha 7 Points Structure Complete English Only Best 25 100 percent Data Master Teacher Inside All Things Decided For One Course\n"