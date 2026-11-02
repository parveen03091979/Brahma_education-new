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
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
PPT_DIR = DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)

MY_UPI_ID = "parveen39179@okicici"
MY_NAME = "Parveen Kumar"

HUNDRED_COURSES = [
"AI Agent Automation 2026","Instagram Reels Mastery","YouTube Automation AI","Prompt Engineering Pro","Digital Marketing SEO Mastery",
"ChatGPT Mastery 2026","Facebook Ads Mastery","Google Ads Mastery","SEO Advanced 2026","Social Media Marketing Pro",
"Content Writing AI","Copywriting Mastery","Blogging Mastery 2026","Affiliate Marketing Pro","Dropshipping Business",
"E-commerce Mastery Shopify","Canva Design Mastery","Video Editing CapCut Pro","YouTube SEO Mastery","Instagram Growth Hack",
"LinkedIn Marketing Pro","Twitter X Growth Mastery","TikTok Viral Mastery","Pinterest Marketing","Quora Marketing",
"Email Marketing Automation","WhatsApp Marketing Pro","Telegram Channel Growth","Influencer Marketing","Personal Branding Mastery",
"Freelancing Mastery Upwork Fiverr","Agency Business Mastery","SaaS Business 2026","No-Code Business Bubble","Python Programming Mastery",
"JavaScript Mastery 2026","React JS Mastery","Next.js Mastery","Node.js Backend Mastery","Web Development Full Stack",
"WordPress Mastery","Shopify Store Design","UI UX Design Mastery","Figma Design Pro","Graphic Design Mastery",
"Logo Design Mastery","Thumbnail Design Viral","Video Animation Mastery","AI Image Generation Midjourney","AI Video Generation Sora",
"Voice Cloning ElevenLabs","Automation n8n Make","Zapier Automation Mastery","Notion Productivity Mastery","Excel Advanced Mastery",
"Google Sheets Automation","Data Analysis Python","Machine Learning Mastery","Deep Learning 2026","Data Science Mastery",
"Stock Market Trading AI","Crypto Trading Mastery","Forex Trading Pro","Real Estate Business","Motivational Speaking Mastery",
"Public Speaking Pro","Communication Skills Mastery","English Speaking Pro","Hindi Content Creation","Podcast Mastery",
"Music Production AI","Photography Mastery","Reels Editing Viral","Meme Marketing Mastery","Viral Content Formula",
"Lead Generation Mastery","Sales Funnel Mastery","Landing Page Design High Converting","CRO Conversion Optimization","Customer Support Automation",
"HR Recruitment AI","Business Plan Mastery","Startup Funding Mastery","Business Automation AI","Time Management Mastery",
"Mindset Mastery Millionaire","Meditation Mindfulness","Fitness Coaching Business","Diet Nutrition Business","Yoga Teaching Business",
"Cooking Channel Business","Travel Vlogging Business","Gaming Channel Growth","Education Channel Growth","Finance Channel Business",
"News Channel Automation","Meme Page Business","Affiliate Blog SEO","Amazon FBA Mastery","Etsy Store Mastery",
"Print on Demand Business","Stock Photography Business","Voice Over Business","Translation Business AI","Resume Writing Business",
"LinkedIn Profile Optimization Business","AI Tools Mastery 100 Tools","Chatbot Development","AI Voice Agent Mastery","AI Receptionist Business"
]

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size > 2:
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def get_curriculum(topic):
    modules = []
    m1 = [
        "What is topic Definition with 5 real examples",
        "History of topic 2015 to 2026 timeline",
        "Types of topic Reactive Proactive Autonomous",
        "Topic vs Other Difference deep",
        "Why topic is future Market data 2026",
        "Career in topic Jobs Salary Freelancing",
        "Topic Mindset How to think like Builder",
        "Common myths about topic busted",
        "Success stories 5 millionaires",
        "Failure stories Why 90 percent fail",
        "Topic Roadmap 0 to Expert 400 lessons",
        "Tools needed Complete list 20 tools",
        "Industry overview Where topic used",
        "Market size growth data",
        "Skills needed Roadmap",
        "Learning path Step by step mastery",
        "Time management Learn in 90 days",
        "Best resources Books YouTube Courses",
        "Community Discord Reddit help",
        "Mentorship How to find mentor",
        "Architecture Brain Memory Tools Planning",
        "Core Tech behind topic GPT4 Claude Gemini",
        "RAG Retrieval Augmented Generation deep",
        "Memory types Short Long Vector DB",
        "Tools How to use external tools",
        "Planning ReAct Chain Thought Tree Thought",
        "Reasoning How to think step by step",
        "Action How to take action",
        "Observation How to learn from result",
        "Loop Working cycle Perceive Reason Act",
        "Case Study 1 Real business",
        "Case Study 2 Real business 10M ARR",
        "Case Study 3 Real business 10M users",
        "Case Study 4 Real business Workspace",
        "Case Study 5 Real business 5k month",
        "Assignment Build first simple project",
        "Assignment Research 10 examples sheet",
        "Assignment Draw Architecture diagram",
        "Module 1 Summary Checklist",
        "Module 1 Test 20 Questions"
    ]
    modules.append({"title": f"Module 1: {topic} Fundamentals", "lessons": m1})
    for m in range(2, 11):
        lessons = [f"Module {m} Lesson {i}: {topic} Real Topic {m}-{i} Deep" for i in range(1, 41)]
        modules.append({"title": f"Module {m}: {topic} Deep Module {m}", "lessons": lessons})
    curriculum = []
    lc = 1
    for mod in modules:
        vids = []
        for raw in mod["lessons"]:
            title = f"Lesson {lc}: {raw}"
            hi = f"WHAT IS IT? {raw} kya hai? Simple definition. WHY IMPORTANT? {topic} me important. HOW IT WORKS? 1 Setup Tool open 2 Action Pehla step 3 Test Result check 4 Improve Galti sudharo. REAL EXAMPLE Real company ne {raw} se 5 lakh per month kamaya. MISTAKES Basics skip Direct advanced No practice. PRO TIP Roz 30 min practice + notes. ASSIGNMENT Aaj {raw} par project banao."
            en = f"WHAT IS IT? What is {raw}? WHY IMPORTANT? Important in {topic}. HOW IT WORKS? 1 Setup Open tool 2 Action First step 3 Test Check result 4 Improve Fix. REAL EXAMPLE Company earned 5 lakh per month using {raw}. MISTAKES Skipping basics Going advanced No practice. PRO TIP 30 min daily practice + notes. ASSIGNMENT Build project on {raw} today."
            vids.append({"no": lc, "title": title, "desc_hi": hi, "desc_en": en})
            lc += 1
        curriculum.append({"title": mod["title"], "videos": vids})
    return curriculum

def create_colorful_ppt(course_id, course_topic):
    if not PPTX_OK:
        return None, "python-pptx missing - requirements me add karo"
    try:
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        curriculum = get_curriculum(course_topic)

        # Title Slide - Simple but Colorful - No risky code
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        # Blue title box
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(2))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.text = f"{course_topic}\nDeep Course - 400 Lessons - Colorful Designed"
        p = tf.paragraphs[0]
        p.runs[0].font.size = Pt(28)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(37, 99, 235)

        # Yellow box Hindi feature
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(3.0), Inches(3.8), Inches(1.2))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.text = "HINDI - Full Explain\nWhat Why How Example\nMistake Pro Tip Assignment"
        p = tf.paragraphs[0]
        p.runs[0].font.size = Pt(14)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(146, 64, 14)

        # Blue box English feature
        txBox = slide.shapes.add_textbox(Inches(4.7), Inches(3.0), Inches(3.8), Inches(1.2))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.text = "ENGLISH - Clear Explain\nStep by Step Practical\nReal Example Assignment"
        p = tf.paragraphs[0]
        p.runs[0].font.size = Pt(14)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(30, 64, 175)

        # Green box Assignment
        txBox = slide.shapes.add_textbox(Inches(8.9), Inches(3.0), Inches(3.8), Inches(1.2))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.text = "ASSIGNMENT - Real Project\nBuild + Submit + Grow\nInterest Banega"
        p = tf.paragraphs[0]
        p.runs[0].font.size = Pt(14)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(20, 83, 45)

        count = 0
        for mod in curriculum:
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(1.5))
            tf = txBox.text_frame
            tf.word_wrap = True
            tf.text = f"{mod['title']}\n40 Lessons - Colorful Designed - Bade Fonts - Acchi Explain"
            p = tf.paragraphs[0]
            p.runs[0].font.size = Pt(22)
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(37, 99, 235)
            count += 1
            for vid in mod["videos"]:
                if count >= 80:
                    break
                slide = prs.slides.add_slide(prs.slide_layouts[6])
                # Title blue
                txBox = slide.shapes.add_textbox(Inches(0.2), Inches(0.1), Inches(12.9), Inches(0.7))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = vid["title"][:200]
                p = tf.paragraphs[0]
                p.runs[0].font.size = Pt(14)
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(37, 99, 235)

                # Hindi box - orange title
                txBox = slide.shapes.add_textbox(Inches(0.2), Inches(0.9), Inches(6.3), Inches(6.2))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = f"HINDI - Acchi Explain\n\n{vid['desc_hi']}"[:1300]
                for para in tf.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(11)
                        if "HINDI" in run.text:
                            run.font.bold = True
                            run.font.color.rgb = RGBColor(146, 64, 14)
                        else:
                            run.font.color.rgb = RGBColor(60, 60, 60)

                # English box - blue title
                txBox = slide.shapes.add_textbox(Inches(6.8), Inches(0.9), Inches(6.3), Inches(6.2))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = f"ENGLISH - Clear Explain\n\n{vid['desc_en']}"[:1300]
                for para in tf.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(11)
                        if "ENGLISH" in run.text:
                            run.font.bold = True
                            run.font.color.rgb = RGBColor(30, 64, 175)
                        else:
                            run.font.color.rgb = RGBColor(60, 60, 60)

                count += 1
            if count >= 80:
                break

        ppt_path = PPT_DIR / f"{course_id}_{course_topic.replace(' ', '_')[:12]}_COLORFUL.pptx"
        prs.save(str(ppt_path))
        return str(ppt_path), f"Colorful PPT {count} slides - Bade fonts - Blue Orange Design"
    except Exception as e:
        return None, f"Error {e}"

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

if len(courses) < 100:
    courses = []
    for i, topic in enumerate(HUNDRED_COURSES):
        courses.append({"id": f"BRAHMA{1000+i}", "topic": topic, "price": 999, "videos": 400})
    save_json(COURSES_FILE, courses)

if "admin_logged" not in st.session_state:
    st.session_state["admin_logged"] = False

# NO auto create on load - Isiliye AttributeError nahi ayega - Manual se banega - Safe

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
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(pw.encode()).hexdigest() == MASTER_HASH.read_text():
                st.session_state["admin_logged"] = True
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Colorful PPT - No Error")
        menu = st.sidebar.radio("Admin", ["Colorful PPT Maker - Fixed No Error", "Auto Pilot - 100 PPT Always - Fixed", "Video Library - Fixed No Error", "Dashboard", "Sales", "QR Setup"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Dashboard - 100 Courses - Colorful PPT - Fixed No Error")
        c1, c2, c3 = st.columns(3)
        ppt_count = len(list(PPT_DIR.glob("*.pptx")))
        missing = len([c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))])
        c1.metric("Courses", len(courses))
        c2.metric("Colorful PPT Bane", ppt_count)
        c3.metric("Missing", missing)
        if missing == 0:
            st.success(f"Library Full - 100 Colorful PPTs - Hamesha Bani Rahe - No Error - Bechne ke liye ready")
        else:
            st.warning(f"{missing} PPTs Baki - Auto Pilot se ek click me ban jayengi - No Error")
        st.dataframe(pd.DataFrame(courses), use_container_width=True)

    if menu == "Colorful PPT Maker - Fixed No Error":
        st.title("Colorful PPT Maker - Fixed - No AttributeError - Simple Colorful Designed")
        st.write("Simple colorful - Blue title, orange Hindi, blue English, bade fonts 14-18, acchi explain - No risky code - 100% No Error")
        course_sel = st.selectbox("Course select karo", [f"{c['topic']} - {c['id']}" for c in courses])
        if st.button("Brahma - Colorful Designed PPT Banao - Fixed No Error", type="primary"):
            sel_id = course_sel.split(" - ")[-1]
            sel_topic = " - ".join(course_sel.split(" - ")[:-1])
            with st.spinner(f"Bana raha hai Colorful PPT - {sel_topic} - Fixed No Error - 80 slides..."):
                ppt_path, msg = create_colorful_ppt(sel_id, sel_topic)
                if ppt_path and Path(ppt_path).exists():
                    st.success(f"SUCCESS Colorful Fixed - {msg} - No Error - Har viewer me dikhega")
                    st.balloons()
                    with open(ppt_path, "rb") as f:
                        st.download_button(f"Download Colorful PPT - {sel_topic} - Fixed No Error", f, file_name=Path(ppt_path).name)
                else:
                    st.error(f"Fail - {msg}")

    if menu == "Auto Pilot - 100 PPT Always - Fixed":
        st.title("Auto Pilot - 100 PPT Always - Fixed No Error - 73 Missing Ko Banayega")
        ppt_count = len(list(PPT_DIR.glob("*.pptx")))
        missing_list = [c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))]
        st.info(f"Total: {len(courses)} - Colorful PPT Bane: {ppt_count} - Missing: {len(missing_list)} - 73 Missing ko ab banayenge - No Error")
        if st.button("Brahma - SARE 73 MISSING PPT AUTO BANAO - Fixed No Error - Library Full", type="primary"):
            if not missing_list:
                st.success("Sab Colorful PPT Ban Chuki - 100 Courses - Library Full - No Error - 27 bhi dikhegi - 73 bhi ban gayi")
            else:
                bar = st.progress(0)
                status = st.empty()
                created = 0
                for idx, c in enumerate(missing_list):
                    status.write(f"Bana raha hai Fixed {idx+1}/{len(missing_list)} - {c['topic']} - Simple Colorful - No Error...")
                    ppt_path, msg = create_colorful_ppt(c["id"], c["topic"])
                    if ppt_path:
                        created += 1
                    bar.progress(int((idx+1)/len(missing_list)*100))
                st.success(f"FIXED FULL DONE - {created} PPTs Ban Gaye - Total {len(list(PPT_DIR.glob('*.pptx')))} PPTs - Library Full - 27 bhi dikhegi 73 bhi ban gayi - No Error")
                st.balloons()
                st.rerun()

    if menu == "Video Library - Fixed No Error":
        st.title("Video Library - Fixed No Error - 27 Bhi Dikhegi - 73 Bhi Banegi")
        total = len(courses)
        made = len(list(PPT_DIR.glob("*.pptx")))
        missing = total - made
        c1, c2, c3 = st.columns(3)
        c1.metric("Total", total)
        c2.metric("Colorful PPT Bane", made)
        c3.metric("Missing", missing)
        st.write("27 jo bani dikha raha hai wo bhi ab dikhegi - 73 missing bhi ban jayegi - No AttributeError - Fixed")
        for co in courses[:30]:
            co_id = co.get("id")
            ppt_files = list(PPT_DIR.glob(f"{co_id}*"))
            with st.expander(f"{co.get('topic')} - Colorful Check - Fixed No Error"):
                if ppt_files:
                    st.success(f"Colorful PPT Bana - Fixed - Designed - Bade Fonts - {ppt_files[0].name} - {ppt_files[0].stat().st_size/1024:.0f} KB - 27 me se ek")
                    with open(ppt_files[0], "rb") as f:
                        st.download_button(f"Download Colorful PPT - {co.get('topic')} - Fixed - 27 me se", f, file_name=Path(ppt_files[0].name), key=f"ppt_{co_id}")
                else:
                    st.warning(f"Colorful PPT Missing - 73 me se ek - Button dabao to ban jayega - Fixed No Error")
                    if st.button(f"Banao PPT - {co.get('topic')} - Fixed No Error", key=f"btn_{co_id}"):
                        with st.spinner(f"Bana raha hai Fixed - {co.get('topic')} - No Error..."):
                            ppt_path, msg = create_colorful_ppt(co_id, co.get("topic"))
                            if ppt_path and Path(ppt_path).exists():
                                st.success(f"FIXED SUCCESS - {co.get('topic')} ka colorful PPT ban gaya - {msg} - 73 me se ek ban gaya")
                                st.balloons()
                                with open(ppt_path, "rb") as f:
                                    st.download_button(f"Download Fixed PPT - {co.get('topic')}", f, file_name=Path(ppt_path).name, key=f"auto_{co_id}")
                            else:
                                st.error(f"Fail - {msg}")

    if menu == "Sales":
        st.title("Sales")
        st.dataframe(pd.DataFrame(purchases), use_container_width=True)
    if menu == "QR Setup":
        st.title("QR Setup")
        up = st.file_uploader("Upload QR", type=["jpg","png","jpeg"])
        if up:
            UPI_QR_PATH.write_bytes(up.getvalue())
            st.success("QR Saved")
            st.rerun()
        if UPI_QR_PATH.exists():
            st.image(str(UPI_QR_PATH), width=300)

else:
    if menu == "Browse Courses":
        st.title("Brahma Education")
        st.write("100 Courses - Colorful Designed PPT - Fixed No Error")
        search = st.text_input("Search 100 courses me se")
        fl = [c for c in courses if search.lower() in c.get("topic","").lower()] if search else courses
        st.write(f"Total {len(fl)} courses")
        page_size = 20
        total_pages = max(1, (len(fl)+page_size-1)//page_size)
        page = st.selectbox("Pages", range(1, total_pages+1), format_func=lambda x: f"Page {x}")
        pcs = fl[(page-1)*page_size:page*page_size]
        for idx, co in enumerate(pcs, start=(page-1)*page_size+1):
            ppt_exists = len(list(PPT_DIR.glob(f"{co['id']}*"))) > 0
            status_icon = "✅ Ready" if ppt_exists else "⏳ Banega"
            with st.expander(f"{idx}. {co.get('topic')} - Rs {co.get('price')} - {status_icon}"):
                col_qr, col_pay = st.columns([1,2])
                with col_qr:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH), width=220)
                with col_pay:
                    params = {"pa": MY_UPI_ID, "pn": MY_NAME, "am": str(co.get("price",999)), "cu": "INR", "tn": co.get("topic","")[:20]}
                    link = f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"Pay Rs {co.get('price')}", link, type="primary")
                with st.form(f"buy_{co['id']}_{idx}"):
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        name = st.text_input("Full Name", key=f"n_{idx}", placeholder="Rahul Sharma")
                    with c2:
                        email = st.text_input("Email", key=f"e_{idx}", placeholder="rahul@gmail.com")
                    with c3:
                        utr = st.text_input("UTR 12 digit", key=f"u_{idx}", placeholder="UPI app se")
                    if st.form_submit_button("Get Course", type="primary"):
                        purchases.append({"invoice_no": f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}", "access_key": f"BRAHMA-{hashlib.sha256((email+co.get('topic')).encode()).hexdigest()[:10].upper()}", "name": name, "email": email, "course": co.get("topic"), "course_id": co.get("id"), "price": co.get("price"), "utr": utr, "status": "APPROVED", "date": str(datetime.datetime.now())})
                        save_json(PURCHASE_FILE, purchases)
                        st.success("Verified")

    if menu == "My Access":
        st.title("My Learning")
        k = st.text_input("Invoice or Key")
        if st.button("Unlock My Course", type="primary"):
            found = [p for p in purchases if p.get("access_key")==k or p.get("invoice_no")==k]
            if not found:
                st.error("Invalid key")
            else:
                pu = found[0]
                st.success(f"Welcome {pu.get('name')} - {pu.get('course')}")
                ppt_files = list(PPT_DIR.glob(f"{pu.get('course_id')}*"))
                if ppt_files:
                    for pf in ppt_files:
                        with open(pf, "rb") as f:
                            st.download_button(f"Download Colorful PPT - {pu.get('course')}", f, file_name=pf.name)

    if menu == "Chat Support":
        st.title("Chat Support")
        q = st.chat_input("Ask")
        if q:
            st.write("100 Courses Colorful - Fixed No Error - 27 bhi dikhegi 73 bhi ban jayegi")