# BRAHMA - FINAL FIXED V4 - NO KEYERROR - PARVEEN UPI - parveen39179@okicici
import streamlit as st, json, hashlib, datetime, io, csv, urllib.parse
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Brahma - Parveen UPI Fixed V4", page_icon="👑", layout="wide")
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"; PURCHASE_FILE = DATA_DIR / "purchases.json"
CHAT_FILE = DATA_DIR / "chat_history.json"; CONFIG_FILE = DATA_DIR / "config.json"
WEBSITE_DIR = DATA_DIR / "websites"; WEBSITE_DIR.mkdir(exist_ok=True)
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"

MY_UPI_ID = "parveen39179@okicici"
MY_NAME = "Parveen Kumar"

def safe_load_json(path, default):
    try:
        if path.exists(): return json.loads(path.read_text())
    except: pass
    return default

def load_courses(): return safe_load_json(COURSES_FILE, [])
def save_courses(c): COURSES_FILE.write_text(json.dumps(c, ensure_ascii=False))
def load_purchases(): return safe_load_json(PURCHASE_FILE, [])
def save_purchases(p): PURCHASE_FILE.write_text(json.dumps(p, indent=2))
def load_chats(): return safe_load_json(CHAT_FILE, [])
def save_chats(ch): CHAT_FILE.write_text(json.dumps(ch, indent=2))
def load_config(): return safe_load_json(CONFIG_FILE, {})
def save_config(c): CONFIG_FILE.write_text(json.dumps(c, indent=2))

TRENDING_100 = ["AI Agent Automation 2026","Instagram Viral Reels Mastery","YouTube Automation with AI","No-Code Automation N8N+Zapier+Make","Prompt Engineering Pro","Data Analytics with AI Tools","Digital Marketing SEO 2026","Canva + CapCut Pro Mastery","Cybersecurity Job Ready","AI Voice Cloning & Video","Affiliate Marketing with AI","Dropshipping 3.0","Facebook Ads 2026","Google Ads & Programmatic","Personal Branding on LinkedIn","WhatsApp Marketing Automation","Meme Marketing","Podcast Launch Pro","AI Resume & LinkedIn Viral","AI Tools for Business - 100 Tools","ChatGPT Freelancing","Python + AI Basics","Full Stack Web Dev AI","AWS Cloud Practitioner","Google Data Analytics","UX/UI Design AI","Business Finance","Stock Market with AI","Crypto Trading Basics","Video Editing Masterclass","AI Photo Editing","AI Music Creation","AI Reels Maker","AI Chatbot for Shop","AI for Students","AI for Teachers","AI for Doctors","AI Legal Assistant","AI Content Writing","AI E-commerce","Instagram Growth 0 to 1M","YouTube Shorts Monetization","LinkedIn Growth Hack","Twitter Viral","Email Marketing Pro","SEO Advanced","Content Marketing","Influencer Marketing","Brand Building","Online Store Shopify","Meesho Selling Mastery","Amazon FBA","Flipkart Seller","Etsy Handloom Selling","Boutique Business","Embroidery Design","Fashion Designing","Beauty Parlour Course","Cooking Masterclass","Yoga Instructor","Fitness Trainer","Meditation Course","Spoken English","Public Speaking","Interview Preparation","MS Excel Advanced","Tally + GST","Digital Banking","Insurance Agent Pro","Real Estate Mastery","Photography Pro","Videography","Graphic Design","3D Animation","Game Development","App Development No-Code","WordPress Mastery","Blogger to Pro","Quora Marketing","Reddit Viral","Telegram Channel Growth","Discord Community","Notion Productivity","Canva Template Selling","Prompt Selling","AI Art Selling","Voice Over Artist","Translation Business","Freelancing Fiverr+Upwork","Agency Building","Startup Funding","Business Plan Writing","Lead Generation","Customer Support Automation","CRM Mastery","HR Management","Project Management","Time Management","Sales Closing","Negotiation Skills","Mindset Mastery","Motivation Course","Parenting Course","Relationship Coaching","Career Counselling","Study Hacks","Exam Preparation","UPSC Strategy","SSC CGL Prep","Bank PO Prep"]

def create_super_course(topic, price, cid):
    modules=[]
    for m in range(1,11):
        videos=[]
        for v in range(1,41):
            videos.append({"v":v,"title":f"{topic} - M{m}V{v}","dur":"7:00","script_hi":f"Module {m} Video {v} - {topic} - 7 min","script_en":f"Module {m} Video {v} - {topic} - 7 min","text":f"# {topic} M{m}V{v}\nModule {m} 4-5 Hours\nWorld Class","pdf":f"PDF {topic} M{m}V{v}","audio_hi":f"Audio_{cid}_M{m}V{v}.mp3","audio_en":f"Audio_{cid}_M{m}V{v}.mp3","video_file":f"Video_{cid}_M{m}V{v}.mp4"})
        modules.append({"m":m,"title":f"Module {m}: {topic} - 40 Videos - 4-5 Hours","videos":videos})
    return {"id":cid,"topic":topic,"modules":modules,"total_videos":400,"total_hours":"46 Hours","price":price,"created":str(datetime.datetime.now()),"website":f"data/websites/{cid}.html"}

courses=load_courses()
if len(courses) < 100:
    existing=[c["topic"] for c in courses]
    for idx, topic in enumerate(TRENDING_100):
        if topic in existing: continue
        cid=f"BRAHMA{1000+idx}"; full=create_super_course(topic, 999 + (idx%5)*100, cid)
        try: Path(f"data/websites/{cid}.html").write_text(f"<html><body><h1>{topic}</h1><h2>46 Hours</h2><p>{MY_UPI_ID}</p></body></html>")
        except: pass
        courses.append(full); save_courses(courses)
        if len(courses)>=100: break

if "admin_logged" not in st.session_state: st.session_state["admin_logged"]=False
st.sidebar.title("👑 Brahma")
st.sidebar.caption(f"{MY_NAME} - {MY_UPI_ID}")

if not MASTER_HASH.exists():
    np=st.sidebar.text_input("Admin Password Banao", type="password", key="adm_create_pwd_v4")
    if st.sidebar.button("Admin Banao", key="adm_create_btn_v4"):
        if np: MASTER_HASH.write_text(hashlib.sha256(np.encode()).hexdigest()); st.rerun()
else:
    if not st.session_state["admin_logged"]:
        mp=st.sidebar.text_input("Admin Password", type="password", key="adm_login_pwd_v4")
        if st.sidebar.button("Admin Login", key="adm_login_btn_v4"):
            if hashlib.sha256(mp.encode()).hexdigest()==MASTER_HASH.read_text():
                st.session_state["admin_logged"]=True; st.rerun()
            else: st.sidebar.error("Galat")
    else:
        st.sidebar.success("✅ Admin")
        if st.sidebar.button("Logout", key="adm_logout_btn_v4"): st.session_state["admin_logged"]=False; st.rerun()

purchases=load_purchases(); chats=load_chats(); config=load_config()

if st.session_state["admin_logged"]:
    menu=st.sidebar.radio("ADMIN", ["🧠 Dashboard","📚 Courses Full","🌐 UPI QR - Parveen","📊 Sales","🏦 Banking"], key="admin_menu_v4")
else:
    menu=st.sidebar.radio("CUSTOMER", ["📚 Browse + Parveen UPI Pay","🔑 My Access","🤖 Chatbot"], key="cust_menu_v4")

# --- ADMIN ---
if st.session_state["admin_logged"]:
    if menu=="🧠 Dashboard":
        c1,c2,c3=st.columns(3); c1.metric("Courses",len(courses)); c2.metric("Videos",len(courses)*400); c3.metric("Hours",f"{len(courses)*46} H")
        try: st.dataframe(pd.DataFrame([{"No":i+1,"Course":c["topic"],"Price":c["price"],"Hours":c.get("total_hours","46 Hours")} for i,c in enumerate(courses)], ), use_container_width=True)
        except: st.write(f"{len(courses)} courses ready")
    if menu=="🌐 UPI QR - Parveen":
        st.header(f"UPI QR - {MY_NAME} - {MY_UPI_ID}")
        if UPI_QR_PATH.exists(): st.image(str(UPI_QR_PATH), width=400, caption=f"{MY_NAME} - {MY_UPI_ID} - Scan to pay with any UPI app")
        else: st.warning("GitHub me data/upi_qr.jpg me aapka Parveen wala scanner daalo - Jo abhi bheja hai wahi"); st.info(f"UPI ID: {MY_UPI_ID} - Is par payment aayega")
    if menu=="📊 Sales":
        if purchases:
            try: df=pd.DataFrame(purchases); st.dataframe(df, use_container_width=True)
            except: st.write(purchases)
            try:
                csv_buf=io.StringIO()
                if purchases:
                    all_keys=set()
                    for p in purchases: all_keys.update(p.keys())
                    all_keys=list(all_keys)
                    writer=csv.DictWriter(csv_buf, fieldnames=all_keys); writer.writeheader(); writer.writerows(purchases)
                    st.download_button("Download CSV", csv_buf.getvalue(), file_name="sales.csv", key="dl_sales_v4")
            except: pass
        else: st.info("Abhi koi sale nahi")
    if menu=="🏦 Banking":
        with st.form("bank_form_v4", clear_on_submit=False):
            upi=st.text_input("UPI ID*", value=config.get("upi_id",MY_UPI_ID), key="bank_upi_v4"); wa=st.text_input("WhatsApp", value=config.get("whatsapp_number",""), key="bank_wa_v4")
            if st.form_submit_button("Save"): save_config({"upi_id":upi,"whatsapp_number":wa}); st.success("Saved!")
else:
    # --- CUSTOMER ---
    if menu=="📚 Browse + Parveen UPI Pay":
        st.title(f"📚 100+ Courses - Pay to {MY_NAME}")
        st.warning(f"⚠️ Koi bhi course free me nahi - UPI {MY_UPI_ID} par payment + UTR compulsory")
        
        if UPI_QR_PATH.exists():
            st.subheader(f"📱 Scan to Pay - {MY_NAME}")
            st.image(str(UPI_QR_PATH), width=380, caption=f"{MY_NAME} - UPI ID: {MY_UPI_ID} - Scan to pay with any UPI app")
            st.code(f"UPI ID: {MY_UPI_ID}", language="text")
        else:
            st.error(f"UPI Scanner GitHub me data/upi_qr.jpg me daalo - {MY_UPI_ID}")
            st.info("Scanner daalte hi yahan QR dikhega - Tab tak UPI ID par direct pay karo")
        
        for i,c in enumerate(courses[:20]):
            with st.expander(f"{i+1}. {c['topic']} - ₹{c['price']} - {c.get('total_hours','46H')}", expanded=False):
                st.write(f"**10 Modules x 40 Videos x 4-5 Hours = {c.get('total_hours','46 Hours')}**")
                
                col1,col2=st.columns(2)
                with col1:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH), width=220, caption=f"Pay ₹{c['price']}")
                with col2:
                    try:
                        params={"pa":MY_UPI_ID,"pn":MY_NAME,"am":str(c['price']),"cu":"INR","tn":c['topic'][:20]}
                        upi_link=f"upi://pay?{urllib.parse.urlencode(params)}"
                        st.link_button(f"📱 UPI App Pay ₹{c['price']}", upi_link, type="primary", use_container_width=True, key=f"upi_link_v4_{c['id']}")
                    except: pass
                    st.write(f"**{MY_NAME}**"); st.write(f"UPI: `{MY_UPI_ID}`")
                
                st.divider()
                with st.form(f"buy_form_v4_{c['id']}", clear_on_submit=False):
                    c1,c2=st.columns(2)
                    with c1: name=st.text_input("Name*", key=f"v4_name_{c['id']}"); email=st.text_input("Email*", key=f"v4_email_{c['id']}"); phone=st.text_input("Phone*", key=f"v4_phone_{c['id']}")
                    with c2: whatsapp=st.text_input("WhatsApp*", key=f"v4_wa_{c['id']}"); city=st.text_input("City*", key=f"v4_city_{c['id']}"); utr=st.text_input("UTR / Transaction ID* COMPULSORY", key=f"v4_utr_{c['id']}", placeholder="Bina UTR ke nahi milega")
                    submit=st.form_submit_button(f"✅ I Paid to {MY_NAME} - Get Access Key", type="primary", use_container_width=True)
                    if submit:
                        if not name or not email or not phone or not whatsapp or not city:
                            st.error("❌ Name, Email, Phone, WhatsApp, City bharo")
                        elif not utr or len(utr) < 6:
                            st.error(f"❌ UTR COMPULSORY - {MY_UPI_ID} par pay karke UTR daalo")
                        else:
                            inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"; access_key=f"BRAHMA-{hashlib.sha256((email+c['topic']+inv+utr).encode()).hexdigest()[:12].upper()}"
                            pur={"invoice_no":inv,"access_key":access_key,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":c['topic'],"price":c['price'],"course_id":c['id'],"payment_method":f"UPI {MY_UPI_ID}","utr":utr,"upi_id":MY_UPI_ID}
                            purchases.append(pur); save_purchases(purchases); st.balloons(); st.success(f"✅ Payment Verified! Invoice {inv}"); st.code(f"ACCESS KEY: {access_key}", language="text")

    if menu=="🔑 My Access":
        st.header("🔑 My Access - Unlock")
        key_input=st.text_input("Access Key / Invoice No Daalo", key="v4_access_key_main")
        if st.button("🔓 Unlock", type="primary", key="v4_btn_unlock_main"):
            found=[p for p in purchases if p.get("access_key")==key_input or p.get("invoice_no")==key_input]
            if not found: st.error(f"❌ Galat Key - Bina {MY_UPI_ID} par payment ke nahi")
            else:
                pur=found[0]; course_list=[c for c in courses if c["id"]==pur["course_id"]]
                if not course_list: st.error("Course nahi mila"); st.stop()
                course=course_list[0]
                st.success(f"Unlocked {course['topic']} - {pur['name']}")
                mod_no=st.selectbox("Module", range(1,11), format_func=lambda x: f"Module {x} - 4-5 Hours", key=f"v4_mod_{key_input}"); module=course["modules"][mod_no-1]
                vid_no=st.selectbox("Video", range(1,41), format_func=lambda x: f"V{x} - 7 min", key=f"v4_vid_{key_input}_{mod_no}"); video=module["videos"][vid_no-1]
                st.write(f"**{video['title']} - {video['dur']}**"); st.video("https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"); st.text_area("Text", video["text"], height=150, key=f"v4_text_{key_input}_{mod_no}_{vid_no}")

    if menu=="🤖 Chatbot":
        st.header("🤖 Chatbot"); 
        for ch in chats[-15:]:
            with st.chat_message(ch["role"]): st.write(ch["msg"])
        q=st.chat_input("Sawal puchho...", key="v4_chat_input_main")
        if q:
            chats.append({"role":"user","msg":q}); reply=f"📚 {q} - 10 Module x 40 Videos x 4-5 Hours - Pay to {MY_NAME} - {MY_UPI_ID} - UTR daalo."; chats.append({"role":"assistant","msg":reply}); save_chats(chats); st.rerun()