import streamlit as st
import json, hashlib, datetime, urllib.parse
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Brahma Education V97 Full Restore", layout="wide")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
ADMIN_SESSION = DATA_DIR / ".admin_session"
COURSES_FILE = DATA_DIR / "courses.json"
PPT_DIR = DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)
MARKETING_FILE = DATA_DIR / "marketing.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
API_FILE = DATA_DIR / "api_keys.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"

MY_UPI_ID = "parveen39179@okicici"
MY_NAME = "Parveen Kumar"

TOPICS_STR = "AI Agent Automation 2026|Instagram Reels Mastery|YouTube Automation AI|Prompt Engineering Pro|Digital Marketing SEO Mastery|ChatGPT Mastery 2026|Facebook Ads Mastery|Google Ads Mastery|SEO Advanced 2026|Social Media Marketing Pro|Content Writing AI|Copywriting Mastery|Blogging Mastery 2026|Affiliate Marketing Pro|Dropshipping Business|E-commerce Mastery Shopify|Canva Design Mastery|Video Editing CapCut Pro|YouTube SEO Mastery|Instagram Growth Hack|LinkedIn Marketing Pro|Twitter X Growth Mastery|TikTok Viral Mastery|Pinterest Marketing|Quora Marketing|Email Marketing Automation|WhatsApp Marketing Pro|Telegram Channel Growth|Influencer Marketing|Personal Branding Mastery|Freelancing Mastery|Agency Business Mastery|SaaS Business 2026|No-Code Business Bubble|Python Programming Mastery|JavaScript Mastery 2026|React JS Mastery|Next.js Mastery|Node.js Backend Mastery|Web Development Full Stack|WordPress Mastery|Shopify Store Design|UI UX Design Mastery|Figma Design Pro|Graphic Design Mastery|Logo Design Mastery|Thumbnail Design Viral|Video Animation Mastery|AI Image Generation Midjourney|AI Video Generation Sora|Voice Cloning ElevenLabs|Automation n8n Make|Zapier Automation Mastery|Notion Productivity Mastery|Excel Advanced Mastery|Google Sheets Automation|Data Analysis Python|Machine Learning Mastery|Deep Learning 2026|Data Science Mastery|Stock Market Trading AI|Crypto Trading Mastery|Forex Trading Pro|Real Estate Business|Motivational Speaking Mastery|Public Speaking Pro|Communication Skills Mastery|English Speaking Pro|Hindi Content Creation|Podcast Mastery|Music Production AI|Photography Mastery|Reels Editing Viral|Meme Marketing Mastery|Viral Content Formula|Lead Generation Mastery|Sales Funnel Mastery|Landing Page Design|CRO Conversion Optimization|Customer Support Automation|HR Recruitment AI|Business Plan Mastery|Startup Funding Mastery|Business Automation AI|Time Management Mastery|Mindset Mastery Millionaire|Meditation Mindfulness|Fitness Coaching Business|Diet Nutrition Business|Yoga Teaching Business|Cooking Channel Business|Travel Vlogging Business|Gaming Channel Growth|Education Channel Growth|Finance Channel Business|News Channel Automation|Meme Page Business|Affiliate Blog SEO|Amazon FBA Mastery|Etsy Store Mastery|Print on Demand Business|Stock Photography Business|Voice Over Business|Translation Business AI|Resume Writing Business|LinkedIn Profile Optimization|AI Tools Mastery 100 Tools|Chatbot Development|AI Voice Agent Mastery|AI Receptionist Business"
TOPICS = TOPICS_STR.split("|")

def load_json(p,d):
    if p.exists():
        t=p.read_text(encoding="utf-8")
        if len(t)>2:
            try: return json.loads(t)
            except: return d
    return d

def save_json(p,d):
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")

class MasterTeacherAI:
    def title(self, topic, n):
        titles={
            1:"M01 WHAT IS "+topic,
            2:"M02 WHY IMPORTANT "+topic,
            3:"M03 WHERE USE "+topic,
            4:"M04 WHEN TIMING "+topic,
            5:"M05 WHO ELIGIBLE "+topic,
            6:"M06 HOW ARCHITECTURE "+topic,
            7:"M07 WITH WHAT TOOLS "+topic,
            8:"M08 WHAT USE EARNING "+topic,
            9:"M09 HOW TO USE PRACTICAL "+topic,
            10:"M10 HOW TO DO RIGHT WAY "+topic,
            11:"M11 FUNDAMENTALS "+topic,
            12:"M12 TOOLS PART1 "+topic,
            13:"M13 TOOLS PART2 "+topic,
            14:"M14 PERCEIVE REASON ACT "+topic,
            15:"M15 RAG MEMORY "+topic,
            16:"M16 PROMPT ENGINEERING "+topic,
            17:"M17 REAL STORY RAHUL VILLAGE "+topic,
            18:"M18 CASE STUDY 1L MONTH "+topic,
            19:"M19 CASE STUDY 10M ARR "+topic,
            20:"M20 MISTAKES 90 FAIL "+topic,
            21:"M21 PRO TIP SECRET DIARY "+topic,
            22:"M22 MINDSET MILLIONAIRE "+topic,
            23:"M23 TIME MANAGEMENT 30 DAYS "+topic,
            24:"M24 FREELANCING UPWORK FIVERR "+topic,
            