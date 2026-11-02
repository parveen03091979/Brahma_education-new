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

HUNDRED = []
HUNDRED.append("AI Agent Automation 2026")
HUNDRED.append("Instagram Reels Mastery")
HUNDRED.append("YouTube Automation AI")
HUNDRED.append("Prompt Engineering Pro")
HUNDRED.append("Digital Marketing SEO Mastery")
HUNDRED.append("ChatGPT Mastery 2026")
HUNDRED.append("Facebook Ads Mastery")
HUNDRED.append("Google Ads Mastery")
HUNDRED.append("SEO Advanced 2026")
HUNDRED.append("Social Media Marketing Pro")
HUNDRED.append("Content Writing AI")
HUNDRED.append("Copywriting Mastery")
HUNDRED.append("Blogging Mastery 2026")
HUNDRED.append("Affiliate Marketing Pro")
HUNDRED.append("Dropshipping Business")
HUNDRED.append("E-commerce Mastery Shopify")
HUNDRED.append("Canva Design Mastery")
HUNDRED.append("Video Editing CapCut Pro")
HUNDRED.append("YouTube SEO Mastery")
HUNDRED.append("Instagram Growth Hack")
HUNDRED.append("LinkedIn Marketing Pro")
HUNDRED.append("Twitter X Growth Mastery")
HUNDRED.append("TikTok Viral Mastery")
HUNDRED.append("Pinterest Marketing")
HUNDRED.append("Quora Marketing")
HUNDRED.append("Email Marketing Automation")
HUNDRED.append("WhatsApp Marketing Pro")
HUNDRED.append("Telegram Channel Growth")
HUNDRED.append("Influencer Marketing")
HUNDRED.append("Personal Branding Mastery")
HUNDRED.append("Freelancing Mastery Upwork Fiverr")
HUNDRED.append("Agency Business Mastery")
HUNDRED.append("SaaS Business 2026")
HUNDRED.append("No-Code Business Bubble")
HUNDRED.append("Python Programming Mastery")
HUNDRED.append("JavaScript Mastery 2026")
HUNDRED.append("React JS Mastery")
HUNDRED.append("Next.js Mastery")
HUNDRED.append("Node.js Backend Mastery")
HUNDRED.append("Web Development Full Stack")
HUNDRED.append("WordPress Mastery")
HUNDRED.append("Shopify Store Design")
HUNDRED.append("UI UX Design Mastery")
HUNDRED.append("Figma Design Pro")
HUNDRED.append("Graphic Design Mastery")
HUNDRED.append("Logo Design Mastery")
HUNDRED.append("Thumbnail Design Viral")
HUNDRED.append("Video Animation Mastery")
HUNDRED.append("AI Image Generation Midjourney")
HUNDRED.append("AI Video Generation Sora")
HUNDRED.append("Voice Cloning ElevenLabs")
HUNDRED.append("Automation n8n Make")
HUNDRED.append("Zapier Automation Mastery")
HUNDRED.append("Notion Productivity Mastery")
HUNDRED.append("Excel Advanced Mastery")
HUNDRED.append("Google Sheets Automation")
HUNDRED.append("Data Analysis Python")
HUNDRED.append("Machine Learning Mastery")
HUNDRED.append("Deep Learning 2026")
HUNDRED.append("Data Science Mastery")
HUNDRED.append("Stock Market Trading AI")
HUNDRED.append("Crypto Trading Mastery")
HUNDRED.append("Forex Trading Pro")
HUNDRED.append("Real Estate Business")
HUNDRED.append("Motivational Speaking Mastery")
HUNDRED.append("Public Speaking Pro")
HUNDRED.append("Communication Skills Mastery")
HUNDRED.append("English Speaking Pro")
HUNDRED.append("Hindi Content Creation")
HUNDRED.append("Podcast Mastery")
HUNDRED.append("Music Production AI")
HUNDRED.append("Photography Mastery")
HUNDRED.append("Reels Editing Viral")
HUNDRED.append("Meme Marketing Mastery")
HUNDRED.append("Viral Content Formula")
HUNDRED