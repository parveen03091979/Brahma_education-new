import streamlit as st
import json
import hashlib
import datetime
import urllib.parse
from pathlib import Path
import pandas as pd

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    PPTX_OK = True
except:
    PPTX_OK = False

st.set_page_config(page_title="Brahma Education", layout="wide")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
ADMIN_SESSION = DATA_DIR / ".admin_session"
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
PPT_DIR = DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)

MY_UPI_ID = "parveen39179@okicici"
MY_NAME = "Parveen Kumar"

def get_topics():
    t = []
    t.append("AI Agent Automation 2026")
    t.append("Instagram Reels Mastery")
    t.append("YouTube Automation AI")
    t.append("Prompt Engineering Pro")
    t.append("Digital Marketing SEO Mastery")
    t.append("ChatGPT Mastery 2026")
    t.append("Facebook Ads Mastery")
    t.append("Google Ads Mastery")
    t.append("SEO Advanced 2026")
    t.append("Social Media Marketing Pro")
    t.append("Content Writing AI")
    t.append("Copywriting Mastery")
    t.append("Blogging Mastery 2026")
    t.append("Affiliate Marketing Pro")
    t.append("Dropshipping Business")
    t.append("E-commerce Mastery Shopify")
    t.append("Canva Design Mastery")
    t.append("Video Editing CapCut Pro")
    t.append("YouTube SEO Mastery")
    t.append("Instagram Growth Hack")
    t.append("LinkedIn Marketing Pro")
    t.append("Twitter X Growth Mastery")
    t.append("TikTok Viral Mastery")
    t.append("Pinterest Marketing")
    t.append("Quora Marketing")
    t.append("Email Marketing Automation")
    t.append("WhatsApp Marketing Pro")
    t.append("Telegram Channel Growth")
    t.append("Influencer Marketing")
    t.append("Personal Branding Mastery")
    t.append("Freelancing Mastery Upwork Fiverr")
    t.append("Agency Business Mastery")
    t.append("SaaS Business 2026")
    t.append("No-Code Business Bubble")
    t.append("Python Programming Mastery")
    t.append("JavaScript Mastery 2026")
    t.append("React JS Mastery")
    t.append("Next.js Mastery")
    t.append("Node.js Backend Mastery")
    t.append("Web Development Full Stack")
    t.append("WordPress Mastery")
    t.append("Shopify Store Design")
    t.append("UI UX Design Mastery")
    t.append("Figma Design Pro")
    t.append("Graphic Design Mastery")
    t.append("Logo Design Mastery")
    t.append("Thumbnail Design Viral")
    t.append("Video Animation Mastery")
    t.append("AI Image Generation Midjourney")
    t.append("AI Video Generation Sora")
    t.append("Voice Cloning ElevenLabs")
    t.append("Automation n8n Make")
    t.append("Zapier Automation Mastery")
    t.append("Notion Productivity Mastery")
    t.append("Excel Advanced Mastery")
    t.append("Google Sheets Automation")
    t.append("Data Analysis Python")
    t.append("Machine Learning Mastery")
    t.append("Deep Learning 2026")
    t.append("Data Science Mastery")
    t.append("Stock Market Trading AI")
    t.append("Crypto Trading Mastery")
    t.append("Forex Trading Pro")
    t.append("Real Estate Business")
    t.append("Motivational Speaking Mastery")
    t.append("Public Speaking Pro")
    t.append("Communication Skills Mastery")
    t.append("English Speaking Pro")
    t.append("Hindi Content Creation")
    t.append("Podcast Mastery")
    t.append("Music Production AI")
    t.append("Photography Mastery")
    t.append("Reels Editing Viral")
    t.append("Meme Marketing Mastery")
    t.append("Viral Content Formula")
    t.append("Lead Generation Mastery")
    t.append("Sales Funnel Mastery")
    t.append("Landing Page Design High Converting")
    t.append("CRO Conversion Optimization")
    t.append("Customer Support Automation")
    t.append("HR Recruitment AI")
    t.append("Business Plan Mastery")
    t.append("Startup Funding Mastery")
    t.append("Business Automation AI")
    t.append("Time Management Mastery")
    t.append("Mindset Mastery Millionaire")
    t.append("Meditation Mindfulness")
    t.append("Fitness Coaching Business")
    t.append("Diet Nutrition Business")
    t.append("Yoga Teaching Business")
    t.append("Cooking Channel Business")
    t.append("Travel Vlogging Business")
    t.append("Gaming Channel Growth")
    t.append("Education Channel Growth")
    t.append("Finance Channel Business")
    t.append("News Channel Automation")
    t.append("Meme Page Business")
    t.append("Affiliate Blog SEO")
    t.append("Amazon FBA Mastery")
    t.append("Etsy Store Mastery")
    t.append("Print on Demand Business")
    t.append("Stock Photography Business")
    t.append("Voice Over Business")
    t.append("Translation Business AI")
    t.append("Resume Writing Business")
    t.append("LinkedIn Profile Optimization Business")
    t.append("AI Tools Mastery 100 Tools")
    t.append("Chatbot Development")
    t.append("AI Voice Agent Mastery")
    t.append("AI Receptionist Business")
    return t

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size > 2:
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def get_lessons(topic):
    lessons = []
    lessons.append("What is " + topic + " definition with 5 real examples")
    lessons.append("History of " + topic + " 2015 to 2026")
    lessons.append("Types of " + topic + " 7 types detail")
    lessons.append(topic + " vs Traditional difference")
    lessons.append("Why " + topic + " is future market data proof")
    lessons.append("Career in " + topic + " jobs salary freelancing")
    lessons.append(topic + " mindset how to think like expert")
    lessons.append("Myths about " + topic + " 10 myths busted")
    lessons.append("Success stories " + topic + " 5 people 1Cr earned")
    lessons.append("Failure stories " + topic + " why 90 percent fail")
    lessons.append(topic + " roadmap zero to expert 90 days")
    lessons.append("Tools needed " + topic + " 20 tools list")
    lessons.append("Industry overview " + topic + " top 10 industries")
    lessons.append("Market size " + topic + " 2026 report")
    lessons.append("Skills needed " + topic + " technical plus soft")
    lessons.append("Learning path " + topic + " step by step")
    lessons.append("Time management for " + topic + " daily routine")
    lessons.append("Best resources for " + topic + " books videos")
    lessons.append("Community for " + topic + " discord reddit")
    lessons.append("Mentorship for " + topic + " how to find mentor")
    lessons.append(topic + " architecture basic structure")
    lessons.append("Core technology behind " + topic)
    lessons.append("RAG in " + topic + " deep")
    lessons.append("Memory in " + topic + " short long vector")
    lessons.append("Tools integration in " + topic)
    lessons.append("Planning in " + topic + " ReAct Chain Thought")
    lessons.append("Reasoning in " + topic + " how expert thinks")
    lessons.append("Action in " + topic + " how to take action")
    lessons.append("Observation in " + topic + " learn from result")
    lessons.append("Loop in " + topic + " Perceive Reason Act")
    lessons.append("Case Study 1 " + topic + " 1L per month business")
    lessons.append("Case Study 2 " + topic + " 10M ARR story")
    lessons.append("Case Study 3 " + topic + " 10M users growth")
    lessons.append("Case Study 4 " + topic + " real implementation")
    lessons.append("Case Study 5 " + topic + " 5k to 5L small business")
    lessons.append("Assignment 1 " + topic + " first simple project")
    lessons.append("Assignment 2 " + topic + " 10 examples research")
    lessons.append("Assignment 3 " + topic + " architecture diagram")
    lessons.append("Summary " + topic + " fundamentals checklist")
    lessons.append("Test " + topic + " fundamentals 20 questions")
    return lessons

def create_ppt(cid, ctopic):
    if not PPTX_OK:
        return None, "pptx missing"
    try:
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        curr = get_lessons(ctopic)

        slide = prs.slides.add_slide(prs.slide_layouts[6])
        box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(1.5))
        tf = box.text_frame
        tf.word_wrap = True
        tf.text = ctopic + " Complete Course 400 Lessons Business Level Real Learning"
        tf.paragraphs[0].runs[0].font.size = Pt(20)
        tf.paragraphs[0].runs[0].font.bold = True
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)

        cnt = 0
        for raw in curr:
            if cnt >= 60:
                break
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            box = slide.shapes.add_textbox(Inches(0.2), Inches(0.1), Inches(12.9), Inches(0.7))
            tf = box.text_frame
            tf.word_wrap = True
            title = "Lesson " + str(cnt+1) + ": " + raw
            tf.text = title[:200]
            tf.paragraphs[0].runs[0].font.size = Pt(12)
            tf.paragraphs[0].runs[0].font.bold = True
            tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)

            hi = "TOPIC " + raw + " KYA HAI " + raw + " kya hai " + ctopic + " me simple 5 examples. KYON HAI kyon zaroori bina fail 90 percent fail market 300 percent bada. KAHAN HAI kahan use Instagram YouTube Business Job Freelancing top 5. KAB Best subah 6-8 Monday Thursday. KAUN Student Housewife Job Business 16 to 60. KAISE Step 1 Socho Step 2 Tool kholo Step 3 Pehla step Step 4 Result Step 5 Sudharo. KISSE Free tools Canva CapCut ChatGPT. KYA USE Freelancing 20k-50k Business 1L Job 30k-80k. KAISE USE Mobile Instagram plus Reels Laptop browser dashboard. KAISE KARNA Sahi Roz 30 min diary hafte revise Galat 5 ghante ek din phir kuch nahi. REAL Rahul gaon se 2 mahine roz 1 ghanta daily project teesre mahine client 15k chauthe 5 clients 75k aaj 2 lakh. MISTAKES Galti1 bina samjhe advanced Galti2 practice nahi Galti3 only video Galti4 paise peeche. PRO TIP Diary rakho roz kya seekha galti kal kya karna raat 10 min padho. HOMEWORK Aaj " + raw + " par project banao kal bhejo."

            box = slide.shapes.add_textbox(Inches(0.2), Inches(0.9), Inches(12.9), Inches(6.0))
            tf = box.text_frame
            tf.word_wrap = True
            tf.text = hi[:2000]
            for p in tf.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9)

            cnt += 1

        path = PPT_DIR / (cid + "_Course.pptx")
        prs.save(str(path))
        return str(path), "Course " + str(cnt) + " slides Business Level"
    except Exception as e:
        return None, "Error " + str(e)

topics = get_topics()
courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

need_reset = False
if len(courses) > 0:
    first = courses[0]
    if isinstance(first, str):
        need_reset = True

if len(courses) < 100 or need_reset:
    courses = []
    for i in range(len(topics)):
        t = topics[i]
        courses.append({"id":"BRAHMA" + str(1000+i),"topic":t,"price":999,"videos":400})
    save_json(COURSES_FILE, courses)

if "admin_logged" not in st.session_state:
    st.session_state["admin_logged"] = False

def check_persist():
    try:
        if ADMIN_SESSION.exists():
            d = json.loads(ADMIN_SESSION.read_text(encoding="utf-8"))
            exp = datetime.datetime.fromisoformat(d.get("expiry"))
            if datetime.datetime.now() < exp:
                return True
            else:
                ADMIN_SESSION.unlink(missing_ok=True)
    except:
        pass
    return False

if check_persist():
    st.session_state["admin_logged"] = True

st.sidebar.title("Brahma Education")
if not MASTER_HASH.exists():
    pw = st.sidebar.text_input("Create Admin Password", type="password")
    if st.sidebar.button("Create Admin"):
        if pw and len(pw) >= 4:
            MASTER_HASH.write_text(hashlib.sha256(pw.encode()).hexdigest())
            st.rerun()
    menu = "Browse Courses"
else:
    if not st.session_state["admin_logged"]:
        menu = st.sidebar.radio("Menu",["Browse Courses","My Access","Chat Support"])
        st.sidebar.divider()
        pw = st.sidebar.text_input("Admin Password", type="password")
        rem = st.sidebar.checkbox("Yaad Rakho 7 din", value=True)
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(pw.encode()).hexdigest() == MASTER_HASH.read_text():
                st.session_state["admin_logged"] = True
                if rem:
                    exp = datetime.datetime.now() + datetime.timedelta(days=7)
                    save_json(ADMIN_SESSION,{"expiry":exp.isoformat()})
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Admin Login 7 Din Business")
        menu = st.sidebar.radio("Admin",["Dashboard","Super Agent","Course Library","Sales QR"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Dashboard - 100 Courses Business Level")
        total = len(courses)
        proper = len(list(PPT_DIR.glob("*Course.pptx")))
        allppt = len(list(PPT_DIR.glob("*.pptx")))
        bekar = allppt - proper
        missing = 0
        for c in courses:
            if not list(PPT_DIR.glob(c.get("id") + "*Course*")):
                missing += 1
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Total Courses",total)
        c2.metric("Courses Ready",proper)
        c3.metric("Old PPTs