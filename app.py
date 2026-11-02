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

st.set_page_config(page_title='Brahma Education', layout='wide')

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / '.master_hash'
COURSES_FILE = DATA_DIR / 'courses.json'
PURCHASE_FILE = DATA_DIR / 'purchases.json'
CHAT_FILE = DATA_DIR / 'chat_history.json'
CONFIG_FILE = DATA_DIR / 'config.json'
LOG_FILE = DATA_DIR / 'log.json'
UPI_QR_PATH = DATA_DIR / 'upi_qr.jpg'
VOICE_DIR = DATA_DIR / 'voice'
VOICE_DIR.mkdir(exist_ok=True)
SEO_DIR = DATA_DIR / 'seo'
SEO_DIR.mkdir(exist_ok=True)
BLOG_DIR = DATA_DIR / 'blogs'
BLOG_DIR.mkdir(exist_ok=True)
SOCIAL_DIR = DATA_DIR / 'social'
SOCIAL_DIR.mkdir(exist_ok=True)

MY_UPI_ID = 'parveen39179@okicici'
MY_NAME = 'Parveen Kumar'

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size > 2:
            return json.loads(p.read_text(encoding='utf-8'))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])
chats = load_json(CHAT_FILE, [])
config = load_json(CONFIG_FILE, [])
logs = load_json(LOG_FILE, [])

if len(courses) == 0:
    for i in range(100):
        topic = f'Course {i+1} - Professional Skill'
        if i == 0: topic = 'AI Agent Automation 2026'
        if i == 1: topic = 'Instagram Viral Reels Mastery'
        if i == 2: topic = 'YouTube Automation AI'
        if i == 3: topic = 'Prompt Engineering Pro'
        if i == 4: topic = 'Digital Marketing SEO 2026'
        courses.append({'id': f'BRAHMA{1000+i}', 'topic': topic, 'price': 999, 'videos': 400})
    save_json(COURSES_FILE, courses)

if 'admin_logged' not in st.session_state:
    st.session_state['admin_logged'] = False

st.sidebar.title('Brahma Education')
if not MASTER_HASH.exists():
    pw = st.sidebar.text_input('Create Admin Password', type='password')
    if st.sidebar.button('Create Admin'):
        if pw and len(pw) >= 4:
            MASTER_HASH.write_text(hashlib.sha256(pw.encode()).hexdigest())
            st.rerun()
    menu = 'Browse Courses'
else:
    if not st.session_state['admin_logged']:
        menu = st.sidebar.radio('Menu', ['Browse Courses', 'My Access', 'Chat Support'])
        st.sidebar.divider()
        pw = st.sidebar.text_input('Admin Password', type='password')
        if st.sidebar.button('Admin Login'):
            if hashlib.sha256(pw.encode()).hexdigest() == MASTER_HASH.read_text():
                st.session_state['admin_logged'] = True
                st.rerun()
            else:
                st.sidebar.error('Wrong Password')
    else:
        st.sidebar.success('Admin Panel')
        menu = st.sidebar.radio('Admin', ['Dashboard', 'Price Edit', 'QR Setup', 'Super Brain', 'Sales', 'Settings'])
        if st.sidebar.button('Logout'):
            st.session_state['admin_logged'] = False
            st.rerun()

def make_voice(text, lang, path):
    if not GTTS_OK: return False
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(str(path))
        return True
    except: return False

# SMART CHATBOT - NO REPEAT - PROFESSIONAL ANSWERS
def get_smart_answer(user_q, courses_list):
    q = (user_q or '').lower().strip()
    if any(x in q for x in ['kya kya hai', 'kitne course', 'course list', 'kaun kaun']):
        top5 = ', '.join([c.get('topic') for c in courses_list[:5]])
        return f"Hamare paas 100+ professional courses hain. Top courses: {top5} aur bhi 95 courses. Browse Courses me full list dekho. Har course me 400 videos Hindi English me."
    if 'best' in q and 'course' in q:
        return "Best courses: 1. AI Agent Automation 2026 2. Instagram Viral Reels Mastery 3. YouTube Automation AI 4. Digital Marketing SEO 5. Prompt Engineering Pro. Aapki interest ke hisab se choose karo."
    if 'price' in q or 'fees' in q or 'kitne ka' in q or 'paisa' in q:
        return f"Har course Rs 999 se Rs 1399 me. 400 videos, 46 hours, Hindi English, lifetime access. Secure UPI payment {MY_UPI_ID}."
    if 'hindi' in q:
        return "Haan, har course Hindi aur English dono me available hai. 400 videos Hindi me alag, English me alag. Voice bhi Hindi English separate FREE tools se banayi hai."
    if 'certificate' in q or 'job' in q or 'naukri' in q:
        return "Har course complete karne par certificate mile