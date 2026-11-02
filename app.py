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
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
PPT_DIR = DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)

MY_UPI_ID = "parveen39179@okicici"
MY_NAME = "Parveen Kumar"

def get_topics():
    t = []
    t.append("AI Agent Automation 2026")
    t.append("Instagram Reels Mastery")
    t.append("YouTube Automation AI")
    t.append("Prompt Engineering Pro")
    t.append("Digital Marketing SEO Mastery")
    t.append("ChatGPT Mastery 2026")
    t.append("Facebook Ads Mastery")
    t.append("Google Ads Mastery")
    t.append("SEO Advanced 2026")
    t.append("Social Media Marketing Pro")
    t.append("Content Writing AI")
    t.append("Copywriting Mastery")
    t.append("Blogging Mastery 2026")
    t.append("Affiliate Marketing Pro")
    t.append("Dropshipping Business")
    t.append("E-commerce Mastery Shopify")
    t.append("Canva Design Mastery")
    t.append("Video Editing CapCut Pro")
    t.append("YouTube SEO Mastery")
    t.append("Instagram Growth Hack")
    t.append("LinkedIn Marketing Pro")
    t.append("Twitter X Growth Mastery")
    t.append("TikTok Viral Mastery")
    t.append("Pinterest Marketing")
    t.append("Quora Marketing")
    t.append("Email Marketing Automation")
    t.append("WhatsApp Marketing Pro")
    t.append("Telegram Channel Growth")
    t.append("Influencer Marketing")
    t.append("Personal Branding Mastery")
    t.append("Freelancing Mastery Upwork Fiverr")
    t.append("Agency Business Mastery")
    t.append("SaaS Business 2026")
    t.append("No-Code Business Bubble")
    t.append("Python Programming Mastery")
    t.append("JavaScript Mastery 2026")
    t.append("React JS Mastery")
    t.append("Next.js Mastery")
    t.append("Node.js Backend Mastery")
    t.append("Web Development Full Stack")
    t.append("WordPress Mastery")
    t.append("Shopify Store Design")
    t.append("UI UX Design Mastery")
    t.append("Figma Design Pro")
    t.append("Graphic Design Mastery")
    t.append("Logo Design Mastery")
    t.append("Thumbnail Design Viral")
    t.append("Video Animation Mastery")
    t.append("AI Image Generation Midjourney")
    t.append("AI Video Generation Sora")
    t.append("Voice Cloning ElevenLabs")
    t.append("Automation n8n Make")
    t.append("Zapier Automation Mastery")
    t.append("Notion Productivity Mastery")
    t.append("Excel Advanced Mastery")
    t.append("Google Sheets Automation")
    t.append("Data Analysis Python")
    t.append("Machine Learning Mastery")
    t.append("Deep Learning 2026")
    t.append("Data Science Mastery")
    t.append("Stock Market Trading AI")
    t.append("Crypto Trading Mastery")
    t.append("Forex Trading Pro")
    t.append("Real Estate Business")
    t.append("Motivational Speaking Mastery")
    t.append("Public Speaking Pro")
    t.append("Communication Skills Mastery")
    t.append("English Speaking Pro")
    t.append("Hindi Content Creation")
    t.append("Podcast Mastery")
    t.append("Music Production AI")
    t.append("Photography Mastery")
    t.append("Reels Editing Viral")
    t.append("Meme Marketing Mastery")
    t.append("Viral Content Formula")
    t.append("Lead Generation Mastery")
    t.append("Sales Funnel Mastery")
    t.append("Landing Page Design High Converting")
    t.append("CRO Conversion Optimization")
    t.append("Customer Support Automation")
    t.append("HR Recruitment AI")
    t.append("Business Plan Mastery")
    t.append("Startup Funding Mastery")
    t.append("Business Automation AI")
    t.append("Time Management Mastery")
    t.append("Mindset Mastery Millionaire")
    t.append("Meditation Mindfulness")
    t.append("Fitness Coaching Business")
    t.append("Diet Nutrition Business")
    t.append("Yoga Teaching Business")
    t.append("Cooking Channel Business")
    t.append("Travel Vlogging Business")
    t.append("Gaming Channel Growth")
    t.append("Education Channel Growth")
    t.append("Finance Channel Business")
    t.append("News Channel Automation")
    t.append("Meme Page Business")
    t.append("Affiliate Blog SEO")
    t.append("Amazon FBA Mastery")
    t.append("Etsy Store Mastery")
    t.append("Print on Demand Business")
    t.append("Stock Photography Business")
    t.append("Voice Over Business")
    t.append("Translation Business AI")
    t.append("Resume Writing Business")
    t.append("LinkedIn Profile Optimization Business")
    t.append("AI Tools Mastery 100 Tools")
    t.append("Chatbot Development")
    t.append("AI Voice Agent Mastery")
    t.append("AI Receptionist Business")
    return t

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size > 2:
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def create_course_file(cid, ctopic):
    try:
        content = ""
        content += "Course: " + ctopic + "\n"
        content += "Complete Course Business Level\n"
        content += "Super Teacher 20 saal teaching har cheez ki knowledge\n"
        content += "KYA HAI: What is " + ctopic + " 5 examples\n"
        content += "KYON HAI: Why future market data 90 percent fail\n"
        content += "KAHAN HAI: Where use Instagram YouTube Business Job\n"
        content += "KAB: When best morning 6-8 Monday Thursday\n"
        content += "KAUN: Who Student Housewife Job Business 16 to 60\n"
        content += "KAISE: How Step 1 Socho Step 2 Tool kholo Step 3 Pehla step\n"
        content += "KISSE: With whom free tools Canva CapCut ChatGPT\n"
        content += "KYA USE: What use earn 20k-50k business 1L plus\n"
        content += "KAISE USE: How to use mobile plus Reels laptop browser\n"
        content += "KAISE KARNA: How should do right daily 30 min diary\n"
        content += "REAL KAHANI: Rahul gaon se 2 mahine roz 1 ghanta project\n"
        content += "MISTAKES: Galti1 advanced Galti2 no practice Galti3 only video\n"
        content += "PRO TIP: Diary rakho roz kya seekha kal kya karna\n"
        content += "HOMEWORK: Aaj project banao kal bhejo Business Level\n"
        path = PPT_DIR / (cid + "_Course.txt")
        path.write_text(content, encoding="utf-8")
        ppt_path = PPT_DIR / (cid + "_Course.pptx")
        ppt_path.write_text(content, encoding="utf-8")
        return str(ppt_path), "Ready"
    except Exception as e:
        return None, "Error " + str(e)

topics = get_topics()
courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

if len(courses) < 100:
    courses = []
    for i in range(len(topics)):
        t = topics[i]
        courses.append({"id":"BRAHMA" + str(1000+i),"topic":t,"price":999,"videos":400})
    save_json(COURSES_FILE, courses)

if "admin_logged" not in st.session_state:
    st.session_state["admin