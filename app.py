import streamlit as st
import json
import hashlib
import secrets
import datetime
import urllib.parse
import os
from pathlib import Path

# Static configuration check to guarantee python-pptx initialization
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-pptx"])
    from pptx import Presentation
    from pptx.util import Inches, Pt

# 1. Core Page Initialization
st.set_page_config(page_title="Brahma Education V100", page_icon="🎓", layout="wide")

# Persistent File Ecosystem
DATA = Path("data")
PPT_DIR = DATA / "ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

COURSES_FILE = DATA / "courses.json"
PURCHASE_FILE = DATA / "purchases.json"
MARKETING_FILE = DATA / "marketing.json"
API_FILE = DATA / "api_keys.json"
MASTER_HASH = DATA / ".master_hash"
ADMIN_SESSION = DATA / ".admin_session"
QR_FILE = DATA / "upi_qr.jpg"

# Global Business Constants
UPI_ID = "parveen39179@okicici"
OWNER = "Parveen Kumar"
DEFAULT_PRICE = 99

# Compact, high-efficiency list layout mapping exactly 100 enterprise domains
TOPICS = [
    "AI Agent Automation", "Instagram Reels Mastery", "YouTube Automation", "Prompt Engineering",
    "Digital Marketing SEO", "ChatGPT Mastery", "Facebook Ads", "Google Ads", "SEO Advanced",
    "Social Media Marketing", "Content Writing AI", "Copywriting", "Blogging", "Affiliate Marketing",
    "Dropshipping", "E-commerce Shopify", "Canva Design", "Video Editing CapCut", "YouTube SEO",
    "Instagram Growth", "LinkedIn Marketing", "Twitter X Growth", "TikTok Viral", "Pinterest",
    "Quora", "Email Marketing Automation", "WhatsApp Marketing", "Telegram Growth", "Influencer Marketing",
    "Personal Branding", "Freelancing Mastery", "Agency Business", "SaaS Business", "No-Code Bubble",
    "Python", "JavaScript", "React", "Next.js", "Node.js", "Full Stack Web Dev", "WordPress",
    "Shopify Store", "UI UX Design", "Figma", "Graphic Design", "Logo Design", "Thumbnail Design Viral",
    "Video Animation", "AI Image Midjourney", "AI Video Sora", "Voice Cloning ElevenLabs",
    "Automation n8n Make", "Zapier", "Notion", "Excel Advanced", "Google Sheets Automation",
    "Data Analysis Python", "Machine Learning", "Deep Learning", "Data Science", "Stock Trading AI",
    "Crypto Trading", "Forex Trading", "Real Estate Business", "Motivational Speaking", "Public Speaking",
    "Communication Skills", "English Speaking", "Podcast Mastery", "Music Production AI", "Photography",
    "Reels Editing Viral", "Meme Marketing", "Viral Content Formula", "Lead Generation", "Sales Funnel",
    "Landing Page Design", "CRO", "Customer Support Automation", "HR Recruitment AI", "Business Plan Mastery",
    "Startup Funding", "Business Automation AI", "Time Management", "Mindset Millionaire", "Meditation",
    "Fitness Coaching Business", "Diet Nutrition Business", "Yoga Teaching Business", "Cooking Channel Business",
    "Travel Vlogging Business", "Gaming Channel Growth", "Education Channel Growth", "Finance Channel Business",
    "News Channel Automation", "Meme Page Business", "Affiliate Blog SEO", "Amazon FBA", "Etsy Store",
    "Print on Demand", "Stock Photography Business", "Voice Over Business", "Translation Business AI",
    "Resume Writing Business", "LinkedIn Profile Optimization", "AI Tools Mastery", "Chatbot Development",
    "AI Voice Agent", "AI Receptionist Business"
]

MODULE_TITLES = [
    "WHAT IS", "WHY IMPORTANT", "WHERE USE", "WHEN TIMING", "WHO ELIGIBLE", "HOW ARCHITECTURE",
    "WITH WHAT TOOLS", "WHAT EARN", "HOW TO USE", "HOW TO DO RIGHT WAY", "BEGINNER FOUNDATION",
    "CORE CONCEPTS", "ADVANCED CONCEPTS", "STEP BY STEP PROCESS", "REAL BUSINESS EXAMPLES",
    "CLIENT REQUIREMENTS", "REAL STORY", "PROJECT PLANNING", "IMPLEMENTATION", "MISTAKES 90 PERCENT FAIL",
    "PRO TIP", "EXPERT STRATEGY", "TOOLS COMPARISON", "FREE VS PAID", "PORTFOLIO BUILDING",
    "CLIENT FINDING", "FREELANCING", "AGENCY MODEL", "BUSINESS MODEL", "SCALING STRATEGY",
    "SEO AND MARKETING", "LEAD GENERATION", "SALES STRATEGY", "AUTOMATION", "OPTIMIZATION",
    "CASE STUDY", "DAILY PRACTICE", "HOMEWORK", "REVISION", "FINAL PROJECT CERTIFICATION"
]

# JSON IO Abstraction Modules
def io_load(target_path, factory):
    try:
        if target_path.exists():
            payload = target_path.read_text(encoding="utf-8").strip()
            if payload:
                return json.loads(payload)
    except Exception:
        pass
    return factory

def io_save(target_path, data):
    try:
        scratch = target_path.with_suffix(".tmp")
        scratch.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        scratch.replace(target_path)
        return True
    except Exception:
        return False

def sync_catalog():
    disk_data = io_load(COURSES_FILE, [])
    if not isinstance(disk_data, list):
        disk_data = []
    
    registry = {}
    for item in disk_data:
        if isinstance(item, dict) and "topic" in item:
            registry[item["topic"].strip().lower()] = item

    fresh_catalog = []
    for idx, topic in enumerate(TOPICS):
        norm_key = topic.strip().lower()
        if norm_key in registry:
            node = registry[norm_key]
        else:
            node = {"id": "BRAHMA" + str(1000 + idx), "topic": topic, "price": DEFAULT_PRICE}
        
        try:
            val = int(node.get("price", DEFAULT_PRICE))
            if val > 200 or val < 1:
                val = DEFAULT_PRICE
            node["price"] = val
        except Exception:
            node["price"] = DEFAULT_PRICE
        fresh_catalog.append(node)
        
    io_save(COURSES_FILE, fresh_catalog)
    return fresh_catalog

# Global Variable Registration
courses_db = sync_catalog()
purchases_db = io_load(PURCHASE_FILE, [])
marketing_db = io_load(MARKETING_FILE, [])
api_keys_db = io_load(API_FILE, {})

# Deep 40 Module Engine Content Mapping
def compile_slide_text(topic, cursor):
    hdr = MODULE_TITLES[cursor - 1]
    base = "LESSON CORE: " + topic + " - STRUCTURE PLAN: " + hdr + ". "
    
    if cursor == 1:
        return base + "DEFINITION: Systems automation workflow optimization. Real enterprise level architecture mapping. 5 structured field test examples. Saves up to 80% time overhead operations."
    elif cursor == 2:
        return base + "MARKET DATA: Future proof skill verified by 2026 economic data index. Industry demand trends high. Average career salary scale jumps up to 3x multiplier."
    elif cursor == 3:
        return base + "APPLICATION VERTICALS: Instagram Reels engagement loops, YouTube Shorts channels, programmatic business workflow logic. Job rank enhancement and freelance consulting."
    elif cursor == 4:
        return base + "CHRONO TIMING: Peak execution blocks morning 6 AM to 8 AM. Mind state fresh. Data confirms Monday and Thursday posting schedule yields 40% higher structural discovery rate."
    elif cursor == 5:
        return base + "CRITERIA ELIGIBILITY: Students age 16 plus, technical professionals, active business owners up to 60 years old. No formal university degree demanded. Commits 30 minutes daily."
    elif cursor == 6:
        return base + "ENGINEERING ARCHITECTURE: Perceive-Reason-Act workflow configuration. ReAct operational framework, Chain of Thought orchestration, RAG vector context arrays, prompt logic."
    elif cursor == 7:
        return base + "INFRASTRUCTURE UTILITIES: Free tiers utilize Canva layouts, CapCut rendering, ChatGPT processing, Notion logs, Google Sheets database. Paid arrays include ElevenLabs audio, n8n, Make, Zapier."
    elif cursor == 8:
        return base + "MONETIZATION INDEX: Freelancing pipelines on Upwork and Fiverr map 20k to 50k month one. Month three touches 1L checkpoint. Enterprise agency structures return 2L plus monthly."
    elif cursor == 9:
        return base + "DEPLOYMENT HARDWARE: Mobile execution scripts via InShot, CapCut layers, mobile layout apps. High scale browser control panels via computer workstations and dashboard terminals."
    elif cursor == 10:
        return base + "LEARNING ROADMAP: Strict 30 minutes daily block inside personal diary. 15 minutes theoretical absorption matched to 15 minutes live sandbox operations. Weekly revision loops every Sunday."
    elif cursor == 17:
        return base + "CASE ARCHIVE: Rahul village profile. Initial hardware limited to old Redmi 8 phone on Jio 1GB tier. No computing workstation. Engages Master Teacher track 2 months, 1 hour daily. Month 3 fires 20 Upwork proposals, hits 19 rejections, lands 1 US enterprise route for 15k. Month 4 scales to 5 retainers tracking 75k. Month 6 expands into full agency operation tracking 2 Lakh. Rebuilds family house ecosystem."
    elif cursor == 20:
        return base + "FAIL SAFE CONTROLS: 90% breakdown matrix analysis. Mistake 1 skips core foundations to chase advanced tricks. Mistake 2 consumes streams without sandbox test. Mistake 3 maps tracking behind currency instead of competency. Mistake 4 drops tracking log diary. Mistake 5 attempts path solo without mentor."
    elif cursor == 21:
        return base + "STRATEGY INJECTION: Hidden night logging habit. Dedicate 10 minutes tracking 4 indices before rest: clear core item learned, distinct operations mistake recorded, tomorrow execution map, 1 raw innovation idea."
    elif cursor == 31:
        return base + "DISCOVERY ENGINE: Optimizing index platforms. Scaling content visibility to rank position 1 on Google search nodes. Intent validation via tools like Google Keyword Planner."
    elif cursor == 40:
