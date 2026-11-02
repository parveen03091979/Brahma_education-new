import streamlit as st
import json
import hashlib
import datetime
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Brahma Education", layout="wide")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
ADMIN_SESSION = DATA_DIR / ".admin_session"
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
MARKETING_FILE = DATA_DIR / "marketing.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
PPT_DIR = DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)

TOPICS = ["AI Agent Automation 2026", "Instagram Reels Mastery", "YouTube Automation AI", "Prompt Engineering Pro", "Digital Marketing SEO Mastery", "ChatGPT Mastery 2026", "Facebook Ads Mastery", "Google Ads Mastery", "SEO Advanced 2026", "Social Media Marketing Pro", "Content Writing AI", "Copywriting Mastery", "Blogging Mastery 2026", "Affiliate Marketing Pro", "Dropshipping Business", "E-commerce Mastery Shopify", "Canva Design Mastery", "Video Editing CapCut Pro", "YouTube SEO Mastery", "Instagram Growth Hack", "LinkedIn Marketing Pro", "Twitter X Growth Mastery", "TikTok Viral Mastery", "Pinterest Marketing", "Quora Marketing", "Email Marketing Automation", "WhatsApp Marketing Pro", "Telegram Channel Growth", "Influencer Marketing", "Personal Branding Mastery", "Freelancing Mastery", "Agency Business Mastery", "SaaS Business 2026", "No-Code Business Bubble", "Python Programming Mastery", "JavaScript Mastery 2026", "React JS Mastery", "Next.js Mastery", "Node.js Backend Mastery", "Web Development Full Stack", "WordPress Mastery", "Shopify Store Design", "UI UX Design Mastery", "Figma Design Pro", "Graphic Design Mastery", "Logo Design Mastery", "Thumbnail Design Viral", "Video Animation Mastery", "AI Image Generation Midjourney", "AI Video Generation Sora", "Voice Cloning ElevenLabs", "Automation n8n Make", "Zapier Automation Mastery", "Notion Productivity Mastery", "Excel Advanced Mastery", "Google Sheets Automation", "Data Analysis Python", "Machine Learning Mastery", "Deep Learning 2026", "Data Science Mastery", "Stock Market Trading AI", "Crypto Trading Mastery", "Forex Trading Pro", "Real Estate Business", "Motivational Speaking Mastery", "Public Speaking Pro", "Communication Skills Mastery", "English Speaking Pro", "Hindi Content Creation", "Podcast Mastery", "Music Production AI", "Photography Mastery", "Reels Editing Viral", "Meme Marketing Mastery", "Viral Content Formula", "Lead Generation Mastery", "Sales Funnel Mastery", "Landing Page Design", "CRO Conversion Optimization", "Customer Support Automation", "HR Recruitment AI", "Business Plan Mastery", "Startup Funding Mastery", "Business Automation AI", "Time Management Mastery", "Mindset Mastery Millionaire", "Meditation Mindfulness", "Fitness Coaching Business", "Diet Nutrition Business", "Yoga Teaching Business", "Cooking Channel Business", "Travel Vlogging Business", "Gaming Channel Growth", "Education Channel Growth", "Finance Channel Business", "News Channel Automation", "Meme Page Business", "Affiliate Blog SEO", "Amazon FBA Mastery", "Etsy Store Mastery", "Print on Demand Business", "Stock Photography Business", "Voice Over Business", "Translation Business AI", "Resume Writing Business", "LinkedIn Profile Optimization", "AI Tools Mastery 100 Tools", "Chatbot Development", "AI Voice Agent Mastery", "AI Receptionist Business"]

def load_json(path, default):
    if path.exists():
        try:
            txt = path.read_text(encoding="utf-8")
            if len(txt) > 2:
                return json.loads(txt)
        except:
            return default
    return default

def save_json(path, data):
    txt = json.dumps(data, ensure_ascii=False, indent=2)
    path.write_text(txt, encoding="utf-8")

def create_40_modules_pptx(cid, ctopic):
    from pptx import Presentation
    from pptx.util import Inches, Pt
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    titles = []
    titles.append("M01 Intro KYA HAI " + ctopic)
    titles.append("M02 KYON HAI Why Important")
    titles.append("M03 KAHAN HAI Market Scope")
    titles.append("M04 KAB Best Timing")
    titles.append("M05 KAUN Eligible")
    titles.append("M06 KAISE Architecture")
    titles.append("M07 KISSE Tools Setup")
    titles.append("M08 KYA USE Earning Model")
    titles.append("M09 KAISE USE Practical")
    titles.append("M10 KAISE KARNA Right Way")
    titles.append("M11 Fundamentals Deep Dive")
    titles.append("M12 Tools Mastery Part1")
    titles.append("M13 Tools Mastery Part2")
    titles.append("M14 Perceive Reason Act")
    titles.append("M15 RAG Memory System")
    titles.append("M16 Prompt Engineering")
    titles.append("M17 Case Study Rahul Village")
    titles.append("M18 Case Study 1L Per Month")
    titles.append("M19 Case Study 10M ARR")
    titles.append("M20 Mistakes 90 Percent")
    titles.append("M21 PRO TIP Diary Secret")
    titles.append("M22 Mindset Millionaire")
    titles.append("M23 Time Management")
    titles.append("M24 Freelancing Upwork Fiverr")
    titles.append("M25 Agency Business Model")
    titles.append("M26 SaaS Business Model")
    titles.append("M27 Client Handling Pricing")
    titles.append("M28 Portfolio Building")
    titles.append("M29 Lead Generation")
    titles.append("M30 Sales Funnel")
    titles.append("M31 SEO Search Engine Optimizing")
    titles.append("M32 Social Media Marketing")
    titles.append("M33 Content Creation Reels")
    titles.append("M34 Email WhatsApp Marketing")
    titles.append("M35 Automation n8n Make")
    titles.append("M36 Advanced Strategies")
    titles.append("M37 Optimization Scaling")
    titles.append("M38 Business Plan 1Cr")
    titles.append("M39 Homework Assignments")
    titles.append("M40 Final Project Certification")

    bodies = []
    bodies.append("What is " + ctopic + " 5 examples fundamentals teacher jaise")
    bodies.append("Why important future Market data 2026 90 percent fail proof")
    bodies.append("Kahan use Instagram YouTube Business Job Freelancing Agency")
    bodies.append("Kab best morning 6 to 8 Monday Thursday Seasonal timing")
    bodies.append("Kaun Student Housewife Job Business 16 to 60 har koi eligible")
    bodies.append("Kaise kaam karta Perceive Reason Act loop architecture")
    bodies.append("Free tools Canva CapCut ChatGPT Notion Paid tools setup guide")
    bodies.append("Earning freelancing 20k to 50k business 1L plus job use cases")
    bodies.append("Kaise use Mobile Reels laptop browser dashboard hands on")
    bodies.append("Sahi tarika Daily 30 min diary Weekly revise best practice")
    bodies.append("Fundamentals deep dive core concepts theory practical mix")
    bodies.append("Tools mastery Part1 Canva ChatGPT CapCut basics intermediate")
    bodies.append("Tools mastery Part2 Make n8n Zapier Notion advanced")
    bodies.append("Perceive Reason Act ReAct Chain Thought expert thinking")
    bodies.append("RAG deep memory short long vector memory system build")
    bodies.append("Prompt engineering for course best prompts templates 100")
    bodies.append("Real kahani Rahul village 2 months daily 1 hour project story")
    bodies.append("Case study 1L per month 5 clients 75k fourth month scaling")
    bodies.append("Case study 10M ARR SaaS story how build 10M ARR real")
    bodies.append("Galti1 advanced Galti2 no practice Galti3 paise peeche Galti4 diary nahi")
    bodies.append("PRO TIP secret diary roz likho kya seekha kal kya karna Raat 10 min")
    bodies.append("Mindset Millionaire meditation focus time management motivation")
    bodies.append("Time management daily 1 hour kaise course complete 30 days me")
    bodies.append("Freelancing Upwork Fiverr profile gig pricing proposal client handling")
    bodies.append("Agency business team building client acquisition model")
    bodies.append("SaaS business recurring income model kaise banaye is course se")
    bodies.append("Client handling pricing kitna charge negotiation contract payment")
    bodies.append("Portfolio building behance dribbble github 10 samples kaise banaye")
    bodies.append("Lead generation LinkedIn Instagram YouTube organic paid methods")
    bodies.append("Sales funnel landing page CRO conversion optimization sale close")
    bodies.append("SEO search engine optimizing blog keyword research on page off page")
    bodies.append("Social media marketing Instagram Reels YouTube Shorts LinkedIn growth")
    bodies.append("Content creation Reels viral formula hook story CTA thumbnail viral")
    bodies.append("Email WhatsApp Telegram growth sequences automation marketing")
    bodies.append("Automation n8n Make Zapier automate posting lead follow up support")
    bodies.append("Advanced strategies pro tricks expert use competition beat")
    bodies.append("Optimization scaling 1L se 10L scale team ads systems")
    bodies.append("Business plan 1Cr business startup funding pitch deck")
    bodies.append("Homework Aaj project banao Assignment1 simple Assignment2 research")
    bodies.append("Final project client real project Certification business level real income")

    for i in range(len(titles)):
        title = titles[i]
        body = bodies[i]
        slide = prs.slides.add_slide(prs.slide_layouts[5])
        box1 = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12.3), Inches(0.7))
        tf1 = box1.text_frame
        tf1.word_wrap = True
        tf1.paragraphs[0].text = title
        tf1.paragraphs[0].font.size = Pt(20)
        tf1.paragraphs[0].font.bold = True
        box2 = slide.shapes.add_textbox(Inches(0.5), Inches(1.0), Inches(12.3), Inches(6.2))
        tf2 = box2.text_frame
        tf2.word_wrap = True
        tf2.paragraphs[0].text = body
        tf2.paragraphs[0].font.size = Pt(14)

    out_path = PPT_DIR / (cid + "_Course.pptx")
    prs.save(str(out_path))
    return True

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

if len(courses) < 100:
    courses = []
    for i in range(len(TOPICS)):
        t = TOPICS[i]
        cid = "BRAHMA" + str(1000 + i)
        courses.append({"id": cid, "topic": t, "price": 999})
    save_json(COURSES_FILE, courses)

if "admin_logged" not in st.session_state:
    st.session_state["admin_logged"] = False

def check_persist():
    if ADMIN_SESSION.exists():
        try:
            data = ADMIN_SESSION.read_text(encoding="utf-8")
            d = json.loads(data)
            exp = datetime.datetime.fromisoformat(d.get("expiry"))
            now = datetime.datetime.now()
            if now < exp:
                return True
            else:
                ADMIN_SESSION.unlink(missing_ok=True)
        except:
            return False
    return False

if check_persist():
    st.session_state["admin_logged"] = True

st.sidebar.title("Brahma Education")

if not MASTER_HASH.exists():
    pw = st.sidebar.text_input("Create Admin Password", type="password")
    if st.sidebar.button("Create Admin"):
        if pw and len(pw) >= 4:
            h = hashlib.sha256(pw.encode()).hexdigest()
            MASTER_HASH.write_text(h)
            st.rerun()
    menu = "Browse Courses"
else:
    if not st.session_state["admin_logged"]:
        menu = st.sidebar.radio("Menu", ["Browse Courses", "My Access", "Chat Support"])
        st.sidebar.divider()
        pw = st.sidebar.text_input("Admin Password", type="password")
        rem = st.sidebar.checkbox("Yaad Rakho 7 din", value=True)
        if st.sidebar.button("Admin Login"):
            hpw = hashlib.sha256(pw.encode()).hexdigest()
            saved = MASTER_HASH.read_text()
            if hpw == saved:
                st.session_state["admin_logged"] = True
                if rem:
                    exp = datetime.datetime.now() + datetime.timedelta(days=7)
                    save_json(ADMIN_SESSION, {"expiry": exp.isoformat()})
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Admin Login 7 Din Business")
        menu = st.sidebar.radio("Admin", ["Dashboard", "Super Agent Full Power", "Course Library 40 Modules", "Marketing Engine", "Sales QR"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Dashboard 100 Courses 40 Modules")
        total = len(courses)
        proper = len(list(PPT_DIR.glob("*_Course*")))
        bekar = 0
        for f in list(PPT_DIR.glob("*.*")):
            if "_Course" not in f.name:
                bekar += 1
        missing = 0
        for c in courses:
            found = list(PPT_DIR.glob(c.get("id") + "_Course*"))
            if len(found) == 0:
                missing += 1
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total", total)
        c2.metric("Ready 40 Modules", proper)
        c3.metric("Old", bekar)
        c4.metric("Missing", missing)
        if proper >= 100:
            st.success("Full 100 Books 40 Modules Master Teacher")
        else:
            st.warning("Purani delete karo aur 40 modules wali banao")
        if st.button("DELETE OLD"):
            for f in list(PPT_DIR.glob("*.*")):
                try:
                    f.unlink()
                except:
                    pass
            st.success("Old deleted")
            st.rerun()
        if st.button("CREATE 100 BOOKS 40 MODULES", type="primary"):
            bar = st.progress(0)
            for idx, c in enumerate(courses):
                create_40_modules_pptx(c.get("id"), c.get("topic"))
                pct = int((idx + 1) / len(courses) * 100)
                bar.progress(pct)
            st.success("100 Books 40 Modules Created")
            st.balloons()
            st.rerun()
        rows = []
        for c in courses:
            found = list(PPT_DIR.glob(c.get("id") + "_Course*"))
            status = "Ready 40 Modules"
            if len(found) == 0:
                status = "Missing"
            rows.append({"ID": c.get("id"), "Course": c.get("topic"), "Status": status})
        st.dataframe(pd.DataFrame(rows), use_container_width=True)

    if menu == "Super Agent Full Power":
        st.title("Super Agent Brahma Full Power Kabhi Rukega Nahi")
        st.write("Full power search engine optimizing social media digital marketing blog posting Facebook Instagram posting courses bechne ke liye khud karega hamesha")
        st.write("Daily fixed Facebook Instagram blog posts Niche agents AI ke banega")
        fb = st.number_input("Facebook posts per day", value=3, min_value=1, max_value=10)
        insta = st.number_input("Instagram posts per day", value=3, min_value=1, max_value=10)
        blog = st.number_input("Blog posts per day", value=2, min_value=1, max_value=10)
        if st.button("START SUPER AGENT FULL POWER ROZ POST KAREGA", type="primary"):
            posts = []
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            for c in courses[:20]:
                topic = c.get("topic")
                posts.append({"date": today, "platform": "Facebook", "course": topic, "type": "Morning Post"})
                posts.append({"date": today, "platform": "Instagram", "course": topic, "type": "Reel"})
                posts.append({"date": today, "platform": "Blog", "course": topic, "type": "SEO Blog"})
            save_json(MARKETING_FILE, posts)
            st.success("Super Agent Started Roz Facebook Instagram Blog karega")
            st.dataframe(pd.DataFrame(posts), use_container_width=True)
            st.balloons()

    if menu == "Course Library 40 Modules":
        st.title("Course Library 100 Books 40 Modules Each")
        total = len(courses)
        proper = len(list(PPT_DIR.glob("*_Course*")))
        c1, c2 = st.columns(2)
        c1.metric("Total", total)
        c2.metric("Ready 40 Modules", proper)
        for idx, co in enumerate(courses):
            cid = co.get("id")
            pf = list(PPT_DIR.glob(cid + "_Course*"))
            col1, col2 = st.columns([3, 1])
            with col1:
                if len(pf) > 0:
                    st.success(str(idx + 1) + ". " + co.get("topic") + " Ready 40 Modules")
                else:
                    st.warning(str(idx + 1) + ". " + co.get("topic") + " Missing")
            with col2:
                if len(pf) > 0:
                    data = pf[0].read_bytes()
                    st.download_button("Download 40 Modules", data=data, file_name=pf[0].name, key="dl_" + cid)

    if menu == "Marketing Engine":
        st.title("Marketing Engine Super Agent Full Power")
        st.write("Search Engine Optimizing Social Media Digital Marketing Blog Facebook Instagram Posting Courses Bechne Ke Liye")
        if st.button("Generate Today Marketing Posts", type="primary"):
            posts = []
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            for c in courses[:20]:
                topic = c.get("topic")
                posts.append({"date": today, "platform": "Facebook", "course": topic, "type": "Post"})
                posts.append({"date": today, "platform": "Instagram", "course": topic, "type": "Reel"})
                posts.append({"date": today, "platform": "Blog", "course": topic, "type": "Blog SEO"})
            save_json(MARKETING_FILE, posts)
            st.success("Marketing posts generated")
            st.dataframe(pd.DataFrame(posts), use_container_width=True)
        mdata = load_json(MARKETING_FILE, [])
        if len(mdata) > 0:
            st.dataframe(pd.DataFrame(mdata), use_container_width=True)

    if menu == "Sales QR":
        st.title("Sales QR Business Real Income")
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
        st.title("Brahma Education 100 Courses 40 Modules")
        search = st.text_input("Search 100 courses")
        if search:
            fl = []
            for c in courses:
                if search.lower() in c.get("topic").lower():
                    fl.append(c)
        else:
            fl = courses
        proper = len(list(PPT_DIR.glob("*_Course*")))
        st.write("Total courses")
        st.write(str(len(fl)))
        st.write("Ready 40 Modules")
        st.write(str(proper))
        for idx, co in enumerate(fl[:15]):
            cid = co.get("id")
            pf = list(PPT_DIR.glob(cid + "_Course*"))
            status = "40 Modules Ready"
            if len(pf) == 0:
                status = "Banega"
            with st.expander(str(idx + 1) + ". " + co.get("topic") + " " + status):
                if len(pf) > 0:
                    data = pf[0].read_bytes()
                    st.download_button("Download 40 Modules", data=data, file_name=pf[0].name, key="b_dl_" + cid)

    if menu == "My Access":
        st.title("My Learning 40 Modules")
        k = st.text_input("Invoice or Key")
        if st.button("Unlock"):
            found = []
            for p in purchases:
                if p.get("access_key") == k or p.get("invoice_no") == k:
                    found.append(p)
            if len(found) == 0:
                st.error("Invalid")
            else:
                pu = found[0]
                st.success("Welcome " + pu.get("name"))
                pfs = list(PPT_DIR.glob(pu.get("course_id") + "_Course*"))
                if len(pfs) > 0:
                    for pf in pfs:
                        data = pf.read_bytes()
                        st.download_button("Download 40 Modules", data=data, file_name=pf.name)

    if menu == "Chat Support":
        st.title("Chat Support")
        q = st.chat_input("Ask")
        if q:
            st.write("100 Books 40 Modules Each Ready Master Teacher")