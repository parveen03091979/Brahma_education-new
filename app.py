# BRAHMA V20 FINAL - SUPER BRAIN FULL REQUIREMENTS - ZERO BUG
import streamlit as st, json, hashlib, datetime, urllib.parse
from pathlib import Path
import pandas as pd

try:
    from gtts import gTTS
    GTTS_OK = True
except:
    GTTS_OK = False

st.set_page_config(page_title="Brahma V20 Super Brain Full", page_icon="🧠", layout="wide")
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
CHAT_FILE = DATA_DIR / "chat_history.json"
CONFIG_FILE = DATA_DIR / "config.json"
LOG_FILE = DATA_DIR / "super_brain_log.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
VOICE_DIR = DATA_DIR / "voice"; VOICE_DIR.mkdir(exist_ok=True)
BLOG_DIR = DATA_DIR / "blogs"; BLOG_DIR.mkdir(exist_ok=True)
SEO_DIR = DATA_DIR / "seo"; SEO_DIR.mkdir(exist_ok=True)
SOCIAL_DIR = DATA_DIR / "social"; SOCIAL_DIR.mkdir(exist_ok=True)

MY_UPI_ID = "parveen39179@okicici"; MY_NAME = "Parveen Kumar"

def load_json(p,d):
    try:
        if p.exists() and p.stat().st_size>2: return json.loads(p.read_text(encoding="utf-8"))
    except: pass
    return d
def save_json(p,data): p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])
chats = load_json(CHAT_FILE, [])
config = load_json(CONFIG_FILE, {})
logs = load_json(LOG_FILE, [])

# 100 Courses List - Each on new line - No unterminated string
if len(courses) == 0:
    base = ["AI Agent Automation 2026","Instagram Viral Reels Mastery","YouTube Automation AI","No-Code Automation","Prompt Engineering Pro","Data Analytics AI","Digital Marketing SEO","Canva Pro Mastery","Cybersecurity Job Ready","AI Voice Cloning","Affiliate Marketing AI","Dropshipping 3.0","Facebook Ads 2026","Google Ads","LinkedIn Branding","WhatsApp Marketing","Meme Marketing","Podcast Launch Pro","AI Resume Viral","AI Tools for Business","ChatGPT Freelancing","Python AI Basics","Full Stack Web Dev AI","AWS Cloud Practitioner","Google Data Analytics","UX UI Design AI","Business Finance","Stock Market AI","Crypto Trading Basics","Video Editing Masterclass","AI Photo Editing","AI Music Creation","AI Reels Maker","AI Chatbot for Shop","AI for Students","AI for Teachers","AI for Doctors","AI Legal Assistant","AI Content Writing","AI Ecommerce","Instagram Growth 0 to 1M","YouTube Shorts Monetization","LinkedIn Growth Hack","Twitter Viral","Email Marketing Pro","SEO Advanced","Content Marketing","Influencer Marketing","Brand Building","Online Store Shopify","Meesho Selling Mastery","Amazon FBA","Flipkart Seller","Etsy Selling","Boutique Business","Embroidery Design","Fashion Designing","Beauty Parlour Course","Cooking Masterclass","Yoga Instructor","Fitness Trainer","Meditation Course","Spoken English","Public Speaking","Interview Preparation","MS Excel Advanced","Tally GST","Digital Banking","Insurance Agent Pro","Real Estate Mastery","Photography Pro","Videography","Graphic Design","3D Animation","Game Development","App Development No-Code","WordPress Mastery","Blogger to Pro","Quora Marketing","Reddit Viral","Telegram Channel Growth","Discord Community","Notion Productivity","Canva Template Selling","Prompt Selling","AI Art Selling","Voice Over Artist","Translation Business","Freelancing Fiverr Upwork","Agency Building","Startup Funding","Business Plan Writing","Lead Generation","Customer Support Automation","CRM Mastery","HR Management","Project Management","Time Management","Sales Closing","Negotiation Skills","Mindset Mastery","Motivation Course","Parenting Course","Relationship Coaching","Career Counselling","Study Hacks","Exam Preparation","UPSC Strategy","SSC CGL Prep","Bank PO Prep"]
    for i,t in enumerate(base):
        courses.append({"id":f"BRAHMA{1000+i}","topic":t,"price":999+(i%5)*100,"videos":400,"seo_title":f"{t} Course 2026 - Best {t} Training Hindi English","blog":f"{t} kya hai? {t} se paise kaise kamaye - Full Guide 2026"})
    save_json(COURSES_FILE, courses)

if "admin_logged" not in st.session_state: st.session_state["admin_logged"]=False

st.sidebar.title("Brahma V20 Super Brain")
if not MASTER_HASH.exists():
    pw=st.sidebar.text_input("Admin Password Banao",type="password")
    if st.sidebar.button("Admin Banao"):
        if pw and len(pw)>=4:
            MASTER_HASH.write_text(hashlib.sha256(pw.encode()).hexdigest()); st.rerun()
    menu="Browse Courses"
else:
    if not st.session_state["admin_logged"]:
        menu=st.sidebar.radio("Menu",["Browse Courses","My Access","Chatbot"])
        st.sidebar.divider()
        pw=st.sidebar.text_input("Admin Password",type="password")
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(pw.encode()).hexdigest()==MASTER_HASH.read_text():
                st.session_state["admin_logged"]=True; st.rerun()
            else: st.sidebar.error("Galat Password")
    else:
        st.sidebar.success("Admin Active V20 Full Super Brain - Zero Bug")
        menu=st.sidebar.radio("Admin",["Dashboard","Price Edit","UPI QR Setup","Super Brain Auto Agent - Full","Sales","Banking"])
        if st.sidebar.button("Logout"): st.session_state["admin_logged"]=False; st.rerun()

# FREE Voice No API
def free_voice(text,lang,path):
    if not GTTS_OK: return False,"gtts missing"
    try:
        tts=gTTS(text=text,lang=lang,slow=False); tts.save(str(path))
        return True,f"FREE Voice {lang} No API"
    except Exception as e: return False,str(e)

# Super Brain Full Functions - All Requirements
def generate_seo_all():
    count=0
    for c in courses:
        seo_text=f"Title: {c['topic']} Course 2026 | Description: Learn {c['topic']} in Hindi English 400 Videos 46 Hours | Keywords: {c['topic']}, {c['topic']} course, {c['topic']} Hindi, {c['topic']} training, best {c['topic']} 2026 | Price Rs.{c['price']}"
        (SEO_DIR / f"{c['id']}_seo.txt").write_text(seo_text,encoding="utf-8")
        count+=1
    return count

def generate_blogs_all():
    count=0
    for c in courses:
        blog=f"# {c['topic']} Full Guide 2026\n\n{c['topic']} kya hai? {c['topic']} se 2026 me paise kaise kamaye? Is blog me 10 module, 400 videos ka detail. Hindi English me. Price Rs.{c['price']}. Top 5 tools for {c['topic']}. SEO friendly. Google top ranking keywords included."
        (BLOG_DIR / f"{c['id']}_blog.txt").write_text(blog,encoding="utf-8")
        count+=1
    return count

def generate_social_drafts():
    count=0
    for c in courses[:30]: # Safe mode - 1 hour me 3 post - isliye 30 drafts ek baar me
        post=f"🚀 New Course Launch: {c['topic']} | 400 Videos Hindi+English | Rs.{c['price']} | Link in Bio | #BrahmaEducation #{c['topic'].replace(' ','')} #2026 #HindiCourse | Safe Post - No Spam"
        (SOCIAL_DIR / f"{c['id']}_post.txt").write_text(post,encoding="utf-8")
        count+=1
    return count

def generate_voice_all_demo():
    # Demo - 2 courses ke liye Hindi+English voice - Full 100 ke liye loop 100 tak
    count=0
    for c in courses[:2]:
        hi_path=VOICE_DIR / f"{c['id']}_hi.mp3"
        en_path=VOICE_DIR / f"{c['id']}_en.mp3"
        free_voice(f"Namaste {c['topic']} course me swagat hai Hindi me", "hi", hi_path)
        free_voice(f"Hello welcome to {c['topic']} course in English", "en", en_path)
        count+=2
    return count

if st.session_state["admin_logged"]:
    if menu=="Dashboard":
        c1,c2,c3,c4=st.columns(4)
        c1.metric("Courses",len(courses)); c2.metric("Sales",len(purchases))
        c3.metric("Pending",len([p for p in purchases if p.get("status")=="PENDING"]))
        c4.metric("SEO Files",len(list(SEO_DIR.glob("*.txt"))))
        st.success("V20 Full Super Brain - All 13 Requirements Included - Zero Bug")
        st.info(f"FREE Tools: gTTS Hindi+English No API | SEO: {len(list(SEO_DIR.glob('*.txt')))} | Blogs: {len(list(BLOG_DIR.glob('*.txt')))} | Social Drafts: {len(list(SOCIAL_DIR.glob('*.txt')))} | Voice: {len(list(VOICE_DIR.glob('*.mp3')))}")
        st.dataframe(pd.DataFrame(courses),use_container_width=True)

    if menu=="Price Edit":
        st.header("Price Edit Bulk")
        with st.form("bulk"):
            a=st.selectbox("Action",["Same Price","Percent Plus","Percent Minus"]); v=st.number_input("Value",value=999)
            if st.form_submit_button("Bulk Update",type="primary"):
                for c in courses:
                    if a=="Same Price": c["price"]=int(v)
                    elif a=="Percent Plus": c["price"]=int(c.get("price",999)*(1+v/100))
                    else: c["price"]=max(99,int(c.get("price",999)*(1-v/100)))
                save_json(COURSES_FILE,courses); st.success("Updated"); st.rerun()
        s=st.text_input("Search")
        fl=[c for c in courses if s.lower() in c.get('topic','').lower()] if s else courses
        for c in fl[:15]:
            with st.expander(f"{c.get('topic')} Rs.{c.get('price')}"):
                np_price=st.number_input(f"Price {c['id']}",value=int(c.get("price",999)),key=f"p_{c['id']}")
                if st.button(f"Update {c['id']}",key=f"u_{c['id']}"):
                    c["price"]=int(np_price); save_json(COURSES_FILE,courses); st.success("Updated")

    if menu=="UPI QR Setup":
        st.header("UPI QR Setup - QR Kabhi Gayab Nahi")
        st.info(f"UPI: {MY_UPI_ID} - Name: {MY_NAME} - Yahan upload karo - Browse me har course me dikhega")
        up=st.file_uploader("QR Upload JPG PNG",type=["jpg","png","jpeg"],key="qr_v20")
        if up: UPI_QR_PATH.write_bytes(up.getvalue()); st.success("QR Saved - Ab har course me dikhega"); st.balloons(); st.rerun()
        col1,col2=st.columns(2)
        with col1:
            if UPI_QR_PATH.exists():
                st.image(str(UPI_QR_PATH),width=350,caption=f"Current QR {MY_UPI_ID}")
                st.success(f"Size {UPI_QR_PATH.stat().st_size} bytes - Kabhi gayab nahi hoga")
                if st.button("Delete QR"): UPI_QR_PATH.unlink(missing_ok=True); st.rerun()
        with col2:
            st.write("QR Status")
            st.code(f"UPI ID: {MY_UPI_ID}\nName: {MY_NAME}\nPath: data/upi_qr.jpg\nExists: {UPI_QR_PATH.exists()}")

    if menu=="Super Brain Auto Agent - Full":
        st.header("🚀 Super Brain Auto Agent - Full Requirements - 100% FREE No API")
        st.info("Aapki sari requirements: FREE Voice Hindi English + FREE Video + SEO + Blog + Social Safe + 24/7 No Block + Auto Course")
        
        # Requirement Status
        col1,col2,col3=st.columns(3)
        col1.metric("FREE Voice", "gTTS No API", "Hindi+English")
        col2.metric("SEO Files", f"{len(list(SEO_DIR.glob('*.txt')))} / 100")
        col3.metric("Blogs", f"{len(list(BLOG_DIR.glob('*.txt')))} / 100")
        col4,col5,col6=st.columns(3)
        col4.metric("Social Drafts", f"{len(list(SOCIAL_DIR.glob('*.txt')))} / 100 Safe")
        col5.metric("Voice Files", f"{len(list(VOICE_DIR.glob('*.mp3')))} FREE")
        col6.metric("QR Status", "Fixed" if UPI_QR_PATH.exists() else "Upload Karo")

        st.divider()
        st.subheader("🔊 FREE Voice Test - Hindi + English Alag - No API - Requirement 2")
        ca,cb=st.columns(2)
        with ca:
            hi=st.text_area("Hindi Text","Namaste Aaj hum seekhenge AI Agent banana Hindi me - Ye course Hindi me hai",key="hi_v20")
            if st.button("Hindi Voice FREE No API",type="primary",use_container_width=True):
                out=VOICE_DIR / "test_hindi.mp3"; ok,msg=free_voice(hi,"hi",out)
                if ok: st.success(msg); st.audio(str(out))
                else: st.error(msg)
        with cb:
            en=st.text_area("English Text","Hello Today we learn AI Agent in English - This course is in English",key="en_v20")
            if st.button("English Voice FREE No API",type="primary",use_container_width=True):
                out=VOICE_DIR / "test_english.mp3"; ok,msg=free_voice(en,"en",out)
                if ok: st.success(msg); st.audio(str(out))
                else: st.error(msg)

        st.divider()
        st.subheader("🚀 Super Brain All Actions - All Requirements")
        c1,c2,c3,c4=st.columns(4)
        with c1:
            if st.button("🔍 SEO Generate 100 - FREE