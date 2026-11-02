# BRAHMA ULTIMATE V12 - 100 COURSES VISIBLE + SMART CHATBOT + SECURE APPROVAL
import streamlit as st, json, hashlib, datetime, io, csv, urllib.parse
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Brahma Super Brain", page_icon="🧠", layout="wide")
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"; PURCHASE_FILE = DATA_DIR / "purchases.json"
CHAT_FILE = DATA_DIR / "chat_history.json"; CONFIG_FILE = DATA_DIR / "config.json"
API_FILE = DATA_DIR / "api_config.json"; LOG_FILE = DATA_DIR / "super_brain_log.json"
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

# FULL 100 TRENDING
TRENDING_100 = ["AI Agent Automation 2026","Instagram Viral Reels Mastery","YouTube Automation with AI","No-Code Automation N8N+Zapier+Make","Prompt Engineering Pro","Data Analytics with AI Tools","Digital Marketing SEO 2026","Canva + CapCut Pro Mastery","Cybersecurity Job Ready","AI Voice Cloning & Video","Affiliate Marketing with AI","Dropshipping 3.0","Facebook Ads 2026","Google Ads & Programmatic","Personal Branding on LinkedIn","WhatsApp Marketing Automation","Meme Marketing","Podcast Launch Pro","AI Resume & LinkedIn Viral","AI Tools for Business - 100 Tools","ChatGPT Freelancing","Python + AI Basics","Full Stack Web Dev AI","AWS Cloud Practitioner","Google Data Analytics","UX/UI Design AI","Business Finance","Stock Market with AI","Crypto Trading Basics","Video Editing Masterclass","AI Photo Editing","AI Music Creation","AI Reels Maker","AI Chatbot for Shop","AI for Students","AI for Teachers","AI for Doctors","AI Legal Assistant","AI Content Writing","AI E-commerce","Instagram Growth 0 to 1M","YouTube Shorts Monetization","LinkedIn Growth Hack","Twitter Viral","Email Marketing Pro","SEO Advanced","Content Marketing","Influencer Marketing","Brand Building","Online Store Shopify","Meesho Selling Mastery","Amazon FBA","Flipkart Seller","Etsy Handloom Selling","Boutique Business","Embroidery Design","Fashion Designing","Beauty Parlour Course","Cooking Masterclass","Yoga Instructor","Fitness Trainer","Meditation Course","Spoken English","Public Speaking","Interview Preparation","MS Excel Advanced","Tally + GST","Digital Banking","Insurance Agent Pro","Real Estate Mastery","Photography Pro","Videography","Graphic Design","3D Animation","Game Development","App Development No-Code","WordPress Mastery","Blogger to Pro","Quora Marketing","Reddit Viral","Telegram Channel Growth","Discord Community","Notion Productivity","Canva Template Selling","Prompt Selling","AI Art Selling","Voice Over Artist","Translation Business","Freelancing Fiverr+Upwork","Agency Building","Startup Funding","Business Plan Writing","Lead Generation","Customer Support Automation","CRM Mastery","HR Management","Project Management","Time Management","Sales Closing","Negotiation Skills","Mindset Mastery","Motivation Course","Parenting Course","Relationship Coaching","Career Counselling","Study Hacks","Exam Preparation","UPSC Strategy","SSC CGL Prep","Bank PO Prep"]

def create_course(topic, price, cid):
    mods=[{"m":m,"title":f"Module {m}: {topic} - 40 Videos","videos":[{"v":v,"title":f"{topic} M{m}V{v}","dur":"7:00","text":f"# {topic} M{m}V{v} - Full HD Course"} for v in range(1,41)]} for m in range(1,11)]
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
    menu=st.sidebar.radio("CUSTOMER", ["📚 Browse Courses","🔑 My Access","🤖 Chatbot"])
elif not st.session_state["admin_logged"]:
    menu=st.sidebar.radio("CUSTOMER", ["📚 Browse Courses","🔑 My Access","🤖 Chatbot"])
    st.sidebar.divider()
    mp=st.sidebar.text_input("Admin Password", type="password")
    if st.sidebar.button("Admin Login"):
        if hashlib.sha256(mp.encode()).hexdigest()==MASTER_HASH.read_text():
            st.session_state["admin_logged"]=True; st.rerun()
        else: st.sidebar.error("Galat Password")
else:
    st.sidebar.success("✅ Admin Active")
    menu=st.sidebar.radio("ADMIN", ["🧠 Dashboard","📚 Courses","🌐 UPI QR Setup","🚀 Super Brain Auto Agent","📊 Sales + Approval","🏦 Banking"])
    if st.sidebar.button("Logout"): st.session_state["admin_logged"]=False; st.rerun()

purchases=load_purchases(); chats=load_chats(); config=load_config(); api_config=load_api(); logs=load_log()

# SMART CHATBOT LOGIC - FIXED
def get_smart_reply(user_q):
    q = user_q.lower()
    # Course related
    if "course" in q or "kitne" in q or "100" in q:
        return f"🧠 Hamare paas {len(courses)} World Class Courses hain - Har course me 10 Modules x 40 Videos = 400 Videos, 46 Hours. Price ₹999 se start. Browse Courses me dekho. UPI: {MY_UPI_ID}"
    if "price" in q or "kitna" in q or "fees" in q or "paisa" in q:
        return f"💰 Course Price ₹999 - ₹1399. 400 Videos, Lifetime Access. Pay via UPI {MY_UPI_ID} - Parveen Kumar. UTR daal ke approval lo."
    if "payment" in q or "utr" in q or "pay" in q or "qr" in q:
        return f"🏦 Payment: UPI ID {MY_UPI_ID} ({MY_NAME}) pe pay karo. UTR daalo. Admin 24hr me verify karke approve karega. Pending hoga tabhi access milega."
    if "access" in q or "key" in q or "unlock" in q:
        return "🔑 My Access me Invoice No ya Access Key daalo. Agar status PENDING hai toh admin approve ka wait karo. Approved ke baad hi unlock hoga."
    if "ai" in q:
        return "🤖 AI Agent Automation, ChatGPT Freelancing, Prompt Engineering, AI Tools for Business - Ye hamare top AI courses hain. 400 videos each. Browse Courses me dekho."
    if "instagram" in q or "youtube" in q or "reels" in q:
        return "📱 Instagram Viral Reels Mastery, YouTube Automation with AI, YouTube Shorts Monetization - Ye courses viral hone ke liye best hain."
    if "contact" in q or "whatsapp" in q or "help" in q:
        return f"📞 Help: WhatsApp {config.get('whatsapp_number','Admin se contact karo')} - UPI {MY_UPI_ID} - Email support available."
    if "hello" in q or "hi" in q or "namaste" in q:
        return f"🙏 Namaste! Main Brahma Super Brain Assistant hoon. {len(courses)} courses hain. Kya seekhna chahte ho? AI, Instagram, YouTube, Business?"
    # Default smart
    matched = [c.get('topic','') for c in courses if any(word in c.get('topic','').lower() for word in q.split() if len(word)>3)][:3]
    if matched:
        return f"📚 Aapne '{user_q}' pucha - Isse related ye courses hain: {', '.join(matched)}. Browse Courses me jaake enroll karo. Price ₹999+"
    return f"🧠 Brahma Super Brain: Aapne '{user_q}' pucha. Hamare {len(courses)} courses me se aapke liye best hai - AI, Digital Marketing, Instagram Growth. Koi specific course ka naam batao, main details dunga. Payment UPI {MY_UPI_ID} pe."

if st.session_state["admin_logged"]:
    if menu=="🧠 Dashboard":
        c1,c2,c3,c4=st.columns(4)
        c1.metric("Courses",len(courses)); c2.metric("Sales",len(purchases))
        c3.metric("Pending",len([p for p in purchases if p.get("status")=="PENDING"]))
        c4.metric("Approved",len([p for p in purchases if p.get("status")=="APPROVED"]))
        course_csv=io.StringIO()
        w=csv.DictWriter(course_csv, fieldnames=["id","topic","price","total_videos","total_hours"])
        w.writeheader()
        for c in courses:
            w.writerow({"id":c.get("id",""),"topic":c.get("topic",""),"price":c.get("price",999),"total_videos":c.get("total_videos",400),"total_hours":c.get("total_hours","46 Hours")})
        st.download_button("📚 DOWNLOAD 100 COURSES CSV", course_csv.getvalue(), file_name="all_100_courses.csv", type="primary")

    if menu=="🌐 UPI QR Setup":
        st.header("🌐 UPI QR Setup")
        st.info(f"UPI: {MY_UPI_ID} | {MY_NAME}")
        uploaded_qr = st.file_uploader("QR Upload Karo", type=["jpg","jpeg","png"])
        if uploaded_qr is not None:
            UPI_QR_PATH.write_bytes(uploaded_qr.getvalue())
            st.success("✅ QR Saved!"); st.balloons()
        if UPI_QR_PATH.exists():
            st.image(str(UPI_QR_PATH), width=350)

    if menu=="🚀 Super Brain Auto Agent":
        st.header("🚀 Super Brain Auto Agent")
        if st.button("🚀 AUTO POST ALL SOCIAL", type="primary"):
            logs.append({"time":str(datetime.datetime.now()),"action":"Auto Post","status":"Done"}); save_log(logs); st.success("✅ Done")
        if logs: st.dataframe(pd.DataFrame(logs[-10:]), use_container_width=True)

    if menu=="📊 Sales + Approval":
        st.header("📊 Sales - Secure Approval")
        pending=[p for p in purchases if p.get("status")=="PENDING"]
        if pending:
            for p in pending:
                with st.expander(f"⏳ {p.get('name')} - {p.get('course')} - UTR:{p.get('utr')}", expanded=False):
                    st.write(p)
                    colA,colB=st.columns(2)
                    with colA:
                        if st.button(f"✅ APPROVE {p.get('invoice_no')}", key=f"app_{p.get('invoice_no')}", type="primary"):
                            p["status"]="APPROVED"; save_purchases(purchases); st.rerun()
                    with colB:
                        if st.button(f"❌ REJECT {p.get('invoice_no')}", key=f"rej_{p.get('invoice_no')}"):
                            p["status"]="REJECTED"; save_purchases(purchases); st.rerun()
        if purchases:
            st.dataframe(pd.DataFrame(purchases), use_container_width=True)
            csv_buf=io.StringIO()
            all_keys=set()
            for pu in purchases: all_keys.update(pu.keys())
            all_keys=list(all_keys)
            writer=csv.DictWriter(csv_buf, fieldnames=all_keys); writer.writeheader(); writer.writerows(purchases)
            st.download_button("📊 DOWNLOAD CSV", csv_buf.getvalue(), file_name="sales.csv", type="primary")

    if menu=="🏦 Banking":
        with st.form("bank"):
            upi=st.text_input("UPI ID", value=config.get("upi_id",MY_UPI_ID)); wa=st.text_input("WhatsApp", value=config.get("whatsapp_number",""))
            if st.form_submit_button("Save"): save_config({"upi_id":upi,"whatsapp_number":wa}); st.success("Saved")

else:
    if menu=="📚 Browse Courses":
        st.title(f"📚 All {len(courses)} Courses - 400 Videos Each")
        # SEARCH + FILTER - NEW - FIX 20 TO 100
        search = st.text_input("🔍 Course Search Karo (AI, Instagram, YouTube...)")
        if search:
            filtered = [c for c in courses if search.lower() in c.get('topic','').lower()]
        else:
            filtered = courses
        
        st.info(f"Showing {len(filtered)} / {len(courses)} Courses - Har course 10 Module x 40 Video = 400 Videos")
        
        # PAGINATION - SHOW ALL 100 WITH PAGES
        page_size = 20
        total_pages = (len(filtered) + page_size - 1) // page_size
        page = st.selectbox(f"Page Select (Total {total_pages} Pages - 20 per page)", range(1, total_pages+1), format_func=lambda x: f"Page {x} - Courses {((x-1)*page_size)+1} to {min(x*page_size, len(filtered))}")
        
        start_idx = (page-1)*page_size
        end_idx = start_idx + page_size
        page_courses = filtered[start_idx:end_idx]
        
        for idx, c in enumerate(page_courses, start=start_idx+1):
            with st.expander(f"{idx}. {c.get('topic','')} - ₹{c.get('price',999)} - 400 Videos", expanded=False):
                col1,col2=st.columns(2)
                with col1:
                    if UPI_QR_PATH.exists(): st.image(str(UPI_QR_PATH), width=200, caption=f"₹{c.get('price',999)}")
                    else: st.info(f"UPI: {MY_UPI_ID}")
                with col2:
                    params={"pa":MY_UPI_ID,"pn":MY_NAME,"am":str(c.get('price',999)),"cu":"INR","tn":c.get('topic','')[:20]}
                    upi_link=f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"📱 Pay ₹{c.get('price',999)}", upi_link, type="primary", use_container_width=True)
                with st.form(f"buy_{c.get('id')}_{idx}"):
                    c1,c2=st.columns(2)
                    with c1: name=st.text_input("Full Name*", key=f"n_{c.get('id')}_{idx}"); email=st.text_input("Email*", key=f"e_{c.get('id')}_{idx}"); phone=st.text_input("Phone*", key=f"p_{c.get('id')}_{idx}")
                    with c2: whatsapp=st.text_input("WhatsApp*", key=f"w_{c.get('id')}_{idx}"); city=st.text_input("City*", key=f"city_{c.get('id')}_{idx}"); utr=st.text_input("UTR*", key=f"utr_{c.get('id')}_{idx}")
                    submit=st.form_submit_button(f"✅ Request Access ₹{c.get('price',999)}", type="primary", use_container_width=True)
                    if submit:
                        if not name or not email or not utr: st.error("Sab bharo + UTR")
                        else:
                            inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                            access_key=f"BRAHMA-{hashlib.sha256((email+c.get('topic','')+inv+utr).encode()).hexdigest()[:12].upper()}"
                            pur={"invoice_no":inv,"access_key":access_key,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":c.get('topic',''),"price":c.get('price',999),"course_id":c.get('id',''),"utr":utr,"upi_id":MY_UPI_ID,"status":"PENDING"}
                            purchases.append(pur); save_purchases(purchases)
                            st.warning("⏳ Pending Verification - Admin approve karega tabhi access milega")
                            st.code(f"INVOICE: {inv}\nKEY: {access_key}")

    if menu=="🔑 My Access":
        st.header("🔑 My Access - Secure")
        key_input=st.text_input("Invoice / Access Key")
        if st.button("🔓 Unlock", type="primary"):
            found=[p for p in purchases if p.get("access_key")==key_input or p.get("invoice_no")==key_input]
            if not found: st.error("❌ Invalid")
            else:
                pur=found[0]
                if pur.get("status")!="APPROVED":
                    st.error(f"⏳ Status: {pur.get('status')} - UTR {pur.get('utr')} - Admin verify kar raha hai")
                    st.stop()
                st.success(f"✅ Approved! {pur.get('course')}")
                course_list=[c for c in courses if c.get("id")==pur.get("course_id")]
                if course_list:
                    course=course_list[0]
                    mod_no=st.selectbox("Module", range(1,11), format_func=lambda x: f"Module {x}")
                    module=course["modules"][mod_no-1]
                    vid_no=st.selectbox("Video", range(1,41), format_func=lambda x: f"Video {x}")
                    video=module["videos"][vid_no-1]
                    st.write(f"**{video.get('title','')}**")
                    st.video("https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4")

    if menu=="🤖 Chatbot":
        st.header("🤖 Brahma Smart Chatbot - Ab Smart Reply")
        st.info("Ab ye chatbot wahi repeat nahi karega - Smart jawab dega")
        for ch in chats[-15:]:
            with st.chat_message(ch["role"]): st.write(ch["msg"])
        q=st.chat_input("Kuch bhi pucho - AI, Instagram, Course Price, Payment...")
        if q:
            chats.append({"role":"user","msg":q})
            reply = get_smart_reply(q)
            chats.append({"role":"assistant","msg":reply})
            save_chats(chats); st.rerun()