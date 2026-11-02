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

def get_teacher_lessons(topic):
    m1 = [
        f"What is {topic} definition with 5 real examples",
        f"History of {topic} timeline 2015 to 2026",
        f"Types of {topic} 7 types detail",
        f"{topic} vs Traditional method difference",
        f"Why {topic} is future market data proof",
        f"Career in {topic} jobs salary freelancing",
        f"{topic} mindset how to think like expert",
        f"Myths about {topic} 10 myths busted",
        f"Success stories {topic} 5 people 1Cr earned",
        f"Failure stories {topic} why 90 percent fail",
        f"{topic} roadmap zero to expert 90 days",
        f"Tools needed for {topic} 20 tools list",
        f"Industry overview {topic} top 10 industries",
        f"Market size {topic} 2026 report",
        f"Skills needed for {topic} technical plus soft",
        f"Learning path {topic} step by step",
        f"Time management for {topic} daily routine",
        f"Best resources for {topic} books videos",
        f"Community for {topic} discord reddit",
        f"Mentorship for {topic} how to find mentor",
        f"{topic} architecture basic structure",
        f"Core technology behind {topic}",
        f"RAG in {topic} deep",
        f"Memory in {topic} short long vector",
        f"Tools integration in {topic}",
        f"Planning in {topic} ReAct Chain Thought",
        f"Reasoning in {topic} how expert thinks",
        f"Action in {topic} how to take action",
        f"Observation in {topic} learn from result",
        f"Loop in {topic} Perceive Reason Act",
        f"Case Study 1 {topic} 1L per month business",
        f"Case Study 2 {topic} 10M ARR story",
        f"Case Study 3 {topic} 10M users growth",