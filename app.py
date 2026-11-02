import streamlit as st, json, secrets, datetime, urllib.parse
from pathlib import Path
st.set_page_config(page_title='Brahma AI', layout='wide')
DATA=Path('data')
PPT_DIR=DATA/'ppts'
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)
CF=DATA/'courses.json'
PF=DATA/'purchases.json'
MH=DATA/'.hash'
AS=DATA/'.sess'
UID='parveen39179@okicici'
OWNER='Parveen Kumar'
def load(p,d):
 try:
  return json.loads(p.read_text())
 except:
  return d
def save(p,d):
 p.write_text(json.dumps(d,indent=2))
# BEST 25 DEMANDING 2026 ENGLISH ONLY
TOP25=['AI Product Mgmt','AI Project Mgmt','Gen AI Prompt','AI Agents','AI Eng LLM','ML MLOps','AI Strategy','LLM RAG','AI Auto n8n','Data Science','Data Analytics','Data Eng','CyberSec','Cloud AWS','DevOps','FullStack MERN','Python FullStack','Digital Mkt','SEO','FinTech','Blockchain','NoCode','Chatbot','SaaS','Ecom Shopify']
MODS=['WHAT IS','WHY IMP','WHERE USE','WHEN USE','WHO LEARN','HOW WORKS','TOOLS','EARN MONEY','PRACTICAL','RIGHT WAY','FOUNDATION','CORE','ADVANCED','STEP PROCESS','EXAMPLE','CLIENT REQ','REAL STORY','PLANNING','IMPLEMENT','MISTAKES','PRO TIP','EXPERT','COMPARE','FREE PAID','PORTFOLIO','FIND CLIENT','FREELANCING','AGENCY','MODEL','SCALING','SEO','LEAD','SALES','AUTO','OPTIMIZE','CASE STUDY','DAILY','HOMEWORK','REVISION','FINAL PROJECT']
def writer(topic,n):
 t=MODS[n-1]
 nxt=MODS[n] if n<40 else 'COMPLETE'
 return (
 f'ENGLISH ONLY SINGLE FILE 100% DATA {topic} M{n:02d} {t}\n'
 f'COVER {topic} Tagline Most Demanding 2026 Price 99 Master Teacher 40 Modules\n'
 f'OVERVIEW What is {topic} {t}? Who for? What learn? Future $180K-$320K 600+ openings 300% growth\n'
 f'OUTCOMES 10 After M{n:02d} define {t} explain to 5 build project save 2h use tools find clients earn $50/hr portfolio avoid mistakes final project\n'
 f'PREREQ Phone internet 1h daily No laptop No degree 10th fail village Redmi 8 Jio 1GB Rahul 1h daily 2L\n'
 f'ROADMAP Month1-2 foundation M01-M10 {t} Month3 portfolio 3 projects Month4 5 clients 75k Month6 agency 2L Next {nxt}\n'
 f'TOOLS ChatGPT Make.com n8n Sheet WhatsApp API Canva Loom Free vs Paid\n'
 f'MODULE M{n:02d} {topic} - {t} - ENGLISH ONLY - Writer Teacher Style - Price 99 - No Ulta Sidha\n'
 f'GOAL After this you can {t} in {topic} explain to 5 real example\n'
 f'WHY IMPORTANT Salary 56% premium $180K-$320K Without {t} fail With {t} salary 3x $50/hr 80% save Top demanding 2026\n'
 f'CORE CONCEPT {t} simple Perceive Reason Act Engine car WhatsApp check think reply\n'
 f'DEEP DIVE Definition Types How {t} works Architecture Input Output Frontend Backend API When use when not\n'
 f'STEP BY STEP 5 STEPS Choose task {topic} {t} Open ChatGPT prompt You are {t} expert Connect Make.com Test second account Diary 15m theory practical