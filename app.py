import streamlit as st
import json
import hashlib
import datetime
import urllib.parse
from pathlib import Path
import pandas as pd

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

TOPICS = ["AI Agent Automation 2026", "Instagram Reels Mastery", "YouTube Automation AI", "Prompt Engineering Pro", "Digital Marketing SEO Mastery", "ChatGPT Mastery 2026", "Facebook Ads Mastery", "Google Ads Mastery", "SEO Advanced 2026", "Social Media Marketing Pro", "Content Writing AI", "Copywriting Mastery", "Blogging Mastery 2026", "Affiliate Marketing Pro", "Dropshipping Business", "E-commerce Mastery Shopify", "Canva Design Mastery", "Video Editing CapCut Pro", "YouTube SEO Mastery", "Instagram Growth Hack", "LinkedIn Marketing Pro", "Twitter X Growth Mastery", "TikTok Viral Mastery", "Pinterest Marketing", "Quora Marketing", "Email Marketing Automation", "WhatsApp Marketing Pro", "Telegram Channel Growth", "Influencer Marketing", "Personal Branding Mastery", "Freelancing Mastery", "Agency Business Mastery", "SaaS Business 2026", "No-Code Business Bubble", "Python Programming Mastery", "JavaScript Mastery 2026", "React JS Mastery", "Next.js Mastery", "Node.js Backend Mastery", "Web Development Full Stack", "WordPress Mastery", "Shopify Store Design", "UI UX Design Mastery", "Figma Design Pro", "Graphic Design Mastery", "Logo Design Mastery", "Thumbnail Design Viral", "Video Animation Mastery", "AI Image Generation Midjourney", "AI Video Generation Sora", "Voice Cloning ElevenLabs", "Automation n8n Make", "Zapier Automation Mastery", "Notion Productivity Mastery", "Excel Advanced Mastery", "Google Sheets Automation", "Data Analysis Python", "Machine Learning Mastery", "Deep Learning 2026", "Data Science Mastery", "Stock Market Trading AI", "Crypto Trading Mastery", "Forex Trading Pro", "Real Estate Business", "Motivational Speaking Mastery", "Public Speaking Pro", "Communication Skills Mastery", "English Speaking Pro", "Hindi Content Creation", "Podcast Mastery", "Music Production AI", "Photography Mastery", "Reels Editing Viral", "Meme Marketing Mastery", "Viral Content Formula", "Lead Generation Mastery", "Sales Funnel Mastery", "Landing Page Design", "CRO Conversion Optimization", "Customer Support Automation", "HR Recruitment AI", "Business Plan Mastery", "Startup Funding Mastery", "Business Automation AI", "Time Management Mastery", "Mindset Mastery Millionaire", "Meditation Mindfulness", "Fitness Coaching Business", "Diet Nutrition Business", "Yoga Teaching Business", "Cooking Channel Business", "Travel Vlogging Business", "Gaming Channel Growth", "Education Channel Growth", "Finance Channel Business", "News Channel Automation", "Meme Page Business", "Affiliate Blog SEO", "Amazon FBA Mastery", "Etsy Store Mastery", "Print on Demand Business", "Stock Photography Business", "Voice Over Business", "Translation Business AI", "Resume Writing Business", "LinkedIn Profile Optimization", "AI Tools Mastery 100 Tools", "Chatbot Development", "AI Voice Agent Mastery", "AI Receptionist Business"]

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size > 2:
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def create_real_pptx(cid, ctopic):
    try:
        from pptx import Presentation
        from pptx.util import Inches
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)

        # Slide 1 - Title
        slide = prs.slides.add_slide(prs.slide_layouts[5])
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12), Inches(1))
        tf = txBox.text_frame
        tf.text = ctopic + " - Super Teacher Business Level"

        txBox2 = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(12), Inches(5.5))
        tf2 = txBox2.text_frame
        tf2.word_wrap = True
        content = ""
        content += "Super Agent Brahma Master Teacher Super Teacher 20 years teaching\n\n"
        content += "KYA HAI: What is " + ctopic + " 5 examples\n"
        content += "KYON HAI: Why future market data 90 percent fail proof\n"
        content += "KAHAN HAI: Where use Instagram YouTube Business Job Freelancing\n"
        content += "KAB: When best morning 6 to 8 Monday Thursday\n"
        content += "KAUN: Who can do Student Housewife Job Business 16 to 60\n"
        content += "KAISE: How Step 1 Socho Step 2 Tool kholo Step 3 Pehla step\n"
        content += "KISSE: Free tools Canva CapCut ChatGPT Notion\n"
        content += "KYA USE: Earning freelancing 20k to 50k business 1L plus\n"
        content += "KAISE USE: Mobile plus Reels laptop browser dashboard\n"
        content += "KAISE KARNA: Right daily 30 min diary weekly revise\n"
        content += "REAL KAHANI: Rahul village 2 months daily 1 hour project third month client 15k\n"
        content += "MISTAKES: Galti1 advanced Galti2 no practice Galti3 only video\n"
        content += "PRO TIP: Diary daily what learned tomorrow plan\n"
        content += "HOMEWORK: Aaj project banao kal bhejo Business Level Real Income\n\n"
        content += "Module 1 Fundamentals Module 2 Tools Module 3 Architecture Module 4 Case Studies Module 5 Marketing Module 6 Mistakes Module 7 Final Project\n"
        tf2.text = content

        # Slide 2 - Details
        slide2 = prs.slides.add_slide(prs.slide_layouts[5])
        txBox3 = slide2.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12), Inches(6.5))
        tf3 = txBox3.text_frame
        tf3.word_wrap = True
        tf3.text = "Business Level Professional Course\n\n" + ctopic + " Complete Book 400 Lessons\nSuper Teacher Se Bani Hai\nReal Income App Strong\nCourses Likha Hai\nNo Fake - Real PPTX - Phone Me Khulegi"

        path = PPT_DIR / (cid + "_Course.pptx")
        prs.save(str(path))
        return str(path)
    except Exception as e:
        return None

topics = TOPICS
courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

if len(courses) < 100:
    courses = []
    for i in range(len(topics)):
        t = topics[i]
        courses.append({"id": "BRAHMA" + str(1000+i), "topic": t, "price": 999, "videos": 400})
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
        menu = st.sidebar.radio("Menu", ["Browse Courses", "My Access", "Chat Support"])
        st.sidebar.divider()
        pw = st.sidebar.text_input("Admin Password", type="password")
        rem = st.sidebar.checkbox("Yaad Rakho 7 din", value=True)
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(pw.encode()).hexdigest() == MASTER_HASH.read_text():
                st.session_state["admin_logged"] = True
                if rem:
                    exp = datetime.datetime.now() + datetime.timedelta(days=7)
                    save_json(ADMIN_SESSION, {"expiry": exp.isoformat()})
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Admin Login 7 Din Business")
        menu = st.sidebar.radio("Admin", ["Dashboard", "Super Agent", "Course Library", "Sales QR"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Dashboard - 100 Courses Business Level")
        total = len(courses)
        proper = len(list(PPT_DIR.glob("*_Course*")))
        bekar = 0
        for f in list(PPT_DIR.glob("*.*")):
            if "_Course" not in f.name:
                bekar += 1
        missing = 0
        for c in courses:
            if not list(PPT_DIR.glob(c.get("id") + "_Course*")):
                missing += 1
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Total Courses", total)
        c2.metric("Courses Ready", proper)
        c3.metric("Old Files", bekar)
        c4.metric("Missing", missing)
        if proper >= 100:
            st.success("Course Library Full 100 Books Real PPTX - Phone Me Khulegi")
        else:
            st.warning("Missing hai - Neeche button se real PPTX banao")
        if st.button("100 KI 100 SARI PURANI CORRUPTED DELETE KARO", type="secondary"):
            for f in list(PPT_DIR.glob("*.*")):
                try:
                    f.unlink()
                except:
                    pass
            st.success("100 ki 100 sari purani corrupted delete kar di")
            st.rerun()
        if st.button("100 REAL PPTX SUPER TEACHER SE BANAO - PHONE ME KHULEGI", type="primary"):
            bar = st.progress(0)
            for idx, c in enumerate(courses):
                create_real_pptx(c.get("id"), c.get("topic"))
                bar.progress(int((idx+1)/len(courses)*100))
            st.success("100 Real PPTX Ban Gayi - Phone Me Khulegi - No Corrupted - Super Teacher Se")
            st.balloons()
            st.rerun()
        df_data = []
        for c in courses:
            s = "Ready Real PPTX" if list(PPT_DIR.glob(c.get("id") + "_Course*")) else "Missing"
            df_data.append({"ID": c.get("id"), "Course Name": c.get("topic"), "Price": c.get("price"), "Status": s})
        st.dataframe(pd.DataFrame(df_data), use_container_width=True)

    if menu == "Course Library":
        st.title("Course Library - 100 Real PPTX Books")
        total = len(courses)
        proper = len(list(PPT_DIR.glob("*_Course*")))
        st.write("Total " + str(total) + " Courses Ready " + str(proper) + " Real PPTX")
        for idx, co in enumerate(courses):
            cid = co.get("id")
            pf = list(PPT_DIR.glob(cid + "_Course*"))
            col1,col2 = st.columns([3,1])
            with col1:
                if pf:
                    st.success(str(idx+1) + ". " + co.get("topic") + " Ready Real PPTX - Phone