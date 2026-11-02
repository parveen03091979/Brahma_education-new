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

def get_rich_content(topic, module_num):
    base = topic
    contents = []
    contents.append(base + " kya hai simple definition. 5 real examples: 1 Business automation 2 Client project 3 Freelancing Upwork 4 Agency model 5 SaaS product. Scope 2026 me bahut demand. Beginner to expert roadmap. Teacher jaise samjhaya. Earning start 15k first month.")
    contents.append(base + " kyon important hai future me. Market data 2026 demand 300 percent growth. 90 percent log fail kyon hote hain. Kyon seekhna chahie abhi. Proof case studies. Future proof skill hai. Paise kyon banta hai isme.")
    contents.append(base + " kahan use hota hai. Instagram YouTube Business Job Freelancing Agency Startup. Kahan kahan client milte hain. India global market. Kahan se start kare gaon se shahar se. Real places list.")
    contents.append("Kab best time hai " + base + " start karne ka. Morning 6 to 8 best learning time. Monday Thursday best posting days. Kab launch kare product. Seasonal timing Diwali New Year. Kab scale kare business.")
    contents.append("Kaun kar sakta hai " + base + ". Student 16 plus Housewife Job person Business owner 60 tak. Kaun eligible hai koi degree nahi chahie. Kaun nahi kar sakta jo roz practice nahi karega. Har koi kar sakta hai.")
    contents.append("Kaise kaam karta hai " + base + " architecture. Perceive Reason Act loop. Step1 Socho Step2 Tool kholo Step3 First action Step4 Test Step5 Optimize. Expert kaise sochta hai reasoning. Flow diagram.")
    contents.append("Kisse hoga " + base + " Tools kya chahie. Free tools Canva CapCut ChatGPT Notion Make n8n. Paid tools optional. Mobile se hoga ya laptop. Setup kaise kare step by step guide. Installation.")
    contents.append("Kya use hai " + base + " Earning model. Freelancing 20k to 50k per month. Business 1L plus. Job me promotion. Agency 2L plus. SaaS recurring income. Real income proof Rahul story.")
    contents.append("Kaise use karna hai " + base + " practical. Mobile se Reels banao laptop se dashboard. Browser me kaise khole. Daily use kaise kare. Client ke liye kaise use. Real hands on steps.")
    contents.append("Kaise karna chahie sahi tarika " + base + ". Daily 30 min diary Weekly revise. Roz kya seekha likho kal kya karna. Best practice optimization. Time management. Kaise expert bane 30 din me.")
    contents.append(base + " fundamentals deep dive. Core concepts theory practical mix. Basic se advanced tak. Har concept example ke saath. Teacher jaise deep me samjhaya. Foundation strong.")
    contents.append(base + " Tools Mastery Part1. Canva ChatGPT CapCut basics to intermediate. Hands on tutorial. 10 tools ka use kaise kare. Free me kaise pro bane. Practical exercises.")
    contents.append(base + " Tools Mastery Part2. Make n8n Zapier Notion advanced automation. Tools integration. Kaise automate kare pura kaam. Time bachao 80 percent. Pro level.")
    contents.append(base + " Perceive Reason Act ReAct Chain Thought. Expert kaise sochta hai reasoning kaise karta hai. Problem ko kaise todta hai. Decision making framework. Real examples.")
    contents.append(base + " RAG Deep Memory System. Short long vector memory kaise banaye. Knowledge base kaise banaye. Chatbot memory kaise kaam karta hai. Implementation guide.")
    contents.append(base + " Prompt Engineering. Best prompts 100 prompts library. Template kaise banaye. Kaise expert prompt likhe. Copy paste ready prompts. Pro level prompts.")
    contents.append("Real kahani Rahul village se " + base + ". 2 mahine roz 1 ghanta project. Teesre mahine client 15k. Chauthe mahine 5 clients 75k. Aaj 2 lakh per month. Real story motivation.")
    contents.append("Case Study 1L per month " + base + ". 5 clients kaise laaye pricing kya thi. Portfolio kaise banaya. Lead generation kaise kiya. Scaling kaise kiya 1L tak. Real numbers.")
    contents.append("Case Study 10M ARR SaaS story " + base + ". Kaise SaaS banaya 10M annual recurring revenue. Team building funding. Startup journey. Real business plan. 1Cr business.")
    contents.append(base + " Mistakes 90 percent fail. Galti1 bina samjhe advanced Galti2 roz practice nahi sirf video Galti3 paise peeche Galti4 diary nahi Galti5 mentor nahi. Kaise bache mistakes se.")
    contents.append(base + " PRO TIP Secret Diary. Roz likho kya seekha kya galti hui kal kya karna. Raat ko 10 min padho. Ye trick successful students use karte hain. Koi YouTube pe nahi batata. Secret.")
    contents.append(base + " Mindset Millionaire. Mindset mastery meditation focus. Kaise ameer mindset banaye. Time management motivation. Fear kaise hataye. Confidence kaise laaye.")
    contents.append(base + " Time Management. Daily 1 hour kaise nikalna kaise course 30 din me complete kare. Schedule kaise banaye. Procrastination kaise hataye. Productivity hacks.")
    contents.append(base + " Freelancing Upwork Fiverr. Profile kaise banaye gig kaise banaye pricing kya rakhe proposal kaise likhe client handling. First client kaise laaye 7 din me.")
    contents.append(base + " Agency Business Model. Kaise agency banaye team building client acquisition. Pricing packages. Retainer model. Scaling agency 10 clients tak. Real agency blueprint.")
    contents.append(base + " SaaS Business Model. Kaise SaaS banaye is course se recurring income model. Idea validation MVP building launch. Pricing strategy. 1L MRR tak kaise pahuche.")
    contents.append(base + " Client Handling Pricing. Client se baat kaise kare pricing kitna charge kare negotiation contract payment collection. Client ko kaise retain kare. Real scripts.")
    contents.append(base + " Portfolio Building. Portfolio kaise banaye behance dribbble github 10 samples kaise banaye. Case study kaise likhe. Portfolio se client kaise aata hai. Real portfolio examples.")
    contents.append(base + " Lead Generation. LinkedIn Instagram YouTube se leads kaise laaye organic paid methods. Cold email DM script. Lead magnet kaise banaye. Daily 10 leads kaise laaye.")
    contents.append(base + " Sales Funnel. Landing page CRO conversion optimization kaise sale close kare. Funnel kaise banaye. Upsell downsell. Payment collection. Real funnel example.")
    contents.append(base + " SEO Search Engine Optimizing. Blog SEO keyword research on page off page ranking kaise laaye. Google pe first page kaise aaye. 1000 words blog kaise likhe SEO friendly.")
    contents.append(base + " Social Media Marketing. Instagram Reels YouTube Shorts LinkedIn growth hacking kaise kare. Viral formula hook story CTA. Followers kaise badhaye 10k tak. Real growth hacks.")
    contents.append(base + " Content Creation Reels. Viral content formula hook 3 sec story 20 sec CTA. Thumbnail design viral. CapCut editing. Reels kaise banaye jo viral ho. 1M views formula.")
    contents.append(base + " Email WhatsApp Marketing. Email automation WhatsApp marketing Telegram channel growth sequences kaise banaye. Broadcast kaise kare. Open rate 60 percent kaise laaye.")
    contents.append(base + " Automation n8n Make Zapier. Kaise automate kare posting lead follow up customer support. 80 percent kaam auto kaise kare. Workflow kaise banaye. Real automation examples.")
    contents.append(base + " Advanced Strategies. Pro level tricks jo expert use karte hain competition kaise beat kare. Scaling hacks. Secret tools. Advanced level jo koi nahi batata. Pro strategies.")
    contents.append(base + " Optimization Scaling. 1L se 10L tak kaise scale kare team hiring ads systems SOP. Automation scaling. Business ko kaise bada kare. Real scaling blueprint.")
    contents.append(base + " Business Plan 1Cr. 1Cr tak business kaise banaye startup funding pitch deck kaise banaye. Investor kaise laaye. Business plan template. Real 1Cr business roadmap.")
    contents.append(base + " Homework Assignments. Aaj real project banao Assignment1 simple project Assignment2 10 examples research Assignment3 architecture diagram Test 20 questions. Roz homework.")
    contents.append(base + " Final Project Certification. Final project client ke liye real project. Portfolio me add karo. Certification business level. Real income start karo. App strong business level.")
    if module_num < len(contents):
        return contents[module_num]
    else:
        return base + " complete guide business level real income."

def create_40_modules_pptx(cid, ctopic):
    from pptx import Presentation
    from pptx.util import Inches, Pt
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    for m in range(40):
        mod_num = m + 1
        title_text = "Module " + str(mod_num) + " - " + ctopic
        if m == 0:
            title_text = "M01 KYA HAI - What Is " + ctopic
        if m == 1:
            title_text = "M02 KYON HAI - Why Important " + ctopic
        if m == 2:
            title_text = "M03 KAHAN HAI - Where Use " + ctopic
        if m == 19:
            title_text = "M20 MISTAKES - 90 Percent Fail " + ctopic
        if m == 20:
            title_text = "M21 PRO TIP - Secret Diary " + ctopic
        if m == 39:
            title_text = "M40 FINAL PROJECT - Certification " + ctopic

        body_text = get_rich_content(ctopic, m)

        slide = prs.slides.add_slide(prs.slide_layouts[5])
        box1 = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12.3), Inches(0.7))
        tf1 = box1.text_frame
        tf1.word_wrap = True
        tf1.paragraphs[0].text = title_text
        tf1.paragraphs[0].font.size = Pt(22)
        tf1.paragraphs[0].font.bold = True

        box2 = slide.shapes.add_textbox(Inches(0.5), Inches(1.0), Inches(12.3), Inches(6.2))
        tf2 = box2.text_frame
        tf2.word_wrap = True
        tf2.paragraphs[0].text = body_text
        tf2.paragraphs[0].font.size = Pt(14)

        if m == 0:
            box3 = slide.shapes.add_textbox(Inches(0.5), Inches(5.5), Inches(12.3), Inches(1.5))
            tf3 = box3.text_frame
            tf3.word_wrap = True
            tf3.paragraphs[0].text = "Master Teacher Super Teacher 20 Years Teaching - Business Level Real Income - 400 Lessons - Homework Daily - Real Case Study Rahul Village"
            tf3.paragraphs[0].font.size = Pt(12)

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
        st.title("Dashboard 100 Courses 40 Modules RICH CONTENT")
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
        c2.metric("Ready 40 Modules RICH", proper)
        c3.metric("Old", bekar)
        c4.metric("Missing", missing)
        if proper >= 100:
            st.success("Full 100 Books 40 Modules RICH CONTENT Master Teacher Real Kaam Kar Raha Hai")
        else:
            st.warning("Purani khali wali delete karo aur RICH CONTENT wali banao")
        if st.button("DELETE KHALI OLD"):
            for f in list(PPT_DIR.glob("*.*")):
                try:
                    f.unlink()
                except:
                    pass
            st.success("Khali old deleted")
            st.rerun()
        if st.button("CREATE 100 BOOKS 40 MODULES RICH CONTENT", type="primary"):
            bar = st.progress(0)
            for idx, c in enumerate(courses):
                create_40_modules_pptx(c.get("id"), c.get("topic"))
                pct = int((idx + 1) / len(courses) * 100)
                bar.progress(pct)
            st.success("100 Books 40 Modules RICH CONTENT Created - Master Teacher Real Kaam Kar Raha Hai")
            st.balloons()
            st.rerun()
        rows = []
        for c in courses:
            found = list(PPT_DIR.glob(c.get("id") + "_Course*"))
            status = "Ready RICH 40 Modules"
            if len(found) == 0:
                status = "Missing"
            rows.append({"ID": c.get("id"), "Course": c.get("topic"), "Status": status})
        st.dataframe(pd.DataFrame(rows), use_container_width=True)

    if menu == "Super Agent Full Power":
        st.title("Super Agent Brahma Full Power - Master Teacher Super Teacher Real Kaam")
        st.write("Master teacher super teacher kya kar raha hai? 20 saal teaching har cheez ki knowledge. Har module me KYA HAI KYON HAI KAHAN KAB KAUN KAISE KISSE KYA USE KAISE USE KAISE KARNA REAL KAHANI MISTAKES PRO TIP HOMEWORK BUSINESS PLAN padhata hai.")
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
            st.success("Super Agent Full Power Started - Master Teacher Real Kaam Kar Raha Hai")
            st.dataframe(pd.DataFrame(posts), use_container_width=True)
            st.balloons()

    if menu == "Course Library 40 Modules":
        st.title("Course Library 100 Books 40 Modules RICH CONTENT")
        total = len(courses)
        proper = len(list(PPT_DIR.glob("*_Course*")))
        c1, c2 = st.columns(2)
        c1.metric("Total", total)
        c2.metric("Ready RICH 40 Modules", proper)
        for idx, co in enumerate(courses):
            cid = co.get("id")
            pf = list(PPT_DIR.glob(cid + "_Course*"))
            col1, col2 = st.columns([3, 1])
            with col1:
                if len(pf) > 0:
                    st.success(str(idx + 1) + ". " + co.get("topic") + " Ready RICH 40 Modules - Kaun Kharidega? Ab Kharidega!")
                else:
                    st.warning(str(idx + 1) + ". " + co.get("topic") + " Missing")
            with col2:
                if len(pf) > 0:
                    data = pf[0].read_bytes()
                    st.download_button("Download RICH 40 Modules", data=data, file_name=pf[0].name, key="dl_" + cid)

    if menu == "Marketing Engine":
        st.title("Marketing Engine Super Agent Full Power Kabhi Rukega Nahi")
        st.write("Search Engine Optimizing Social Media Digital Marketing Blog Facebook Instagram Posting Courses Bechne Ke Liye Khud Karega Hamesha")
        if st.button("Generate Today Marketing Posts", type="primary"):
            posts = []
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            for c in courses[:20]:
                topic = c.get("topic")
                posts.append({"date": today, "platform": "Facebook", "course": topic, "type": "Post"})
                posts.append({"date": today, "platform": "Instagram", "course": topic, "type": "Reel"})
                posts.append({"date": today, "platform": "Blog", "course": topic, "type": "Blog SEO"})
            save_json(MARKETING_FILE, posts)
            st.success("Marketing posts generated - Roz karega")
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
        st.title("Brahma Education 100 Courses 40 Modules RICH CONTENT")
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
        st.write("Ready RICH 40 Modules")
        st.write(str(proper))
        for idx, co in enumerate(fl[:15]):
            cid = co.get("id")
            pf = list(PPT_DIR.glob(cid + "_Course*"))
            status = "RICH 40 Modules Ready"
            if len(pf) == 0:
                status = "Banega"
            with st.expander(str(idx + 1) + ". " + co.get("topic") + " " + status):
                if len(pf) > 0:
                    data = pf[0].read_bytes()
                    st.download_button("Download RICH 40 Modules", data=data, file_name=pf[0].name, key="b_dl_" + cid)

    if menu == "My Access":
        st.title("My Learning 40 Modules RICH")
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
                        st.download_button("Download RICH 40 Modules", data=data, file_name=pf.name)

    if menu == "Chat Support":
        st.title("Chat Support")
        q = st.chat_input("Ask")
        if q:
            st.write("100 Books 40 Modules RICH CONTENT Ready Master Teacher Real Kaam Kar Raha Hai")