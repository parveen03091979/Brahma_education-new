import streamlit as st
import json
import hashlib
import secrets
import datetime
import urllib.parse
from pathlib import Path

# 1. Page Configuration & Theme Setup
st.set_page_config(page_title="Brahma Education V100", page_icon="🎓", layout="wide")

# Paths Configuration
DATA = Path("data")
DATA.mkdir(exist_ok=True)

COURSES_FILE = DATA / "courses.json"
PURCHASE_FILE = DATA / "purchases.json"
MARKETING_FILE = DATA / "marketing.json"
API_FILE = DATA / "api_keys.json"
MASTER_HASH = DATA / ".master_hash"
ADMIN_SESSION = DATA / ".admin_session"

# Core Constants
UPI_ID = "parveen39179@okicici"
OWNER = "Parveen Kumar"
DEFAULT_PRICE = 99

TOPICS = [
    "AI Agent Automation", "Instagram Reels Mastery", "YouTube Automation", "Prompt Engineering",
    "Digital Marketing SEO", "ChatGPT Mastery", "Facebook Ads", "Google Ads", "SEO Advanced",
    "Social Media Marketing", "Content Writing AI", "Copywriting Mastery", "Blogging Mastery",
    "Affiliate Marketing", "Dropshipping", "E-commerce Shopify", "Canva Design", "Video Editing CapCut",
    "YouTube SEO", "Instagram Growth", "LinkedIn Marketing", "Twitter X Growth", "TikTok Viral",
    "Pinterest Marketing", "Quora Marketing", "Email Marketing Automation", "WhatsApp Marketing",
    "Telegram Growth", "Influencer Marketing", "Personal Branding", "Freelancing Mastery",
    "Agency Business", "SaaS Business", "No-Code Bubble", "Python Mastery", "JavaScript Mastery",
    "React JS", "Next.js", "Node.js", "Web Development Full Stack", "WordPress Mastery",
    "Shopify Store Design", "UI UX Design", "Figma Design", "Graphic Design", "Logo Design",
    "Thumbnail Design Viral", "Video Animation", "AI Image Midjourney", "AI Video Sora",
    "Voice Cloning ElevenLabs", "Automation n8n Make", "Zapier Automation", "Notion Productivity",
    "Excel Advanced", "Google Sheets Automation", "Data Analysis Python", "Machine Learning",
    "Deep Learning", "Data Science", "Stock Trading AI", "Crypto Trading", "Forex Trading",
    "Real Estate Business", "Motivational Speaking", "Public Speaking", "Communication Skills",
    "English Speaking", "Podcast Mastery", "Music Production AI", "Photography Mastery",
    "Reels Editing Viral", "Meme Marketing", "Viral Content Formula", "Lead Generation",
    "Sales Funnel", "Landing Page Design", "CRO Optimization", "Customer Support Automation",
    "HR Recruitment AI", "Business Plan Mastery", "Startup Funding", "Business Automation AI",
    "Time Management", "Mindset Millionaire", "Meditation Mindfulness", "Fitness Coaching Business",
    "Diet Nutrition Business", "Yoga Teaching Business", "Cooking Channel Business", "Travel Vlogging Business",
    "Gaming Channel Growth", "Education Channel Growth", "Finance Channel Business", "News Channel Automation",
    "Meme Page Business", "Affiliate Blog SEO", "Amazon FBA Mastery", "Etsy Store Mastery",
    "Print on Demand Business", "Stock Photography Business", "Voice Over Business", "Translation Business AI",
    "Resume Writing Business", "LinkedIn Profile Optimization", "AI Tools Mastery", "Chatbot Development",
    "AI Voice Agent", "AI Receptionist Business"
]

MODULES = [
    "WHAT IS", "WHY IMPORTANT", "WHERE USE", "WHEN TO USE", "WHO ELIGIBLE",
    "HOW ARCHITECTURE", "TOOLS REQUIRED", "EARNING OPPORTUNITIES", "PRACTICAL USAGE", "RIGHT WAY TO LEARN",
    "BEGINNER FOUNDATION", "CORE CONCEPTS", "ADVANCED CONCEPTS", "STEP BY STEP PROCESS", "REAL BUSINESS EXAMPLES",
    "CLIENT REQUIREMENTS", "REAL STORY", "PROJECT PLANNING", "IMPLEMENTATION", "MISTAKES TO AVOID",
    "PRO TIP", "EXPERT STRATEGY", "TOOLS COMPARISON", "FREE VS PAID", "PORTFOLIO BUILDING",
    "CLIENT FINDING", "FREELANCING", "AGENCY MODEL", "BUSINESS MODEL", "SCALING STRATEGY",
    "SEO AND MARKETING", "LEAD GENERATION", "SALES STRATEGY", "AUTOMATION", "OPTIMIZATION",
    "CASE STUDY", "DAILY PRACTICE", "HOMEWORK", "REVISION", "FINAL PROJECT AND CERTIFICATION"
]

# 2. Helper Functions (File Handling & Security)
def load_json_data(path, default_factory):
    try:
        if path.exists():
            content = path.read_text(encoding="utf-8").strip()
            if content:
                return json.loads(content)
    except Exception:
        pass
    return default_factory

def save_json_data(path, data):
    try:
        temp = path.with_suffix(".tmp")
        temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        temp.replace(path)
        return True
    except Exception as e:
        st.error(f"Error saving data: {str(e)}")
        return False

def initialize_courses():
    data = load_json_data(COURSES_FILE, [])
    if not isinstance(data, list):
        data = []
    
    existing = {}
    for item in data:
        if isinstance(item, dict) and "topic" in item:
            existing[item["topic"].strip().lower()] = item

    updated_data = []
    for i, topic in enumerate(TOPICS):
        lower_topic = topic.strip().lower()
        if lower_topic in existing:
            course = existing[lower_topic]
        else:
            course = {"id": f"BRAHMA{1000 + i}", "topic": topic, "price": DEFAULT_PRICE}
        
        try:
            price = int(course.get("price", DEFAULT_PRICE))
            if price < 1:
                price = DEFAULT_PRICE
            course["price"] = price
        except ValueError:
            course["price"] = DEFAULT_PRICE
            
        updated_data.append(course)
        
    save_json_data(COURSES_FILE, updated_data)
    return updated_data

# Core Content Generator Logic
def module_content(topic, number):
    title = MODULES[number - 1]
    text = f"COURSE TOPIC: {topic}. MODULE: {title}. This lesson introduces the subject and explains its importance in professional and business applications. Understand main concepts, terminology, tools, processes and practical implementation. Start with foundation and move towards professional applications. "
    
    if number == 17:
        text += "REAL STORY: Rahul is fictional case study. Begins with basic smartphone and limited resources. Studies daily, practices skills and builds portfolio. Approaches clients, receives rejections and improves proposals. Eventually completes first project. Progress from practice and consistent improvement. "
    elif number == 20:
        text += "FIVE COMMON MISTAKES: Skipping foundation, watching without practicing, chasing money before learning, not maintaining diary and avoiding feedback. Create weekly plan to avoid mistakes. "
    elif number == 21:
        text += "PRO TIP: Write four things diary every night: what you learned, what mistake you made, what you will improve tomorrow and one new idea. Review every Sunday. "
    elif number == 31:
        text += "SEO: Search Engine Optimization helps useful content discovered in search engines. Learn keyword research, search intent, titles, descriptions, headings, internal links, image alt text and quality content. "
    elif number == 40:
        text += "FINAL PROJECT: Create professional project based on this course. Include problem, solution, workflow, tools, testing, portfolio and final presentation. Submit for evaluation. "
    
    return text + text

def make_password_hash(password):
    salt = secrets.token_bytes(16)
    hashed = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
    return f"{salt.hex()}:{hashed.hex()}"

def verify_password(password, stored):
    try:
        salt_hex, hash_hex = stored.split(":")
        salt = bytes.fromhex(salt_hex)
        actual = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
        return secrets.compare_digest(actual.hex(), hash_hex)
    except Exception:
        old = hashlib.sha256(password.encode()).hexdigest()
        return secrets.compare_digest(old, stored)

def is_session_valid():
    try:
        data = load_json_data(ADMIN_SESSION, {})
        if "expiry" in data:
            expiry = datetime.datetime.fromisoformat(data["expiry"])
            return datetime.datetime.now() < expiry
    except Exception:
        pass
    return False

# 3. Session State & Routing Engine
if "admin_logged" not in st.session_state:
    st.session_state.admin_logged = is_session_valid()

# Initialize data reactive pipelines
courses = initialize_courses()
purchases = load_json_data(PURCHASE_FILE, [])
marketing = load_json_data(MARKETING_FILE, [])
api_keys = load_json_data(API_FILE, {})

# Sidebar Navigation System
st.sidebar.title("Brahma Education V100")

if not MASTER_HASH.exists():
    pw = st.sidebar.text_input("Create Admin Password", type="password", key="create_pw_field")
    if st.sidebar.button("Create Admin Account"):
        if pw and len(pw) >= 4:
            MASTER_HASH.write_text(make_password_hash(pw), encoding="utf-8")
            st.success("Admin Profile Configured!")
            st.rerun()
        else:
            st.sidebar.error("Password must be at least 4 characters long.")
    menu = "Browse Courses"
else:
    if not st.session_state.admin_logged:
        menu = st.sidebar.radio("Navigation Menu", ["Browse Courses", "My Access"])
        st.sidebar.divider()
        pw = st.sidebar.text_input("Enter Admin Password", type="password", key="login_pw_field")
        if st.sidebar.button("Admin Secure Login"):
            stored = MASTER_HASH.read_text(encoding="utf-8").strip()
            if verify_password(pw, stored):
                if ":" not in stored:
                    MASTER_HASH.write_text(make_password_hash(pw), encoding="utf-8")
                expiry = datetime.datetime.now() + datetime.timedelta(days=7)
                save_json_data(ADMIN_SESSION, {"expiry": expiry.isoformat()})
                st.session_state.admin_logged = True
                st.rerun()
            else:
                st.sidebar.error("Invalid Credentials Provided.")
    else:
        st.sidebar.success("Admin Active: Price 99 Lock")
        # FIXED CRITICAL SYNTAX BUG: All list items correctly bounded and closed
