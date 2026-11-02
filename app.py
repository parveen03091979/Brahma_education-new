import streamlit as st, json, hashlib, datetime, urllib.parse
from pathlib import Path
DATA_DIR=Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH=DATA_DIR/".master_hash"
ADMIN_SESSION=DATA_DIR/".admin_session"
COURSES_FILE=DATA_DIR/"courses.json"
PPT_DIR=DATA_DIR/"ppts"
PPT_DIR.mkdir(exist_ok=True)
MARKETING_FILE=DATA_DIR/"marketing.json"
PURCHASE_FILE=DATA_DIR/"purchases.json"
API_FILE=DATA_DIR/"api_keys.json"
UPI_QR_PATH=DATA_DIR/"upi_qr.jpg"
UPI_ID="parveen39179@okicici"
NAME="Parveen Kumar"
TOPICS=["AI Agent Automation","Instagram Reels Mastery","YouTube Automation","Prompt Engineering","Digital Marketing SEO","ChatGPT Mastery","Facebook Ads","Google Ads","SEO Advanced","Social Media Marketing","Content Writing AI","Copywriting Mastery","Blogging Mastery","Affiliate Marketing","Dropshipping","E-commerce Shopify","Canva Design","Video Editing CapCut","YouTube SEO","Instagram Growth","LinkedIn Marketing","Twitter X Growth","TikTok Viral","Pinterest Marketing","Quora Marketing","Email Marketing Automation","WhatsApp Marketing","Telegram Growth","Influencer Marketing","Personal Branding","Freelancing Mastery","Agency Business","SaaS Business","No-Code Bubble","Python Mastery","JavaScript Mastery","React JS","Next.js","Node.js","Web Development Full Stack","WordPress Mastery","Shopify Store Design","UI UX Design","Figma Design","Graphic Design","Logo Design","Thumbnail Design Viral","Video Animation","AI Image Midjourney","AI Video Sora","Voice Cloning ElevenLabs","Automation n8n Make","Zapier Automation","Notion Productivity","Excel Advanced","Google Sheets Automation","Data Analysis Python","Machine Learning","Deep Learning","Data Science","Stock Trading AI","Crypto Trading","Forex Trading","Real Estate Business","Motivational Speaking","Public Speaking","Communication Skills","English Speaking","Podcast Mastery","Music Production AI","Photography Mastery","Reels Editing Viral","Meme Marketing","Viral Content Formula","Lead Generation","Sales Funnel","Landing Page Design","CRO Optimization","Customer Support Automation","HR Recruitment AI","Business Plan Mastery","Startup Funding","Business Automation AI","Time Management","Mindset Millionaire","Meditation Mindfulness","Fitness Coaching Business","Diet Nutrition Business","Yoga Teaching Business","Cooking Channel Business","Travel Vlogging Business","Gaming Channel Growth","Education Channel Growth","Finance Channel Business","News Channel Automation","Meme Page Business","Affiliate Blog SEO","Amazon FBA Mastery","Etsy Store Mastery","Print on Demand Business","Stock Photography Business","Voice Over Business","Translation Business AI","Resume Writing Business","LinkedIn Profile Optimization","AI Tools Mastery","Chatbot Development","AI Voice Agent","AI Receptionist Business"]

def load(p,d):
    try:
        if p.exists():
            t=p.read_text(encoding="utf-8")
            if len(t)>2:
                return json.loads(t)
    except:
        pass
    return d
def save(p,d):
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")

class MT:
    def ttl(self,t,n):
        return f"M{str(n).zfill(2)} {t} Module {n}"
    def cnt(self,t,n):
        intro=["WHAT IS definition 5 examples business automation 80 percent time save Upwork 15k Fiverr 20k agency 2L SaaS recurring scope 2026 300 percent growth roadmap 30 days foundation strong first month 15k deep detail English only. ","WHY IMPORTANT future proof market data 2026 demand high salary 3x AI era job safe freelancing high business 90 percent fail reasons foundation skip no practice no diary no mentor Rahul village proof 15k to 2L future value 10x. ","WHERE USE Instagram Reels YouTube Shorts business automation job promotion freelancing agency startup clients Upwork Fiverr LinkedIn Instagram DM Facebook groups India global village mobile e-commerce education real estate. ","WHEN best timing morning 6 to 8 brain fresh Monday Thursday posting 40 percent high Diwali New Year seasonal product launch scale 3 clients stable retainer pricing every 3 clients 20 percent increase time management daily 1 hour job. ","WHO eligible student 16 plus professional job business owner 60 years no degree daily 30 minutes motivation who cannot no practice only video age gender location not matter. ","HOW architecture Perceive Reason Act loop ReAct Chain Thought RAG memory prompt engineering Perceive input understand Reason best approach Act tool use loop Observe Repeat reel example. ","WITH WHAT tools free Canva CapCut ChatGPT Notion Google Sheets paid ElevenLabs n8n Make Zapier free self host 1000 ops 100 tasks setup step by step free vs paid beginner 0 cost pro 20 dollar installation. ","WHAT USE earning freelancing Upwork Fiverr 20k to 50k first month 3 month 1L business agency 2L plus 5 clients SaaS 29 dollar monthly 100 customers 2.4L recurring job promotion 40 percent e-commerce automate pricing 15k 35k 75k proof. ","HOW TO USE practical mobile reels InShot CapCut Canva mobile ChatGPT app script laptop browser dashboard automation hands on Step1 topic Step2 script ChatGPT Step3 design Canva Step4 video CapCut Step5 scheduling no laptop mobile 100 percent 30 min daily. ","HOW TO DO right way daily 30 min diary 15 learning 15 practical weekly revise Sunday best practice daily 1 project 10 min diary not only video one day 5 hours then 5 days nothing consistency 30 days challenge motivation right way. "]
        ex=""
        if n==17:
            ex="REAL STORY Rahul village phone old Redmi 8 internet Jio 1GB no laptop village people farming Rahul Master Teacher course 2 months daily 1 hour night 9 to 10 diary Third month Upwork 20 proposals 19 reject 1 USA client 2 days complete 15k 5 star Fourth month 5 clients 75k 6th month agency 2 friends Today 2 lakh house built parents happy. "
        if n==20:
            ex="MISTAKES 90 percent fail Mistake1 no foundation advanced skip Mistake2 no practice only video Mistake3 behind money no learning Mistake4 no diary forget Mistake5 no mentor alone how to avoid roadmap daily 30 min diary weekly revise. "
        if n==21:
            ex="PRO TIP secret diary night 