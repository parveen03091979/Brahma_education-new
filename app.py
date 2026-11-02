import streamlit as st, json, secrets, datetime, urllib.parse
from pathlib import Path
st.set_page_config(page_title="Brahma AI", layout="wide")
DATA=Path("data")
PPT_DIR=DATA/"ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)
CF=DATA/"courses.json"
PF=DATA/"purchases.json"
MH=DATA/".hash"
AS=DATA/".sess"
UID="parveen39179@okicici"
OWNER="Parveen Kumar"
def load(p,d):
 try:
  return json.loads(p.read_text())
 except:
  return d
def save(p,d):
 p.write_text(json.dumps(d,indent=2))
TOP25=["AI Product Mgmt","AI Project Mgmt","Gen AI Prompt","AI Agents","AI Eng LLM","ML MLOps","AI Strategy","LLM RAG","AI Auto n8n","Data Science","Data Analytics","Data Eng","CyberSec","Cloud AWS","DevOps","FullStack MERN","Python FullStack","Digital Mkt","SEO","FinTech","Blockchain","NoCode","Chatbot","SaaS","Ecom Shopify"]
MODS=["WHAT IS","WHY IMP","WHERE USE","WHEN USE","WHO LEARN","HOW WORKS","TOOLS","EARN MONEY","PRACTICAL","RIGHT WAY","FOUNDATION","CORE","ADVANCED","STEP PROCESS","EXAMPLE","CLIENT REQ","REAL STORY","PLANNING","IMPLEMENT","MISTAKES","PRO TIP","EXPERT","COMPARE","FREE PAID","PORTFOLIO","FIND CLIENT","FREELANCING","AGENCY","MODEL","SCALING","SEO","LEAD","SALES","AUTO","OPTIMIZE","CASE STUDY","DAILY","HOMEWORK","REVISION","FINAL PROJECT"]
def writer(topic,n):
 t=MODS[n-1]
 nxt=MODS[n] if n<40 else "COMPLETE"
 s=""
 s=s+"ENGLISH ONLY SINGLE FILE 100 PERCENT DATA "+topic+" M"+str(n)+" "+t+"\n"
 s=s+"COVER "+topic+" Tagline Most Demanding 2026 Price 99 Master Teacher 40 Modules\n"
 s=s+"OVERVIEW What is "+topic+" "+t+" Who for What learn Future 180K to 320K 600 openings 300 percent growth\n"
 s=s+"OUTCOMES 10 After M"+str(n)+" define "+t+" explain to 5 build project save 2h use tools find clients earn 50 per hour portfolio avoid mistakes final project\n"
 s=s+"PREREQ Phone internet 1h daily No laptop No degree 10th fail village Redmi 8 Jio 1GB Rahul 1h daily 2L\n"
 s=s+"ROADMAP Month1-2 foundation M01-M10 "+t+" Month3 portfolio 3 projects Month4 5 clients 75k Month6 agency 2L Next "+nxt+"\n"
 s=s+"TOOLS ChatGPT Make.com n8n Sheet WhatsApp API Canva Loom Free vs Paid\n"
 s=s+"MODULE M"+str(n)+" "+topic+" - "+t+" - ENGLISH ONLY - Writer Teacher Style - Price 99 - No Ulta Sidha\n"
 s=s+"GOAL After this you can "+t+" in "+topic+" explain to 5 real example\n"
 s=s+"WHY IMPORTANT Salary 56 percent premium 180K to 320K Without "+t+" fail With "+t+" salary 3x 50 per hour 80 percent save Top demanding 2026\n"
 s=s+"CORE CONCEPT "+t+" simple Perceive Reason Act Engine car WhatsApp check think reply\n"
 s=s+"DEEP DIVE Definition Types How "+t+" works Architecture Input Output Frontend Backend API When use when not\n"
 s=s+"STEP BY STEP 5 STEPS Choose task "+topic+" "+t+" Open ChatGPT prompt You are "+t+" expert Connect Make.com Test second account Diary 15m theory practical\n"
 s=s+"TOOLS PRACTICAL Which tools "+t+" "+topic+" Free vs Paid How use click by click 15m explore each\n"
 s=s+"REAL EXAMPLES Success Company A used "+t+" "+topic+" growth 3x 5h to 30m Failure Company B skipped fail Note why\n"
 s=s+"CASE STUDY Rahul village Redmi 8 Jio 1GB no laptop 1h daily "+topic+" "+t+" Before 4h manual after 30m auto 90 percent auto shop owner paid 10k monthly 3 referrals proof\n"
 s=s+"MISTAKES PRO TIPS 90 percent fail "+t+" "+topic+" M1 Skip foundation Fix M01-M10 twice M2 Only watch Fix 15m theory practical daily M3 Money chase Fix 30 days skill only M4 No diary Fix 10m diary 4 points M5 No mentor Fix community daily doubt Pro Tip Extra value 2h extra 5 star shortcut save 6 months\n"
 s=s+"PRACTICAL HOMEWORK QUIZ Today 15m theory plus 15m practical Build mini project "+t+" "+topic+" automate 1 task screenshot Teach "+t+" "+topic+" to friend voice note 2m Quiz What is "+t+" When use Tools\n"
 s=s+"NEXT STEPS Next "+nxt+" builds on "+t+" Link next module Previous M"+str(n-1)+" Next "+nxt+"\n"
 s=s+"PROJECTS 5 Minor every 8 modules 1 small project "+t+" "+topic+" 2 Major after M20 M30 Real client Before After ROI 1 Final M40 Full portfolio Problem choose Plan workflow Build Test 10x Result screenshot Portfolio upload Behance GitHub LinkedIn 1Cr roadmap This is interview\n"
 s=s+"EXTRA Templates prompts Make.com blueprints Sheet templates WhatsApp API Canva Checklists Daily 1h Weekly Portfolio Client onboarding Cheat Sheets Tools comparison Free vs Paid Pricing Salary 180K to 320K Case Studies 10 Rahul story Shop owner Ecom YouTuber Freelancer Interview Q and A Top 20 Answer Freelancing Upwork Fiverr profile proposal 20 proposals 19 reject First client 15k 5 star Referral 5 clients 75k Agency 2L Resources YouTube Docs Communities LinkedIn Discord Mentors\n"
 s=s+"ASSESSMENT Quiz 3 to 5 self check Assignment practical screenshot video submit Final Exam M40 final project review Certificate Brahma Professional English Only\n"
 s=s+"SUPER AGENT SEO Title "+topic+" "+t+" Master Course 2026 Top 25 Demanding Price 