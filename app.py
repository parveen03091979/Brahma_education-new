import streamlit as st
import json
import secrets
import datetime
import urllib.parse
from pathlib import Path

st.set_page_config(page_title="Brahma AI", layout="wide")

try:
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
    try:
      p.write_text(json.dumps(d, indent=2))
    except Exception as e:
      st.error("Save Error: " + str(e))

  TOP25 = ["AI Product Mgmt","AI Project Mgmt","Gen AI Prompt","AI Agents","AI Eng LLM","ML MLOps","AI Strategy","LLM RAG","AI Auto n8n","Data Science","Data Analytics","Data Eng","CyberSec","Cloud AWS","DevOps","FullStack MERN","Python FullStack","Digital Mkt","SEO","FinTech","Blockchain","NoCode","Chatbot","SaaS","Ecom Shopify"]

  def writer(topic, n):
    try:
      txt = "ENGLISH ONLY " + topic + " M" + str(n) + " Master Teacher All Decided\n"
      txt += "COURSE COVER " + topic + " Price 99 Master Teacher 40 Modules Single File 100 percent Data Har Page Alag Distinct Market Best\n"
      txt += "OVERVIEW What is " + topic + " Future Market $180K-$320K 600 openings 2026 Most Demanding Top 25\n"
      txt += "OUTCOMES 10 define explain build save tools clients earn portfolio final\n"
      txt += "PREREQ Phone internet 1h daily No laptop Village Redmi 8 Jio Rahul 1h daily 2L\n"
      txt += "ROADMAP Month1-2 foundation Month3 portfolio Month4 5 clients 75k Month6 agency 2L Next M" + str(n+1) + "\n"
      txt += "TOOLS ChatGPT Make.com n8n Sheet WhatsApp API Canva Free vs Paid\n"
      txt += "MODULE M" + str(n) + " " + topic + " Master Teacher Price 99 No Ulta Sidha Proper Arrange\n"
      txt += "GOAL After M" + str(n) + " explain to 5 real example proof\n"
      txt += "WHY Salary 56 percent premium 180K With " + topic + " salary 3x Top 2026\n"
      txt += "CORE Perceive Reason Act Engine car WhatsApp check think reply auto\n"
      txt += "DEEP Definition Types How works Input Output Frontend Backend API When use when not\n"
      txt += "STEP 5 STEPS Choose task Open ChatGPT prompt You are expert Connect Make.com Test Diary 15m theory + 15m practical\n"
      txt += "TOOLS PRACTICAL Which tools Free vs Paid How use click by click\n"
      txt += "EXAMPLE Success Company A growth 3x 5h to 30m Failure B skipped fail\n"
      txt += "CASE Rahul village Redmi 8 Jio no laptop 1h daily Before 4h after 30m auto 90 percent shop owner 10k 3 referrals proof\n"
      txt += "MISTAKES 90 percent fail M1 Skip foundation Fix M01-M10 twice M2 Only