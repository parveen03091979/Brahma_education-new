import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
st.set_page_config(page_title="Brahma Top 50 Master", layout="wide")
DATA=Path("data")
PPT_DIR=DATA/"ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)
CF=DATA/"courses.json"
PF=DATA/"purchases.json"
QF=DATA/"upi_qr.jpg"
MH=DATA/".master_hash"
AS=DATA/".admin_session"
UID="parveen39179@okicici"
OWNER="Parveen Kumar"
def load(p,d):
 try:
  if p.exists():
   return json.loads(p.read_text(encoding="utf-8"))
 except:
  pass
 return d
def save(p,d):
 t=p.with_suffix(".tmp")
 t.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
 t.replace(p)
TOP50="AI Product Management Hottest 2026,AI Project Management,Generative AI Prompt Engineering,AI Agents Automation,AI Engineering LLM,Machine Learning MLOps,AI Strategy Consulting,LLM Fine Tuning RAG,AI Automation n8n Make,Data Science Big Data,Data Analytics Power BI,Data Engineering,Cybersecurity Ethical Hacking,Cloud Computing AWS Azure,DevOps Kubernetes,Full Stack MERN,Python Full Stack,Java Full Stack,UI UX Product Design,Digital Marketing Performance,SEO Content Marketing,Social Media Influencer,Video Editing Motion Graphics,Graphic Design Branding,Blockchain Web3,FinTech Analytics,Stock Crypto Trading,Product Management,Project Management PMP,Business Analytics,Robotics Human Robot,Quantum Computing,IoT Embedded,AR VR Metaverse,Game Development Unity,Mobile App Flutter,No Code Low Code,Chatbot Development,SaaS Product Building,Ecommerce Shopify,YouTube Automation,Copywriting Sales Funnel,Resume Interview Skills,Communication Public Speaking,Leadership Management,EV Technology,Renewable Solar Energy,Digital Health Telemedicine,Bioinformatics,Supply Chain Logistics,HR Analytics,Accounting Tally GST".split(",")
def init50():
 d=[]
 for i,name in enumerate(TOP50):
  d.append({"id":f"BRAHMA{1000+i}","topic":name.strip(),"price":99})
 save(CF,d)
 return d
courses=init50()
purchases=load(PF,[])
MODS="WHAT IS,WHY IMPORTANT,WHERE USE,WHEN USE,WHO CAN LEARN,HOW IT WORKS ARCHITECTURE,TOOLS YOU NEED,HOW YOU EARN MONEY,HOW TO USE PRACTICALLY,RIGHT WAY TO LEARN,BEGINNER FOUNDATION,CORE CONCEPTS,ADVANCED CONCEPTS,STEP BY STEP PROCESS,REAL BUSINESS EXAMPLES,CLIENT REQUIREMENTS,REAL STORY OF SUCCESS,PROJECT PLANNING,IMPLEMENTATION,MISTAKES 90 PERCENT FAIL,PRO TIP SECRET,EXPERT STRATEGY,TOOLS COMPARISON,FREE VS PAID,PORTFOLIO BUILDING,HOW TO FIND CLIENTS,FREELANCING START,AGENCY BUSINESS,BUSINESS MODEL,HOW TO SCALE,SEO AND MARKETING,LEAD GENERATION,SALES CLOSING,AUTOMATION SETUP,OPTIMIZATION,CASE STUDY ANALYSIS,DAILY PRACTICE ROUTINE,HOMEWORK TASK,REVISION METHOD,FINAL PROJECT AND NEXT STEPS".split(",")
def master_en(topic,num):
 title=MODS[num-1]
 base=f"COURSE: {topic} | MODULE {num} - {title} | ENGLISH | Master Teacher | Market Best 100 Percent | Price Rs 99\n\n"
 market=""
 if "AI Product" in topic:
  market="MARKET DATA: AI Product Manager hottest role 2026 - 600+ openings - $180K-$320K total comp $400K+ frontier labs - 300% YoY growth - 15-25% premium over normal PM - Only 1 in 8 applicants qualified - Top hirers OpenAI Anthropic Google DeepMind - "
 elif "AI Project" in topic:
  market="MARKET DATA: AI Project Manager $128,091 salary - Most in-demand IT role 2026 - 768 postings - AI skills 56% wage premium - Strong hiring tech healthcare finance - "
 elif "Generative AI" in topic or "Prompt" in topic:
  market="MARKET DATA: Generative AI LLM expertise 57,000 active listings $200K average - AI wage premium 56% - RAG systems top skill 2026 - "
 elif "AI Agent" in topic:
  market="MARKET DATA: AI Agents Automation workflow automation engineers lead demand - AI needs builders data pipelines security infrastructure - "
 if num==1:
  return base+market+f"GOAL: After this module you can explain {topic} to 5 people in simple words with real example.\nWHY IMPORTANT: 2026 me {topic} future proof high salary - Every business needs 80% time save - Job salary 3x - Freelancing $50 per hour.\nCONCEPT: {topic} = Perceive (dekho) + Reason (socho) + Act (karo) - Like you check WhatsApp message think what to reply then type.\nSTEP BY STEP PROCESS - PRACTICAL:\nStep 1: Choose 1 daily boring task in {topic} - Ex Instagram comment reply or lead follow up\nStep 2: Open ChatGPT - Write prompt - You are {topic} expert reply friendly professional\nStep 3: Connect tool - Make.com or n8n - Instagram trigger + ChatGPT action +