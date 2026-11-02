import streamlit as st
import json
import hashlib
import secrets
import datetime
import urllib.parse
import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt

st.set_page_config(page_title="Brahma Education V100", page_icon="🎓", layout="wide")

DATA = Path("data")
PPT_DIR = DATA / "ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

COURSES_FILE = DATA / "courses.json"
PURCHASE_FILE = DATA / "purchases.json"
MARKETING_FILE = DATA / "marketing.json"
API_FILE = DATA / "api_keys.json"
QR_FILE = DATA / "upi_qr.jpg"
MASTER_HASH = DATA / ".master_hash"
ADMIN_SESSION = DATA / ".admin_session"

UPI_ID = "parveen39179@okicici"
OWNER = "Parveen Kumar"
DEFAULT_PRICE = 99

TOPICS = """
AI Agent Automation
Instagram Reels Mastery
YouTube Automation
Prompt Engineering
Digital Marketing SEO
ChatGPT Mastery
Facebook Ads
Google Ads
SEO Advanced
Social Media Marketing
Content Writing AI
Copywriting Mastery
Blogging Mastery
Affiliate Marketing
Dropshipping
E-commerce Shopify
Canva Design
Video Editing CapCut
YouTube SEO
Instagram Growth
LinkedIn Marketing
Twitter X Growth
TikTok Viral
Pinterest Marketing
Quora Marketing
Email Marketing Automation
WhatsApp Marketing
Telegram Growth
Influencer Marketing
Personal Branding
Freelancing Mastery
Agency Business
SaaS Business
No-Code Bubble
Python Mastery
JavaScript Mastery
React JS
Next.js
Node.js
Web Development Full Stack
WordPress Mastery
Shopify Store Design
UI UX Design
Figma Design
Graphic Design
Logo Design
Thumbnail Design Viral
Video Animation
AI Image Midjourney
AI Video Sora
Voice Cloning ElevenLabs
Automation n8n Make
Zapier Automation
Notion Productivity
Excel Advanced
Google Sheets Automation
Data Analysis Python
Machine Learning
Deep Learning
Data Science
Stock Trading AI
Crypto Trading
Forex Trading
Real Estate Business
Motivational Speaking
Public Speaking
Communication Skills
English Speaking
Podcast Mastery
Music Production AI
Photography Mastery
Reels Editing Viral
Meme Marketing
Viral Content Formula
Lead Generation
Sales Funnel
Landing Page Design
CRO Optimization
Customer Support Automation
HR Recruitment AI
Business Plan Mastery
Startup Funding
Business Automation AI
Time Management
Mindset Millionaire
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
AI Tools Mastery
Chatbot Development
AI Voice Agent
AI Receptionist Business
""".strip().splitlines()

def load(path, default):
    try:
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    except:
        pass
    return default

def save(path, data):
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(path)

def initialize_courses():
    data = load(COURSES_FILE, [])
    if not isinstance(data, list):
        data = []
    existing = {c.get("topic","").strip().lower() for c in data if isinstance(c, dict)}
    for i, topic in enumerate(TOPICS):
        if topic.lower() not in existing:
            data.append({"id": "BRAHMA"+str(1000+i), "topic": topic, "price": 99})
    for course in data:
        try:
            price = int(course.get("price", 999))
            if price > 200 or price < 1:
                price = 99
            course["price"] = price
        except:
            course["price"] = 99
    save(COURSES_FILE, data)
    return data

courses = initialize_courses()
purchases = load(PURCHASE_FILE, [])
marketing = load(MARKETING_FILE, [])
api_keys = load(API_FILE, {})

MODULES = [
"WHAT IS","WHY IMPORTANT","WHERE USE","WHEN TO USE","WHO ELIGIBLE",
"HOW ARCHITECTURE","TOOLS REQUIRED","EARNING OPPORTUNITIES","PRACTICAL USAGE","RIGHT WAY TO LEARN",
"BEGINNER FOUNDATION","CORE CONCEPTS","ADVANCED CONCEPTS","STEP BY STEP PROCESS","REAL BUSINESS EXAMPLES",
"CLIENT REQUIREMENTS","REAL STORY","PROJECT PLANNING","IMPLEMENTATION","MISTAKES TO AVOID",
"PRO TIP","EXPERT STRATEGY","TOOLS COMPARISON","FREE VS PAID","PORTFOLIO BUILDING",
"CLIENT FINDING","FREELANCING","AGENCY MODEL","BUSINESS MODEL","SCALING STRATEGY",
"SEO AND MARKETING","LEAD GENERATION","SALES STRATEGY","AUTOMATION","OPTIMIZATION",
"CASE STUDY","DAILY PRACTICE","HOMEWORK","REVISION","FINAL PROJECT AND CERTIFICATION"
]

def module_content(topic, number):
    title = MODULES[number-1]
    text = "COURSE TOPIC: "+topic+". MODULE: "+title+". This lesson introduces the subject and explains its importance in professional and business applications. Understand main concepts, terminology, tools, processes and practical implementation. Start with foundation and move towards professional applications. "
    if number == 17:
        text += "REAL STORY: Rahul is fictional case study. Begins with basic smartphone and limited resources. Studies daily, practices skills and builds portfolio. Approaches clients, receives rejections and improves proposals. Eventually completes first project. Progress from practice and consistent improvement. "
    if number == 20:
        text += "FIVE COMMON MISTAKES: Skipping foundation, watching without practicing, chasing money before learning, not maintaining diary and avoiding feedback. Create weekly plan to avoid mistakes. "
    if number == 21:
        text += "PRO TIP: Write four things diary every night: what you learned, what mistake you made, what you will improve tomorrow and one new idea. Review every Sunday. "
    if number == 31:
        text += "SEO: Search Engine Optimization helps useful content discovered in search engines. Learn keyword research, search intent, titles, descriptions, headings, internal links, image alt text and quality content. "
    if number == 40:
        text += "FINAL PROJECT: Create professional project based on this course. Include problem, solution, workflow, tools, testing, portfolio and final presentation. Submit for evaluation. "
    return text+text

def make_ppt(course):
    cid = course["id"]
    topic = course["topic"]
    output = PPT_DIR / (cid+"_40_MODULES_V100.pptx")
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)
    for n in range(1, 41):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        title_box = slide.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.text = "M"+str(n).zfill(2)+" "+topic+" Module "+str(n)
        tf.paragraphs[0].font.size = Pt(20)
        tf.paragraphs[0].font.bold = True
        body_box = slide.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
        bf = body_box.text_frame
        bf.word_wrap = True
        bf.text = module_content(topic, n)
        bf.paragraphs[0].font.size = Pt(13)
    prs.save(str(output))
    return output

def make_password_hash(password):
    salt = secrets.token_bytes(16)
    hashed = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
    return salt.hex()+":"+hashed.hex()

def verify_password(password, stored):
    try:
        salt_hex, hash_hex = stored.split(":")
        salt = bytes.fromhex(salt_hex)
        actual = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
        return secrets.compare_digest(actual.hex(), hash_hex)
    except:
        old = hashlib.sha256(password.encode()).hexdigest()
        return secrets.compare_digest(old, stored)

def session_valid():
    try:
        data = load(ADMIN_SESSION, {})
        expiry = datetime.datetime.fromisoformat(data["expiry"])
        return datetime.datetime.now() < expiry
    except:
        return False

if "admin_logged" not in st.session_state:
    st.session_state.admin_logged = session_valid()

st.sidebar.title("Brahma Education V100")
if not MASTER_HASH.exists():
    pw = st.sidebar.text_input("Create Admin Password", type="password")
    if st.sidebar.button("Create Admin"):
        if pw and len(pw)>=4:
            MASTER_HASH.write_text(make_password_hash(pw), encoding="utf-8")
            st.rerun()
    menu = "Browse Courses"
else:
    if not st.session_state.admin_logged:
        menu = st.sidebar.radio("Menu", ["Browse Courses","My Access"])
        st.sidebar.divider()
        pw = st.sidebar.text_input("Admin Password", type="password")
        if st.sidebar.button("Admin Login"):
            stored = MASTER_HASH.read_text(encoding="utf-8").strip()
            if verify_password(pw, stored):
                if ":" not in stored:
                    MASTER_HASH.write_text(make_password_hash(pw), encoding="utf-8")
                expiry = datetime.datetime.now()+datetime.timedelta(days=7)
                save(ADMIN_SESSION, {"expiry": expiry.isoformat()})
                st.session_state.admin_logged = True
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Admin Login - Price 99 Stable")
        menu = st.sidebar.radio("Admin", ["Dashboard","Price Manager 99","Deep Maker","Course Library","Video Library","API Keys","UPI QR Setup","Sales","Marketing","Super Agent"])
        if st.sidebar.button("Logout"):
            st.session_state.admin_logged = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state.admin_logged:
    if menu == "Dashboard":
        st.title("Dashboard - 100 Courses Price 99")
        total = len(courses)
        ready = len(list(PPT_DIR.glob("*_40_MODULES_V100.pptx")))
        avg_price = sum([c.get("price",99) for c in courses])//max(1,total)
        c1,c2,c3 = st.columns(3)
        c1.metric("Total Courses", total)
        c2.metric("Ready Books", ready)
        c3.metric("Avg Price", "Rs "+str(avg_price))
        if st.button("DELETE OLD FILES", type="secondary"):
            for f in PPT_DIR.glob("*.*"):
                try:
                    f.unlink()
                except:
                    pass
            st.success("Old files deleted")
            st.rerun()
        if st.button("CREATE 100 BOOKS PRICE 99", type="primary"):
            bar = st.progress(0)
            for idx, c in enumerate(courses):
                make_ppt(c)
                bar.progress(int((idx+1)/len(courses)*100))
            st.success("100 Books Created Price 99")
            st.balloons()
            st.rerun()

    elif menu == "Price Manager 99":
        st.title("Price Manager - Sabhi Ka Ek Sath Aur Har Ek Ka Alag-Alag")
        st.success("Jo aapne bola tha - Sabhi courses ka price 99 + Bulk + Single - V100 exact + 2 cheez add")
        bulk = st.number_input("Set All To Price Rs", value=99, min_value=1, max_value=10000, step=1)
        if st.button("SET ALL BULK", type="primary"):
            for c in courses:
                c["price"] = int(bulk)
            save(COURSES_FILE, courses)
            st.success("Sare courses ka price Rs "+str(bulk)+" Bulk Done")
            st.rerun()
        inc = st.number_input("Increase Decrease All By Rs", value=10, min_value=-1000, max_value=1000, step=1)
        if st.button("APPLY BULK CHANGE", type="secondary"):
            for c in courses:
                np = c.get("price",99)+int(inc)
                c["price"] = int(max(1,np))
            save(COURSES_FILE, courses)
            st.success("Bulk change "+str(inc)+" Done")
            st.rerun()
        if st.button("SET ALL TO 99 ONE CLICK", type="primary"):
            for c in courses:
                c["price"] = 99
            save(COURSES_FILE, courses)
            st.success("Sare 100