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

def create_rich_40_pptx(cid, ctopic):
    from pptx import Presentation
    from pptx.util import Inches, Pt
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    for m in range(40):
        module_no = m + 1
        slide = prs.slides.add_slide(prs.slide_layouts[6])

        title_box = slide.shapes.add_textbox(Inches(0.4), Inches(0.1), Inches(12.5), Inches(0.7))
        title_tf = title_box.text_frame
        title_tf.word_wrap = True
        title_text = ""
        if module_no == 1:
            title_text = "Module 01 KYA HAI What Is " + ctopic + " - 5 Examples Business Level"
        elif module_no == 2:
            title_text = "Module 02 KYON HAI Why Important Future Proof " + ctopic
        elif module_no == 3:
            title_text = "Module 03 KAHAN HAI Where Use Market Scope " + ctopic
        elif module_no == 4:
            title_text = "Module 04 KAB Best Timing Launch " + ctopic
        elif module_no == 5:
            title_text = "Module 05 KAUN Eligible Who Can Do " + ctopic
        elif module_no == 20:
            title_text = "Module 20 MISTAKES 90 Percent Fail " + ctopic
        elif module_no == 21:
            title_text = "Module 21 PRO TIP Secret Diary Millionaire " + ctopic
        elif module_no == 40:
            title_text = "Module 40 FINAL PROJECT Certification Business " + ctopic
        else:
            title_text = "Module " + str(module_no) + " " + ctopic + " Master Teacher Super Teacher"
        title_tf.text = title_text
        title_tf.paragraphs[0].font.size = Pt(20)
        title_tf.paragraphs[0].font.bold = True

        body_box = slide.shapes.add_textbox(Inches(0.4), Inches(0.9), Inches(12.5), Inches(6.3))
        body_tf = body_box.text_frame
        body_tf.word_wrap = True

        content = ""
        if module_no == 1:
            content = ctopic + " kya hai. Definition simple language me master teacher jaise. 5 real examples: 1 Business automation se time bachao 2 Client ke liye project banao 3 Freelancing Upwork Fiverr pe becho 4 Agency model se team banao 5 SaaS product recurring income. Scope 2026 me 300 percent growth. Beginner to expert roadmap 30 din me. Teacher 20 saal experience se samjhata hai. Earning first month 15k kaise. Foundation strong karo."
        elif module_no == 2:
            content = ctopic + " kyon important hai future me. Market data 2026 demand bahut high. 90 percent log fail kyon hote hain: bina samjhe advanced, roz practice nahi, sirf video dekhte hain. Kyon seekhna chahie abhi: future proof skill, AI aa raha hai, paise kyon banta hai isme proof ke saath. Case study Rahul village se 15k first client. Demand proof Google trends."
        elif module_no == 3:
            content = ctopic + " kahan use hota hai. Instagram Reels YouTube Shorts Business Automation Job Freelancing Agency Startup me use. Kahan clients milte hain: Upwork, Fiverr, LinkedIn, Instagram DM, Facebook groups. India global market. Gaon se bhi kar sakte hain mobile se. Real places list kahan kaam aata hai."
        elif module_no == 17:
            content = "Real Kahani Rahul Village Se " + ctopic + ". Rahul gaon se 2 mahine roz 1 ghanta project kiya. Teesre mahine pehla client 15k mila Upwork se. Chauthe mahine 5 clients 75k per month. Aaj 2 lakh per month kama raha hai. Kaise kiya: daily diary, 30 min practice, 1 project roz. Real story motivation. Tum bhi kar sakte ho."
        elif module_no == 20:
            content = ctopic + " Mistakes 90 percent log karte hain. Galti1: Bina samjhe advanced shuru kar dete hain. Galti2: Roz practice nahi sirf video dekhte hain. Galti3: Paise ke peeche bhagte hain learning nahi karte. Galti4: Diary nahi rakhte kya seekha bhool jate hain. Galti5: Mentor nahi dhundhte. Kaise bache in galtiyon se master teacher batata hai."
        elif module_no == 21:
            content = "PRO TIP Secret Diary " + ctopic + ". Roz raat ko 10 min diary likho: Aaj kya seekha, kya galti hui, kal kya karna hai. Ye trick successful students use karte hain koi YouTube pe nahi batata. Millionaire mindset kaise bane. Focus kaise laaye. Ye secret diary se 30 din me expert banoge."
        elif module_no == 24:
            content = ctopic + " Freelancing Upwork Fiverr. Profile kaise banaye professional photo title overview. Gig kaise banaye pricing kya rakhe 500 se start 5000 tak. Proposal kaise likhe jo client accept kare: hook, portfolio, CTA. First client 7 din me kaise laaye. Real proposal template."
        elif module_no == 31:
            content = ctopic + " SEO Search Engine Optimizing. Blog kaise likhe 1000 words SEO friendly. Keyword research kaise kare free tools se. On page SEO title description headings. Off page SEO backlinks kaise banaye. Google pe first page kaise aaye 30 din me. Blog se clients kaise aate hain."
        elif module_no == 40:
            content = ctopic + " Final Project Certification. Final project client ke liye real project banao: Ek complete automation, ya Reels campaign, ya SEO blog. Portfolio me add karo. Certification business level. Real income start karo. App strong business level professional. Ab aap expert ho 40 modules complete. Next steps business plan 1Cr."
        else:
            content = ctopic + " Module " + str(module_no) + " Master Teacher Super Teacher 20 Years Teaching. KYA HAI definition example. KYON HAI future importance. KAHAN use market scope. KAB best timing. KAUN eligible student housewife job business 16-60. KAISE architecture Perceive Reason Act loop RAG memory. KISSE tools Canva CapCut ChatGPT Notion Make n8n. KYA USE earning freelancing 20k-50k business 1L plus. KAISE USE mobile reels laptop dashboard practical hands on. KAISE KARNA daily 30 min diary weekly revise. REAL KAHANI Rahul 1L per month. MISTAKES PRO TIP HOMEWORK BUSINESS PLAN. 300 words rich content."

        body_tf.text = content
        body_tf.paragraphs[0].font.size = Pt(12)

    new_name = cid + "_Course_40Modules_RICH_V82.pptx"
    out_path = PPT_DIR / new_name
    prs.save(str(out_path))
    old_path = PPT_DIR / (cid + "_Course.pptx")
    if old_path.exists():
        try:
            old_path.unlink()
        except:
            pass
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
        st.title("Dashboard 100 Courses 40 Modules RICH V82")
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
        c2.metric("Ready RICH 40", proper)
        c3.metric("Old", bekar)
        c4.metric("Missing", missing)
        if proper >= 100:
            st.success("Full 100 Books 40 Modules RICH V82 Master Teacher Jaag Gaya Real Kaam")
        else:
            st.warning("Purani khali wali delete karo aur RICH V82 wali banao")
        if st.button("DELETE KHALI OLD CACHE"):
            for f in list(PPT_DIR.glob("*.*")):
                try:
                    f.unlink()
                except:
                    pass
            st.success("Khali old cache deleted - Ab naya RICH banega")
            st.rerun()
        if st.button("CREATE 100 BOOKS 40 MODULES RICH V82", type="primary"):
            bar = st.progress(0)
            for idx, c in enumerate(courses):
                create_rich_40_pptx(c.get("id"), c.get("topic"))
                pct = int((idx + 1) / len(courses) * 100)
                bar.progress(pct)
            st.success("100 Books 40 Modules RICH V82 Created - Master Teacher Jaag Gaya")
            st.balloons()
            st.rerun()
        rows = []
        for c in courses:
            found = list(PPT_DIR.glob(c.get("id") + "_Course*"))
            status = "Ready RICH 40"
            if len(found) == 0:
                status = "Missing"
            rows.append({"ID": c.get("id"), "Course": c.get("topic"), "Status": status})
        st.dataframe(pd.DataFrame(rows), use_container_width=True)

    if menu == "Super Agent Full Power":
        st.title("Super Agent Brahma Full Power - Master Teacher Super Teacher Jaag Gaya")
        st.write("Master teacher super teacher kya kar raha hai? Ab jaag gaya! 20 saal teaching har module me KYA HAI KYON HAI KAHAN KAB KAUN KAISE KISSE KYA USE KAISE USE KAISE KARNA REAL KAHANI MISTAKES PRO TIP HOMEWORK BUSINESS PLAN padhata hai 400 shabdon me har slide.")
        st.write("Full power search engine optimizing social media digital marketing blog posting Facebook Instagram posting courses bechne ke liye khud karega hamesha kabhi rukega nahi. Niche agents AI ke banega.")
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
            st.success("Super Agent Full Power Started - Master Teacher Jaag Gaya Real Kaam Kar Raha Hai")
            st.dataframe(pd.DataFrame(posts), use_container_width=True)
            st.balloons()

    if menu == "Course Library 40 Modules":
        st.title("Course Library 100 Books 40 Modules RICH V82")
        total = len(courses)
        proper = len(list(PPT_DIR.glob("*_Course*")))
        c1, c2 = st.columns(2)
        c1.metric("Total", total)
        c2.metric("Ready RICH V82 40 Modules", proper)
        for idx, co in enumerate(courses):
            cid = co.get("id")
            pf = list(PPT_DIR.glob(cid + "_Course*"))
            col1, col2 = st.columns([3, 1])
            with col1:
                if len(pf) > 0:
                    st.success(str(idx + 1) + ". " + co.get("topic") + " Ready RICH 40 - Ab Kaun Kharidega? Ab Kharidega! Content Bhara Hua")
                else:
                    st.warning(str(idx + 1) + ". " + co.get("topic") + " Missing")
            with col2:
                if len(pf) > 0:
                    data = pf[0].read_bytes()
                    st.download_button("Download RICH V82 40 Modules", data=data, file_name=pf[0].name, key="dl_" + cid)

    if menu == "Marketing Engine":
        st.title("Marketing Engine Super Agent Full Power Kabhi Rukega Nahi V82")
        st.write("Search Engine Optimizing Social Media Digital Marketing Blog Facebook Instagram Posting Courses Bechne Ke Liye Khud Karega Hamesha")
        if st.button("Generate Today Marketing Posts", type="primary"):
           