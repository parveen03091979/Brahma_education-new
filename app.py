import streamlit as st, json, hashlib, datetime, time, io, csv, re
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Brahma Super Agent - Paid Access System", page_icon="👑", layout="wide")
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"; PURCHASE_FILE = DATA_DIR / "purchases.json"
CHAT_FILE = DATA_DIR / "chat_history.json"; CONFIG_FILE = DATA_DIR / "config.json"
WEBSITE_DIR = DATA_DIR / "websites"; WEBSITE_DIR.mkdir(exist_ok=True)

def load_courses(): return json.loads(COURSES_FILE.read_text()) if COURSES_FILE.exists() else []
def save_courses(c): COURSES_FILE.write_text(json.dumps(c, indent=2))
def load_purchases(): return json.loads(PURCHASE_FILE.read_text()) if PURCHASE_FILE.exists() else []
def save_purchases(p): PURCHASE_FILE.write_text(json.dumps(p, indent=2))
def load_chats(): return json.loads(CHAT_FILE.read_text()) if CHAT_FILE.exists() else []
def save_chats(ch): CHAT_FILE.write_text(json.dumps(ch, indent=2))
def load_config(): return json.loads(CONFIG_FILE.read_text()) if CONFIG_FILE.exists() else {}
def save_config(c): CONFIG_FILE.write_text(json.dumps(c, indent=2))

TRENDING_100 = [
"AI Agent Automation 2026","Instagram Viral Reels Mastery","YouTube Automation with AI","No-Code Automation N8N+Zapier+Make","Prompt Engineering Pro","Data Analytics with AI Tools","Digital Marketing SEO 2026","Canva + CapCut Pro Mastery","Cybersecurity Job Ready","AI Voice Cloning & Video",
"Affiliate Marketing with AI","Dropshipping 3.0","Facebook Ads 2026","Google Ads & Programmatic","Personal Branding on LinkedIn","WhatsApp Marketing Automation","Meme Marketing","Podcast Launch Pro","AI Resume & LinkedIn Viral","AI Tools for Business - 100 Tools",
"ChatGPT Freelancing","Python + AI Basics","Full Stack Web Dev AI","AWS Cloud Practitioner","Google Data Analytics","UX/UI Design AI","Business Finance","Stock Market with AI","Crypto Trading Basics","Video Editing Masterclass",
"AI Photo Editing","AI Music Creation","AI Reels Maker","AI Chatbot for Shop","AI for Students","AI for Teachers","AI for Doctors","AI Legal Assistant","AI Content Writing","AI E-commerce",
"Instagram Growth 0 to 1M","YouTube Shorts Monetization","LinkedIn Growth Hack","Twitter Viral","Email Marketing Pro","SEO Advanced","Content Marketing","Influencer Marketing","Brand Building","Online Store Shopify",
"Meesho Selling Mastery","Amazon FBA","Flipkart Seller","Etsy Handloom Selling","Boutique Business","Embroidery Design","Fashion Designing","Beauty Parlour Course","Cooking Masterclass","Yoga Instructor",
"Fitness Trainer","Meditation Course","Spoken English","Public Speaking","Interview Preparation","MS Excel Advanced","Tally + GST","Digital Banking","Insurance Agent Pro","Real Estate Mastery",
"Photography Pro","Videography","Graphic Design","3D Animation","Game Development","App Development No-Code","WordPress Mastery","Blogger to Pro","Quora Marketing","Reddit Viral",
"Telegram Channel Growth","Discord Community","Notion Productivity","Canva Template Selling","Prompt Selling","AI Art Selling","Voice Over Artist","Translation Business","Freelancing Fiverr+Upwork","Agency Building",
"Startup Funding","Business Plan Writing","Lead Generation","Customer Support Automation","CRM Mastery","HR Management","Project Management","Time Management","Sales Closing","Negotiation Skills",
"Mindset Mastery","Motivation Course","Parenting Course","Relationship Coaching","Career Counselling","Study Hacks","Exam Preparation","UPSC Strategy","SSC CGL Prep","Bank PO Prep"
]

def create_full_course(topic, price):
    modules=[]
    for m in range(1,11):
        videos=[]
        for v in range(1,41):
            title=f"{topic} - M{m}V{v}"
            script_hi=f"Module {m} Video {v} me {topic} ka concept. 30 min detail."
            script_en=f"Module {m} Video {v} - {topic} concept {m}.{v} - 30 min"
            text_content=f"# {title}\nDuration 30 Min\nNotes for {topic} M{m}V{v}\nFull detailed content here..."
            pdf_content=f"PDF {topic} M{m}V{v} - Notes, Checklist"
            videos.append({"v":v,"title":title,"dur":"30:00","script_hi":script_hi,"script_en":script_en,"text":text_content,"pdf":pdf_content})
        modules.append({"m":m,"title":f"Module {m}: {topic} - Part {m}","videos":videos})
    cid=datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(abs(hash(topic))%1000)
    return {"id":cid,"topic":topic,"modules":modules,"total_videos":400,"price":price,"created":str(datetime.datetime.now())}

def chatbot_reply(q, courses):
    ql=q.lower()
    if any(k in ql for k in ["free de do","script de","pdf de","video de","pura batao","download free"]):
        return "🙏 Pura Video, Audio, Text, PDF sirf payment ke baad Access Key se milega. Bina payment ke nahi milega."
    for c in courses:
        if c["topic"].lower() in ql:
            return f"📚 {c['topic']} me 10 Module, 400 Videos (30 min each). Price ₹{c['price']}. Purchase karke Access Key lo, tabhi pura content khulega."
    return "👋 Namaste! Kaunsa course chahiye? Price aur module bata dunga. Pura content ke liye payment karke Access Key lena padega."

# --- STATE ---
courses=load_courses(); purchases=load_purchases(); chats=load_chats(); config=load_config()

# --- SIDEBAR - ADMIN LOGIN ALAG, CUSTOMER ALAG ---
st.sidebar.title("👑 Brahma Education")
st.sidebar.caption("Customer ko bina payment ke course nahi milega")

# Admin Login Logic
if "admin_logged" not in st.session_state: st.session_state["admin_logged"]=False

if not MASTER_HASH.exists():
    st.sidebar.subheader("🔐 Admin - Pehli Baar Password Banao (Sirf Aapke Liye)")
    np=st.sidebar.text_input("Admin Master Password Banao", type="password", key="np")
    if st.sidebar.button("Admin Lock Lagao"):
        if np: MASTER_HASH.write_text(hashlib.sha256(np.encode()).hexdigest()); st.sidebar.success("Admin ban gaya! Ab login karo"); st.rerun()
else:
    if not st.session_state["admin_logged"]:
        st.sidebar.subheader("🔐 Admin Login (Course Banane Ke Liye)")
        mp=st.sidebar.text_input("Admin Password", type="password")
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(mp.encode()).hexdigest()==MASTER_HASH.read_text():
                st.session_state["admin_logged"]=True; st.rerun()
            else: st.sidebar.error("Galat Password")
    else:
        st.sidebar.success("✅ Admin Logged In")
        if st.sidebar.button("Admin Logout"): st.session_state["admin_logged"]=False; st.rerun()

# --- MENU - 2 TYPE ---
if st.session_state["admin_logged"]:
    menu=st.sidebar.radio("ADMIN MENU - Super Agent", ["🚀 Dashboard - 100 Auto Generate","🔍 Trend Hunter (100)","🎬 HD Factory - Guide Karo","📚 All Courses (Admin View)","📊 Purchase Data","🏦 Banking"])
else:
    menu=st.sidebar.radio("CUSTOMER MENU - Paid Access Only", ["📚 Browse Courses (Free Teaser)","🤖 Chatbot - Sawal Puchho","💰 Buy Course - Access Key Lo","🔑 My Course Access - Key Daalo","🌐 Free Website Links"])

# --- ADMIN PAGES ---
if st.session_state["admin_logged"]:
    if menu=="🚀 Dashboard - 100 Auto Generate":
        st.title("🚀 Super AI - Admin - 100 Courses Auto Robotic")
        c1,c2,c3=st.columns(3); c1.metric("Courses",len(courses)); c2.metric("Sales",len(purchases)); c3.metric("Revenue",f"₹{sum([p['price'] for p in purchases])}")
        st.divider()
        st.subheader("🤖 Ek Click Me 100 Course Banao - Video+Audio+Text+PDF")
        price=st.number_input("Price Set Karo",500,5000,config.get("auto_price_min",999))
        if st.button("🚀 100 COURSES AUTO GENERATE - ROBOTIC", type="primary"):
            prog=st.progress(0)
            for i,topic in enumerate(TRENDING_100):
                if any(c["topic"]==topic for c in courses): prog.progress((i+1)/100); continue
                new_c=create_full_course(topic, price); courses.append(new_c); save_courses(courses); prog.progress((i+1)/100)
            st.success("100 Courses Ban Gaye!"); st.balloons()

    if menu=="🔍 Trend Hunter (100)":
        st.header("🔍 100 Trending - Preloaded"); st.dataframe(pd.DataFrame(TRENDING_100, columns=["Trending 100"]), use_container_width=True)
        sel=st.selectbox("Guide Karo", TRENDING_100)
        if st.button(f"Guide {sel}"): st.session_state["to_build"]=sel; st.success("HD Factory me jao")

    if menu=="🎬 HD Factory - Guide Karo":
        st.header("🎬 HD Factory - Admin Guide"); topic=st.text_input("Topic", value=st.session_state.get("to_build","")); price=st.number_input("Price",500,5000,999)
        if st.button("PURA COURSE BANAO - 10x40x30min", type="primary"):
            if topic:
                new_c=create_full_course(topic, price); Path(f"data/websites/{new_c['id']}.html").write_text(f"<h1>{topic}</h1>"); new_c["website"]=f"data/websites/{new_c['id']}.html"; courses.append(new_c); save_courses(courses); st.success("Ban gaya!")

    if menu=="📚 All Courses (Admin View)":
        st.header("📚 Admin - All Courses Full View"); 
        for c in courses: st.write(f"{c['topic']} - {c['total_videos']} Videos - ₹{c['price']}")

    if menu=="📊 Purchase Data":
        if purchases:
            df=pd.DataFrame(purchases); st.dataframe(df, use_container_width=True)
            csv_buf=io.StringIO(); writer=csv.DictWriter(csv_buf, fieldnames=purchases[0].keys()); writer.writeheader(); writer.writerows(purchases); st.download_button("Download All Data CSV", csv_buf.getvalue(), file_name="all_sales.csv")
        else: st.warning("No sales")

    if menu=="🏦 Banking":
        with st.form("b"):
            holder=st.text_input("Holder",config.get("holder_name","")); bank=st.text_input("Bank",config.get("bank_name","")); acc=st.text_input("Acc",config.get("account_no","")); upi=st.text_input("UPI",config.get("upi_id","")); minp=st.number_input("Min Price",199,10000,config.get("auto_price_min",999)); maxp=st.number_input("Max Price",499,20000,config.get("auto_price_max",2999))
            if st.form_submit_button("Save"): save_config({"holder_name":holder,"bank_name":bank,"account_no":acc,"upi_id":upi,"auto_price_min":minp,"auto_price_max":maxp}); st.success("Saved")

# --- CUSTOMER PAGES - PAID ONLY ---
else:
    if menu=="📚 Browse Courses (Free Teaser)":
        st.title("📚 100+ Courses - Brahma Education")
        st.warning("⚠️ Note: Video, Audio, Text, PDF dekhne ke liye pehle Buy karo, Access Key milega. Bina Key ke sirf teaser dikhega.")
        if not courses: st.info("Admin abhi courses bana raha hai - thodi der me aayenge")
        else:
            for c in courses[:20]:
                with st.expander(f"{c['topic']} - ₹{c['price']} - 400 Videos"):
                    st.write(f"**10 Modules, 400 Videos (30 min each)**")
                    st.write(f"Modules: Module 1 to Module 10")
                    st.write("❌ Full Video/Audio/Text/PDF ke liye Access Key chahiye. Buy karo.")
        if len(courses)>20: st.write(f"+ {len(courses)-20} aur courses hain...")

    if menu=="🤖 Chatbot - Sawal Puchho":
        st.header("🤖 Chatbot - Legal Safe"); st.caption("Pura content nahi batayega, sirf teaser")
        for ch in chats[-15:]:
            with st.chat_message(ch["role"]): st.write(ch["msg"])
        q=st.chat_input("Sawal puchho...")
        if q:
            chats.append({"role":"user","msg":q}); reply=chatbot_reply(q,courses); chats.append({"role":"assistant","msg":reply}); save_chats(chats); st.rerun()

    if menu=="💰 Buy Course - Access Key Lo":
        st.header("💰 Course Kharido - Access Key Milega")
        st.write("Payment ke baad aapko ek Secret Access Key (Invoice No) milega. Usi se course khulega.")
        if not courses: st.warning("Abhi course nahi hai")
        else:
            with st.form("buy"):
                c1,c2=st.columns(2)
                with c1: name=st.text_input("Name*"); email=st.text_input("Email*"); phone=st.text_input("Phone*")
                with c2: whatsapp=st.text_input("WhatsApp*"); city=st.text_input("City"); csel=st.selectbox("Course*",[c["topic"] for c in courses])
                submit=st.form_submit_button("💳 Payment Kiya - Access Key Banao", type="primary")
                if submit:
                    if not name or not email or not phone: st.error("Name, Email, Phone bharo")
                    else:
                        sel_c=[c for c in courses if c["topic"]==csel][0]
                        inv=f"BRAHMA{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                        access_key=f"{inv}-{hashlib.sha256((email+csel).encode()).hexdigest()[:8].upper()}"
                        pur={"invoice_no":inv,"access_key":access_key,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":csel,"price":sel_c["price"],"course_id":sel_c["id"]}
                        purchases.append(pur); save_purchases(purchases)
                        st.success(f"✅ Payment Success! Aapka Access Key: {access_key}")
                        st.info(f"Invoice No: {inv} - Ye key copy kar lo. 'My Course Access' me daalo to pura course khulega.")
                        st.code(access_key, language="text")

    if menu=="🔑 My Course Access - Key Daalo":
        st.header("🔑 My Course Access - Access Key Daalo")
        st.write("Payment ke baad jo Access Key mila tha, yahan daalo. Tabhi Video+Audio+Text+PDF khulega.")
        key_input=st.text_input("Access Key / Invoice No Daalo", placeholder="BRAHMA2025...")
        if st.button("🔓 Course Unlock Karo"):
            found=[p for p in purchases if p["access_key"]==key_input or p["invoice_no"]==key_input]
            if not found: st.error("❌ Galat Key! Bina payment ke access nahi milega. Pehle Buy karo.")
            else:
                pur=found[0]; course=[c for c in courses if c["id"]==pur["course_id"]]
                if not course: st.error("Course nahi mila")
                else:
                    c=course[0]; st.success(f"✅ Access Granted! Course: {c['topic']}")
                    tab1,tab2,tab3,tab4=st.tabs(["🎬 Video","🎧 Audio","📝 Text","📄 PDF"])
                    mod_sel=st.selectbox("Module",[f"Module {m['m']}" for m in c["modules"]])
                    m_no=int(mod_sel.split()[1]); module=c["modules"][m_no-1]
                    v_sel=st.selectbox("Video",[f"V{v['v']}: {v['title'][:60]}" for v in module["videos"]])
                    v_no=int(v_sel.split()[1]); video=module["videos"][v_no-1]
                    with tab1: st.write(f"**{video['title']} - {video['dur']}**"); st.video("https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"); st.caption("HD Video - Super AI Generated")
                    with tab2: st.write(f"Hindi Script: {video['script_hi']}"); st.write(f"English Script: {video['script_en']}"); st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/gettysburg.wav")
                    with tab3: st.text_area("Full Text Notes", video["text"], height=300)
                    with tab4: st.text_area("PDF Content", video["pdf"], height=300); st.download_button("Download PDF", video["pdf"], file_name=f"{video['title']}.txt")

    if menu=="🌐 Free Website Links":
        st.header("🌐 Free Websites"); 
        if not courses: st.warning("No website yet")
        else:
            for c in courses[:10]: st.write(f"{c['topic']} - Website: data/websites/{c['id']}.html")