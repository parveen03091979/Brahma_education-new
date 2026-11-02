import os, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
import streamlit as st
from pptx import Presentation
from pptx.util import Inches, Pt

st.set_page_config(page_title="Brahma Education V100", page_icon="🎓", layout="wide")

DATA = Path("data")
PPT_DIR = DATA / "ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

CF = DATA / "courses.json"
PF = DATA / "purchases.json"
MF = DATA / "marketing.json"
AF = DATA / "api_keys.json"
QF = DATA / "upi_qr.jpg"
MH = DATA / ".master_hash"
AS = DATA / ".admin_session"

UID = "parveen39179@okicici"
OWNER = "Parveen Kumar"

RAW_TOPICS = [
"AI Agent Automation","Instagram Reels Mastery","YouTube Automation","Prompt Engineering",
"Digital Marketing SEO","ChatGPT Mastery","Facebook Ads","Google Ads","SEO Advanced",
"Social Media Marketing","Content Writing AI","Copywriting","Blogging","Affiliate Marketing",
"Dropshipping","E-commerce Shopify","Canva Design","Video Editing CapCut","YouTube SEO",
"Instagram Growth","LinkedIn Marketing","Twitter X Growth","TikTok Viral","Pinterest",
"Quora","Email Marketing Automation","WhatsApp Marketing","Telegram Growth","Influencer Marketing",
"Personal Branding","Freelancing Mastery","Agency Business","SaaS Business","No-Code Bubble",
"Python","JavaScript","React","Next.js","Node.js","Full Stack Web Dev","WordPress",
"Shopify Store","UI UX Design","Figma","Graphic Design","Logo Design","Thumbnail Design Viral",
"Video Animation","AI Image Midjourney","AI Video Sora","Voice Cloning ElevenLabs",
"Automation n8n Make","Zapier","Notion","Excel Advanced","Google Sheets Automation",
"Data Analysis Python","Machine Learning","Deep Learning","Data Science","Stock Trading AI",
"Crypto Trading","Forex Trading","Real Estate Business","Motivational Speaking","Public Speaking",
"Communication Skills","English Speaking","Podcast Mastery","Music Production AI","Photography",
"Reels Editing Viral","Meme Marketing","Viral Content Formula","Lead Generation","Sales Funnel",
"Landing Page Design","CRO","Customer Support Automation","HR Recruitment AI","Business Plan Mastery",
"Startup Funding","Business Automation AI","Time Management","Mindset Millionaire","Meditation",
"Fitness Coaching Business","Diet Nutrition Business","Yoga Teaching Business","Cooking Channel Business",
"Travel Vlogging Business","Gaming Channel Growth","Education Channel Growth","Finance Channel Business",
"News Channel Automation","Meme Page Business","Affiliate Blog SEO","Amazon FBA","Etsy Store",
"Print on Demand","Stock Photography Business","Voice Over Business","Translation Business AI",
"Resume Writing Business","LinkedIn Profile Optimization","AI Tools Mastery","Chatbot Development",
"AI Voice Agent","AI Receptionist Business"
]

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

def init_courses():
    data=load(CF,[])
    if not isinstance(data,list):
        data=[]
    exist={c.get("topic","").strip().lower() for c in data if isinstance(c,dict)}
    for i,topic in enumerate(RAW_TOPICS):
        if topic.lower() not in exist:
            data.append({"id":"BRAHMA"+str(1000+i),"topic":topic,"price":99})
    for c in data:
        try:
            pr=int(c.get("price",999))
            if pr>200 or pr<1:
                pr=99
            c["price"]=pr
        except:
            c["price"]=99
    save(CF,data)
    return data

courses=init_courses()
purchases=load(PF,[])
api_keys=load(AF,{})

MODS=["WHAT IS","WHY IMPORTANT","WHERE USE","WHEN TO USE","WHO ELIGIBLE","HOW ARCH","TOOLS REQUIRED","EARNING","PRACTICAL USE","RIGHT WAY","FOUNDATION","CORE CONCEPT","ADVANCED","STEP BY STEP","BUSINESS EXAMPLE","CLIENT REQ","REAL STORY","PLANNING","IMPLEMENTATION","MISTAKES","PRO TIP","EXPERT","TOOLS COMPARE","FREE VS PAID","PORTFOLIO","CLIENT FINDING","FREELANCING","AGENCY","BUSINESS MODEL","SCALING","SEO MARKETING","LEAD GEN","SALES","AUTOMATION","OPTIMIZATION","CASE STUDY","DAILY PRACTICE","HOMEWORK","REVISION","FINAL PROJECT"]

def mod_content(topic,num):
    title=MODS[num-1]
    base="COURSE TOPIC: "+topic+". MODULE: "+title+". This lesson explains importance in professional and business applications. Understand main concepts, tools, processes and practical implementation. Start with foundation and move to professional level. "
    extra=""
    if num==17:
        extra="REAL STORY: Rahul from village with basic phone studied daily, built portfolio, approached clients, faced rejections, improved proposals, completed first project with consistent practice. "
    if num==20:
        extra="FIVE MISTAKES: Skipping foundation, watching without practicing, chasing money before learning, not maintaining diary and avoiding feedback. Avoid these with weekly plan. "
    if num==21:
        extra="PRO TIP: Write four things diary nightly: what learned, what mistake, what improve tomorrow, one new idea. Review Sunday. "
    return base+extra+base

def make_ppt(course):
    cid=course["id"]
    topic=course["topic"]
    out=PPT_DIR/(cid+"_40_MODULES_V100.pptx")
    prs=Presentation()
    prs.slide_width=Inches(13.33)
    prs.slide_height=Inches(7.5)
    for n in range(1,41):
        slide=prs.slides.add_slide(prs.slide_layouts[6])
       