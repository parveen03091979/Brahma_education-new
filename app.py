# BRAHMA V18 FINAL - INDENTATION FIXED - QR FIXED - BLANK FIXED
import streamlit as st, json, hashlib, datetime, urllib.parse
from pathlib import Path
import pandas as pd

try:
    from gtts import gTTS
    GTTS_OK = True
except:
    GTTS_OK = False

st.set_page_config(page_title="Brahma V18", page_icon="🧠", layout="wide")
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
CHAT_FILE = DATA_DIR / "chat_history.json"
CONFIG_FILE = DATA_DIR / "config.json"
LOG_FILE = DATA_DIR / "super_brain_log.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
VOICE_DIR = DATA_DIR / "voice"; VOICE_DIR.mkdir(exist_ok=True)
MY_UPI_ID = "parveen39179@okicici"; MY_NAME = "Parveen Kumar"

def safe_load(p,d):
    try:
        if p.exists() and p.stat().st_size>2:
            return json.loads(p.read_text(encoding="utf-8"))
    except: pass
    return d
def save_json(p,data):
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
def load_courses(): return safe_load(COURSES_FILE,[])
def save_courses(c): save_json(COURSES_FILE,c)
def load_purchases(): return safe_load(PURCHASE_FILE,[])
def save_purchases(p): save_json(PURCHASE_FILE,p)
def load_chats(): return safe_load(CHAT_FILE,[])
def save_chats(ch): save_json(CHAT_FILE,ch)
def load_config(): return safe_load(CONFIG_FILE,{})
def save_config(c): save_json(CONFIG_FILE,c)
def load_log(): return safe_load(LOG_FILE,[])
def save_log(l): save_json(LOG_FILE,l)

TRENDING_100=["AI Agent Automation 2026","Instagram Viral Reels Mastery","YouTube Automation with AI","No-Code Automation","Prompt Engineering Pro","Data Analytics with AI","Digital Marketing SEO 2026","Canva Pro Mastery","Cybersecurity Job Ready","AI Voice Cloning","Affiliate Marketing with AI","Dropshipping 3.0","Facebook Ads 2026","Google Ads","Personal Branding LinkedIn","WhatsApp Marketing Automation","Meme Marketing","Podcast Launch Pro","AI Resume Viral","AI Tools for Business","ChatGPT Freelancing","Python + AI Basics","Full Stack Web Dev AI","AWS Cloud Practitioner","Google Data Analytics","UX/UI Design AI","Business Finance","Stock Market with AI","Crypto Trading Basics","Video Editing Masterclass","AI Photo Editing","AI Music Creation","AI Reels Maker","AI