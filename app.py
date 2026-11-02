import streamlit as st
import json
import hashlib
import datetime
import urllib.parse
from pathlib import Path
import pandas as pd

try:
    from gtts import gTTS
    GTTS_OK = True
except:
    GTTS_OK = False

st.set_page_config(page_title="Brahma Education - Professional Courses", layout="wide")
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
CHAT_FILE = DATA_DIR / "chat_history.json"
CONFIG_FILE = DATA_DIR / "config.json"
LOG_FILE = DATA_DIR / "log.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
VOICE_DIR = DATA_DIR / "voice"
VOICE_DIR.mkdir(exist_ok=True)
BLOG_DIR = DATA_DIR / "blogs"
BLOG_DIR.mkdir(exist_ok=True)
SEO_DIR = DATA_DIR / "seo"
SEO_DIR.mkdir(exist_ok=True)
SOCIAL_DIR = DATA_DIR / "social"
SOCIAL_DIR.mkdir(exist_ok=True)

MY_UPI_ID = "parveen39179@okicici"
MY_NAME = "Parveen Kumar"

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size > 2:
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])
chats = load_json(CHAT_FILE, [])
config = load_json(CONFIG_FILE, {})
logs = load_json(LOG_FILE, [])

if len(courses) == 0:
    base_topics = [
        "AI Agent Automation 2026", "Instagram Viral Reels Mastery", "YouTube Automation AI",
        "No-Code Automation", "Prompt Engineering Pro", "Data Analytics AI", "Digital Marketing SEO",
        "Canva Pro Mastery", "Cybersecurity Job Ready", "AI Voice Cloning", "Affiliate Marketing AI",
        "Dropshipping 3.0", "Facebook Ads 2026", "Google Ads", "LinkedIn Branding", "WhatsApp Marketing",
        "Meme Marketing", "Podcast Launch Pro", "AI Resume Viral", "AI Tools for Business", "ChatGPT Freelancing",
        "Python AI Basics", "Full Stack Web Dev AI", "AWS Cloud", "Google Data Analytics", "UX UI Design AI",
        "Business Finance", "Stock Market AI", "Crypto Trading Basics", "Video Editing Masterclass", "AI Photo Editing",
        "AI Music Creation", "AI Reels Maker", "AI Chatbot for Shop", "AI for Students", "AI for Teachers",
        "AI for Doctors", "AI Legal Assistant", "AI Content Writing", "AI Ecommerce", "Instagram Growth 0 to 1M",
        "YouTube Shorts Monetization", "LinkedIn Growth Hack", "Twitter Viral", "Email Marketing Pro", "SEO Advanced",
        "Content Marketing", "Influencer Marketing", "Brand Building", "Online Store Shopify", "Meesho Selling Mastery",
        "Amazon FBA", "Flipkart Seller", "Etsy Selling", "Boutique Business", "Embroidery Design", "Fashion Designing",
        "Beauty Parlour Course", "Cooking Masterclass", "Yoga Instructor", "Fitness Trainer", "Meditation Course",
        "Spoken English", "Public Speaking", "Interview Preparation", "MS Excel Advanced", "Tally GST", "Digital Banking",
        "Insurance Agent Pro", "Real Estate Mastery", "Photography Pro", "Videography", "Graphic Design", "3D Animation",
        "Game Development", "App Development No-Code", "WordPress Mastery", "Blogger to Pro", "Quora Marketing",
        "Reddit Viral", "Telegram Growth", "Discord Community", "Notion Productivity", "Canva Template Selling",
        "Prompt Selling", "AI Art Selling", "Voice Over Artist", "Translation Business", "Freelancing Fiverr Upwork",
        "Agency Building", "Startup Funding", "Business Plan Writing", "Lead Generation", "Customer Support Automation",
        "CRM Mastery", "HR Management", "Project Management", "Time Management", "Sales Closing", "Negotiation Skills",
        "Mindset Mastery", "Motivation Course", "Parenting Course", "Relationship Coaching", "Career Counselling",
        "Study Hacks", "Exam Preparation", "UPSC Strategy", "SSC CGL Prep", "Bank PO Prep"
    ]
    for i, t in enumerate(base_topics):
        courses.append({"id": f"BRAHMA{1000+i}", "topic": t, "price": 999 + (i % 5) * 100, "videos": 400})
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
        st.sidebar.success("Admin Panel")
        menu = st.sidebar.radio("Admin Menu", ["Dashboard", "Price Edit", "UPI QR Setup", "Super Brain", "Sales", "Settings"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            st.rerun()

def free_voice(text, lang, path):
    if not GTTS_OK:
        return False, "Voice engine not ready"
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(str(path))
        return True, "Done"
    except Exception as e:
        return False, str(e)

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Courses", len(courses))
        c2.metric("Total Sales", len(purchases))
        c3.metric("Pending Approval", len([p for p in purchases if p.get("status") == "PENDING"]))
        st.dataframe(pd.DataFrame(courses), use_container_width=True)

    if menu == "Price Edit":
        st.header("Manage Course Pricing")
        with st.form("bulk_form"):
            action = st.selectbox("Action", ["Set Same Price for All", "Increase by Percent", "Decrease by Percent"])
            val = st.number_input("Value", value=999)
            if st.form_submit_button("Update Prices", type="primary"):
                for course in courses:
                    if action == "Set Same Price for All":
                        course["price"] = int(val)
                    elif action == "Increase by Percent":
                        course["price"] = int(course.get("price", 999) * (1 + val / 100))
                    else:
                        course["price"] = max(99, int(course.get("price", 999) * (1 - val / 100)))
                save_json(COURSES_FILE, courses)
                st.success("Prices updated")
                st.rerun()
        search = st.text_input("Search")
        filtered = [c for c in courses if search.lower() in c.get("topic", "").lower()] if search else courses
        for course in filtered[:15]:
            with st.expander(f"{course.get('topic')} - Rs {course.get('price')}"):
                new_price = st.number_input(f"New Price {course['id']}", value=int(course.get("price", 999)), key=f"p_{course['id']}")
                if st.button(f"Update {course['id']}", key=f"u_{course['id']}"):
                    course["price"] = int(new_price)
                    save_json(COURSES_FILE, courses)
                    st.success("Updated")

    if menu == "UPI QR Setup":
        st.header("Payment QR Setup")
        st.info(f"Your UPI {MY_UPI_ID} - This QR will show to customers securely at checkout")
        uploaded = st.file_uploader("Upload Your UPI QR Code", type=["jpg", "png", "jpeg"])
        if uploaded:
            UPI_QR_PATH.write_bytes(uploaded.getvalue())
            st.success("QR Code Saved Successfully")
            st.rerun()
        if UPI_QR_PATH.exists():
            st.image(str(UPI_QR_PATH), width=300)
            if st.button("Remove QR"):
                UPI_QR_PATH.unlink(missing_ok=True)
                st.rerun()

    if menu == "Super Brain":
        st.header("Super Brain - Auto Course Creator")
        st.caption("Auto creates courses, Hindi English voice, SEO blogs, social posts - All FREE tools")
        col1, col2, col3 = st.columns(3)
        col1.metric("SEO Files", len(list(SEO_DIR.glob("*.txt"))))
        col2.metric("Blogs", len(list(BLOG_DIR.glob("*.txt"))))
        col3.metric("Social Posts", len(list(SOCIAL_DIR.glob("*.txt"))))
        
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button("Generate SEO Files", type="primary"):
                for course in courses:
                    (SEO_DIR / f"{course['id']}_seo.txt").write_text(f"{course['topic']} Course 2026 Hindi English 400 Videos", encoding="utf-8")
                st.success("SEO Generated