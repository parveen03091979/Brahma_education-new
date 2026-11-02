import streamlit as st, json, hashlib, datetime
from pathlib import Path

DATA=Path("data")
DATA.mkdir(exist_ok=True)
PPT=DATA/"ppts"
PPT.mkdir(exist_ok=True)
CF=DATA/"courses.json"
PF=DATA/"purchases.json"
MH=DATA/".master_hash"
AS=DATA/".admin_session"

UID="parveen39179@okicici"
OWNER="Parveen Kumar"

TOP25=["AI Product Management","AI Project Management","Gen AI Prompt","AI Agents","AI Eng LLM","ML MLOps","AI Strategy","LLM RAG","AI Auto n8n","Data Science","Data Analytics","Data Eng","CyberSec","Cloud AWS","DevOps","FullStack MERN","Python FullStack","Digital Mkt","SEO Mastery","FinTech","Blockchain","NoCode","Chatbot","SaaS","Ecom Shopify"]

def load(p,d):
  try:
    return json.loads(p.read_text())
  except:
    return d

def save(p,d):
  p.write_text(json.dumps(d,indent=2))

def init25():
  d=[]
  for i,name in enumerate(TOP25):
    d.append({"id":"BRAHMA"+str(1000+i),"topic":name,"price":99})
  save(CF,d)
  return d

def master_content(topic,n):
  txt=""
  txt+="COURSE COVER "+topic+" Price 99 Master Teacher 40 Modules Single File 100 percent Data Har Page Alag Distinct Market Best English Only No M Point\n"
  txt+="OVERVIEW What is "+topic+" Future Market $180K 600 openings 2026 Most Demanding Top 25 Final Me Se Ek\n"
  txt+="OUTCOMES 10 define "+topic+" explain to 5 build 1 project save 2h tools clients earn portfolio final\n"
  txt+="PREREQUISITES Phone internet 1h daily No laptop Village Redmi 8 Jio Rahul 1h daily 2L possible\n"
  txt+="ROADMAP Month1-2 foundation Month3 portfolio Month4 5 clients 75k Month6 agency 2L Next Module builds on previous\n"
  txt+="TOOLS LIST ChatGPT Make.com n8n Sheet WhatsApp API Canva Free vs Paid\n"
  txt+="MODULE TITLE Module "+str(n)+" "+topic+" Master Teacher ENGLISH ONLY Writer Teacher Price 99 No Ulta Sidha Proper Arrange\n"
  txt+="GOAL After Module "+str(n)+" in "+topic+" student can explain to 5 persons with real example with proof\n"
  txt+="WHY IMPORTANT Salary 56 percent premium $180K Without "+topic+" fail With salary