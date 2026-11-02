# BRAHMA ULTIMATE V11 SECURE - PENDING APPROVAL - NO FREE COURSE
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

TRENDING_100 = ["AI Agent Automation 2026","Instagram Viral Reels Mastery","YouTube Automation with AI","No-Code Automation N8N+Zapier+Make","Prompt Engineering Pro","Data Analytics with AI Tools","Digital Marketing SEO 2026","Canva + CapCut Pro Mastery","Cybersecurity Job Ready","AI Voice Cloning & Video"]

def create_course(topic, price, cid):
    mods=[{"m":m,"title":f"Module {m}: {topic} - 40 Videos","videos":[{"v":v,"title":f"{topic} M{m}V{v}","dur":"7:00","text":f"# {topic} M{m}V{v}","pdf":f"PDF"} for v in range(1,41)]} for m in range(1,11)]
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

if st.session_state["admin_logged"]:
    if menu=="🧠 Dashboard":
        c1,c2,c3,c4=st.columns(4)
        c1.metric("Courses",len(courses)); c2.metric("Sales",len(purchases))
        c3.metric("Pending",len([p for p in purchases if p.get("status")=="PENDING"]))
        c4.metric("Approved",len([p for p in purchases if p.get("status")=="APPROVED"]))
        st.subheader("Course Data Download")
        course_csv=io.StringIO()
        w=csv.DictWriter(course_csv, fieldnames=["id","topic","price","total_videos","total_hours"])
        w.writeheader()
        for c in courses:
            w.writerow({"id":c.get("id",""),"topic":c.get("topic",""),"price":c.get("price",999),"total_videos":c.get("total_videos",400),"total_hours":c.get("total_hours","46 Hours")})
        st.download_button("📚 DOWNLOAD COURSES CSV", course_csv.getvalue(), file_name="courses.csv", type="primary")

    if menu=="🌐 UPI QR Setup":
        st.header("🌐 UPI QR Setup - Upload Inside Code")
        st.info(f"UPI: {MY_UPI_ID} | {MY_NAME}")
        uploaded_qr = st.file_uploader("QR Upload Karo (JPG/PNG)", type=["jpg","jpeg","png"])
        if uploaded_qr is not None:
            UPI_QR_PATH.write_bytes(uploaded_qr.getvalue())
            st.success("✅ QR Saved!"); st.balloons()
        if UPI_QR_PATH.exists():
            st.image(str(UPI_QR_PATH), width=350, caption=f"{MY_NAME} - {MY_UPI_ID}")
            if st.button("Delete QR"): UPI_QR_PATH.unlink(missing_ok=True); st.rerun()
        else:
            st.warning("QR upload nahi hai")

    if menu=="🚀 Super Brain Auto Agent":
        st.header("🚀 Super Brain Auto Agent")
        col1,col2=st.columns(2)
        with col1:
            if st.button("🚀 AUTO POST ALL SOCIAL", type="primary", use_container_width=True):
                logs.append({"time":str(datetime.datetime.now()),"action":"Auto Post","status":"Done"}); save_log(logs); st.success("✅ Posts Ready - Demo Mode (API daaloge tabhi asli post)")
        with col2:
            if st.button("🎬 AUTO REELS", type="primary", use_container_width=True):
                logs.append({"time":str(datetime.datetime.now()),"action":"Reels","status":"Done"}); save_log(logs); st.success("✅ Reels Ready")
        if logs: st.dataframe(pd.DataFrame(logs[-10:]), use_container_width=True)

    if menu=="📊 Sales + Approval":
        st.header("📊 Sales - SECURE APPROVAL SYSTEM")
        pending=[p for p in purchases if p.get("status")=="PENDING"]
        approved=[p for p in purchases if p.get("status")=="APPROVED"]
        c1,c2,c3=st.columns(3)
        c1.metric("⏳ Pending",len(pending)); c2.metric("✅ Approved",len(approved)); c3.metric("Total",len(purchases))
        
        if pending:
            st.subheader("⏳ Pending - Inko Check Karke Approve Karo - Nahi toh Free me Le Jayenge")
            for p in pending:
                with st.expander(f"⏳ {p.get('name')} - {p.get('course')} - ₹{p.get('price')} - UTR:{p.get('utr')}", expanded=False):
                    st.write(f"Name: {p.get('name')} | Email: {p.get('email')} | Phone: {p.get('phone')} | WhatsApp: {p.get('whatsapp')}")
                    st.write(f"Course: {p.get('course')} | Invoice: {p.get('invoice_no')} | Date: {p.get('date')}")
                    st.code(f"UTR: {p.get('utr')} - Isko GPay/PhonePe/ICICI App me search karo - ₹{p.get('price')} aaya kya?")
                    colA,colB=st.columns(2)
                    with colA:
                        if st.button(f"✅ APPROVE {p.get('invoice_no')}", key=f"app_{p.get('invoice_no')}", type="primary"):
                            p["status"]="APPROVED"; p["approved_date"]=str(datetime.datetime.now()); save_purchases(purchases); st.success("Approved!"); st.rerun()
                    with colB:
                        if st.button(f"❌ REJECT {p.get('invoice_no')}", key=f"rej_{p.get('invoice_no')}"):
                            p["status"]="REJECTED"; save_purchases(purchases); st.error("Rejected"); st.rerun()
        else:
            st.success("Koi pending nahi")
        
        st.divider()
        if purchases:
            st.subheader("All Sales Data")
            st.dataframe(pd.DataFrame(purchases), use_container_width=True)
            csv_buf=io.StringIO()
            all_keys=set()
            for pu in purchases: all_keys.update(pu.keys())
            all_keys=list(all_keys)
            writer=csv.DictWriter(csv_buf, fieldnames=all_keys); writer.writeheader(); writer.writerows(purchases)
            st.download_button("📊 DOWNLOAD SALES CSV", csv_buf.getvalue(), file_name="sales.csv", type="primary")

    if menu=="🏦 Banking":
        with st.form("bank"):
            upi=st.text_input("UPI ID", value=config.get("upi_id",MY_UPI_ID)); wa=st.text_input("WhatsApp", value=config.get("whatsapp_number",""))
            if st.form_submit_button("Save"): save_config({"upi_id":upi,"whatsapp_number":wa}); st.success("Saved")

else:
    if menu=="📚 Browse Courses":
        st.title("📚 Courses")
        for i,c in enumerate(courses[:20]):
            with st.expander(f"{i+1}. {c.get('topic','')} - ₹{c.get('price',999)}", expanded=False):
                col1,col2=st.columns(2)
                with col1:
                    if UPI_QR_PATH.exists(): st.image(str(UPI_QR_PATH), width=220, caption=f"Pay ₹{c.get('price',999)}")
                    else: st.info(f"UPI: {MY_UPI_ID}")
                with col2:
                    params={"pa":MY_UPI_ID,"pn":MY_NAME,"am":str(c.get('price',999)),"cu":"INR","tn":c.get('topic','')[:20]}
                    upi_link=f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"📱 Pay ₹{c.get('price',999)}", upi_link, type="primary", use_container_width=True)
                with st.form(f"buy_{c.get('id',i)}"):
                    c1,c2=st.columns(2)
                    with c1: name=st.text_input("Full Name*", key=f"n_{i}"); email=st.text_input("Email*", key=f"e_{i}"); phone=st.text_input("Phone*", key=f"p_{i}")
                    with c2: whatsapp=st.text_input("WhatsApp*", key=f"w_{i}"); city=st.text_input("City*", key=f"city_{i}"); utr=st.text_input("UTR / Transaction ID* (12 Digit)", key=f"utr_{i}")
                    submit=st.form_submit_button(f"✅ Submit UTR & Request Access", type="primary", use_container_width=True)
                    if submit:
                        if not name or not email or not phone or not whatsapp or not city:
                            st.error("❌ Sab fields bharo")
                        elif not utr or len(utr) < 6:
                            st.error("❌ Sahi UTR daalo - 12 digit")
                        else:
                            inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                            access_key=f"BRAHMA-{hashlib.sha256((email+c.get('topic','')+inv+utr).encode()).hexdigest()[:12].upper()}"
                            pur={"invoice_no":inv,"access_key":access_key,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":c.get('topic',''),"price":c.get('price',999),"course_id":c.get('id',''),"utr":utr,"upi_id":MY_UPI_ID,"status":"PENDING"}
                            purchases.append(pur); save_purchases(purchases)
                            st.warning("⏳ Request Sent - Payment Verification Pending")
                            st.info(f"Invoice: {inv} | UTR: {utr} - Admin 24 hour me verify karke Approve karega - Tabhi Access Key kaam karega")
                            st.code(f"INVOICE: {inv}\nACCESS KEY (After Approval): {access_key}")

    if menu=="🔑 My Access":
        st.header("🔑 My Access - Secure")
        key_input=st.text_input("Invoice No / Access Key Daalo")
        if st.button("🔓 Unlock Course", type="primary"):
            found=[p for p in purchases if p.get("access_key")==key_input or p.get("invoice_no")==key_input]
            if not found:
                st.error("❌ Invalid Invoice / Key")
            else:
                pur=found[0]
                if pur.get("status")!="APPROVED":
                    st.error(f"⏳ Status: {pur.get('status')} - Payment Abhi Verify Nahi Hua")
                    st.warning(f"Aapne UTR {pur.get('utr')} diya tha - Admin check kar raha hai - 24 Hour wait karo ya WhatsApp karo")
                    st.info(f"Invoice: {pur.get('invoice_no')} - Course: {pur.get('course')}")
                else:
                    st.success(f"✅ Approved! Welcome {pur.get('name')} - {pur.get('course')}")
                    course_list=[c for c in courses if c.get("id")==pur.get("course_id")]
                    if not course_list: st.error("Course not found")
                    else:
                        course=course_list[0]
                        mod_no=st.selectbox("Select Module", range(1,11), format_func=lambda x: f"Module {x}")
                        module=course["modules"][mod_no-1]
                        vid_no=st.selectbox("Select Video", range(1,41), format_func=lambda x: f"Video {x}")
                        video=module["videos"][vid_no-1]
                        st.write(f"**{video.get('title','')}**")
                        st.video("https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4")

    if menu=="🤖 Chatbot":
        st.header("🤖 Chatbot")
        for ch in chats[-10:]:
            with st.chat_message(ch["role"]): st.write(ch["msg"])
        q=st.chat_input("Ask...")
        if q:
            chats.append({"role":"user","msg":q}); chats.append({"role":"assistant","msg":f"Answer for {q}"}); save_chats(chats); st.rerun()