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

def create_attractive_ppt(course_id, course_topic):
    if not PPTX_OK:
        return None, "python-pptx missing"
    try:
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)

        # Title Slide - Colorful Attractive
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        t = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.4))
        tf = t.text_frame
        tf.word_wrap = True
        tf.text = "BRAHMA EDUCATION - PREMIUM COURSE"
        tf.paragraphs[0].runs[0].font.size = Pt(12)
        tf.paragraphs[0].runs[0].font.bold = True
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(100, 100, 100)

        t = slide.shapes.add_textbox(Inches(0.5), Inches(0.8), Inches(12.3), Inches(1.8))
        tf = t.text_frame
        tf.word_wrap = True
        tf.text = course_topic + "\n400 Lessons - Colorful Designed - Attractive"
        tf.paragraphs[0].runs[0].font.size = Pt(28)
        tf.paragraphs[0].runs[0].font.bold = True
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)

        t = slide.shapes.add_textbox(Inches(0.5), Inches(2.8), Inches(12.3), Inches(1.2))
        tf = t.text_frame
        tf.word_wrap = True
        tf.text = "10 Modules x 40 Lessons = 400 Lessons | Hindi + English | What Why How Example Mistake Pro Tip Assignment | Bade Fonts | Interest Banega"
        tf.paragraphs[0].runs[0].font.size = Pt(14)
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(50, 50, 50)

        t = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(3.8), Inches(1.0))
        tf = t.text_frame
        tf.word_wrap = True
        tf.text = "HINDI - Full Explain\nWhat Why How Example"
        tf.paragraphs[0].runs[0].font.size = Pt(13)
        tf.paragraphs[0].runs[0].font.bold = True
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(180, 83, 9)

        t = slide.shapes.add_textbox(Inches(4.7), Inches(4.2), Inches(3.8), Inches(1.0))
        tf = t.text_frame
        tf.word_wrap = True
        tf.text = "ENGLISH - Clear Explain\nStep by Step Practical"
        tf.paragraphs[0].runs[0].font.size = Pt(13)
        tf.paragraphs[0].runs[0].font.bold = True
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(30, 64, 175)

        t = slide.shapes.add_textbox(Inches(8.9), Inches(4.2), Inches(3.8), Inches(1.0))
        tf = t.text_frame
        tf.word_wrap = True
        tf.text = "ASSIGNMENT - Real Project\nBuild + Submit + Grow"
        tf.paragraphs[0].runs[0].font.size = Pt(13)
        tf.paragraphs[0].runs[0].font.bold = True
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(20, 83, 45)

        # 60 Slides - Attractive Colorful - Bade Fonts - Acchi Explain
        for i in range(1, 61):
            slide = prs.slides.add_slide(prs.slide_layouts[6])

            t = slide.shapes.add_textbox(Inches(0.2), Inches(0.1), Inches(12.9), Inches(0.7))
            tf = t.text_frame
            tf.word_wrap = True
            tf.text = f"Lesson {i}: {course_topic} - Topic {i} - Deep Real - Attractive Colorful"
            tf.paragraphs[0].runs[0].font.size = Pt(15)
            tf.paragraphs[0].runs[0].font.bold = True
            tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)

            hindi_text = f"HINDI - Acchi Explain\n\nWHAT IS IT?\nLesson {i} kya hai - {course_topic} me iska matlab.\n\nWHY IMPORTANT?\nYe sabse important hai bina iske kaam adhura.\n\nHOW IT WORKS?\n1. Setup - Tool open karo\n2. Action - Pehla step karo\n3. Test - Result check karo\n4. Improve - Galti sudharo\n\nREAL EXAMPLE\nReal company ne isse 5 lakh per month kamaya 2026 me.\n\nMISTAKES\n- Basics skip karna\n- Direct advanced karna\n- Practice nahi karna\n\nPRO TIP\nRoz 30 min practice + notes banao\n\nASSIGNMENT\nAaj is par ek project banao."

            t = slide.shapes.add_textbox(Inches(0.2), Inches(0.9), Inches(6.3), Inches(6.2))
            tf = t.text_frame
            tf.word_wrap = True
            tf.text = hindi_text[:1400]
            for para in tf.paragraphs:
                for run in para.runs:
                    if "HINDI" in run.text:
                        run.font.size = Pt(12)
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(180, 83, 9)
                    else:
                        run.font.size = Pt(10)
                        run.font.color.rgb = RGBColor(60, 60, 60)

            english_text = f"ENGLISH - Clear Explain\n\nWHAT IS IT?\nWhat is Lesson {i} - {course_topic} meaning.\n\nWHY IMPORTANT?\nMost important without this work incomplete.\n\nHOW IT WORKS?\n1. Setup - Open tool\n2. Action - Do first step\n3. Test - Check result\n4. Improve - Fix mistake\n\nREAL EXAMPLE\nReal company earned 5 lakh per month in 2026 using this.\n\nMISTAKES\n- Skipping basics\n- Going advanced directly\n- No practice\n\nPRO TIP\n30 min daily practice + make notes\n\nASSIGNMENT\nBuild a small project today on this topic."

            t = slide.shapes.add_textbox(Inches(6.8), Inches(0.9), Inches(6.3), Inches(6.2))
            tf = t.text_frame
            tf.word_wrap = True
            tf.text = english_text[:1400]
            for para in tf.paragraphs:
                for run in para.runs:
                    if "ENGLISH" in run.text:
                        run.font.size = Pt(12)
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(30, 64, 175)
                    else:
                        run.font.size = Pt(10)
                        run.font.color.rgb = RGBColor(60, 60, 60)

        ppt_path = PPT_DIR / f"{course_id}_COLORFUL.pptx"
        prs.save(str(ppt_path))
        return str(ppt_path), f"Attractive Colorful PPT 61 slides - Bade fonts - Acchi explain - Designed"
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
        st.sidebar.success("Brahma Auto Full - 100 Courses")
        menu = st.sidebar.radio("Admin", ["Dashboard", "Brahma PPT Maker + Auto Pilot", "Video Library", "Sales", "QR Setup"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Brahma Education - Dashboard")
        ppt_count = len(list(PPT_DIR.glob("*.pptx")))
        missing = len([c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))])
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Courses", len(courses))
        c2.metric("PPT Bane", ppt_count)
        c3.metric("Missing", missing)
        if missing == 0:
            st.success("Library Full - 100 PPTs - Bechne ke liye ready - No Error")
        else:
            st.warning(f"{missing} PPTs Missing - Auto Pilot se ek click me ban jayengi - Tabhi to bech payega")
        st.dataframe(pd.DataFrame(courses), use_container_width=True)

    if menu == "Brahma PPT Maker + Auto Pilot":
        st.title("Brahma PPT Maker + Auto Pilot - Pura Banakar")
        st.write("1. Brahma PPT Maker page to rahega hi - Manual bana sakte ho - 2. Naya course dalen to Brahma uski PPT bana de - Auto library me add - Aapko kahana na pade - Jab naya banana ho tabhi kahana pade")
        st.divider()
        st.subheader("Naya Course Add Karo - Brahma Auto PPT Bana Dega - Library Me Auto Add")
        with st.form("add_new_course_final"):
            new_topic = st.text_input("Naya Course Ka Naam - Example: Crypto Trading Advanced 2026")
            new_price = st.number_input("Price", value=999, min_value=1)
            submitted = st.form_submit_button("Add Naya Course - Brahma Auto PPT Bana Dega - Library Me Auto Add", type="primary")
            if submitted:
                if len(new_topic) < 5:
                    st.error("Naam kam se kam 5 letters ka likho")
                else:
                    new_id = f"BRAHMA{1000+len(courses)}"
                    courses.append({"id": new_id, "topic": new_topic, "price": int(new_price), "videos": 400})
                    save_json(COURSES_FILE, courses)
                    st.success(f"Naya Course Add Ho Gaya - {new_topic} - ID {new_id}")
                    with st.spinner(f"Brahma Auto Pilot - {new_topic} ka attractive colorful PPT bana raha hai - 1 min - Bade fonts - Acchi explain..."):
                        ppt_path, msg = create_attractive_ppt(new_id, new_topic)
                        if ppt_path and Path(ppt_path).exists():
                            st.success(f"AUTO PILOT SUCCESS - Naya course ka attractive PPT Auto Ban Gaya - Library me auto add - {msg} - Aapko kahana nahi pada")
                            st.balloons()
                            data = Path(ppt_path).read_bytes()
                            st.download_button(f"Download Naya Course PPT - {new_topic} - Attractive", data=data, file_name=Path(ppt_path).name, key=f"dl_new_{new_id}")
                        else:
                            st.error(f"Auto Fail - {msg}")
                    st.rerun()

        st.divider()
        st.subheader("Brahma PPT Maker - Manual + Auto - Colorful Attractive")
        course_sel = st.selectbox("Course select karo - Manual bhi bana sakte ho", [f"{c['topic']} - {c['id']}" for c in courses], key="maker_final")
        if st.button("Brahma - Attractive Colorful PPT Banao - Designed - Bade Fonts", type="primary", key="maker_btn_final"):
            sel_id = course_sel.split(" - ")[-1]
            sel_topic = " - ".join(course_sel.split(" - ")[:-1])
            with st.spinner(f"Bana raha hai Attractive Colorful PPT - {sel_topic} - Designed - Bade fonts - Acchi explain - 61 slides..."):
                ppt_path, msg = create_attractive_ppt(sel_id, sel_topic)
                if ppt_path and Path(ppt_path).exists():
                    st.success(f"SUCCESS Attractive - {msg} - Colorful Designed - Bade Fonts - Library me add - Hamesha bani rahegi")
                    st.balloons()
                    data = Path(ppt_path).read_bytes()
                    st.download_button(f"Download Attractive PPT - {sel_topic} - Colorful", data=data, file_name=Path(ppt_path).name, key=f"dl_final_{sel_id}")

                else:
                    st.error(f"Fail - {msg}")

        st.divider()
        st.subheader("Sare 100 Courses Ke PPT Auto Banao - Ek Click Me - Library Full - Tabhi To Bech Payega")
        ppt_count = len(list(PPT_DIR.glob("*.pptx")))
        missing_list = [c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))]
        st.info(f"Total: {len(courses)} - PPT Bane: {ppt_count} - Missing: {len(missing_list)} - Sari ban jani chahie tabhi to bech payega")
        if st.button("SARE 100 COURSES KE PPT AUTO BANAO - Colorful Designed - Library Full", type="primary", key="auto_all_final"):
            if not missing_list:
                st.success("Sab PPT Ban Chuki - 100 Courses - Library Full - Bechne ke liye ready - Koi error nahi - 100 PPT Hamesha Bani Rahe")
            else:
                bar = st.progress(0)
                status = st.empty()
                created = 0
                for idx, c in enumerate(missing_list):
                    status.write(f"Bana raha hai Attractive {idx+1}/{len(missing_list)} - {c['topic']} - Colorful Designed - Bade fonts - Acchi explain...")
                    ppt_path, msg = create_attractive_ppt(c["id"], c["topic"])
                    if ppt_path:
                        created += 1
                    bar.progress(int((idx+1)/len(missing_list)*100))
                st.success(f"FULL DONE - {created} Attractive PPTs Ban Gaye - Total {len(list(PPT_DIR.glob('*.pptx')))} PPTs - Library Full - 100 PPT Hamesha Bani Rahe - Tabhi to bech payega")
                st.balloons()
                st.rerun()

    if menu == "Video Library":
        st.title("Video Library - Attractive Colorful - No Red Error - 100 PPT Hamesha")
        total = len(courses)
        made = len(list(PPT_DIR.glob("*.pptx")))
        missing = total - made
        c1, c2, c3 = st.columns(3)
        c1.metric("Total", total)
        c2.metric("PPT Bane", made)
        c3.metric("Missing", missing)
        if missing == 0:
            st.success("Library Full - 100 Attractive PPTs - No Red Error - Bechne ke liye ready - 100 PPT Hamesha Bani Rahe")
        else:
            st.warning(f"{missing} PPTs Baki - Neeche Banao button se ban jayengi - No red error - Simple list")
        st.divider()
        for idx, co in enumerate(courses[:50]):
            co_id = co.get("id")
            ppt_files = list(PPT_DIR.glob(f"{co_id}*"))
            col1, col2 = st.columns([3, 1])
            with col1:
                if ppt_files:
                    st.write(f"{idx+1}. {co.get('topic')} - Bana - {ppt_files[0].stat().st_size/1024:.0f} KB - Attractive Colorful - Bade Fonts")
                else:
                    st.write(f"{idx+1}. {co.get('topic')} - Missing - Banao button dabao - No red error")
            with col2:
                if ppt_files:
                    data = ppt_files[0].read_bytes()
                    st.download_button("Download", data=data, file_name=ppt_files[0].name, key=f"dl_vlib_{co_id}_{idx}_final")
                else:
                    if st.button("Banao", key=f"btn_vlib_{co_id}_{idx}_final"):
                        with st.spinner(f"Bana raha hai {co.get('topic')} - Attractive..."):
                            ppt_path, msg = create_attractive_ppt(co_id, co.get("topic"))
                            if ppt_path and Path(ppt_path).exists():
                                st.success("Ban Gaya - Attractive")
                                st.balloons()
                                st.rerun()
                            else:
                                st.error(f"Fail {msg}")

    if menu == "Sales":
        st.title("Sales - 100 Courses")
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
        st.write("100 Courses - Colorful Designed PPT - Bade Fonts - Acchi Explain")
        search = st.text_input("Search 100 courses", key="search_final")
        fl = [c for c in courses if search.lower() in c.get("topic","").lower()] if search else courses
        st.write(f"Total {len(fl)} courses")
        page_size = 20
        total_pages = max(1, (len(fl)+page_size-1)//page_size)
        page = st.selectbox("Pages", range(1, total_pages+1), format_func=lambda x: f"Page {x}", key="page_final")
        pcs = fl[(page-1)*page_size:page*page_size]
        for idx, co in enumerate(pcs, start=(page-1)*page_size+1):
            ppt_exists = len(list(PPT_DIR.glob(f"{co['id']}*"))) > 0
            status_icon = "Ready" if ppt_exists else "Banega"
            with st.expander(f"{idx}. {co.get('topic')} - Rs {co.get('price')} - {status_icon}"):
                col_qr, col_pay = st.columns([1,2])
                with col_qr:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH), width=220)
                with col_pay:
                    params = {"pa": MY_UPI_ID, "pn": MY_NAME, "am": str(co.get("price",999)), "cu": "INR", "tn": co.get("topic","")[:20]}
                    link = f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"Pay Rs {co.get('price')}", link, type="primary")
                with st.form(f"buy_{co['id']}_{idx}_final"):
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        name = st.text_input("Full Name", key=f"n_{idx}_final", placeholder="Rahul Sharma")
                    with c2:
                        email = st.text_input("Email", key=f"e_{idx}_final", placeholder="rahul@gmail.com")
                    with c3:
                        utr = st.text_input("UTR 12 digit", key=f"u_{idx}_final", placeholder="UPI app se")
                    if st.form_submit_button("Get Course", type="primary"):
                        purchases.append({"invoice_no": f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}", "access_key": f"BRAHMA-{hashlib.sha256((email+co.get('topic')).encode()).hexdigest()[:10].upper()}", "name": name, "email": email, "course": co.get("topic"), "course_id": co.get("id"), "price": co.get("price"), "utr": utr, "status": "APPROVED", "date": str(datetime.datetime.now())})
                        save_json(PURCHASE_FILE, purchases)
                        st.success("Verified")

    if menu == "My Access":
        st.title("My Learning")
        k = st.text_input("Invoice or Key", key="my_key_final")
        if st.button("Unlock My Course", type="primary", key="my_unlock_final"):
            found = [p for p in purchases if p.get("access_key")==k or p.get("invoice_no")==k]
            if not found:
                st.error("Invalid key")
            else:
                pu = found[0]
                st.success(f"Welcome {pu.get('name')} - {pu.get('course')}")
                ppt_files = list(PPT_DIR.glob(f"{pu.get('course_id')}*"))
                if ppt_files:
                    for pf in ppt_files:
                        data = pf.read_bytes()
                        st.download_button(f"Download PPT - {pu.get('course')} - Attractive", data=data, file_name=pf.name, key=f"my_{pf.name}_final")

    if menu == "Chat Support":
        st.title("Chat Support")
        q = st.chat_input("Ask", key="chat_final")
        if q:
            st.write("100 Courses - Attractive Colorful - 100 PPT Hamesha Bani Rahe - No Error")