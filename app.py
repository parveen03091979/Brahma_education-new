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

def get_teacher_lessons(topic):
    m1 = [
        f"What is {topic} definition with 5 real examples",
        f"History of {topic} timeline 2015 to 2026",
        f"Types of {topic} 7 types detail",
        f"{topic} vs Traditional method difference",
        f"Why {topic} is future market data proof",
        f"Career in {topic} jobs salary freelancing",
        f"{topic} mindset how to think like expert",
        f"Myths about {topic} 10 myths busted",
        f"Success stories {topic} 5 people 1Cr earned",
        f"Failure stories {topic} why 90 percent fail",
        f"{topic} roadmap zero to expert 90 days",
        f"Tools needed for {topic} 20 tools list",
        f"Industry overview {topic} top 10 industries",
        f"Market size {topic} 2026 report",
        f"Skills needed for {topic} technical plus soft",
        f"Learning path {topic} step by step",
        f"Time management for {topic} daily routine",
        f"Best resources for {topic} books videos",
        f"Community for {topic} discord reddit",
        f"Mentorship for {topic} how to find mentor",
        f"{topic} architecture basic structure",
        f"Core technology behind {topic}",
        f"RAG in {topic} deep",
        f"Memory in {topic} short long vector",
        f"Tools integration in {topic}",
        f"Planning in {topic} ReAct Chain Thought",
        f"Reasoning in {topic} how expert thinks",
        f"Action in {topic} how to take action",
        f"Observation in {topic} learn from result",
        f"Loop in {topic} Perceive Reason Act",
        f"Case Study 1 {topic} 1L per month business",
        f"Case Study 2 {topic} 10M ARR story",
        f"Case Study 3 {topic} 10M users growth",
        f"Case Study 4 {topic} real implementation",
        f"Case Study 5 {topic} 5k to 5L small business",
        f"Assignment 1 {topic} first simple project",
        f"Assignment 2 {topic} 10 examples research",
        f"Assignment 3 {topic} architecture diagram",
        f"Summary {topic} fundamentals checklist",
        f"Test {topic} fundamentals 20 questions"
    ]
    base_40 = [
        "Introduction overview what we learn",
        "Setting up workspace zero to setup",
        "Understanding interface every button meaning",
        "First 5 terms basic words meaning",
        "Basic workflow how work happens step by step",
        "First example first real example practical",
        "Hands-on exercise 1 do yourself",
        "Common mistakes in basics 90 percent do",
        "Best practices right way what is",
        "Tools for this stage which tools needed",
        "Time management how much time give",
        "Checklist what done check",
        "Real example 1 real business story 1",
        "Real example 2 real business story 2",
        "Case study deep case study one business",
        "Practical demo live demo step by step",
        "Step by step guide each step written",
        "Troubleshooting problem what to do",
        "Optimization tips how to make better",
        "Advanced basics little advanced level",
        "Interview questions what asked on topic",
        "Freelancing tip how to earn money from this",
        "Client handling how to handle client",
        "Pricing how much charge",
        "Portfolio building how to build portfolio",
        "Review what learned revise",
        "Test 10 questions test",
        "Assignment 1 first homework",
        "Assignment 2 second homework",
        "Pro tip what pros do secret",
        "Secret trick nobody tells trick",
        "Free resource where learn free",
        "Paid resource best paid what is",
        "Community help where get help",
        "Mentorship how to get mentor",
        "Next steps what to do next",
        "Summary whole module summary",
        "FAQ what people ask",
        "Resources books videos links",
        "Final task last work of module"
    ]
    module_themes = [
        "Fundamentals Basic Start",
        "Tools and Setup Which Tools",
        "Practical Basics Hands On",
        "Intermediate Beech Ka Level",
        "Advanced Techniques Expert Level",
        "Case Studies Real Business Kahani",
        "Marketing and Business Paise Kaise Kamaye",
        "Automation and Scaling Auto Kaise Kare",
        "Mistakes and Optimization Galtiyan Sudhar",
        "Final Project and Mastery Aakhri Project"
    ]
    all_mods = [m1]
    m2 = [f"Tool {i+1}: {topic} tool {i+1} setup guide" for i in range(40)]
    all_mods.append(m2)
    for mod_idx in range(2, 10):
        theme = module_themes[mod_idx]
        lessons = []
        for i, base in enumerate(base_40):
            lessons.append(f"{theme} {base} for {topic} lesson {i+1} deep real")
        all_mods.append(lessons)
    curriculum = []
    lc = 1
    for mod_idx, mod_lessons in enumerate(all_mods):
        vids = []
        for raw in mod_lessons:
            title = f"Lesson {lc}: {raw}"
            hi_text = (
                f"TOPIC {raw} "
                f"KYA HAI {raw} kya hai {topic} me simple bhasha me 5 examples. "
                f"KYON HAI {raw} kyon zaroori hai bina iske fail hoge 90 percent fail isiliye hote hain market 300 percent bada. "
                f"KAHAN HAI {raw} kahan use hota hai Instagram YouTube Business Job Freelancing top 5 jagah. "
                f"KAB KARNA Best time subah 6-8 baje Monday Thursday focus. "
                f"KAUN KAR SAKTA Student Housewife Job Business Age 16 to 60. "
                f"KAISE KAAM KARTA Step 1 Socho Step 2 Tool kholo Step 3 Pehla step karo Step 4 Result dekho Step 5 Galti sudharo. "
                f"KISSE HOGA Free tools Canva CapCut ChatGPT Google Notion. "
                f"KYA USE Hai Paise kaise kamaye Freelancing 20k-50k Business 1L plus Job 30k-80k. "
                f"KAISE USE KARNA Mobile se Instagram app kholo plus dabao Reels select karo Laptop se browser me jao dashboard dekho. "
                f"KAISE KARNA CHAHIYE Sahi tarika Roz 30 min practice diary likho hafte me revise Galat tarika Ek din 5 ghante phir 10 din kuch nahi. "
                f"REAL KAHANI Rahul gaon se 2 mahine roz 1 ghanta {raw} pe diya pehle kuch samajh nahi aaya phir daily small project banaya teesre mahine pehla client 15k chauthe mahine 5 clients 75k aaj 2 lakh per month. "
                f"MISTAKES Galti 1 bina samjhe advanced Galti 2 roz practice nahi Galti 3 sirf video dekhna practical nahi Galti 4 paise ke peeche bhagna learning nahi. "
                f"PRO TIP Secret diary rakho roz likho kya seekha kya galti hui kal kya karna raat ko 10 min padho ye trick successful students use karte hain koi YouTube pe nahi batata. "
                f"HOMEWORK Aaj {raw} par real project banao kal bhejo. "
                f"SUMMARY Aaj {raw} seekha Kya Kyon Kahan Kab Kaun Kaise Kisse Use Kaise use Kaise karna chahiye Real kahani Galtiyan Pro tip Homework."
            )
            en_text = (
                f"TOPIC {raw} WHAT IS {raw} meaning in {topic} simple 5 examples. "
                f"WHY Important without fail 90 percent fail market grew 300 percent. "
                f"WHERE Used Instagram YouTube Business Job Freelancing top 5. "
                f"WHEN Best morning 6-8 am Monday Thursday focus. "
                f"WHO Can do Student Housewife Job Business Age 16 to 60. "
                f"HOW WORKS Step 1 Think Step 2 Open tool Step 3 First step Step 4 See result Step 5 Fix. "
                f"WITH WHOM Free tools Canva CapCut ChatGPT Google Notion. "
                f"WHAT USE Earn Freelancing 20k-50k Business 1L Job 30k-80k. "
                f"HOW TO USE Mobile open Instagram plus Reels Laptop browser dashboard. "
                f"HOW SHOULD DO Right daily 30 min diary weekly revise Wrong 5 hours one day then nothing. "
                f"STORY Rahul village 2 months daily 1 hour on {raw} first month no understanding then daily small project third month first client 15k fourth month 5 clients 75k today 2 lakh per month. "
                f"MISTAKES Mistake 1 direct advanced Mistake 2 no daily practice Mistake 3 only watching no practical Mistake 4 behind money not learning. "
                f"PRO TIP Keep diary write daily what learned mistake tomorrow plan read 10 min before sleep trick successful students use nobody tells. "
                f"HOMEWORK Build small real project today on {raw} send tomorrow. "
                f"SUMMARY Today learned {raw} What Why Where When Who How With Whom Use How to use How should do Story Mistakes Pro tip Homework."
            )
            vids.append({"no": lc, "title": title, "desc_hi": hi_text, "desc_en": en_text})
            lc += 1
        curriculum.append({"title": f"Module {mod_idx+1}: {topic} {module_themes[mod_idx]} Book", "videos": vids})
    return curriculum

def create_course_ppt(course_id, course_topic):
    if not PPTX_OK:
        return None, "python-pptx missing"
    try:
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        curriculum = get_teacher_lessons(course_topic)
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(1.5))
        tf = box.text_frame
        tf.word_wrap = True
        tf.text = course_topic + " Complete Course 400 Lessons Har Sawal Ka Jawab Business Level"
        tf.paragraphs[0].runs[0].font.size = Pt(20)
        tf.paragraphs[0].runs[0].font.bold = True
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)
        count = 0
        for mod in curriculum:
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(1.0))
            tf = box.text_frame
            tf.word_wrap = True
            tf.text = mod["title"] + " 40 Lessons Course Book"
            tf.paragraphs[0].runs[0].font.size = Pt(16)
            tf.paragraphs[0].runs[0].font.bold = True
            tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)
            count += 1
            for vid in mod["videos"]:
                if count >= 62:
                    break
                slide = prs.slides.add_slide(prs.slide_layouts[6])
                box = slide.shapes.add_textbox(Inches(0.2), Inches(0.1), Inches(12.9), Inches(0.6))
                tf = box.text_frame
                tf.word_wrap = True
                tf.text = vid["title"][:220]
                tf.paragraphs[0].runs[0].font.size = Pt(11)
                tf.paragraphs[0].runs[0].font.bold = True
                tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(37, 99, 235)
                box = slide.shapes.add_textbox(Inches(0.2), Inches(0.8), Inches(6.3), Inches(6.2))
                tf = box.text_frame
                tf.word_wrap = True
                tf.text = vid["desc_hi"][:2500]
                for para in tf.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(7)
                box = slide.shapes.add_textbox(Inches(6.8), Inches(0.8), Inches(6.3), Inches(6.2))
                tf = box.text_frame
                tf.word_wrap = True
                tf.text = vid["desc_en"][:2500]
                for para in tf.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(7)
                count += 1
            if count >= 62:
                break
        ppt_path = PPT_DIR / f"{course_id}_Course.pptx"
        prs.save(str(ppt_path))
        return str(ppt_path), f"Course PPT {count} slides Har Sawal Ka Jawab Business Level"
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

def check_admin_persist():
    try:
        if ADMIN_SESSION.exists():
            data = json.loads(ADMIN_SESSION.read_text(encoding="utf-8"))
            expiry = datetime.datetime.fromisoformat(data.get("expiry"))
            if datetime.datetime.now() < expiry:
                return True
            else:
                ADMIN_SESSION.unlink(missing_ok=True)
    except:
        pass
    return False

if check_admin_persist():
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
        remember = st.sidebar.checkbox("Yaad Rakho 7 din login rahega", value=True)
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(pw.encode()).hexdigest() == MASTER_HASH.read_text():
                st.session_state["admin_logged"] = True
                if remember:
                    expiry = datetime.datetime.now() + datetime.timedelta(days=7)
                    save_json(ADMIN_SESSION, {"expiry": expiry.isoformat()})
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Admin Login 7 Din Business")
        menu = st.sidebar.radio("Admin", ["Dashboard", "Super Agent", "Course Library", "Course Maker", "Sales QR"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Dashboard Course Library Business Level")
        ppt_count = len(list(PPT_DIR.glob("*Course.pptx")))
        total_ppt = len(list(PPT_DIR.glob("*.pptx")))
        missing = len([c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*Course*"))])
        bekar = total_ppt - ppt_count
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Courses", len(courses))
        c2.metric("Courses Ready", ppt_count)
        c3.metric("Old PPTs", bekar)
        c4.metric("Missing Courses", missing)
        if missing == 0 and ppt_count == 100:
            st.success("Course Library Full 100 Courses Business Level Super Agent Bechta Rahega Link Dalkar")
        else:
            st.warning(f"Course Library me {bekar} purani PPTs hain {missing} courses missing hain Super Agent se proper banao")
            st.info(f"Screenshot me aapke 101 bekar 1 proper 99 missing dikha raha hai Iska matlab purani bekar delete nahi hui aur nayi proper 100 bani nahi - Neeche button se delete aur proper banao")

    if menu == "Super Agent":
        st.title("SUPER AGENT 100 Courses Business Level Real Income")
        st.write("Super Agent ke andar Master Teacher hai jisko har cheez ki knowledge hai har tarah ki study aati hai 20 saal teaching 100 courses expert Real business 1Cr plus Aage aur bhi courses bana sakta hai Ye demo nahi business hai real income honi hai App strong")

        course_sel = st.selectbox("Course select karo Courses", [f"{c['topic']} - {c['id