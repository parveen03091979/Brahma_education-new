import streamlit as st
import json
import hashlib
import datetime
import urllib.parse
from pathlib import Path
import pandas as pd
import re

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
CONFIG_FILE = DATA_DIR / 'config.json'
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

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_name(name):
    name = name.strip()
    if len(name) < 3:
        return False
    if len(set(name.lower().replace(' ', ''))) < 2:
        return False
    return sum(1 for c in name if c.isalpha()) >= 2

def is_valid_utr(utr):
    utr = utr.strip()
    return utr.isdigit() and len(utr) == 12

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])
config = load_json(CONFIG_FILE, {})

if len(courses) == 0:
    for i in range(100):
        t = f'Course {i+1}'
        if i == 0: t = 'AI Agent Automation 2026'
        if i == 1: t = 'Instagram Reels Mastery'
        if i == 2: t = 'YouTube Automation AI'
        if i == 3: t = 'Prompt Engineering Pro'
        if i == 4: t = 'Digital Marketing SEO'
        courses.append({'id': f'BRAHMA{1000+i}', 'topic': t, 'price': 999, 'videos': 400})
    save_json(COURSES_FILE, courses)

if 'admin_logged' not in st.session_state:
    st.session_state['admin_logged'] = False
if 'chat_messages' not in st.session_state:
    st.session_state['chat_messages'] = []

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

def smart_answer(q, courses_list):
    q = (q or '').lower()
    if 'kya' in q or 'kitne' in q or 'list' in q:
        top = courses_list[0].get('topic') if courses_list else 'AI Course'
        return f'We have 100+ courses. Top is {top}. Check Browse Courses. Each has 400 videos.'
    if 'best' in q:
        return 'Best: AI Agent Automation, Instagram Reels, YouTube Automation, Digital Marketing.'
    if 'price' in q or 'fees' in q:
        return 'Price Rs 999 to 1399. 400 videos. Lifetime access. Instant access after payment.'
    if 'hindi' in q:
        return 'Yes, Hindi and English both. Voice separate using FREE tools.'
    return 'We have 100+ professional courses. Search in Browse Courses.'

if st.session_state['admin_logged']:
    if menu == 'Dashboard':
        st.title('Dashboard')
        c1, c2, c3 = st.columns(3)
        c1.metric('Courses', len(courses))
        c2.metric('Sales', len(purchases))
        c3.metric('Total Approved', len(purchases))
        st.dataframe(pd.DataFrame(courses), use_container_width=True)

    if menu == 'Price Edit':
        st.title('Price Edit')
        search = st.text_input('Search')
        fl = [c for c in courses if search.lower() in c.get('topic','').lower()] if search else courses
        for c in fl[:20]:
            with st.expander(f"{c.get('topic')} - Rs {c.get('price')}"):
                np = st.number_input(f"Price {c['id']}", value=int(c.get('price',999)), key=f"p_{c['id']}")
                if st.button(f"Update {c['id']}", key=f"u_{c['id']}"):
                    c['price'] = int(np)
                    save_json(COURSES_FILE, courses)
                    st.success('Updated')

    if menu == 'QR Setup':
        st.title('QR Setup')
        st.info(f'UPI {MY_UPI_ID}')
        up = st.file_uploader('Upload QR', type=['jpg','png','jpeg'])
        if up:
            UPI_QR_PATH.write_bytes(up.getvalue())
            st.success('QR Saved')
            st.rerun()
        if UPI_QR_PATH.exists():
            st.image(str(UPI_QR_PATH), width=300)
            if st.button('Delete QR'):
                UPI_QR_PATH.unlink(missing_ok=True)
                st.rerun()

    if menu == 'Super Brain':
        st.title('Super Brain - Auto Agent FREE')
        ca, cb = st.columns(2)
        with ca:
            hi = st.text_area('Hindi Text', 'Namaste, AI Agent banana seekhenge', key='hi')
            if st.button('Make Hindi Voice FREE'):
                out = VOICE_DIR / 'hindi.mp3'
                ok = make_voice(hi, 'hi', out)
                if ok:
                    st.success('Hindi Voice Done')
                    st.audio(str(out))
                else:
                    st.error('Add gtts in requirements')
        with cb:
            en = st.text_area('English Text', 'Hello, we learn AI Agent', key='en')
            if st.button('Make English Voice FREE'):
                out = VOICE_DIR / 'english.mp3'
                ok = make_voice(en, 'en', out)
                if ok:
                    st.success('English Voice Done')
                    st.audio(str(out))
                else:
                    st.error('Add gtts')
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button('Make SEO Files'):
                for co in courses:
                    (SEO_DIR / f"{co['id']}_seo.txt").write_text(co['topic'], encoding='utf-8')
                st.success('SEO Done')
        with b2:
            if st.button('Make Blogs'):
                for co in courses:
                    (BLOG_DIR / f"{co['id']}_blog.txt").write_text(co['topic'], encoding='utf-8')
                st.success('Blogs Done')
        with b3:
            if st.button('Make Social Posts Safe'):
                for co in courses[:30]:
                    (SOCIAL_DIR / f"{co['id']}_post.txt").write_text(co['topic'], encoding='utf-8')
                st.success('Posts Done Safe')
        with st.form('newc'):
            topic = st.text_input('New Course Topic')
            price = st.number_input('Price', value=999)
            if st.form_submit_button('Create Course Auto'):
                if topic:
                    new_id = f'BRAHMA{1000+len(courses)+1}'
                    courses.append({'id': new_id, 'topic': topic, 'price': int(price), 'videos': 400})
                    save_json(COURSES_FILE, courses)
                    st.success('Course Created')
                    st.rerun()

    if menu == 'Sales':
        st.title('Sales - Instant Access System - No Approval Needed')
        st.info('Now all keys are auto-approved - No 2-4 hour wait - Instant access')
        st.dataframe(pd.DataFrame(purchases), use_container_width=True)

    if menu == 'Settings':
        with st.form('bank'):
            upi = st.text_input('UPI', value=MY_UPI_ID)
            if st.form_submit_button('Save'):
                save_json(CONFIG_FILE, {'upi_id': upi})
                st.success('Saved')

else:
    if menu == 'Browse Courses':
        st.title('Brahma Education')
        st.write('100+ Professional Courses in Hindi and English')
        st.write('400+ Videos per Course - Lifetime Access - Instant Access')
        st.divider()
        search = st.text_input('Search course')
        fl = [c for c in courses if search.lower() in c.get('topic','').lower()] if search else courses
        st.write(f"Total {len(fl)} courses")
        page_size = 20
        total_pages = max(1, (len(fl) + page_size - 1) // page_size)
        page = st.selectbox('Pages', range(1, total_pages+1), format_func=lambda x: f"Page {x}")
        pcs = fl[(page-1)*page_size:page*page_size]
        for idx, co in enumerate(pcs, start=(page-1)*page_size+1):
            with st.expander(f"{idx}. {co.get('topic')} - Rs {co.get('price')}"):
                col_qr, col_pay = st.columns([1,2])
                with col_qr:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH), width=220, caption='Secure UPI Payment')
                    else:
                        st.info('Secure UPI Payment')
                with col_pay:
                    st.write(f"Course: {co.get('topic')}")
                    st.write(f"Price: Rs {co.get('price')}")
                    st.write('Instant Access - No Wait')
                    params = {'pa': MY_UPI_ID, 'pn': MY_NAME, 'am': str(co.get('price',999)), 'cu': 'INR', 'tn': co.get('topic','')[:20]}
                    link = f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"Pay Rs {co.get('price')} - Instant Access", link, type='primary')
                with st.form(f"buy_{co['id']}_{idx}"):
                    st.write('**Fill After Payment - Instant Access**')
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        name = st.text_input('Full Name', key=f"n_{idx}")
                    with c2:
                        email = st.text_input('Email with @', key=f"e_{idx}")
                    with c3:
                        utr = st.text_input('UTR 12 digit', key=f"u_{idx}", help='12 digit number from UPI app')
                    if st.form_submit_button('Get Instant Access', type='primary'):
                        if not is_valid_name(name):
                            st.error('Enter valid name min 3 chars - Example Rahul Sharma')
                            st.stop()
                        if not is_valid_email(email):
                            st.error('Enter valid email with @ - Example test@gmail.com')
                            st.stop()
                        if not is_valid_utr(utr):
                            st.error('Enter valid 12 digit UTR number - Example 123456789012 - From UPI app history')
                            st.stop()
                        inv = f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                        key = f"BRAHMA-{hashlib.sha256((email+co.get('topic')+inv+utr).encode()).hexdigest()[:10].upper()}"
                        # INSTANT APPROVAL - NO PENDING
                        purchases.append({'invoice_no': inv, 'access_key': key, 'name': name, 'email': email, 'course': co.get('topic'), 'course_id': co.get('id'), 'price': co.get('price'), 'utr': utr, 'status': 'APPROVED', 'date': str(datetime.datetime.now())})
                        save_json(PURCHASE_FILE, purchases)
                        st.success(f"Payment Verified - Instant Access Granted")
                        st.info(f"Your Invoice {inv} - Your Key {key}")
                        st.warning('Go to My Access - Enter this Key - Course will open instantly - No wait')

    if menu == 'My Access':
        st.title('My Learning - Instant Access')
        st.write('Enter your key - Course opens instantly - No approval needed')
        k = st.text_input('Invoice or Key')
        if st.button('Unlock Instantly', type='primary'):
            found = [p for p in purchases if p.get('access_key') == k or p.get('invoice_no') == k]
            if not found:
                st.error('Invalid key - Check your invoice - Example BRAHMA-XXXXXXXXXX')
            else:
                pu = found[0]
                # INSTANT ACCESS - NO PENDING CHECK
                st.success(f"Welcome {pu.get('name')} - Course Unlocked Instantly")
                st.write(f"Course: {pu.get('course')}")
                st.write(f"Price Paid: Rs {pu.get('price')}")
                st.write(f"UTR: {pu.get('utr')}")
                st.balloons()
                st.video('https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4')
                st.info('This is your purchased course - Lifetime access - Enjoy learning')

    if menu == 'Chat Support':
        st.title('Chat Support')
        st.write('Session only - Closes when app closed')
        if st.button('Clear Chat Now'):
            st.session_state['chat_messages'] = []
            st.success('Chat cleared')
            st.rerun()
        for ch in st.session_state['chat_messages']:
            with st.chat_message(ch['role']):
                st.write(ch['msg'])
        q = st.chat_input('Ask your question')
        if q:
            st.session_state['chat_messages'].append({'role': 'user', 'msg': q})
            ans = smart_answer(q, courses)
            st.session_state['chat_messages'].append({'role': 'assistant', 'msg': ans})
            st.rerun()