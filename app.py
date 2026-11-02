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

def create_master_teacher_pptx(cid, ctopic):
    try:
        from pptx import Presentation
        from pptx.util import Inches, Pt
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)

        def add_slide(title, body):
            slide = prs.slides.add_slide(prs.slide_layouts[5])
            box1 = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12.3), Inches(0.8))
            tf1 = box1.text_frame
            tf1.word_wrap = True
            p = tf1.paragraphs[0]
            p.text = title
            p.font.size = Pt(28)
            p.font.bold = True
            box2 = slide.shapes.add_textbox(Inches(0.5), Inches(1.1), Inches(12.3), Inches(6.0))
            tf2 = box2.text_frame
            tf2.word_wrap = True
            p2 = tf2.paragraphs[0]
            p2.text = body
            p2.font.size = Pt(16)

        # 13 Slides - Jaise aapne define kiya tha teacher mein kya kya hona chahie
        add_slide(ctopic + " - Super Teacher Book", "Super Agent Brahma - Master Teacher - 20 Saal Teaching - Har Cheez Ki Knowledge - Business Level Real Income - 400 Lessons - Complete Book - App Strong - Real Business 1Cr")
        add_slide("1. KYA HAI - What Is " + ctopic, "Definition simple language me - 5 real examples ke saath - Kya hota hai " + ctopic + " - Kaise kaam karta hai - Basic fundamentals - Industry me kya bolte hain - Beginner ko kaise samjhaye - Teacher jaise")
        add_slide("2. KYON HAI - Why " + ctopic, "Kyon zaroori hai future me - Market data 2026 - 90 percent log fail kyon hote hain - Kyon seekhna chahie - Demand kya hai - Paise kyon banta hai - Proof ke saath")
        add_slide("3. KAHAN HAI - KAB - KAUN - Where When Who", "KAHAN use hota hai Instagram YouTube Business Job Freelancing Agency - KAB best time morning 6 to 8 Monday Thursday - KAUN kar sakta hai Student Housewife Job Business 16 to 60 saal - Har koi")
        add_slide("4. KAISE KAAM KARTA HAI - Architecture", "Kaise kaam karta hai step by step - Perceive Reason Act loop - RAG deep memory short long vector - Tools integration planning ReAct Chain Thought - Expert kaise sochta hai - Reasoning")
        add_slide("5. KISSE HOGA - Tools - Kya Chahie", "Kisse hoga - Free tools list Canva CapCut ChatGPT Notion Make n8n - Paid tools - Mobile se hoga ya laptop - Kya kya chahie start karne ke liye - Setup kaise kare -