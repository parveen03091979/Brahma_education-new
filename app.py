import streamlit as st
import json
import hashlib
import datetime
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Brahma Education", layout="wide")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
ADMIN_SESSION = DATA_DIR / ".admin_session"
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
MARKETING_FILE = DATA_DIR / "marketing.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
PPT_DIR = DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)

TOPICS_TEXT = """AI Agent Automation 2026
Instagram Reels Mastery
YouTube Automation AI
Prompt Engineering Pro
Digital Marketing SEO Mastery
ChatGPT Mastery 2026
Facebook Ads Mastery
Google Ads Mastery
SEO Advanced 2026
Social Media Marketing Pro
Content Writing AI
Copywriting Mastery
Blogging Mastery 2026
Affiliate Marketing Pro
Dropshipping Business
E-commerce Mastery Shopify
Canva Design Mastery
Video Editing CapCut Pro
YouTube SEO Mastery
Instagram Growth Hack
LinkedIn Marketing Pro
Twitter X Growth Mastery
TikTok Viral Mastery
Pinterest Marketing
Quora Marketing
Email Marketing Automation
WhatsApp Marketing Pro
Telegram Channel Growth
Influencer Marketing
Personal Branding Mastery
Freelancing Mastery
Agency Business Mastery
SaaS Business 2026
No-Code Business Bubble
Python Programming Mastery
JavaScript Mastery 2026
React JS Mastery
Next.js Mastery
Node.js Backend Mastery
Web Development Full Stack
WordPress Mastery
Shopify Store Design
UI UX Design Mastery
Figma Design Pro
Graphic Design Mastery
Logo Design Mastery
Thumbnail Design Viral
Video Animation Mastery
AI Image Generation Midjourney
AI Video Generation Sora
Voice Cloning ElevenLabs
Automation n8n Make
Zapier Automation Mastery
Notion Productivity Mastery
Excel Advanced Mastery
Google Sheets Automation
Data Analysis Python
Machine Learning Mastery
Deep Learning 2026
Data Science Mastery
Stock Market Trading AI
Crypto Trading Mastery
Forex Trading Pro
Real Estate Business
Motivational Speaking Mastery
Public Speaking Pro
Communication Skills Mastery
English Speaking Pro
Hindi Content Creation
Podcast Mastery
Music Production AI
Photography Mastery
Reels Editing Viral
Meme Marketing Mastery
Viral Content Formula
Lead Generation Mastery
Sales Funnel Mastery
Landing Page Design
CRO Conversion Optimization
Customer Support Automation
HR Recruitment AI
Business Plan Mastery
Startup Funding Mastery
Business Automation AI
Time Management Mastery
Mindset Mastery Millionaire
Meditation Mindfulness
Fitness Coaching Business
Diet Nutrition Business
Yoga Teaching Business
Cooking Channel Business
Travel Vlogging Business
Gaming Channel Growth
Education Channel Growth
Finance Channel Business
News Channel Automation
Meme Page Business
Affiliate Blog SEO
Amazon FBA Mastery
Etsy Store Mastery
Print on Demand Business
Stock Photography Business
Voice Over Business
Translation Business AI
Resume Writing Business
LinkedIn Profile Optimization
AI Tools Mastery 100 Tools
Chatbot Development
AI Voice Agent Mastery
AI Receptionist Business"""

TOPICS = TOPICS_TEXT.splitlines()

def load_json(path, default):
    if path.exists():
        txt = path.read_text(encoding="utf-8")
        if len(txt) > 2:
            try:
                return json.loads(txt)
            except:
                return default
    return default

def save_json(path, data):
    txt = json.dumps(data, ensure_ascii=False, indent=2)
    path.write_text(txt, encoding="utf-8")

def create_rich_40_pptx(cid, ctopic):
    from pptx import Presentation
    from pptx.util import Inches, Pt
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)
    for m in range(40):
        module_no = m + 1
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        title_box = slide.shapes.add_textbox(Inches(0.4), Inches(0.1), Inches(12.5), Inches(0.7))
        title_tf = title_box.text_frame
        title_tf.word_wrap = True
        if module_no == 1:
            t = "M01 KYA HAI What Is " + ctopic + " - 5 Examples Business Level"
        elif module_no == 2:
            t = "M02 KYON HAI Why Important Future " + ctopic
        elif module_no == 20:
            t = "M20 MISTAKES 90 Percent Fail " + ctopic
        elif module_no == 21:
            t = "M21 PRO TIP Secret Diary " + ctopic
        elif module_no == 40:
            t = "M40 FINAL PROJECT Certification " + ctopic
        else:
            t = "Module " + str(module_no) + " " + ctopic + " Master Teacher"
        title_tf.text = t
        title_tf.paragraphs[0].font.size = Pt(20)
        title_tf.paragraphs[0].font.bold = True
        body_box = slide.shapes.add_textbox(Inches(0.4), Inches(0.9), Inches(12.5), Inches(6.3))
        body_tf = body_box.text_frame
        body_tf.word_wrap = True
        if module_no == 1:
            c = ctopic + " kya hai simple definition 5 real examples Business automation Client project Freelancing Agency SaaS Scope 2026 300 percent growth Beginner to expert roadmap 30 din Teacher 20 saal experience Earning first month 15k Foundation strong."
        elif module_no == 2:
            c = ctopic + " kyon important future Market data 2026 demand high 90 percent fail bina samjhe advanced no practice sirf video Paise peeche Kyon seekhna abhi future proof AI Proof case study Rahul village 15k first client."
        elif module_no == 17:
            c = "Real Kahani Rahul Village Se " + ctopic + " 2 mahine roz 1 ghanta project Teesre mahine client 15k Chauthe mahine 5 clients 75k Aaj 2 lakh per month Kaise daily diary 30 min practice 1 project roz Real story motivation."
        elif module_no == 20:
            c = ctopic + " Mistakes 90 percent log Galti1 bina samjhe advanced Galti2 roz practice nahi sirf video Galti3 paise peeche Galti4 diary nahi Galti5 mentor nahi Kaise bache mistakes se master teacher."
        elif module_no == 21:
            c = "PRO TIP Secret Diary " + ctopic + " Roz raat 10 min diary likho Aaj kya seekha kya galti hui kal kya karna Ye trick successful students use karte hain koi YouTube pe nahi batata Millionaire mindset Focus Secret diary 30 din expert."
        elif module_no == 40:
            c = ctopic + " Final Project Certification Final project client real project Portfolio add Certification business level Real income start App strong business professional Expert 40 modules complete Next business plan 1Cr."
        else:
            c = ctopic + " Module " + str(module_no) + " Master Teacher 20 Years KYA HAI definition KYON HAI future KAHAN market KAB timing KAUN eligible KAISE architecture Perceive Reason Act KISSE tools Canva CapCut ChatGPT Notion KYA USE earning 20k-50k KAISE USE mobile reels laptop KAISE KARNA daily diary REAL KAHANI Rahul MISTAKES PRO TIP HOMEWORK BUSINESS PLAN 300 words rich content."
        body_tf.text = c
        body_tf.paragraphs[0].font.size = Pt(12)
    new_name = cid + "_Course_40Modules_RICH_V84.pptx"
    out_path = PPT_DIR / new_name
    prs.save(str(out_path))
    old_path = PPT_DIR / (cid + "_Course.pptx")
    if old_path.exists():
        old_path.unlink(missing_ok=True)
    return True

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

if len(courses) < 100:
    courses = []
    for i in range(len(TOPICS)):
        t = TOPICS[i]
        cid = "BRAHMA" + str(1000 + i)
        courses.append({"id": cid, "topic": t, "price": 999})
    save_json(COURSES_FILE, courses)

if "admin_logged" not in st.session_state:
    st.session_state["admin_logged"] = False

def check_persist():
    if ADMIN_SESSION.exists():
        try:
            data = ADMIN_SESSION.read_text(encoding="utf-8")
            d = json.loads(data)
            exp = datetime.datetime.fromisoformat(d.get("expiry"))
            now = datetime.datetime.now()
            if now < exp:
                return True
            else:
                ADMIN_SESSION.unlink(missing_ok=True)
                return False
        except:
            return False
    return False

if check_persist():
    st.session_state["admin_logged"] = True

st.sidebar.title("Brahma Education")

if not MASTER_HASH.exists():
    pw = st.sidebar.text_input("Create Admin Password", type="password")
    if st.sidebar.button("Create Admin"):
        if pw and len(pw) >= 4:
            h = hashlib.sha256(pw.encode()).hexdigest()
            MASTER_HASH.write_text(h)
            st.rerun()
    menu = "Browse Courses"
else:
    if not st.session_state["admin_logged"]:
        menu = st.sidebar.radio("Menu", ["Browse Courses", "My Access", "Chat Support"])
        st.sidebar.divider()
        pw = st.sidebar.text_input("Admin Password", type="password")
        rem = st.sidebar.checkbox("Yaad Rakho 7 din", value=True)
        if st.sidebar.button("Admin Login"):
            hpw = hashlib.sha256(pw.encode()).hexdigest()
            saved = MASTER_HASH.read_text()
            if hpw == saved:
                st.session_state["admin_logged"] = True
                if rem:
                    exp = datetime.datetime.now() + datetime.timedelta(days=7)
                    save_json(ADMIN_SESSION, {"expiry": exp.isoformat()})
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Admin Login 7 Din Business")
        menu = st.sidebar.radio("Admin", ["Dashboard", "