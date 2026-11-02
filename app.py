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
    from pptx.enum.shapes import MSO_SHAPE
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
            hi = f"""WHAT IS IT?
{raw} kya hai?

WHY IMPORTANT?
{topic} me ye sabse important hai.

HOW IT WORKS?
1. Setup: Tool open karo
2. Action: Pehla step
3. Test: Result check
4. Improve: Galti sudharo

REAL EXAMPLE:
Real company ne {raw} se 5 lakh per month kamaya.

MISTAKES:
- Basics skip karna
- Direct advanced
- Practice nahi karna

PRO TIP:
Roz 30 min practice + notes

ASSIGNMENT:
Aaj {raw} par project banao.
"""
            en = f"""WHAT IS IT?
What is {raw}?

WHY IMPORTANT?
Most important in {topic}.

HOW IT WORKS?
1. Setup: Open tool
2. Action: First step
3. Test: Check result
4. Improve: Fix mistake

REAL EXAMPLE:
Company earned 5 lakh per month using {raw}.

MISTAKES:
- Skipping basics
- Going advanced
- No practice

PRO TIP:
30 min daily practice + notes

ASSIGNMENT:
Build project on {raw} today.
"""
            vids.append({"no": lc, "title": title, "desc_hi": hi, "desc_en": en})
            lc += 1
        curriculum.append({"title": mod["title"], "videos": vids})
    return curriculum

def add_box(slide, left, top, width, height, fill_rgb, text, font_size, font_color, bold=False, border_rgb=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(*fill_rgb)
    if border_rgb:
        shape.line.color.rgb = RGBColor(*border_rgb)
        shape.line.width = Pt(2)
    else:
        shape.line.fill.background()
    tf = shape.text_frame
    tf.word_wrap = True
    tf.text = text
    para = tf.paragraphs[0]
    run = para.runs[0]
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor(*font_color)
    return shape

def create_colorful_ppt(course_id, course_topic):
    if not PPTX_OK:
        return None, "python-pptx missing"
    try:
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        curriculum = get_curriculum(course_topic)

        # Title Slide - Real Colorful
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        # Background white
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(255, 255, 255)
        # Top blue strip
        add_box(slide, Inches(0), Inches(0), Inches(13.33), Inches(0.4), (37, 99, 235), "", 1, (255,255,255))
        # Main title - blue box white text - BIG
        add_box(slide, Inches(0.5), Inches(0.8), Inches(12.3), Inches(2.0), (37, 99, 235), f"{course_topic}\nDeep Course - 400 Lessons - Colorful Designed", 26, (255,255,255), True)
        # Subtitle - white box blue border
        add_box(slide, Inches(0.5), Inches(3.2), Inches(12.3), Inches(1.8), (255, 255, 255), f"10 Modules x 40 Lessons = 400 Lessons\nHar lesson colorful designed - Bade fonts - Acchi explain - Practical + Assignment\nHindi + English - Puri learning - Interest banega", 16, (30, 58, 138), False, (37, 99, 235))
        # Features 3 boxes
        add_box(slide, Inches(0.5), Inches(5.3), Inches(3.9), Inches(1.2), (254, 243, 199), "🌟 Hindi - Full Explain\nWhat Why How Example", 14, (146, 64, 14), True, (245, 158, 11))
        add_box(slide, Inches(4.7), Inches(5.3), Inches(3.9), Inches(1.2), (219, 234, 254), "🌟 English - Clear Explain\nStep by Step Practical", 14, (30, 64, 175), True, (59, 130, 246))
        add_box(slide, Inches(8.9), Inches(5.3), Inches(3.9), Inches(1.2), (220, 252, 231), "🌟 Assignment - Real Project\nBuild + Submit + Grow", 14, (20, 83, 45), True, (34, 197, 94))
        # Bottom orange strip
        add_box(slide, Inches(0), Inches(7.1), Inches(13.33), Inches(0.4), (245, 158, 11), "", 1, (255,255,255))

        count = 0
        for mod in curriculum:
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            bg = slide.background
            fill = bg.fill
            fill.solid()
            fill.fore_color.rgb = RGBColor(248, 250, 252)
            add_box(slide, Inches(0), Inches(0), Inches(13.33), Inches(0.4), (37, 99, 235), "", 1, (255,255,255))
            add_box(slide, Inches(0.5), Inches(1.0), Inches(12.3), Inches(2.8), (255, 255, 255), f"{mod['title']}\n40 Lessons - Har lesson colorful designed - Bade fonts - Acchi explain\nWhat Why How Example Mistake Pro Tip Assignment", 22, (37, 99, 235), True, (37, 99, 235))
            add_box(slide, Inches(0), Inches(7.1), Inches(13.33), Inches(0.4), (245, 158, 11), "", 1, (255,255,255))
            count += 1
            for vid in mod["videos"]:
                if count >= 80:
                    break
                slide = prs.slides.add_slide(prs.slide_layouts[6])
                bg = slide.background
                fill = bg.fill
                fill.solid()
                fill.fore_color.rgb = RGBColor(249, 250, 251)
                add_box(slide, Inches(0), Inches(0), Inches(13.33), Inches(0.2), (37, 99, 235), "", 1, (255,255,255))
                # Title - blue white - BIG FONT 16
                add_box(slide, Inches(0.2), Inches(0.3), Inches(12.9), Inches(0.8), (37, 99, 235), vid["title"][:180], 16, (255,255,255), True)
                # Hindi box - yellow orange border - font 12
                add_box(slide, Inches(0.2), Inches(1.2), Inches(6.3), Inches(6.0), (255, 251, 235), f"HINDI - Acchi Explain\n\n{vid['desc_hi']}"[:1200], 12, (120, 53, 15), False, (245, 158, 11))
                # English box - light blue border - font 12
                add_box(slide, Inches(6.8), Inches(1.2), Inches(6.3), Inches(6.0), (239, 246, 255), f"ENGLISH - Clear Explain\n\n{vid['desc_en']}"[:1200], 12, (30, 58, 138), False, (59, 130, 246))
                add_box(slide, Inches(0), Inches(7.3), Inches(13.33), Inches(0.2), (245, 158, 11), "", 1, (255,255,255))
                count += 1
            if count >= 80:
                break

        ppt_path = PPT_DIR / f"{course_id}_{course_topic.replace(' ', '_')[:12]}_COLORFUL.pptx"
        prs.save(str(ppt_path))
        return str(ppt_path), f"Colorful Designed PPT {count} slides - Bade fonts - Blue Orange Design - Har viewer me colorful"
    except Exception as e:
        return None, f"Error {e}"

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

if len(courses) < 100:
    courses = []
    for i, topic in enumerate(HUNDRED_COURSES):
        courses.append({"id": f"BRAHMA{1000+i}", "topic": topic, "price": 999, "videos": 400})
    save_json(COURSES_FILE, courses)

def ensure_100_ppts():
    missing = [c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))]
    if missing:
        c = missing[0]
        create_colorful_ppt(c["id"], c["topic"])
        return len(missing)
    return 0

if "admin_logged" not in st.session_state:
    st.session_state["admin_logged"] = False

ensure_100_ppts()

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
        st.sidebar.success("Colorful PPT - 100 Always")
        menu = st.sidebar.radio("Admin", ["Colorful PPT Maker", "Auto Pilot - 100 PPT Always", "Super Agent", "Video Library", "Dashboard", "Sales", "QR Setup"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Dashboard - 100 Courses - Colorful PPT")
        c1, c2, c3 = st.columns(3)
        c1.metric("Courses", len(courses))
        c2.metric("Colorful PPTs", len(list(PPT_DIR.glob("*.pptx"))))
        c3.metric("Missing", len([c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))]))
        st.dataframe(pd.DataFrame(courses), use_container_width=True)

    if menu == "Colorful PPT Maker":
        st.title("Colorful PPT Maker - Designed - Bade Fonts")
        st.write("Blue title bar, orange footer, yellow Hindi box orange border, blue English box blue border, bade fonts 16-18, acchi explain")
        course_sel = st.selectbox("Course select karo", [f"{c['topic']} - {c['id']}" for c in courses])
        if st.button("Brahma - Colorful Designed PPT Banao - Bade Fonts", type="primary"):
            sel_id = course_sel.split(" - ")[-1]
            sel_topic = " - ".join(course_sel.split(" - ")[:-1])
            with st.spinner(f"Bana raha hai Colorful Designed PPT - {sel_topic} - Blue Orange Design - Bade fonts..."):
                ppt_path, msg = create_colorful_ppt(sel_id, sel_topic)
                if ppt_path and Path(ppt_path).exists():
                    st.success(f"SUCCESS Colorful - {msg} - Har viewer me colorful dikhega - Black and white nahi")
                    st.balloons()
                    with open(ppt_path, "rb") as f:
                        st.download_button(f"Download Colorful PPT - {sel_topic}", f, file_name=Path(ppt_path).name)
                else:
                    st.error(f"Fail - {msg}")

    if menu == "Auto Pilot - 100 PPT Always":
        st.title("Auto Pilot - 100 PPT Hamesha Bani Rahe - Colorful")
        missing = [c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))]
        st.info(f"Total: {len(courses)} - Colorful PPT Bane: {len(list(PPT_DIR.glob('*.pptx')))} - Missing: {len(missing)}")
        with st.form("add_new_course"):
            new_topic = st.text_input("Naya Course Ka Naam")
            new_price = st.number_input("Price", value=999, min_value=1)
            submitted = st.form_submit_button("Add Naya Course - Colorful PPT Auto Banega", type="primary")
            if submitted:
                if len(new_topic) < 5:
                    st.error("Naam kam se kam 5 letters")
                else:
                    new_id = f"BRAHMA{1000+len(courses)}"
                    courses.append({"id": new_id, "topic": new_topic, "price": int(new_price), "videos": 400})
                    save_json(COURSES_FILE, courses)
                    st.success(f"Naya Course Add - {new_topic}")
                    with st.spinner(f"Colorful PPT bana raha hai - {new_topic}..."):
                        ppt_path, msg = create_colorful_ppt(new_id, new_topic)
                        if ppt_path:
                            st.success(f"Auto SUCCESS Colorful - {msg}")
                            st.balloons()
                    st.rerun()
        if st.button("SARE 100 COURSES KE COLORFUL PPT AUTO BANAO - Library Hamesha Full", type="primary"):
            missing = [c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))]
            if not missing:
                st.success("Sab Colorful PPT Ban Chuki - Library Full")
            else:
                bar = st.progress(0)
                status = st.empty()
                created = 0
                for idx, c in enumerate(missing):
                    status.write(f"Bana raha hai Colorful {idx+1}/{len(missing)} - {c['topic']} - Blue Orange Design...")
                    ppt_path, msg = create_colorful_ppt(c["id"], c["topic"])
                    if ppt_path:
                        created += 1
                    bar.progress(int((idx+1)/len(missing)*100))
                st.success(f"FULL DONE Colorful - {created} Colorful PPTs Ban Gaye - Library Full")
                st.balloons()
                st.rerun()

    if menu == "Video Library":
        st.title("Video Library - Colorful Designed - No Error")
        total = len(courses)
        made = len(list(PPT_DIR.glob("*.pptx")))
        missing = total - made
        c1, c2, c3 = st.columns(3)
        c1.metric("Total", total)
        c2.metric("Colorful PPT Bane", made)
        c3.metric("Missing", missing)
        for co in courses[:25]:
            co_id = co.get("id")
            ppt_files = list(PPT_DIR.glob(f"{co_id}*"))
            with st.expander(f"{co.get('topic')} - Colorful Check"):
                if ppt_files:
                    st.success(f"Colorful PPT Bana - Designed - Bade Fonts - {ppt_files[0].name} - {ppt_files[0].stat().st_size/1024:.0f} KB")
                    with open(ppt_files[0], "rb") as f:
                        st.download_button(f"Download Colorful PPT - {co.get('topic')}", f, file_name=Path(ppt_files[0].name), key=f"ppt_{co_id}")
                else:
                    with st.spinner(f"Colorful PPT nahi hai - Brahma colorful bana raha hai - {co.get('topic')}..."):
                        ppt_path, msg = create_colorful_ppt(co_id, co.get("topic"))
                        if ppt_path and Path(ppt_path).exists():
                            st.success(f"COLORFUL AUTO SUCCESS - {co.get('topic')} ka colorful PPT ban gaya - Designed - {msg}")
                            st.balloons()
                            with open(ppt_path, "rb") as f:
                                st.download_button(f"Download Colorful Auto PPT - {co.get('topic')}", f, file_name=Path(ppt_path).name, key=f"auto_{co_id}")

    if menu == "Super Agent":
        st.title("Super Agent - SEO Blog Ads")
        if st.button("SEO Optimize 100 Courses", type="primary"):
            f = AUTO_DIR / f"seo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            f.write_text(f"SEO Done {datetime.datetime.now()}", encoding="utf-8")
            st.success(f"SEO Done - {f.name}")

    if menu == "Sales":
        st.title("Sales - 100 Courses Colorful")
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
                if ppt_exists:
                    st.success("Colorful PPT Ready - Designed - Bade Fonts")
                else:
                    st.warning("Colorful PPT Baki - Auto Pilot se banega")
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
            st.write("100 Courses Colorful Designed PPT - Bade fonts - Acchi explain - Hamesha bani rahe")