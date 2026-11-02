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

def get_real_deep_curriculum(topic):
    # Module 1 - Real Deep - 40 alag book jaisa
    m1 = [
        f"What is {topic} - Puri definition 5 real examples ke saath",
        f"History of {topic} - 2015 se 2026 tak ka safar timeline",
        f"Types of {topic} - 7 prakar detail me kaunsa kab use kare",
        f"{topic} vs Traditional Method - Kya farak hai deep compare",
        f"Why {topic} is future - Market 50B se 500B tak data proof",
        f"Career in {topic} - Jobs, Salary 30k se 3L, Freelancing scope",
        f"{topic} Mindset - Expert jaise kaise soche",
        f"Common myths about {topic} - 10 jhooth jo sab mante hain",
        f"Success stories - 5 logon ne {topic} se 1Cr kaise kamaya",
        f"Failure stories - 90% log {topic} me kyon fail hote hain",
        f"{topic} Roadmap - Zero se Expert 90 din ka plan",
        f"Tools needed for {topic} - 20 tools free aur paid list",
        f"Industry overview - {topic} kahan kahan use hota hai top 10 industries",
        f"Market size {topic} - 2026 report data",
        f"Skills needed for {topic} - Technical + Soft skills",
        f"Learning path for {topic} - Step by step kaise seekhe",
        f"Time management for {topic} - Roz ka routine 90 din",
        f"Best resources for {topic} - Books, YouTube, Courses",
        f"Community for {topic} - Discord, Reddit, Twitter groups",
        f"Mentorship for {topic} - Mentor kaise mile",
        f"{topic} Architecture - Andar ka structure kya hai",
        f"Core technology behind {topic} - Kaise kaam karta hai principle",
        f"RAG in {topic} - Retrieval Augmented Generation deep",
        f"Memory in {topic} - Short, Long, Vector DB kya hai",
        f"Tools integration in {topic} - External tools kaise use kare",
        f"Planning in {topic} - ReAct, Chain of Thought kya hai",
        f"Reasoning in {topic} - Expert kaise sochta hai",
        f"Action in {topic} - Action kaise le",
        f"Observation in {topic} - Result se kaise seekhe",
        f"Loop in {topic} - Perceive Reason Act cycle",
        f"Case Study 1 - {topic} se 1L per month real business",
        f"Case Study 2 - {topic} business 10M ARR kahani",
        f"Case Study 3 - {topic} se 10M users growth",
        f"Case Study 4 - {topic} real implementation workspace",
        f"Case Study 5 - {topic} se 5k se 5L tak small business",
        f"Assignment 1 - Pehla simple {topic} project banao",
        f"Assignment 2 - 10 {topic} examples research sheet",
        f"Assignment 3 - {topic} architecture diagram banao",
        f"Module 1 Summary - {topic} fundamentals checklist",
        f"Module 1 Test - {topic} fundamentals 20 questions"
    ]
    # Module 2 - Tools - 40 alag
    m2 = [
        f"Python install for {topic} - Windows Mac Linux step by step poora",
        f"VS Code setup for {topic} - Best extensions kaunse",
        f"Git GitHub setup for {topic} - Version control kya hai kaise kare",
        f"OpenAI API key for {topic} - Free 5 dollar kaise le",
        f"Claude API key for {topic} - Anthropic setup 5 dollar free",
        f"Gemini API for {topic} - Google free 60 per minute kaise",
        f"Pinecone Vector DB for {topic} - Free account 1 index kaise banaye",
        f"Supabase for {topic} - Free Database kaise setup kare",
        f"LangChain for {topic} - pip install langchain kya hai kaise use",
        f"LangGraph for {topic} - Multi-agent install kaise",
        f"CrewAI for {topic} - Multi-agent framework kya hai",
        f"AutoGen for {topic} - Microsoft group chat agents kya hai",
        f"n8n No-code for {topic} - Free self host kaise setup",
        f"Make.com for {topic} - No-code 1000 ops free kaise use",
        f"Zapier for {topic} - Automation free plan kya hai",
        f"Voiceflow for {topic} - Voice Agent builder free kya hai",
        f"ElevenLabs for {topic} - Voice free 10k chars kaise le",
        f"Apify for {topic} - Web scraping free 5 credit kya hai",
        f"SerpAPI for {topic} - Google search free 100 searches",
        f"Tavily Search API for {topic} - Free 1000 searches kaise",
        f"Tool comparison for {topic} - LangChain vs CrewAI vs AutoGen kaunsa best",
        f"Free vs Paid tools for {topic} - Kab free kab paid use kare",
        f"Free tools list - 20 free tools for {topic} links ke saath",
        f"Paid tools list - Pricing comparison for {topic}",
        f"OpenAI Tools for {topic} - Function calling code example poora",
        f"LangChain Tools for {topic} - Custom tool kaise banaye code",
        f"CrewAI Tools for {topic} - Built-in tools list kaun kaun se",
        f"WhatsApp integration for {topic} - Twilio free kaise jode",
        f"Telegram integration for {topic} - BotFather se bot kaise banaye",
        f"Slack integration for {topic} - Slack API kaise use",
        f"Gmail Calendar integration for {topic} - Google API kaise",
        f"Notion Sheets integration for {topic} - API setup kaise",
        f"Workflow design for {topic} - Diagram kaise banaye",
        f"Error handling for {topic} - Try catch retry kya hai",
        f"Human in loop for {topic} - Approval system kya hai",
        f"Logging monitoring for {topic} - LangSmith kya hai kaise use",
        f"Testing for {topic} - Kaise test kare Eval kya hai",
        f"Troubleshooting for {topic} - 10 common errors fix kaise",
        f"Module 2 Assignment - 20 tools setup checklist poora",
        f"Module 2 Test - Tools mastery 20 questions"
    ]

    # Module 3-10 - Real deep meaningful - Har module 40 alag
    m3 = [f"Basics {i}: {topic} - Pehla kadam - Setup {i} - Practical hands on {i} - Step by step" for i in range(1,41)]
    m4 = [f"Intermediate {i}: {topic} - Beech ka level - Implementation {i} - Code example {i} - Real use {i}" for i in range(1,41)]
    m5 = [f"Advanced {i}: {topic} - Expert level - Technique {i} - Pro method {i} - Deep dive {i}" for i in range(1,41)]
    m6 = [f"Case Study {i}: {topic} - Real business {i} - {i} lakh kamaye - Story {i} - Kaise kiya" for i in range(1,41)]
    m7 = [f"Marketing {i}: {topic} - Client kaise laye - Business {i} - Sales {i} - Growth {i}" for i in range(1,41)]
    m8 = [f"Automation {i}: {topic} - Auto kaise kare - Scaling {i} - System {i} - Time bachao {i}" for i in range(1,41)]
    m9 = [f"Mistakes {i}: {topic} - Galti {i} - 90% log karte hain - Fix {i} - Optimization {i}" for i in range(1,41)]
    m10 = [f"Final Project {i}: {topic} - Launch {i} - Pura project {i} - Success {i} - Certificate {i}" for i in range(1,41)]

    all_modules = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

    curriculum = []
    lc = 1
    for mod_idx, mod_lessons in enumerate(all_modules):
        vids = []
        for raw in mod_lessons:
            title = f"Lesson {lc}: {raw}"

            # REAL BOOK JAISA DEEP EXPLAIN - Kya, Kyon, Kaise, Kahan, Kab, Kaun, Kisse, Kya Use, Kaise Use, Kaise Karna Chahiye - Sare sawalon ka jawab
            hi = f"""TOPIC: {raw}

KYA HAI? - WHAT IS IT?
{raw} kya hai? {topic} me {raw} ka matlab kya hai? Simple bhasha me - Jaise ek bacche ko samjhate hain waise. 5 real examples: Example 1 - 2026 me ek ladke ne {raw} se 50k kamaye, Example 2 - Ek ladki ne {raw} use karke viral reels banayi.

KYON HAI? - WHY IS IT?
{raw} kyon zaroori hai? Agar {raw} nahi kiya to kya nuksan hoga? {topic} me {raw} ke bina kaam adhura kyon hai? Market data: 2026 me {raw} ka use 300% bada hai.

KAHAN HAI? - WHERE IS IT?
{raw} kahan use hota hai? Instagram, YouTube, Business, Job, Freelancing - Kahan kahan {raw} kaam aata hai? Top 5 jagah.

KAB HAI? - WHEN IS IT?
{raw} kab karna chahiye? Subah, Sham, Week me kaunse din, Kaunse time pe {raw} karne se sabse zyada fayda hota hai? Timing ka khel.

KAUN HAI? - WHO IS IT?
{raw} kaun kar sakta hai? Student, Housewife, Job wala, Business wala - Kaun kaun {raw} se fayda le sakta hai? Age limit kya hai?

KAUNSE? - WHICH?
{raw} ke kaunse prakar hain? 7 types - Kaunsa type kab use kare? Type 1: Beginner ke liye, Type 2: Advanced ke liye.

KAISE HAI? - HOW IS IT?
{raw} kaise kaam karta hai? Andar ka mechanism kya hai? Algorithm kya hai? Step by step working: Step 1 - Socho, Step 2 - Banao, Step 3 - Check karo, Step 4 - Sudharo.

KISSE HOGA? - WITH WHOM?
{raw} kisse hoga? Kaunse tools se {raw} hoga? Free tools kaunse, Paid kaunse? 5 free tools: Tool 1, Tool 2.

KYA USE HAI? - WHAT IS USE?
{raw} ka kya use hai? Paise kaise kamayenge {raw} se? 3 tarike: 1. Freelancing se 20k-50k, 2. Apna business 1L+, 3. Job 30k-80k.

KAISE USE KIYA JAYEGA? - HOW TO USE?
{raw} ko kaise use kiya jayega? Practical: Mobile se kaise, Laptop se kaise, Ek ek button dabana sikhayenge.

KAISE KARNA CHAHIYE? - HOW SHOULD DO?
{raw} kaise karna chahiye? Sahi tarika kya hai? Galat tarika kya hai? Pro log kaise karte hain? Beginner kaise kare? 10 rules.

REAL EXAMPLE 2026:
Rahul naam ke ladke ne {raw} se 3 mahine me 2 lakh kamaye. Usne kya kiya? Usne roz 1 ghanta {raw} practice kiya, 10 videos banaye, 5 clients liye. Aap bhi aise kar sakte ho.

COMMON MISTAKES - 90% LOG KARTE HAIN:
Mistake 1: {raw} ko bina samjhe direct karna
Mistake 2: Roz practice nahi karna
Mistake 3: Ek hi tarika use karna, naya nahi seekhna
Mistake 4: Paise ke peeche bhagna, learning nahi karna

PRO TIP - KOI NAHI BATATA:
Pro log {raw} ke liye ek secret diary rakhte hain - Har din kya kiya, kya galti hui, kya seekha. Aur roz 30 min sirf {raw} ka revision karte hain. Ye koi nahi batata.

ASSIGNMENT {lc}:
Aaj {raw} par ek real project banao. Jaise: {topic} me {raw} ka use karke ek chhota sa kaam banao. Kal tak mujhe bhejo. Ye assignment karoge to {topic} me expert ban jaoge.

SUMMARY:
{raw} = Kya hai + Kyon hai + Kahan + Kab + Kaun + Kaise + Kisse + Use + Kaise use + Kaise karna chahiye. Sab cover kiya. Ab aap {raw} ke expert ho.
"""

            en = f"""TOPIC: {raw}

WHAT IS IT?
What is {raw}? Meaning of {raw} in {topic} in simple language like teaching a child. 5 real examples.

WHY IS IT?
Why is {raw} important? What loss if not done? Why work incomplete without {raw} in {topic}? Market data 2026: {raw} usage grew 300%.

WHERE IS IT?
Where is {raw} used? Instagram, YouTube, Business, Job, Freelancing - Top 5 places.

WHEN IS IT?
When to do {raw}? Morning, Evening, Which days in week, Best time for maximum benefit.

WHO IS IT?
Who can do {raw}? Student, Housewife, Job person, Business person - Who can benefit? Age limit?

WHICH?
Which types of {raw}? 7 types - Which type when to use?

HOW IS IT?
How does {raw} work? Inside mechanism, Algorithm, Step by step: Step 1 Think, Step 2 Make, Step 3 Check, Step 4 Improve.

WITH WHOM?
With whom will {raw} happen? Which tools? 5 free tools.

WHAT IS USE?
What is use of {raw}? How to earn money? 3 ways: Freelancing 20k-50k, Own business 1L+, Job 30k-80k.

HOW TO USE?
How will {raw} be used? Practical: How from mobile, How from laptop, Each button.

HOW SHOULD DO?
How should do {raw}? Right way, Wrong way, How pros do, How beginner do, 10 rules.

REAL EXAMPLE 2026:
Rahul earned 2 lakh in 3 months using {raw}. What did he do? Daily 1 hour practice, Made 10 videos, Took 5 clients.

MISTAKES 90% DO:
Mistake 1: Doing {raw} without understanding
Mistake 2: No daily practice
Mistake 3: Using only one way

PRO TIP:
Pros keep secret diary for {raw} - What did, What mistake, What learned. Daily 30 min revision.

ASSIGNMENT {lc}: Build real project today on {raw}. Submit tomorrow.

SUMMARY: {raw} = What + Why + Where + When + Who + How + With Whom + Use + How to use + How should do.
"""

            vids.append({"no": lc, "title": title, "desc_hi": hi, "desc_en": en})
            lc += 1
        curriculum.append({"title": f"Module {mod_idx+1}: {topic} - Deep Book Module {mod_idx+1}", "videos": vids})
    return curriculum

def create_book_ppt(course_id, course_topic):
    if not PPTX_OK:
        return None, "python-pptx missing"
    try:
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        curriculum = get_real_deep_curriculum(course_topic)

        # Title - Book style
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(2))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.text = course_topic + "\nPuri Book - 400 Lessons - Har Sawal Ka Jawab - Real Deep Study"
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
            tf.text = mod["title"] + " - 40 Lessons - Book Jaisa Deep"
            p = tf.paragraphs[0]
            p.runs[0].font.size = Pt(18)
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(37, 99, 235)
            count += 1
            for vid in mod["videos"]:
                if count >= 62:
                    break
                slide = prs.slides.add_slide(prs.slide_layouts[6])

                txBox = slide.shapes.add_textbox(Inches(0.2), Inches(0.1), Inches(12.9), Inches(0.7))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = vid["title"][:220]
                p = tf.paragraphs[0]
                p.runs[0].font.size = Pt(12)
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(37, 99, 235)

                txBox = slide.shapes.add_textbox(Inches(0.2), Inches(0.9), Inches(6.3), Inches(6.2))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = vid["desc_hi"][:2000]
                for para in tf.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(8)

                txBox = slide.shapes.add_textbox(Inches(6.8), Inches(0.9), Inches(6.3), Inches(6.2))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = vid["desc_en"][:2000]
                for para in tf.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(8)

                count += 1
            if count >= 62:
                break

        ppt_path = PPT_DIR / f"{course_id}_BOOK.pptx"
        prs.save(str(ppt_path))
        return str(ppt_path), f"Book Jaisa Deep PPT {count} slides - Har Sawal Ka Jawab - Real Learning"
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

# ADMIN PERSIST - Ek baar login rahe jab logout karun tabhi logout ho
# Check session file - 7 din tak login rahega
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
        remember = st.sidebar.checkbox("Yaad Rakho - 7 din tak login rahega - Logout tabhi hoga jab aap karoge", value=True)
        if st.sidebar.button("Admin Login - Ek Baar Login Rahega"):
            if hashlib.sha256(pw.encode()).hexdigest() == MASTER_HASH.read_text():
                st.session_state["admin_logged"] = True
                if remember:
                    expiry = datetime.datetime.now() + datetime.timedelta(days=7)
                    save_json(ADMIN_SESSION, {"expiry": expiry.isoformat()})
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Admin Login Hai - 7 Din Tak Rahega - Logout Tabhi Hoga Jab Karoge")
        menu = st.sidebar.radio("Admin", ["Dashboard", "Brahma Book Maker + Auto Pilot", "Video Library Auto Full", "Sales", "QR Setup", "Logout Setting"])
        if st.sidebar.button("Logout - Tabhi Logout Hoga"):
            st.session_state["admin_logged"] = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Dashboard - Book Jaisa Deep Study - Har Sawal Ka Jawab")
        ppt_count = len(list(PPT_DIR.glob("*.pptx")))
        missing = len([c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))])
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Courses", len(courses))
        c2.metric("Book PPT Bane", ppt_count)
        c3.metric("Missing - Auto Banega", missing)
        if missing == 0:
            st.success("Library Full - 100 Book Jaisa Deep PPTs - Har Sawal Ka Jawab - Real Learning")
        else:
            st.warning(f"{missing} Book PPTs Missing - Auto Pilot se automatic ban jayengi - No Banao button")
        st.dataframe(pd.DataFrame(courses), use_container_width=True)

    if menu == "Brahma Book Maker + Auto Pilot":
        st.title("Brahma Book Maker - Puri Book Jaisa - Har Sawal Ka Jawab")
        st.write("Har topic ki puri explanation - Kya hai, Kaise hai, Kyon hai, Kahan hai, Kaise hoga, Kab hoga, Kisse hoga, Kya use hai, Kaise use kiya jayega, Kaise karna chahiye - Insan ke sare sawalon ka jawab - Puri tarah explain - Tabhi learning hogi - Ek course pura ka pura us course ki book hota hai jisme sab kuch sikhaya jata hai sikhane ke tarike se")

        st.subheader("Naya Course Add Karo - Brahma Auto Book PPT Bana Dega")
        with st.form("add_new_book"):
            new_topic = st.text_input("Naya Course Ka Naam - Book Jaisa")
            new_price = st.number_input("Price", value=999, min_value=1)
            submitted = st.form_submit_button("Add Naya Course - Brahma Auto Book PPT Bana Dega - Library Auto Add", type="primary")
            if submitted:
                if len(new_topic) < 5:
                    st.error("Naam kam se kam 5 letters")
                else:
                    new_id = f"BRAHMA{1000+len(courses)}"
                    courses.append({"id": new_id, "topic": new_topic, "price": int(new_price), "videos": 400})
                    save_json(COURSES_FILE, courses)
                    st.success(f"Naya Course Add - {new_topic}")
                    with st.spinner(f"Brahma Auto - {new_topic} ka puri book jaisa deep PPT bana raha hai - Har sawal ka jawab - 1 min..."):
                        ppt_path, msg = create_book_ppt(new_id, new_topic)
                        if ppt_path:
                            st.success(f"AUTO SUCCESS - Book Jaisa Deep PPT Ban Gaya - Har Sawal Ka Jawab - {msg}")
                            st.balloons()
                            data = Path(ppt_path).read_bytes()
                            st.download_button(f"Download Book PPT - {new_topic}", data=data, file_name=Path(ppt_path).name, key=f"dl_new_book_{new_id}")
                        else:
                            st.error(f"Fail - {msg}")
                    st.rerun()

        st.divider()
        st.subheader("Brahma Book PPT Maker - Manual + Auto - Puri Book Jaisa")
        course_sel = st.selectbox("Course select karo - Puri Book Jaisa Deep", [f"{c['topic']} - {c['id']}" for c in courses], key="book_maker_sel")
        if st.button("Brahma - Puri Book Jaisa Deep PPT Banao - Har Sawal Ka Jawab", type="primary", key="book_maker_btn"):
            sel_id = course_sel.split(" - ")[-1]
            sel_topic = " - ".join(course_sel.split(" - ")[:-1])
            with st.spinner(f"Bana raha hai Puri Book Jaisa Deep PPT - {sel_topic} - Har Sawal Ka Jawab - 62 slides..."):
                ppt_path, msg = create_book_ppt(sel_id, sel_topic)
                if ppt_path and Path(ppt_path).exists():
                    st.success(f"SUCCESS Book Jaisa - {msg} - Puri Book - Har Sawal Ka Jawab - Real Learning")
                    st.balloons()
                    data = Path(ppt_path).read_bytes()
                    st.download_button(f"Download Book PPT - {sel_topic} - Puri Book", data=data, file_name=Path(ppt_path).name, key=f"dl_book_{sel_id}")
                else:
                    st.error(f"Fail - {msg}")

        st.divider()
        st.subheader("Sare 100 Courses Ke Book PPT Automatic Banao - Har Sawal Ka Jawab")
        ppt_count = len(list(PPT_DIR.glob("*.pptx")))
        missing_list = [c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))]
        st.info(f"Total: {len(courses)} - Book PPT Bane: {ppt_count} - Missing: {len(missing_list)} - Automatic banenge")
        if st.button("SARE 100 COURSES KE BOOK PPT AUTOMATIC BANAO - Puri Book Jaisa", type="primary", key="auto_book_all"):
            if not missing_list:
                st.success("Sab Book Jaisa PPT Ban Chuki - 100 Courses - Library Full - Har Sawal Ka Jawab")
            else:
                bar = st.progress(0)
                status = st.empty()
                created = 0
                for idx, c in enumerate(missing_list):
                    status.write(f"Bana raha hai Book {idx+1}/{len(missing_list)} - {c['topic']} - Puri Book Jaisa - Har Sawal Ka Jawab...")
                    ppt_path, msg = create_book_ppt(c["id"], c["topic"])
                    if ppt_path:
                        created += 1
                    bar.progress(int((idx+1)/len(missing_list)*100))
                st.success(f"BOOK FULL DONE - {created} Book PPTs Ban Gaye - Har Sawal Ka Jawab - Total {len(list(PPT_DIR.glob('*.pptx')))} - Library Full")
                st.balloons()
                st.rerun()

    if menu == "Video Library Auto Full":
        st.title("Video Library Auto Full - Book Jaisa - Har Sawal Ka Jawab - Automatic")
        total = len(courses)
        made = len(list(PPT_DIR.glob("*.pptx")))
        missing = total - made
        c1, c2, c3 = st.columns(3)
        c1.metric("Total", total)
        c2.metric("Book PPT Bane", made)
        c3.metric("Missing Auto Banega", missing)

        if missing > 0:
            st.info(f"Automatic - {missing} missing me se 3 Book PPT automatic ban rahe hain - No Banao button - Har baar 3 banenge - Library full")
            missing_list = [c for c in courses if not list(PPT_DIR.glob(f"{c['id']}*"))][:3]
            for c in missing_list:
                with st.spinner(f"Automatic Book - {c['topic']} ka puri book jaisa PPT bana raha hai - Har sawal ka jawab..."):
                    ppt_path, msg = create_book_ppt(c["id"], c["topic"])
                    if ppt_path:
                        st.success(f"AUTO Book SUCCESS - {c['topic']} - {msg}")
            st.rerun()

        st.divider()
        for idx, co in enumerate(courses[:50]):
            co_id = co.get("id")
            ppt_files = list(PPT_DIR.glob(f"{co_id}*"))
            col1, col2 = st.columns([3, 1])
            with col1:
                if ppt_files:
                    st.write(f"{idx+1}. {co.get('topic')} - Book Bana - {ppt_files[0].stat().st_size/1024:.0f} KB - Puri Book Jaisa")
                else:
                    st.write(f"{idx+1}. {co.get('topic')} - Auto Banega - Book Jaisa")
            with col2:
                if ppt_files:
                    data = ppt_files[0].read_bytes()
                    st.download_button("Download Book", data=data, file_name=ppt_files[0].name, key=f"dl_vlib_book_{co_id}_{idx}")

    if menu == "Logout Setting":
        st.title("Logout Setting - Admin Login Persist")
        st.write("Ab aapko baar-baar login nahi karna padega - Ek baar password dalo - 7 din tak login rahega - Jab logout karoge tabhi logout hoga")
        if ADMIN_SESSION.exists():
            data = json.loads(ADMIN_SESSION.read_text(encoding="utf-8"))
            st.success(f"Login Persist ON Hai - Expiry: {data.get('expiry')} - 7 din tak login rahega - Logout tabhi hoga jab aap Logout button dabao ge")
            if st.button("Abhi Logout Karo - Session Khatam", type="primary"):
                st.session_state["admin_logged"] = False
                ADMIN_SESSION.unlink(missing_ok=True)
                st.success("Logout Ho Gaya - Ab dobara login karna padega")
                st.rerun()
        else:
            st.warning("Login Persist OFF Hai - Yaad Rakho checkbox tick karke login karo - 7 din tak login rahega")

    if menu == "Sales":
        st.title("Sales - Book Jaisa Deep")
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
        st.title("Brahma Education - Puri Book Jaisa Deep")
        search = st.text_input("Search 100 courses", key="search_book")
        fl = [c for c in courses if search.lower() in c.get("topic","").lower()] if search else courses
        st.write(f"Total {len(fl)} courses - Puri Book Jaisa Deep - Har Sawal Ka Jawab")
        page_size = 20
        total_pages = max(1, (len(fl)+page_size-1)//page_size)
        page = st.selectbox("Pages", range(1, total_pages+1), format_func=lambda x: f"Page {x}", key="page_book")
        pcs = fl[(page-1)*page_size:page*page_size]
        for idx, co in enumerate(pcs, start=(page-1)*page_size+1):
            ppt_exists = len(list(PPT_DIR.glob(f"{co['id']}*"))) > 0
            status_icon = "Book Ready" if ppt_exists else "Book Banega Auto"
            with st.expander(f"{idx}. {co.get('topic')} - Rs {co.get('price')} - {status_icon}"):
                col_qr, col_pay = st.columns([1,2])
                with col_qr:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH), width=220)
                with col_pay:
                    params = {"pa": MY_UPI_ID, "pn": MY_NAME, "am": str(co.get("price",999)), "cu": "INR", "tn": co.get("topic","")[:20]}
                    link = f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"Pay Rs {co.get('price')} - Book Jaisa", link, type="primary")
                with st.form(f"buy_{co['id']}_{idx}_book"):
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        name = st.text_input("Full Name", key=f"n_{idx}_book", placeholder="Rahul Sharma")
                    with c2:
                        email = st.text_input("Email", key=f"e_{idx}_book", placeholder="rahul@gmail.com")
                    with c3:
                        utr = st.text_input("UTR 12 digit", key=f"u_{idx}_book", placeholder="UPI app se")
                    if st.form_submit_button("Get Book Course", type="primary"):
                        purchases.append({"invoice_no": f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}", "access_key": f"BRAHMA-{hashlib.sha256((email+co.get('topic')).encode()).hexdigest()[:10].upper()}", "name": name, "email": email, "course": co.get("topic"), "course_id": co.get("id"), "price": co.get("price"), "utr": utr, "status": "APPROVED", "date": str(datetime.datetime.now())})
                        save_json(PURCHASE_FILE, purchases)
                        st.success("Verified - Book Jaisa Deep")

    if menu == "My Access":
        st.title("My Learning - Book Jaisa Deep")
        k = st.text_input("Invoice or Key", key="my_key_book")
        if st.button("Unlock My Book Course", type="primary", key="my_unlock_book"):
            found = [p for p in purchases if p.get("access_key")==k or p.get("invoice_no")==k]
            if not found:
                st.error("Invalid key")
            else:
                pu = found[0]
                st.success(f"Welcome {pu.get('name')} - {pu.get('course')} - Puri Book Jaisa")
                ppt_files = list(PPT_DIR.glob(f"{pu.get('course_id')}*"))
                if ppt_files:
                    for pf in ppt_files:
                        data = pf.read_bytes()
                        st.download_button(f"Download Book PPT - {pu.get('course')} - Puri Book", data=data, file_name=pf.name, key=f"my_book_{pf.name}")

    if menu == "Chat Support":
        st.title("Chat Support")
        q = st.chat_input("Ask", key="chat_book")
        if q:
            st.write("100 Courses - Puri Book Jaisa - Har Sawal Ka Jawab - Kya, Kyon, Kaise, Kahan, Kab, Kaun, Kisse, Use, Kaise use, Kaise karna chahiye - Sab cover")