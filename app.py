# BRAHMA ULTIMATE V9 - QR UPLOAD INSIDE ADMIN - NO GITHUB UPLOAD NEEDED
import streamlit as st, json, hashlib, datetime, io, csv, urllib.parse
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Brahma Super Brain", page_icon="🧠", layout="wide")
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"; PURCHASE_FILE = DATA_DIR / "purchases.json"
CHAT_FILE = DATA_DIR / "chat_history.json"; CONFIG_FILE = DATA_DIR / "config.json"
API_FILE = DATA_DIR / "api_config.json"; LOG_FILE = DATA_DIR / "super_brain_log.json"
WEBSITE_DIR = DATA_DIR / "websites"; WEBSITE_DIR.mkdir(exist_ok=True)
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"

MY_UPI_ID = "parveen39179@okicici"
MY_NAME = "Parveen Kumar"

def safe_load(p, d):
    try:
        if p.exists(): return json.loads(p.read_text())
    except: return d
    return d
def load_courses(): return safe_load(COURSES_FILE, [])
def save_courses(c): COURSES_FILE.write_text(json.dumps(c, ensure_ascii=False))
def load_purchases(): return safe_load(PURCHASE_FILE, [])
def save_purchases(p): PURCHASE_FILE.write_text(json.dumps(p, indent=2))
def load_chats(): return safe_load(CHAT_FILE, [])
def save_chats(ch): CHAT_FILE.write_text(json.dumps(ch, indent=2))
def load_config(): return safe_load(CONFIG_FILE, {})
def save_config(c): CONFIG_FILE.write_text(json.dumps(c, indent=2))
def load_api(): return safe_load(API_FILE, {})
def save_api(a): API_FILE.write_text(json.dumps(a, indent=2))
def load_log(): return safe_load(LOG_FILE, [])
def save_log(l): LOG_FILE.write_text(json.dumps(l, indent=2))

TRENDING_100 = ["AI Agent Automation 2026","Instagram Viral Reels Mastery","YouTube Automation with AI","No-Code Automation N8N+Zapier+Make","Prompt Engineering Pro","Data Analytics with AI Tools","Digital Marketing SEO 2026","Canva + CapCut Pro Mastery","Cybersecurity Job Ready","AI Voice Cloning & Video","Affiliate Marketing with AI","Dropshipping 3.0","Facebook Ads 2026","Google Ads & Programmatic","Personal Branding on LinkedIn","WhatsApp Marketing Automation","Meme Marketing","Podcast Launch Pro","AI Resume & LinkedIn Viral","AI Tools for Business - 100 Tools","ChatGPT Freelancing","Python + AI Basics","Full Stack Web Dev AI","AWS Cloud Practitioner","Google Data Analytics","UX/UI Design AI","Business Finance","Stock Market with AI","Crypto Trading Basics","Video Editing Masterclass","AI Photo Editing","AI Music Creation","AI Reels Maker","AI Chatbot for Shop","AI for Students","AI for Teachers","AI for Doctors","AI Legal Assistant","AI Content Writing","AI E-commerce","Instagram Growth 0 to 1M","YouTube Shorts Monetization","LinkedIn Growth Hack","Twitter Viral","Email Marketing Pro","SEO Advanced","Content Marketing","Influencer Marketing","Brand Building","Online Store Shopify","Meesho Selling Mastery","Amazon FBA","Flipkart Seller","Etsy Handloom Selling","Boutique Business","Embroidery Design","Fashion Designing","Beauty Parlour Course","Cooking Masterclass","Yoga Instructor","Fitness Trainer","Meditation Course","Spoken English","Public Speaking","Interview Preparation","MS Excel Advanced","Tally + GST","Digital Banking","Insurance Agent Pro","Real Estate Mastery","Photography Pro","Videography","Graphic Design","3D Animation","Game Development","App Development No-Code","WordPress Mastery","Blogger to Pro","Quora Marketing","Reddit Viral","Telegram Channel Growth","Discord Community","Notion Productivity","Canva Template Selling","Prompt Selling","AI Art Selling","Voice Over Artist","Translation Business","Freelancing Fiverr+Upwork","Agency Building","Startup Funding","Business Plan Writing","Lead Generation","Customer Support Automation","CRM Mastery","HR Management","Project Management","Time Management","Sales Closing","Negotiation Skills","Mindset Mastery","Motivation Course","Parenting Course","Relationship Coaching","Career Counselling","Study Hacks","Exam Preparation","UPSC Strategy","SSC CGL Prep","Bank PO Prep"]

def create_course(topic, price, cid):
    mods=[{"m":m,"title":f"Module {m}: {topic} - 40 Videos","videos":[{"v":v,"title":f"{topic} M{m}V{v}","dur":"7:00","text":f"# {topic} M{m}V{v}","pdf":f"PDF","audio_hi":f"Audio","audio_en":f"Audio","video_file":f"Video"} for v in range(1,41)]} for m in range(1,11)]
    return {"id":cid,"topic":topic,"modules":mods,"total_videos":400,"total_hours":"46 Hours","price":price,"created":str(datetime.datetime.now())}

courses=load_courses()
if len(courses) < 100:
    ex=[c.get("topic","") for c in courses]
    for idx, t in enumerate(TRENDING_100):
        if t in ex: continue
        cid=f"BRAHMA{1000+idx}"; courses.append(create_course(t, 999 + (idx%5)*100, cid)); save_courses(courses)
        if len(courses)>=100: break

if "admin_logged" not in st.session_state: st.session_state["admin_logged"]=False
st.sidebar.title("🧠 Brahma Super Brain")

if not MASTER_HASH.exists():
    np=st.sidebar.text_input("Admin Password Banao", type="password")
    if st.sidebar.button("Admin Banao", type="primary"):
        if np and len(np)>=4: MASTER_HASH.write_text(hashlib.sha256(np.encode()).hexdigest()); st.rerun()
        else: st.sidebar.error("4 akshar se bada banao")
    menu=st.sidebar.radio("CUSTOMER", ["📚 Browse Courses","🔑 My Access","🤖 Chatbot"])
elif not st.session_state["admin_logged"]:
    menu=st.sidebar.radio("CUSTOMER", ["📚 Browse Courses","🔑 My Access","🤖 Chatbot"])
    st.sidebar.divider()
    st.sidebar.caption("🔒 Admin Area")
    mp=st.sidebar.text_input("Admin Password", type="password")
    if st.sidebar.button("Admin Login"):
        if hashlib.sha256(mp.encode()).hexdigest()==MASTER_HASH.read_text():
            st.session_state["admin_logged"]=True; st.rerun()
        else: st.sidebar.error("Galat Password")
else:
    st.sidebar.success("✅ Admin - Super Agent Active")
    menu=st.sidebar.radio("ADMIN SUPER AGENT", ["🧠 Dashboard","📚 Courses","🌐 UPI QR Setup","🔌 API & Social Integration","🚀 Super Brain Auto Agent","📈 Marketing & SEO Auto","📊 Sales + Google Sheet + Invoice + Download","🏦 Banking"])
    if st.sidebar.button("Logout"): st.session_state["admin_logged"]=False; st.rerun()

purchases=load_purchases(); chats=load_chats(); config=load_config(); api_config=load_api(); logs=load_log()

if st.session_state["admin_logged"]:
    if menu=="🧠 Dashboard":
        c1,c2,c3,c4=st.columns(4)
        c1.metric("Courses",len(courses)); c2.metric("Videos",len(courses)*400); c3.metric("Hours",f"{len(courses)*46}H"); c4.metric("Sales",len(purchases))
        st.subheader("Course Download - Yahan se sara data download karo")
        try:
            course_csv=io.StringIO()
            w=csv.DictWriter(course_csv, fieldnames=["id","topic","price","total_videos","total_hours"])
            w.writeheader()
            for c in courses:
                w.writerow({"id": c.get("id",""), "topic": c.get("topic",""), "price": c.get("price",999), "total_videos": c.get("total_videos",400), "total_hours": c.get("total_hours","46 Hours")})
            st.download_button("📚 DOWNLOAD ALL 100 COURSES DATA - CSV", course_csv.getvalue(), file_name="all_100_courses.csv", type="primary")
        except Exception as e:
            st.error(f"Fix: {e}")
            if st.button("Fix Courses"): COURSES_FILE.unlink(missing_ok=True); st.rerun()
        try: st.dataframe(pd.DataFrame([{"No":i+1,"Course":c.get("topic",""),"Price":c.get("price",999)} for i,c in enumerate(courses)]), use_container_width=True)
        except: st.write(f"{len(courses)} courses ready")

    if menu=="🌐 UPI QR Setup":
        st.header("🌐 UPI QR Setup - Admin Only - CODING KE ANDAR")
        st.info(f"Backend UPI: {MY_UPI_ID} - Name: {MY_NAME}")
        
        # NEW: UPLOAD INSIDE CODING - NO GITHUB NEEDED
        st.subheader("📤 Yahan se QR Upload Karo - GitHub ki zarurat nahi")
        uploaded_qr = st.file_uploader("Apna UPI QR JPG Upload Karo (Parveen Kumar wala)", type=["jpg","jpeg","png"], key="upi_uploader_v9")
        if uploaded_qr is not None:
            try:
                UPI_QR_PATH.write_bytes(uploaded_qr.getvalue())
                st.success("✅ QR Code Save Ho Gaya! Ab Customer ko dikhega!")
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
        
        st.divider()
        if UPI_QR_PATH.exists():
            st.success("✅ QR Code Active Hai - Customer ko dikh raha hai")
            st.image(str(UPI_QR_PATH), width=350, caption=f"{MY_NAME} - {MY_UPI_ID}")
            if st.button("🗑️ QR Delete Karo"):
                UPI_QR_PATH.unlink(missing_ok=True); st.rerun()
        else:
            st.warning("⚠️ Abhi koi QR upload nahi hai - Upar se upload karo")
            st.info("Aapne jo QR bheja hai (parveen39179@okicici) wahi yahan upload karo - Fir sab jagah dikhega")

    # Baaki menus same as V8 (API, Super Brain, etc.) - Yahan chhota kiya hai
    if menu=="📊 Sales + Google Sheet + Invoice + Download":
        st.header("📊 Sales Data")
        if purchases:
            st.dataframe(pd.DataFrame(purchases), use_container_width=True)
            csv_buf=io.StringIO()
            all_keys=set()
            for p in purchases: all_keys.update(p.keys())
            all_keys=list(all_keys)
            writer=csv.DictWriter(csv_buf, fieldnames=all_keys); writer.writeheader(); writer.writerows(purchases)
            st.download_button("📊 DOWNLOAD CSV", csv_buf.getvalue(), file_name=f"sales_{datetime.date.today()}.csv", type="primary")
        else: st.info("No sales yet")

else:
    if menu=="📚 Browse Courses":
        st.title("📚 100+ World Class Courses")
        for i,c in enumerate(courses[:20]):
            with st.expander(f"{i+1}. {c.get('topic','')} - ₹{c.get('price',999)} - 400 Videos", expanded=False):
                col1,col2=st.columns(2)
                with col1:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH), width=220, caption=f"Pay ₹{c.get('price',999)} - {MY_NAME}")
                    else:
                        st.info(f"UPI: {MY_UPI_ID}")
                with col2:
                    params={"pa":MY_UPI_ID,"pn":MY_NAME,"am":str(c.get('price',999)),"cu":"INR","tn":c.get('topic','')[:20]}
                    upi_link=f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"📱 Secure UPI Pay ₹{c.get('price',999)}", upi_link, type="primary", use_container_width=True)
                with st.form(f"buy_{c.get('id',i)}", clear_on_submit=False):
                    c1,c2=st.columns(2)
                    with c1: name=st.text_input("Full Name*", key=f"n_{c.get('id',i)}"); email=st.text_input("Email*", key=f"e_{c.get('id',i)}"); phone=st.text_input("Phone*", key=f"p_{c.get('id',i)}")
                    with c2: whatsapp=st.text_input("WhatsApp*", key=f"w_{c.get('id',i)}"); city=st.text_input("City*", key=f"city_{c.get('id',i)}"); utr=st.text_input("UTR*", key=f"utr_{c.get('id',i)}")
                    submit=st.form_submit_button(f"✅ Get Access - ₹{c.get('price',999)}", type="primary", use_container_width=True)
                    if submit:
                        if not name or not email or not utr: st.error("❌ Sab bharo + UTR daalo")
                        else:
                            inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"; access_key=f"BRAHMA-{hashlib.sha256((email+c.get('topic','')+inv+utr).encode()).hexdigest()[:12].upper()}"
                            pur={"invoice_no":inv,"access_key":access_key,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":c.get('topic',''),"price":c.get('price',999),"course_id":c.get('id',''),"utr":utr,"upi_id":MY_UPI_ID}
                            purchases.append(pur); save_purchases(purchases)
                            st.balloons(); st.success(f"✅ Invoice: {inv}"); st.code(f"ACCESS KEY: {access_key}")