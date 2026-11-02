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