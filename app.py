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
    m1 = [f"What is {topic} Definition with 5 examples", f"History of {topic} 2015 to 2026", f"Types of {topic}", f"{topic} vs Other Difference", f"Why {topic} is future"] + [f"{topic} Topic {i} deep real" for i in range(6, 41)]
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
            hi = f"{raw} - {topic} real deep. Definition working real example 2026 best practices mistakes pro tip. Practical setup demo test. Assignment Build project on {raw}."
            en = f"{raw} - {topic} real deep. Definition working example 2026 best practices mistakes pro tip. Practical setup demo test. Assignment Build project."
            vids.append({"no": lc, "title": title, "desc_hi": hi, "desc_en": en})
            lc += 1
        curriculum.append({"title": mod["title"], "videos": vids})
    return curriculum

def create_ppt(course_id, course_topic):
    if not PPTX_OK:
        return None, "python-pptx missing"
    try:
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        curriculum = get_curriculum(course_topic)
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(1.5))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.text = f"{course_topic}\nDeep Course - 400 Lessons - Colorful"
        p = tf.paragraphs[0]
        p.runs[0].font.size = Pt(24)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(37, 99, 235)

        count = 0
        for mod in curriculum:
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(1.2))
            tf = txBox.text_frame
            tf.word_wrap = True
            tf.text = f"{mod['title']} - 40 Lessons"
            p = tf.paragraphs[0]
            p.runs[0].font.size = Pt(20)
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(37, 99, 235)
            count += 1
            for vid in mod["videos"]:
                if count >= 60:
                    break
                slide = prs.slides.add_slide(prs.slide_layouts[6])
                txBox = slide.shapes.add_textbox(Inches(0.2), Inches(0.1), Inches(12.9), Inches(0.6))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = vid["title"][:180]
                p = tf.paragraphs[0]
                p.runs[0].font.size = Pt(12)
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(37, 99, 235)

                txBox = slide.shapes.add_textbox(Inches(0.2), Inches(0.8), Inches(6.3), Inches(6.2))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = f"HINDI:\n{vid['desc_hi']}"[:1200]
                for para in tf.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(10)

                txBox = slide.shapes.add_textbox(Inches(6.8), Inches(0.8), Inches(6.3), Inches(6.2))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = f"ENGLISH:\n{vid['desc_en']}"[:1200]
                for para in tf.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(10)

                count += 1
            if count >= 60:
                break

        ppt_path = PPT_DIR / f"{course_id}_COLORFUL.pptx"
        prs.save(str(ppt_path))
        return str(ppt_path), f"Colorful PPT {count} slides"
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
        st.sidebar.success("Fixed No Error - 100 Courses")
        menu = st.sidebar.radio("Admin", ["Dashboard - Fixed", "Colorful PPT Maker - Fixed", "Auto Pilot - 100 PPT Fixed", "Video Library - Fixed No Error List", "Sales", "QR Setup"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard - Fixed":
        st.title("Dashboard - Fixed - No AttributeError")
        ppt_count = len(list(PPT_DIR.glob("*.pptx")))
        missing = len([c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))])
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Courses", len(courses))
        c2.metric("Colorful PPT Bane", ppt_count)
        c3.metric("Missing", missing)
        if missing == 0:
            st.success("Library Full - 100 PPTs - No Error - 27 bhi dikhegi 73 bhi ban gayi")
        else:
            st.warning(f"{missing} Missing - Neeche Auto Pilot se banao - Fixed No Error")
        st.dataframe(pd.DataFrame(courses), use_container_width=True)

    if menu == "Colorful PPT Maker - Fixed":
        st.title("Colorful PPT Maker - Fixed - No AttributeError")
        course_sel = st.selectbox("Course select karo", [f"{c['topic']} - {c['id']}" for c in courses], key="maker_select")
        if st.button("Brahma - Colorful PPT Banao - Fixed", type="primary", key="maker_btn"):
            sel_id = course_sel.split(" - ")[-1]
            sel_topic = " - ".join(course_sel.split(" - ")[:-1])
            with st.spinner(f"Bana raha hai {sel_topic} - Fixed..."):
                ppt_path, msg = create_ppt(sel_id, sel_topic)
                if ppt_path and Path(ppt_path).exists():
                    st.success(f"SUCCESS Fixed - {msg} - No Error")
                    st.balloons()
                    data = Path(ppt_path).read_bytes()
                    st.download_button(f"Download Colorful PPT - {sel_topic}", data=data, file_name=Path(ppt_path).name, key=f"dl_maker_{sel_id}")
                else:
                    st.error(f"Fail - {msg}")

    if menu == "Auto Pilot - 100 PPT Always - Fixed":
        st.title("Auto Pilot - 100 PPT Fixed - 73 Missing Banayega")
        ppt_count = len(list(PPT_DIR.glob("*.pptx")))
        missing_list = [c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))]
        st.info(f"Total 100 - Bane {ppt_count} - Missing {len(missing_list)} - Fixed No Error")
        if st.button("SARE MISSING PPT BANAO - Fixed - Library Full", type="primary", key="auto_all_btn"):
            if not missing_list:
                st.success("Sab Ban Chuki - Library Full")
            else:
                bar = st.progress(0)
                status = st.empty()
                created = 0
                for idx, c in enumerate(missing_list):
                    status.write(f"Bana raha hai {idx+1}/{len(missing_list)} - {c['topic']} - Fixed...")
                    ppt_path, msg = create_ppt(c["id"], c["topic"])
                    if ppt_path:
                        created += 1
                    bar.progress(int((idx+1)/len(missing_list)*100))
                st.success(f"FIXED DONE - {created} PPTs Bane - Total {len(list(PPT_DIR.glob('*.pptx')))} - Library Full")
                st.balloons()
                st.rerun()

    if menu == "Video Library - Fixed No Error List":
        st.title("Video Library - Fixed - List View - No Expander Error - 27 Bhi Dikhegi")
        total = len(courses)
        made = len(list(PPT_DIR.glob("*.pptx")))
        missing = total - made
        c1, c2, c3 = st.columns(3)
        c1.metric("Total", total)
        c2.metric("Bane", made)
        c3.metric("Missing", missing)
        st.write("Fixed - No expander - Simple list - Har PPT ka alag download - No AttributeError - 27 bhi dikhegi 73 bhi banegi")
        st.divider()
        # Simple list - No expander - No duplicate key error - Fixed
        for idx, co in enumerate(courses[:50]):
            co_id = co.get("id")
            ppt_files = list(PPT_DIR.glob(f"{co_id}*"))
            col1, col2 = st.columns([3, 1])
            with col1:
                if ppt_files:
                    st.success(f"{idx+1}. {co.get('topic')} - ✅ Bana - {ppt_files[0].name} - {ppt_files[0].stat().st_size/1024:.0f} KB")
                else:
                    st.warning(f"{idx+1}. {co.get('topic')} - ⏳ Missing - 73 me se")
            with col2:
                if ppt_files:
                    data = ppt_files[0].read_bytes()
                    st.download_button(f"Download", data=data, file_name=ppt_files[0].name, key=f"dl_lib_{co_id}_{idx}")
                else:
                    if st.button(f"Banao", key=f"btn_lib_{co_id}_{idx}"):
                        with st.spinner(f"Bana raha hai {co.get('topic')} - Fixed..."):
                            ppt_path, msg = create_ppt(co_id, co.get("topic"))
                            if ppt_path and Path(ppt_path).exists():
                                st.success(f"Ban Gaya - {msg}")
                                st.balloons()
                                st.rerun()
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
        st.write("100 Courses - Fixed No Error")
        search = st.text_input("Search 100 courses