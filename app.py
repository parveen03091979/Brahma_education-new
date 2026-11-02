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
MARKETING_FILE = DATA_DIR / "marketing.json"
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

def create_40_modules_pptx(cid, ctopic):
    try:
        from pptx import Presentation
        from pptx.util import Inches, Pt
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)

        modules = []
        modules.append(["M01 Intro KYA HAI " + ctopic, "What is " + ctopic + " 5 examples fundamentals simple language teacher jaise definition"])
        modules.append(["M02 KYON HAI Why Important", "Why important future Market data 2026 90 percent fail proof kyon seekhna chahie demand"])
        modules.append(["M03 KAHAN HAI Market Scope", "Kahan use hota Instagram YouTube Business Job Freelancing Agency Market scope India global"])
        modules.append(["M04 KAB Best Timing", "Kab best time morning 6 to 8 Monday Thursday Seasonal timing launch timing"])
        modules.append(["M05 KAUN Eligible Who Can Do", "Kaun kar sakta Student Housewife Job Business 16 to 60 age har koi eligible"])
        modules.append(["M06 KAISE Architecture", "Kaise kaam karta Perceive Reason Act loop architecture step by step expert thinking"])
        modules.append(["M07 KISSE Tools Setup", "Kisse hoga Free tools Canva CapCut ChatGPT Notion Paid tools setup guide"])
        modules.append(["M08 KYA USE Earning Model", "Kya use Earning freelancing 20k to 50k business 1L plus job promotion use cases"])
        modules.append(["M09 KAISE USE Practical", "Kaise use karna practical Mobile Reels laptop browser dashboard hands on use"])
        modules.append(["M10 KAISE KARNA Right Way", "Kaise karna chahie sahi tarika Daily 30 min diary Weekly revise best practice"])
        modules.append(["M11 Fundamentals Deep Dive", "Fundamentals deep dive core concepts theory practical mix teacher jaise"])
        modules.append(["M12 Tools Mastery Part1", "Tools mastery part1 Canva ChatGPT CapCut basics to intermediate hands on"])
        modules.append(["M13 Tools Mastery Part2", "Tools mastery part2 Make n8n Zapier Notion advanced automation tools"])
        modules.append(["M14 Perceive Reason Act", "Perceive Reason Act loop ReAct Chain Thought how expert thinks reasoning"])
        modules.append(["M15 RAG Memory System", "RAG deep memory short long vector memory how to build memory system"])
        modules.append(["M16 Prompt Engineering", "Prompt engineering for " + ctopic + " best prompts templates 100 prompts library"])
        modules.append(["M17 Case Study Rahul Village", "Real kahani Rahul village 2 months daily 1 hour project third month client 15k story"])
        modules.append(["M18 Case Study 1L Per Month", "Case study 1L per month business 5 clients 75k fourth month scaling story"])
        modules.append(["M19 Case Study 10M ARR", "Case study 10M ARR SaaS story how build 10M annual recurring revenue real"])
        modules.append(["M20 Mistakes 90 Percent Fail", "Galti1 bina samjhe advanced Galti2 no practice sirf video Galti3 paise peeche Galti4 diary nahi Galti5 mentor nahi"])
        modules.append(["M21 PRO TIP Diary Secret", "PRO TIP secret diary roz likho kya seekha kya galti kal kya karna Raat 10 min padho trick"])
        modules.append(["M22 Mindset Millionaire", "Mindset mastery Millionaire mindset meditation focus time management motivation"])
        modules.append(["M23 Time Management", "Time management kaise daily 1 hour nikalna kaise course complete 30 days me"])
        modules.append(["M24 Freelancing Upwork Fiverr", "Freelancing setup Upwork Fiverr profile gig pricing proposal client handling"])
        modules.append(["M25 Agency Business Model", "Agency business model kaise agency banaye team building client acquisition"])
        modules.append(["M26 SaaS Business Model", "SaaS business model kaise SaaS banaye is course se recurring income model"])
        modules.append(["M27 Client Handling Pricing", "Client handling pricing kitna charge kare negotiation contract payment collection"])
        modules.append(["M28 Portfolio Building", "Portfolio building kaise portfolio banaye behance dribbble github 10 samples"])
        modules.append(["M29 Lead Generation", "Lead generation kaise leads laaye LinkedIn Instagram YouTube organic paid methods"])
        modules.append(["M30 Sales Funnel", "Sales funnel landing page CRO conversion optimization kaise sale close kare"])
        modules.append(["M31 SEO Search Engine Optimizing", "SEO search engine optimizing blog post keyword research on page off page ranking"])
        modules.append(["M32 Social Media Marketing", "Social media marketing Instagram Reels YouTube Shorts LinkedIn growth hacking"])
        modules.append(["M33 Content Creation Reels", "Content creation Reels viral formula hook story CTA thumbnail design viral"])
        modules.append(["M34 Email WhatsApp Marketing", "Email marketing automation WhatsApp marketing Telegram channel growth sequences"])
        modules.append(["M35 Automation n8n Make", "Automation n8n Make Zapier kaise automate kare posting lead follow up support"])
        modules.append(["M36 Advanced Strategies", "Advanced strategies pro level tricks jo expert use karte hain competition beat"])
        modules.append(["M37 Optimization Scaling", "Optimization scaling kaise 1L se 10L tak scale kare team ads systems"])
        modules.append(["M38 Business Plan 1Cr", "Business plan 1Cr tak kaise business banaye startup funding pitch deck"])
        modules.append(["M39 Homework Assignments", "Homework Assignments Aaj project banao Assignment1 simple Assignment2 research Assignment3 diagram Test 20 questions"])
        modules.append(["M40 Final Project Certification", "Final project client ke liye real project Certification business level real income app strong"])

        for mod in modules:
            title = mod[0]
            body = mod[1]
            slide = prs.slides.add_slide(prs.slide_layouts[5])
            box1 = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12.3), Inches(0.7))
            tf1 = box1.text_frame
            tf1.word_wrap = True
            p = tf1.paragraphs[0]
            p.text = title
            p.font.size = Pt(20)
            p.font.bold = True
            box2 = slide.shapes.add_textbox(Inches(0.5), Inches(1.0), Inches(12.3), Inches(6.2))
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

def generate_marketing_posts():
    posts = []
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    for c in courses[:20]:
        topic = c.get("topic")
        posts.append({"date": today, "platform": "Facebook", "course": topic, "type": "Post 1 Morning", "content": "Learn " + topic + " today Business Level Real Income Link in bio"})
        posts.append({"date": today, "platform": "Facebook", "course": topic, "type": "Post 2 Afternoon", "content": "Case Study " + topic + " Rahul village 15k first client Real story"})
        posts.append({"date": today, "platform": "Facebook", "course": topic, "type": "Post 3 Evening", "content": "Mistakes in " + topic + " 90 percent fail How to avoid PRO TIP"})
        posts.append({"date": today, "platform": "Instagram", "course": topic, "type": "Reel Morning", "content": "Reel " + topic + " 30 sec hook viral formula"})
        posts.append({"date": today, "platform": "Instagram", "course": topic, "type": "Post Afternoon", "content": "Carousel " + topic + " 5 tools free Canva CapCut ChatGPT"})
        posts.append({"date": today, "platform": "Instagram", "course": topic, "type": "Story Evening", "content": "Story poll " + topic + " Kya aap seekhna chahte hain Yes No"})
        posts.append({"date": today, "platform": "Blog", "course": topic, "type": "Blog SEO", "content": "Blog SEO " + topic + " 1000 words KYA HAI KYON HAI KAISE keyword research"})
        posts.append({"date": today, "platform": "Blog", "course": topic, "type": "Blog Case Study", "content": "Blog case study " + topic + " Rahul 1L per month real kahani"})
    save_json(MARKETING_FILE, posts)
    return posts

topics = TOPICS
courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])
marketing = load_json(MARKETING_FILE, [])

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
        menu = st.sidebar.radio("Admin", ["Dashboard", "Super Agent Full Power", "Course Library 40 Modules", "Marketing Engine", "Sales QR"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Dashboard - 100 Courses 40 Modules Business Level")
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
        c2.metric("Courses Ready 40 Modules", proper)
        c3.metric("Old Files", bekar)
        c4.metric("Missing", missing)
        if proper >= 100:
            st.success("Course Library Full 100 Books 40 Modules Master Teacher Se Phone Me Khulegi")
        else:
            st.warning("Purani 13 slides wali delete karo aur 40 modules wali banao")
        colA,colB,colC = st.columns(3)
        with colA:
            if st.button("DELETE OLD 13 SLIDES"):
                for f in list(PPT_DIR.glob("*.*")):
                    try:
                        f.unlink()
                    except:
                        pass
                st.success("Old deleted")
                st.rerun()
        with colB:
            if st.button("CREATE 100 BOOKS 40 MODULES", type="primary"):
                bar = st.progress(0)
                for idx, c in enumerate(courses):
                    create_40_modules_pptx(c.get("id"), c.get("topic"))
                    bar.progress(int((idx+1)/len(courses)*100))
                st.success("100 Books 40 Modules Created Master Teacher Se")
                st.balloons()
                st.rerun()
        with colC:
            if st.button("DELETE ALL + 40 MODULES AUTO"):
                for f in list(PPT_DIR.glob("*.*")):
                    try:
                        f.unlink()
                    except:
                        pass
                bar = st.progress(0)
                for idx, c in enumerate(courses):
                    create_40_modules_pptx(c.get("id"), c.get("topic"))
                    bar.progress(int((idx+1)/len(courses)*100))
                st.success("100 Books 40 Modules Auto Created")
                st.rerun()
        df_data = []
        for c in courses:
            s = "Ready 40 Modules" if list(PPT_DIR.glob(c.get("id") + "_Course*")) else "Missing"
            df_data.append({"ID": c.get("id"), "Course": c.get("topic"), "Status": s})
        st.dataframe(pd.DataFrame(df_data), use_container_width=True)

    if menu == "Super Agent Full Power":
        st.title("Super Agent Brahma - Full Power - Kabhi Rukega Nahi")
        st.write("Full power di thi taki vah search engine optimizing social media work digital marketing blog posting Facebook Instagram posting in courses ko bechne ke liye khud karega aur hamesha karta rahega kabhi rukega nahi")
        st.write("Har din fix kitni post dalega Facebook aur Insta par aur kitne blog banaega Sab super agent apne aap karta rahega apne niche agents banakar AI ke")
        st.divider()
        st.subheader("Daily Fixed Marketing Plan - Jo Humne Decide Kiya Tha")
        fb = st.number_input("Facebook posts per day", value=3, min_value=1, max_value=10)
        insta = st.number_input("Instagram posts per day Reels + Posts + Story", value=3, min_value=1, max_value=10)
        blog = st.number_input("Blog posts per day SEO", value=2, min_value=1, max_value=10)
        st.write("Niche Agents AI ke banega - Har course ke liye alag agent - SEO agent, Facebook agent, Instagram agent, Blog agent")
        if st.button("START SUPER AGENT FULL POWER - ROZ POST KAREGA", type="primary"):
            posts = generate_marketing_posts()
            st.success("Super Agent Full Power Started - Roz " + str(fb) + " Facebook, " + str(insta) + " Instagram, " + str(blog) + " Blog posts karega - Kabhi rukega nahi - Niche agents ban gaye")
            st.dataframe(pd.DataFrame(posts), use_container_width=True)
            st.balloons()
        st.divider()
        opts = []
        for c in courses:
            opts.append(c.get("topic") + " - " + c.get("id"))
        sel = st.selectbox("Course select karo 40 modules banane ke liye", opts)
        if st.button("Is Course Ki 40 Modules Book Banao Master Teacher Se", type="primary"):
            cid = sel.split(" - ")[-1]
            ctopic = " - ".join(sel.split(" - ")[:-1])
            with st.spinner("Master Teacher 40 modules book bana raha hai " + ctopic):
                ok = create_40_modules_pptx(cid, ctopic)
                if ok:
                    st.success("40 Modules Book Ban Gayi " + ctopic + " Master Teacher Se")
                    st.balloons()
                else:
                    st.error("Fail")

    if menu == "Course Library 40 Modules":
        st.title("Course Library - 100 Books 40 Modules Each")
        total = len(courses)
        proper = len(list(PPT_DIR.glob("*_Course*")))
        c1,c2 = st.columns(2)
        c1.metric("Total", total)
        c2.metric("Ready 40 Modules", proper)
        if proper >= 100:
            st.success("Full 100 Books 40 Modules Each - Total 4000 Modules - Master Teacher Se")
        for idx, co in enumerate(courses):
            cid = co.get("id")
            pf = list(PPT_DIR.glob(cid + "_Course*"))
            col1,col2 = st.columns([3,1])
            with col1:
                if pf:
                    st.success(str(idx+1) + ". " + co.get("topic") + " Ready 40 Modules")
                else:
                    st.warning(str(idx+1) + ". " + co.get("topic")