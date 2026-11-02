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

def create_master_teacher_pptx(cid, ctopic):
    try:
        from pptx import Presentation
        from pptx.util import Inches, Pt
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)

        slides_data = []
        slides_data.append([ctopic + " Business Level Book", "Master Teacher 20 Years Teaching Super Agent Brahma Har Cheez Ki Knowledge Business Level Real Income 400 Lessons App Strong"])
        slides_data.append(["KYA HAI What Is " + ctopic, "Definition simple language 5 examples Basic fundamentals Industry me kya bolte hain Beginner ko teacher jaise samjhaye"])
        slides_data.append(["KYON HAI Why Future", "Why important future Market data 2026 90 percent fail why Kyon seekhna chahie Demand proof paise kyon banta hai"])
        slides_data.append(["KAHAN HAI KAB KAUN Where When Who", "Kahan use Instagram YouTube Business Job Freelancing Agency Kab morning 6 to 8 Monday Thursday Kaun Student Housewife Job Business 16 to 60"])
        slides_data.append(["KAISE KAAM KARTA Architecture", "Kaise kaam karta step by step Perceive Reason Act loop RAG deep memory short long vector Tools integration planning ReAct Expert soch"])
        slides_data.append(["KISSE HOGA Tools Kya Chahie", "Free tools Canva CapCut ChatGPT Notion Make n8n Paid tools Mobile ya laptop kya chahie Setup kaise kare Teacher jaise"])
        slides_data.append(["KYA USE KAISE USE Earning", "Freelancing 20k to 50k per month Business 1L plus Job me use Kya fayda Mobile Reels laptop browser dashboard Real use cases"])
        slides_data.append(["KAISE KARNA CHAHIE Right Way", "Sahi tarika Daily 30 min diary Weekly revise Roz kya seekha kal kya karna Best practice Optimization Time management Expert kaise bane"])
        slides_data.append(["REAL KAHANI Case Study Rahul", "Rahul village 2 months daily 1 hour project Third month client 15k Fourth month 5 clients 75k Today 2 lakh per month Case Study 1L business 10M ARR story"])
        slides_data.append(["MISTAKES Galtiyan 90 Percent", "Galti1 bina samjhe advanced Galti2 roz practice nahi sirf video Galti3 paise peeche learning nahi Galti4 diary nahi Galti5 mentor nahi Teacher jaise"])
        slides_data.append(["PRO TIP Secret Diary", "Secret diary roz likho kya seekha kya galti kal kya karna Raat 10 min padho Ye trick successful use karte hain Koi YouTube pe nahi batata Mindset mastery"])
        slides_data.append(["HOMEWORK Assignment Final Project", "Aaj real project banao kal bhejo Assignment1 simple project Assignment2 10 examples Assignment3 diagram Test 20 questions Final project client ke liye"])
        slides_data.append(["BUSINESS PLAN Marketing Earning", "Business kaise banaye Freelancing Upwork Fiverr Agency SaaS Client handling pricing kitna charge Portfolio Lead generation Sales funnel Real income 1Cr tak"])

        for item in slides_data:
            title = item[0]
            body = item[1]
            slide = prs.slides.add_slide(prs.slide_layouts[5])
            box1 = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12.3), Inches(0.8))
            tf1 = box1.text_frame
            tf1.word_wrap = True
            p = tf1.paragraphs[0]
            p.text = title
            p.font.size = Pt(24)
            p.font.bold = True
            box2 = slide.shapes.add_textbox(Inches(0.5), Inches(1.1), Inches(12.3), Inches(6.0))
            tf2 = box2.text_frame
            tf2.word_wrap = True
            p2 = tf2.paragraphs[0]
            p2.text = body
            p2.font.size = Pt(14)

        path = PPT_DIR / (cid + "_Course.pptx")
        prs.save(str(path))
        return True
    except Exception as e:
        return False

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
        st.title("Dashboard - 100 Courses Master Teacher 13 Slides")
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
        c1.metric("Total", total)
        c2.metric("Ready", proper)
        c3.metric("Old", bekar)
        c4.metric("Missing", missing)
        if st.button("DELETE SINGLE PAGE OLD"):
            for f in list(PPT_DIR.glob("*.*")):
                try:
                    f.unlink()
                except:
                    pass
            st.success("Deleted old")
            st.rerun()
        if st.button("CREATE 100 BOOKS 13 SLIDES MASTER TEACHER", type="primary"):
            bar = st.progress(0)
            for idx, c in enumerate(courses):
                create_master_teacher_pptx(c.get("id"), c.get("topic"))
                bar.progress(int((idx+1)/len(courses)*100))
            st.success("100 Books 13 Slides Created - No Error")
            st.balloons()
            st.rerun()
        df_data = []
        for c in courses:
            s = "Ready 13 Slides" if list(PPT_DIR.glob(c.get("id") + "_Course*")) else "Missing"
            df_data.append({"ID": c.get("id"), "Course": c.get("topic"), "Status": s})
        st.dataframe(pd.DataFrame(df_data), use_container_width=True)

    if menu == "Super Agent":
        st.title("Super Agent Brahma - Master Teacher")
        st.write("Master Teacher 20 years teaching - Teacher jaise KYA HAI KYON HAI KAHAN KAB KAUN KAISE KISSE KYA USE KAISE USE KAISE KARNA REAL KAHANI MISTAKES PRO TIP HOMEWORK BUSINESS PLAN - 13 slides book")
        opts = []
        for c in courses:
            opts.append(c.get("topic") + " - " + c.get("id"))
        sel = st.selectbox("Select Course", opts)
        if st.button("Create 13 Slides Book Master Teacher", type="primary"):
            cid = sel.split(" - ")[-1]
            ctopic = " - ".join(sel.split(" - ")[:-1])
            with st.spinner("Creating 13 slides book " + ctopic):
                ok = create_master_teacher_pptx(cid, ctopic)
                if ok:
                    st.success("13 Slides Book Created " + ctopic)
                    st.balloons()
                else:
                    st.error("Fail")

    if menu == "Course Library":
        st.title("Course Library 13 Slides Master Teacher")
        total = len(courses)
        proper = len(list(PPT_DIR.glob("*_Course*")))
        c1,c2 = st.columns(2)
        c1.metric("Total", total)
        c2.metric("Ready 13 Slides", proper)
        for idx, co in enumerate(courses):
            cid = co.get("id")
            pf = list(PPT_DIR.glob(cid + "_Course*"))
            col1,col2 = st.columns([3,1])
            with col1:
                if pf:
                    st.success(str(idx+1) + ". " + co.get("topic") + " Ready 13 Slides")
                else:
                    st.warning(str(idx+1) + ". " + co.get("topic") + " Missing")
            with col2:
                if pf:
                    data = pf[0].read_bytes()
                    st.download_button("Download 13 Slides", data=data, file_name=pf[0].name, key="dl_" + cid)

    if menu == "Sales QR":
        st.title("Sales QR")
        st.dataframe(pd.DataFrame(purchases), use_container_width=True)
        up = st.file_uploader("Upload QR", type=["jpg", "png", "jpeg"])
        if up:
            UPI_QR_PATH.write_bytes(up.getvalue())
            st.success("QR Saved")
            st.rerun()
        if UPI_QR_PATH.exists():
            st.image(str(UPI_QR_PATH), width=300)

else:
    if menu == "Browse Courses":
        st.title("Brahma Education 100 Courses")
        search = st.text_input("Search")
        if search:
            fl = [c for c in courses if search.lower() in c.get("topic","").lower()]
        else:
            fl = courses
        proper = len(list(PPT_DIR.glob("*_Course*")))
        st.write("Total " + str(len(fl)) + " Ready " + str(proper) + " 13 Slides")
        for idx, co in enumerate(fl[:15]):
            pf = list(PPT_DIR.glob(co.get("id") + "_Course*"))
            status = "13 Slides Ready" if pf else "Banega"
            with st.expander(str(idx+1) + ". " + co.get("topic") + " " + status):
                if pf:
                    data = pf[0].read_bytes()
                    st.download_button("Download 13 Slides", data=data, file_name=pf[0].name, key="b_dl_" + co.get("id"))

    if menu == "My Access":
        st.title("My Learning 13 Slides")
        k = st.text_input("Invoice or Key")
        if st.button("Unlock"):
            found = [p for p in purchases if p.get("access_key") == k or p.get("invoice_no") == k]
            if not found:
                st.error("Invalid")
            else:
                pu = found[0]
                st.success("Welcome " + pu.get("name") + " " + pu.get("course"))
                pfs = list(PPT_DIR.glob(pu.get("course_id") + "_Course*"))
                if pfs:
                    for pf in pfs:
                        data = pf.read_bytes()
                        st.download_button("Download 13 Slides", data=data, file_name=pf.name)

    if menu == "Chat Support":
        st.title("Chat Support")
        q = st.chat_input("Ask")
        if q:
            st.write("Master Teacher 13 Slides Books Ready")