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

st.set_page_config(page_title="Brahma Education - 100 Courses", layout="wide")

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

def get_100_topics():
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
    m1 = []
    m1.append("What is " + topic + " definition with 5 real examples")
    m1.append("History of " + topic + " timeline 2015 to 2026")
    m1.append("Types of " + topic + " 7 types detail")
    m1.append(topic + " vs Traditional difference")
    m1.append("Why " + topic + " is future market data proof")
    m1.append("Career in " + topic + " jobs salary freelancing")
    m1.append(topic + " mindset how to think like expert")
    m1.append("Myths about " + topic + " 10 myths busted")
    m1.append("Success stories " + topic + " 5 people 1Cr earned")
    m1.append("Failure stories " + topic + " why 90 percent fail")
    m1.append(topic + " roadmap zero to expert 90 days")
    m1.append("Tools needed " + topic + " 20 tools list")
    m1.append("Industry overview " + topic + " top 10 industries")
    m1.append("Market size " + topic + " 2026 report")
    m1.append("Skills needed " + topic + " technical plus soft")
    m1.append("Learning path " + topic + " step by step")
    m1.append("Time management for " + topic + " daily routine")
    m1.append("Best resources for " + topic + " books videos")
    m1.append("Community for " + topic + " discord reddit")
    m1.append("Mentorship for " + topic + " how to find mentor")
    m1.append(topic + " architecture basic structure")
    m1.append("Core technology behind " + topic)
    m1.append("RAG in " + topic + " deep")
    m1.append("Memory in " + topic + " short long vector")
    m1.append("Tools integration in " + topic)
    m1.append("Planning in " + topic + " ReAct Chain Thought")
    m1.append("Reasoning in " + topic + " how expert thinks")
    m1.append("Action in " + topic + " how to take action")
    m1.append("Observation in " + topic + " learn from result")
    m1.append("Loop in " + topic + " Perceive Reason Act")
    m1.append("Case Study 1 " + topic + " 1L per month business")
    m1.append("Case Study 2 " + topic + " 10M ARR story")
    m1.append("Case Study 3 " + topic + " 10M users growth")
    m1.append("Case Study 4 " + topic + " real implementation")
    m1.append("Case Study 5 " + topic + " 5k to 5L small business")
    m1.append("Assignment 1 " + topic + " first simple project")
    m1.append("Assignment 2 " + topic + " 10 examples research")
    m1.append("Assignment 3 " + topic + " architecture diagram")
    m1.append("Summary " + topic + " fundamentals checklist")
    m1.append("Test " + topic + " fundamentals 20 questions")

    base = []
    base.append("Intro overview what we learn")
    base.append("Workspace setup zero to setup")
    base.append("Interface meaning every button")
    base.append("5 terms basic words meaning")
    base.append("Workflow step how work happens")
    base.append("First example first real example practical")
    base.append("Exercise 1 do yourself")
    base.append("Mistakes basics 90 percent do")
    base.append("Best practices right way what is")
    base.append("Tools stage which tools needed")
    base.append("Time management how much time give")
    base.append("Checklist what done check")
    base.append("Real example 1 real business story 1")
    base.append("Real example 2 real business story 2")
    base.append("Case study deep case study one business")
    base.append("Practical demo live demo step by step")
    base.append("Step guide each step written")
    base.append("Troubleshooting problem what to do")
    base.append("Optimization tips how to make better")
    base.append("Advanced basics little advanced level")
    base.append("Interview Q what asked on topic")
    base.append("Freelancing tip how to earn money from this")
    base.append("Client handling how to handle client")
    base.append("Pricing how much charge")
    base.append("Portfolio building how to build portfolio")
    base.append("Review what learned revise")
    base.append("Test 10 Q test")
    base.append("Assignment 1 first homework")
    base.append("Assignment 2 second homework")
    base.append("Pro tip what pros do secret")
    base.append("Secret trick nobody tells trick")
    base.append("Free resource where learn free")
    base.append("Paid resource best paid what is")
    base.append("Community help where get help")
    base.append("Mentorship how to get mentor")
    base.append("Next steps what to do next")
    base.append("Summary whole module summary")
    base.append("FAQ what people ask")
    base.append("Resources books videos links")
    base.append("Final task last work of module")

    themes = []
    themes.append("Fundamentals Basic Start")
    themes.append("Tools Setup Which Tools")
    themes.append("Practical Basics Hands On")
    themes.append("Intermediate Beech Ka Level")
    themes.append("Advanced Techniques Expert Level")
    themes.append("Case Studies Real Business Kahani")
    themes.append("Marketing Business Paise Kaise Kamaye")
    themes.append("Automation Scaling Auto Kaise Kare")
    themes.append("Mistakes Optimization Galtiyan Sudhar")
    themes.append("Final Project Aakhri Project")

    all_mods = []
    all_mods.append(m1)
    m2 = []
    for i in range(40):
        m2.append("Tool " + str(i+1) + " " + topic + " setup guide")
    all_mods.append(m2)
    for mi in range(2,10):
        th = themes[mi]
        lst = []
        for j,b in enumerate(base):
            lst.append(th + " " + b + " for " + topic + " lesson " + str(j+1) + " deep real")
        all_mods.append(lst)

    curr = []
    lc = 1
    for mi,ml in enumerate(all_mods):
        vids = []
        for raw in ml:
            title = "Lesson " + str(lc) + ": " + raw
            hi = "TOPIC " + raw + " KYA HAI " + raw + " kya hai " + topic + " me simple 5 examples. KYON HAI kyon zaroori bina fail 90 percent fail market 300 percent bada. KAHAN HAI kahan use Instagram YouTube Business Job Freelancing top 5. KAB Best subah 6-8 Monday Thursday. KAUN Student Housewife Job Business 16 to 60. KAISE Step 1 Socho Step 2 Tool kholo Step 3 Pehla step Step 4 Result Step 5 Sudharo. KISSE Free tools Canva CapCut ChatGPT Google Notion. KYA USE Freelancing 20k-50k Business 1L plus Job 30k-80k. KAISE USE Mobile Instagram plus Reels Laptop browser dashboard. KAISE KARNA Sahi Roz 30 min diary hafte revise Galat 5 ghante ek din phir kuch nahi. REAL Rahul gaon se 2 mahine roz 1 ghanta daily project teesre mahine client 15k chauthe 5 clients 75k aaj 2 lakh per month. MISTAKES Galti1 bina samjhe advanced Galti2 practice nahi Galti3 only video Galti4 paise peeche. PRO TIP Diary rakho roz kya seekha galti kal kya karna raat 10 min padho ye trick successful students use karte hain. HOMEWORK Aaj " + raw + " par real project banao kal bhejo. SUMMARY Aaj " + raw + " Kya Kyon Kahan Kab Kaun Kaise Kisse Use."
            en = "TOPIC " + raw + " WHAT " + raw + " meaning in " + topic + " 5 examples. WHY fail 90 percent market 300 percent. WHERE Instagram YouTube Business Job Freelancing top 5. WHEN morning 6-8 Monday Thursday. WHO Student Housewife Job Business 16 to 60. HOW Step1 Think Step2 Open Step3 First Step4 Result Step5 Fix. WITH Free Canva CapCut ChatGPT Google Notion. WHAT USE Earn 20k-50k Business 1L Job 30k-80k. HOW USE Mobile plus Reels Laptop browser dashboard. HOW SHOULD Right daily 30 min diary weekly revise Wrong 5 hours one day then nothing. STORY Rahul village 2 months daily 1 hour on " + raw + " first month no idea then daily project third month first client 15k fourth 5 clients 75k today 2 lakh per month. MISTAKES M1 advanced M2 no practice M3 only video M4 money behind. PRO TIP Diary daily what learned mistake tomorrow plan read 10 min before sleep trick successful students use. HOMEWORK Build small real project today on " + raw + " send tomorrow. SUMMARY Today " + raw + " What Why Where When Who How."
            vids.append({"no":lc,"title":title,"hi":hi,"en":en})
            lc += 1
        curr.append({"title":"Module " + str(mi+1) + " " + topic + " " + themes[mi] + " Book","videos":vids})
    return curr

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
        tf.text = ctopic + " Complete Course 400 Lessons Business Level"
        tf.paragraphs[0].runs[0].font.size = Pt(20)
        tf.paragraphs[0].runs[0].font.bold = True
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)
        cnt = 0
        for mod in curr:
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(1.0))
            tf = box.text_frame
            tf.word_wrap = True
            tf.text = mod["title"] + " 40 Lessons Course Book"
            tf.paragraphs[0].runs[0].font.size = Pt(16)
            tf.paragraphs[0].runs[0].font.bold = True
            tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)
            cnt += 1
            for vid in mod["videos"]:
                if cnt >= 62:
                    break
                slide = prs.slides.add_slide(prs.slide_layouts[6])
                box = slide.shapes.add_textbox(Inches(0.2), Inches(0.1), Inches(12.9), Inches(0.6))
                tf = box.text_frame
                tf.word_wrap = True
                tf.text = vid["title"][:200]
                tf.paragraphs[0].runs[0].font.size = Pt(11)
                tf.paragraphs[0].runs[0].font.bold = True
                tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)
                box = slide.shapes.add_textbox(Inches(0.2), Inches(0.8), Inches(6.3), Inches(6.2))
                tf = box.text_frame
                tf.word_wrap = True
                tf.text = vid["hi"][:2500]
                for p in tf.paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(7)
                box = slide.shapes.add_textbox(Inches(6.8), Inches(0.8), Inches(6.3), Inches(6.2))
                tf = box.text_frame
                tf.word_wrap = True
                tf.text = vid["en"][:2500]
                for p in tf.paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(7)
                cnt += 1
            if cnt >= 62:
                break
        path = PPT_DIR / (cid + "_Course.pptx")
        prs.save(str(path))
        return str(path), "Course " + str(cnt) + " slides Business Level"
    except Exception as e:
        return None, "Error " + str(e)

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

# Professional fix - Agar courses.json me raw list hai string ki to use delete karo - Screenshot wala [ 0: "AI Agent..." ] hatana hai
need_reset = False
if len(courses) > 0:
    first = courses[0]
    if isinstance(first, str):
        need_reset = True

topics = get_100_topics()
if len(courses) < 100 or need_reset:
    courses = []
    for i,t in enumerate(topics):
        courses.append({"id":"BRAHMA" + str(1000+i),"topic":t,"price":999,"videos":400})
    save_json(COURSES_FILE, courses)
    if need_reset:
        st.warning("Purana raw list [0: AI Agent...] delete kiya - Professional courses banaye")

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
        menu = st.sidebar.radio("Admin",["Dashboard","Super Agent","Course Library","Course Maker","Sales QR"])
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
               