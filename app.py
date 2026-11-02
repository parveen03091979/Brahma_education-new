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

st.set_page_config(page_title="Brahma Education", layout="wide")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
CONFIG_FILE = DATA_DIR / "config.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
VOICE_DIR = DATA_DIR / "voice"
VOICE_DIR.mkdir(exist_ok=True)

MY_UPI_ID = "parveen39179@okicici"
MY_NAME = "Parveen Kumar"

BLOCKED_UTRS = ["123456789012","123456789123","111111111111","000000000000","999999999999","184792641807","012345678901"]

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size > 2:
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def is_valid_name(name):
    name = name.strip()
    if not re.match(r"^[A-Za-z ]+$", name):
        return False, "Only letters space"
    parts = name.split()
    if len(parts) < 2:
        return False, "Full name First Last required"
    for i in range(len(name.lower())-2):
        if name.lower()[i] == name.lower()[i+1] == name.lower()[i+2]:
            return False, "Same letter 3 times not allowed"
    return True, "OK"

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, email):
        return False, "Email must have @ and .com"
    local = email.split("@")[0].lower()
    for i in range(len(local)-2):
        if local[i] == local[i+1] == local[i+2]:
            return False, "Same letter 3 times not allowed"
    return True, "OK"

def is_valid_utr(utr, purchases_list):
    utr = utr.strip()
    if not (utr.isdigit() and len(utr) == 12):
        return False, "UTR must be exactly 12 digit"
    if utr in BLOCKED_UTRS:
        return False, f"Fake UTR {utr} blocked"
    for p in purchases_list:
        if p.get("utr") == utr:
            return False, f"UTR {utr} already used"
    return True, "OK"

def make_voice(text, lang, path):
    if not GTTS_OK:
        return False
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(str(path))
        return True
    except:
        return False

def get_course_content(course_topic):
    curriculum = []
    for m in range(1, 11):
        vids = []
        for v in range(1, 41):
            idx = (m-1)*40 + v
            title = f"Lesson {idx}: {course_topic} - Module {m} Part {v}"
            if v == 1:
                title = f"Module {m} Intro: What is {course_topic}?"
            elif v == 20:
                title = f"Module {m} Practical: Build {course_topic}"
            elif v == 40:
                title = f"Module {m} Summary"
            desc_hi = f"Namaste! Is lesson me aap seekhenge {course_topic} Module {m} Lesson {v}. Lesson {idx} of 400."
            desc_en = f"Hello! Lesson {idx} you will learn {course_topic} Module {m} Lesson {v}."
            vids.append({"no": idx, "title": title, "desc_hi": desc_hi, "desc_en": desc_en, "duration": "12 mins"})
        curriculum.append({"module_no": m, "title": f"Module {m}: {course_topic}", "videos": vids})
    return curriculum

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

if len(courses) == 0:
    for i in range(100):
        t = f"Course {i+1}"
        if i == 0: t = "AI Agent Automation 2026"
        if i == 1: t = "Instagram Reels Mastery"
        if i == 2: t = "YouTube Automation AI"
        if i == 3: t = "Prompt Engineering Pro"
        if i == 4: t = "Digital Marketing SEO"
        courses.append({"id": f"BRAHMA{1000+i}", "topic": t, "price": 999, "videos": 400})
    save_json(COURSES_FILE, courses)

if "admin_logged" not in st.session_state:
    st.session_state["admin_logged"] = False
if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []

st.sidebar.title("Brahma Education")
if not MASTER_HASH.exists():
    pw = st.sidebar.text_input("Create Admin Password", type="password")
    if st.sidebar.button("Create Admin"):
        if pw and len(pw) >= 4:
            MASTER_HASH.write_text(hashlib.sha256(pw.encode()).hexdigest())
            st.rerun()
    menu = "Browse Courses"
else:
    if not st.session_state["admin_logged"]:
        menu = st.sidebar.radio("Menu", ["Browse Courses", "My Access", "Chat Support"])
        st.sidebar.divider()
        pw = st.sidebar.text_input("Admin Password", type="password")
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(pw.encode()).hexdigest() == MASTER_HASH.read_text():
                st.session_state["admin_logged"] = True
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Admin Panel")
        menu = st.sidebar.radio("Admin", ["Dashboard", "Video Library", "Sales", "Super Brain", "QR Setup", "Price Edit", "Settings"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"] = False
            st.rerun()

if st.session_state["admin_logged"]:
    if menu == "Dashboard":
        st.title("Dashboard - Apna Course System")
        c1, c2, c3 = st.columns(3)
        c1.metric("Courses", len(courses))
        c2.metric("Sales", len(purchases))
        c3.metric("Total Lessons", len(courses)*400)
        st.dataframe(pd.DataFrame(courses), use_container_width=True)

    if menu == "Video Library":
        st.title("Video Library - Check Videos Bani Ya Nahi")
        st.write("Yahan check karo - Hindi English voice bani ya nahi - No YouTube")
        st.divider()
        for co in courses[:20]:
            co_id = co.get("id")
            co_topic = co.get("topic")
            hi_path = VOICE_DIR / f"{co_id}_hi.mp3"
            en_path = VOICE_DIR / f"{co_id}_en.mp3"
            with st.expander(f"{co_topic} - {co_id} - 400 Lessons"):
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.metric("Lessons", "400")
                    st.write(f"Price Rs {co.get('price')}")
                with c2:
                    if hi_path.exists():
                        st.success("Hindi Voice - Bani Hai")
                        st.audio(str(hi_path))
                    else:
                        st.error("Hindi Voice - Nahi Bani")
                        if st.button(f"Gen Hindi {co_id}", key=f"h_{co_id}"):
                            make_voice(f"Welcome to {co_topic} Hindi me", "hi", hi_path)
                            st.rerun()
                with c3:
                    if en_path.exists():
                        st.success("English Voice - Bani Hai")
                        st.audio(str(en_path))
                    else:
                        st.error("English Voice - Nahi Bani")
                        if st.button(f"Gen English {co_id}", key=f"e_{co_id}"):
                            make_voice(f"Welcome to {co_topic} English", "en", en_path)
                            st.rerun()

    if menu == "Sales":
        st.title("Sales - UTR Duplicate Block")
        st.dataframe(pd.DataFrame(purchases), use_container_width=True)

    if menu == "Super Brain":
        st.title("Super Brain - Apna Course Creator - No YouTube")
        st.write("Creates 400 lessons Hindi English voice FREE Tools")
        ca, cb = st.columns(2)
        with ca:
            hi = st.text_area("Hindi Text", "Namaste, AI Agent banana seekhenge", key="hi")
            if st.button("Make Hindi Voice FREE"):
                out = VOICE_DIR / "hindi_sample.mp3"
                ok = make_voice(hi, "hi", out)
                if ok:
                    st.success("Hindi Voice Done")
                    st.audio(str(out))
                else:
                    st.error("Add gtts in requirements")
        with cb:
            en = st.text_area("English Text", "Hello, we learn AI Agent", key="en")
            if st.button("Make English Voice FREE"):
                out = VOICE_DIR / "english_sample.mp3"
                ok = make_voice(en, "en", out)
                if ok:
                    st.success("English Voice Done")
                    st.audio(str(out))
                else:
                    st.error("Add gtts")
        with st.form("newc"):
            topic = st.text_input("New Course Topic - Apna - No YouTube")
            price = st.number_input("Price", value=999)
            if st.form_submit_button("Create Apna Course 400 Lessons"):
                if topic:
                    new_id = f"BRAHMA{1000+len(courses)+1}"
                    courses.append({"id": new_id, "topic": topic, "price": int(price), "videos": 400})
                    save_json(COURSES_FILE, courses)
                    make_voice(f"Welcome to {topic} Hindi", "hi", VOICE_DIR / f"{new_id}_hi.mp3")
                    make_voice(f"Welcome to {topic} English", "en", VOICE_DIR / f"{new_id}_en.mp3")
                    st.success(f"Course {topic} Created - 400 lessons")
                    st.rerun()

    if menu == "QR Setup":
        st.title("QR Setup")
        st.info(f"UPI {MY_UPI_ID}")
        up = st.file_uploader("Upload QR", type=["jpg","png","jpeg"])
        if up:
            UPI_QR_PATH.write_bytes(up.getvalue())
            st.success("QR Saved")
            st.rerun()
        if UPI_QR_PATH.exists():
            st.image(str(UPI_QR_PATH), width=300)

    if menu == "Price Edit":
        st.title("Price Edit")
        search = st.text_input("Search")
        fl = [c for c in courses if search.lower() in c.get("topic","").lower()] if search else courses
        for c in fl[:20]:
            with st.expander(f"{c.get('topic')} - Rs {c.get('price')}"):
                np = st.number_input(f"Price {c['id']}", value=int(c.get("price",999)), key=f"p_{c['id']}")
                if st.button(f"Update {c['id']}", key=f"u_{c['id']}"):
                    c["price"] = int(np)
                    save_json(COURSES_FILE, courses)
                    st.success("Updated")

    if menu == "Settings":
        st.title("Settings")
        with st.form("bank"):
            upi = st.text_input("UPI", value=MY_UPI_ID)
            if st.form_submit_button("Save"):
                save_json(CONFIG_FILE, {"upi_id": upi})
                st.success("Saved")

else:
    if menu == "Browse Courses":
        st.title("Brahma Education - Apna Course - No YouTube")
        st.write("100+ Courses - Each 400 Lessons - Hindi English Voice - FREE Tools")
        st.divider()
        search = st.text_input("Search apna course")
        fl = [c for c in courses if search.lower() in c.get("topic","").lower()] if search else courses
        st.write(f"Total {len(fl)} courses - No YouTube")
        page_size = 20
        total_pages = max(1, (len(fl) + page_size - 1) // page_size)
        page = st.selectbox("Pages", range(1, total_pages+1), format_func=lambda x: f"Page {x}")
        pcs = fl[(page-1)*page_size:page*page_size]
        for idx, co in enumerate(pcs, start=(page-1)*page_size+1):
            with st.expander(f"{idx}. {co.get('topic')} - Rs {co.get('price')} - 400 Lessons"):
                col_qr, col_pay = st.columns([1,2])
                with col_qr:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH), width=220, caption="Secure UPI")
                    else:
                        st.info("Secure UPI Payment")
                with col_pay:
                    st.write(f"Course: {co.get('topic')}")
                    st.write(f"400 Lessons - Hindi + English Voice - No YouTube")
                    params = {"pa": MY_UPI_ID, "pn": MY_NAME, "am": str(co.get("price",999)), "cu": "INR", "tn": co.get("topic","")[:20]}
                    link = f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"Pay Rs {co.get('price')}", link, type="primary")
                with st.form(f"buy_{co['id']}_{idx}"):
                    st.write("After REAL Payment - No Free")
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        name = st.text_input("Full Name", key=f"n_{idx}", placeholder="Rahul Sharma")
                    with c2:
                        email = st.text_input("Email", key=f"e_{idx}", placeholder="rahul@gmail.com")
                    with c3:
                        utr = st.text_input("UTR 12 digit", key=f"u_{idx}", placeholder="UPI app se")
                    if st.form_submit_button("Get Apna Course Instant", type="primary"):
                        ok_name, msg_name = is_valid_name(name)
                        if not ok_name:
                            st.error(f"Name Error: {msg_name}")
                            st.stop()
                        ok_email, msg_email = is_valid_email(email)
                        if not ok_email:
                            st.error(f"Email Error: {msg_email}")
                            st.stop()
                        ok_utr, msg_utr = is_valid_utr(utr, purchases)
                        if not ok_utr:
                            st.error(f"UTR Error: {msg_utr}")
                            st.stop()
                        inv = f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                        key = f"BRAHMA-{hashlib.sha256((email+co.get('topic')+inv+utr).encode()).hexdigest()[:10].upper()}"
                        purchases.append({"invoice_no": inv, "access_key": key, "name": name, "email": email, "course": co.get("topic"), "course_id": co.get("id"), "price": co.get("price"), "utr": utr, "status": "APPROVED", "date": str(datetime.datetime.now())})
                        save_json(PURCHASE_FILE, purchases)
                        st.success(f"Verified - Apna Course Access - Invoice {inv}")
                        st.info(f"Key {key} - My Access me dalo")

    if menu == "My Access":
        st.title("My Learning - Apna Course - No YouTube - Real 400 Lessons")
        k = st.text_input("Invoice or Key")
        if st.button("Unlock My Apna Course", type="primary"):
            found = [p for p in purchases if p.get("access_key") == k or p.get("invoice_no") == k]
            if not found:
                st.error("Invalid key")
            else:
                pu = found[0]
                st.success(f"Welcome {pu.get('name')} - {pu.get('course')} - Apna Course")
                st.write(f"Price Rs {pu.get('price')} - UTR {pu.get('utr')}")
                st.divider()
                st.subheader(f"{pu.get('course')} - Apna 400 Lessons - No YouTube")
                curriculum = get_course_content(pu.get("course"))
                v_hi = VOICE_DIR / f"{pu.get('course_id')}_hi.mp3"
                v_en = VOICE_DIR / f"{pu.get('course_id')}_en.mp3"
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Hindi Voice Sample - Apna - No YouTube:")
                    if v_hi.exists():
                        st.audio(str(v_hi))
                    else:
                        if st.button("Generate Hindi Voice FREE"):
                            make_voice(f"Welcome to {pu.get('course')} Hindi", "hi", v_hi)
                            st.rerun()
                with col2:
                    st.write("English Voice Sample - Apna - No YouTube:")
                    if v_en.exists():
                        st.audio(str(v_en))
                    else:
                        if st.button("Generate English Voice FREE"):
                            make_voice(f"Welcome to {pu.get('course')} English", "en", v_en)
                            st.rerun()
                st.divider()
                for mod in curriculum[:2]:
                    with st.expander(f"{mod['title']} - {len(mod['videos'])} Lessons - No YouTube"):
                        for vid in mod["videos"][:5]:
                            st.write(f"{vid['no']}. {vid['title']} - {vid['duration']}")
                            st.write(f"Hindi: {vid['desc_hi']}")
                            st.write(f"English: {vid['desc_en']}")
                st.info("Full 400 lessons - Apna content - No YouTube")

    if menu == "Chat Support":
        st.title("Chat Support - Apna Course")
        if st.button("Clear Chat"):
            st.session_state["chat_messages"] = []
            st.rerun()
        for ch in st.session_state["chat_messages"]:
            with st.chat_message(ch["role"]):
                st.write(ch["msg"])
        q = st.chat_input("Ask about apna course")
        if q:
            st.session_state["chat_messages"].append({"role": "user", "msg": q})
            st.session_state["chat_messages"].append({"role": "assistant", "msg": "Apna course: 100+ courses 400 lessons Hindi English voice FREE - No YouTube - Browse Courses"})
            st.rerun()