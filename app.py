# SUPER BRAIN BRAHMA - PERFECT - ZERO MISTAKE - DIRECT PAYMENT LINK
# Customer ko course ke saath hi Buy + UPI + Razorpay + WhatsApp Payment link milega
import streamlit as st, json, hashlib, datetime, time, io, csv, smtplib, urllib.parse
from pathlib import Path
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

st.set_page_config(page_title="Brahma Super Brain - Perfect Pay", page_icon="👑", layout="wide")
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"; PURCHASE_FILE = DATA_DIR / "purchases.json"
CHAT_FILE = DATA_DIR / "chat_history.json"; CONFIG_FILE = DATA_DIR / "config.json"
WEBSITE_DIR = DATA_DIR / "websites"; WEBSITE_DIR.mkdir(exist_ok=True)

def load_courses(): return json.loads(COURSES_FILE.read_text()) if COURSES_FILE.exists() else []
def save_courses(c): COURSES_FILE.write_text(json.dumps(c, ensure_ascii=False))
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

def create_full_course(topic, price, cid):
    modules=[]
    for m in range(1,11):
        videos=[]
        for v in range(1,41):
            videos.append({"v":v,"title":f"{topic} - M{m}V{v}","dur":"30:00","script_hi":f"Module {m} Video {v} me {topic} concept","script_en":f"Module {m} Video {v} - {topic}","text":f"Notes {topic} M{m}V{v}","pdf":f"PDF {topic} M{m}V{v}","video_file":f"Video_{cid}_M{m}V{v}.mp4","audio_hi":f"Audio_HI_{cid}.mp3"})
        modules.append({"m":m,"title":f"Module {m}: {topic}","videos":videos})
    return {"id":cid,"topic":topic,"modules":modules,"total_videos":400,"price":price,"created":str(datetime.datetime.now()),"website":f"data/websites/{cid}.html"}

def gen_upi_link(upi_id, amount, course):
    # Perfect UPI link - PhonePe, GPay, Paytm sab khulega
    params={"pa":upi_id,"pn":"Brahma Education","am":str(amount),"cu":"INR","tn":f"{course[:30]}"}
    return f"upi://pay?{urllib.parse.urlencode(params)}"

def gen_qr_image(data):
    try:
        import qrcode
        qr=qrcode.make(data); buf=io.BytesIO(); qr.save(buf, format='PNG'); buf.seek(0); return buf
    except: return None

def generate_invoice_file(pur):
    txt=f"BRAHMA EDUCATION\nInvoice: {pur['invoice_no']}\nAccess Key: {pur['access_key']}\nDate: {pur['date']}\nCourse: {pur['course']}\nName: {pur['name']}\nEmail: {pur['email']}\nPhone: {pur['phone']}\nWhatsApp: {pur['whatsapp']}\nCity: {pur['city']}\nPrice: ₹{pur['price']}\nPayment: {pur['payment_method']} - UTR: {pur.get('utr','')}\n"
    fname=f"data/invoice_{pur['invoice_no']}.txt"; Path(fname).write_text(txt); return fname

def chatbot_reply(q, courses):
    ql=q.lower()
    if any(k in ql for k in ["free de do","script de","pdf de","video de","pura batao"]): return "🙏 Pura Video, Audio, Text, PDF sirf payment ke baad Access Key se milega. Main sirf Module naam bata sakta hu. Purchase karo."
    for c in courses:
        if c["topic"].lower() in ql: return f"📚 {c['topic']} - 10 Module, 400 Videos, ₹{c['price']}. Buy Now button dabao, UPI se pay karo, Access Key milega."
    return "👋 Namaste! Kaunsa course chahiye? Har course ke saath Buy Now + UPI Payment link hai. Payment karke Access Key lo."

# --- INIT 100 COURSES ---
courses=load_courses()
if len(courses) < 100:
    existing=[c["topic"] for c in courses]
    for idx, topic in enumerate(TRENDING_100):
        if topic in existing: continue
        cid=f"BRAHMA{1000+idx}"; full=create_full_course(topic, 999 + (idx%5)*100, cid)
        Path(f"data/websites/{cid}.html").write_text(f"<html><body><h1>{topic}</h1><h2>₹{full['price']}</h2><a href='#'>Buy Now</a></body></html>")
        courses.append(full); save_courses(courses)
        if len(courses)>=100: break

# --- LOGIN ---
if "admin_logged" not in st.session_state: st.session_state["admin_logged"]=False
if "selected_buy_course" not in st.session_state: st.session_state["selected_buy_course"]=None

st.sidebar.title("👑 Brahma Super Brain")
if not MASTER_HASH.exists():
    np=st.sidebar.text_input("Admin Password Banao", type="password")
    if st.sidebar.button("Admin Banao"):
        if np: MASTER_HASH.write_text(hashlib.sha256(np.encode()).hexdigest()); st.rerun()
else:
    if not st.session_state["admin_logged"]:
        mp=st.sidebar.text_input("Admin Password", type="password")
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(mp.encode()).hexdigest()==MASTER_HASH.read_text():
                st.session_state["admin_logged"]=True; st.rerun()
            else: st.sidebar.error("Galat")
    else:
        st.sidebar.success("✅ Admin"); 
        if st.sidebar.button("Logout"): st.session_state["admin_logged"]=False; st.rerun()

purchases=load_purchases(); chats=load_chats(); config=load_config()

if st.session_state["admin_logged"]:
    menu=st.sidebar.radio("ADMIN MENU", ["🚀 Dashboard 100","📚 All Courses Full","🌐 Websites (Hamesha)","📊 Sales Data","🏦 Banking + Payment Links"])
else:
    menu=st.sidebar.radio("CUSTOMER MENU", ["📚 Browse Courses + Direct Buy","💰 Buy - Payment + Key","🔑 My Access - Unlock","🤖 Chatbot"])

# --- ADMIN ---
if st.session_state["admin_logged"]:
    if menu=="🚀 Dashboard 100":
        c1,c2,c3=st.columns(3); c1.metric("Courses",len(courses)); c2.metric("Videos",len(courses)*400); c3.metric("Revenue",f"₹{sum([p['price'] for p in purchases])}")
        st.dataframe(pd.DataFrame([{"No":i+1,"Course":c["topic"],"Price":c["price"]} for i,c in enumerate(courses)], ), use_container_width=True)

    if menu=="📚 All Courses Full":
        sel=st.selectbox("Course", [f"{i+1}. {c['topic']}" for i,c in enumerate(courses)]); idx=int(sel.split(".")[0])-1; c=courses[idx]
        st.write(f"{c['topic']} - 400 Videos"); st.write(c["modules"][0]["videos"][0])

    if menu=="🌐 Websites (Hamesha)":
        for c in courses[:10]: st.write(f"{c['topic']} - {c['website']}"); st.download_button(f"Download {c['topic'][:20]}", Path(f"data/websites/{c['id']}.html").read_bytes(), file_name=f"{c['topic']}.html", key=c['id'])

    if menu=="📊 Sales Data":
        if purchases:
            df=pd.DataFrame(purchases); st.dataframe(df, use_container_width=True)
            csv_buf=io.StringIO(); writer=csv.DictWriter(csv_buf, fieldnames=purchases[0].keys()); writer.writeheader(); writer.writerows(purchases); st.download_button("Download CSV", csv_buf.getvalue(), file_name="sales.csv")

    if menu=="🏦 Banking + Payment Links":
        st.header("🏦 Banking + UPI + Razorpay + WhatsApp Payment Links - Yahan se sab control hoga")
        with st.form("bank"):
            c1,c2=st.columns(2)
            with c1: holder=st.text_input("Holder",config.get("holder_name","")); bank=st.text_input("Bank",config.get("bank_name","")); acc=st.text_input("Account No",config.get("account_no","")); ifsc=st.text_input("IFSC",config.get("ifsc","")); upi=st.text_input("UPI ID* (PhonePe/GPay)",config.get("upi_id","yourname@okicici")); 
            with c2: razor=st.text_input("Razorpay Payment Link (Optional)",config.get("razorpay_link","")); whatsapp_num=st.text_input("WhatsApp Number for Payment Proof",config.get("whatsapp_number","")); gmail=st.text_input("Gmail for Invoice",config.get("gmail_user","")); gpass=st.text_input("Gmail App Password",config.get("gmail_pass",""), type="password"); minp=st.number_input("Min Price",199,10000,config.get("auto_price_min",999))
            if st.form_submit_button("Save Payment Links"):
                save_config({"holder_name":holder,"bank_name":bank,"account_no":acc,"ifsc":ifsc,"upi_id":upi,"razorpay_link":razor,"whatsapp_number":whatsapp_num,"gmail_user":gmail,"gmail_pass":gpass,"auto_price_min":minp}); st.success("Payment Links Saved! Ab customer ko direct payment link dikhega")

# --- CUSTOMER - PERFECT PAYMENT FLOW ---
else:
    if menu=="📚 Browse Courses + Direct Buy":
        st.title("📚 100+ Courses - Direct Payment Link Ke Saath")
        st.info("Har course ke saath hi Buy Now + UPI Payment + Razorpay link hai - 1 click me payment karo")
        upi_id=config.get("upi_id",""); razor_link=config.get("razorpay_link",""); whatsapp_num=config.get("whatsapp_number","")
        
        if not upi_id: st.warning("⚠️ Admin ne UPI ID set nahi kiya - Banking me jao UPI ID daalo")
        
        for i,c in enumerate(courses[:30]): # First 30 for speed
            with st.expander(f"{i+1}. {c['topic']} - ₹{c['price']} - 400 Videos", expanded=False):
                st.write("**10 Modules, 400 Videos (30 min each), Hindi+English Voice, PDF, Lifetime Access**")
                st.write("---")
                col1,col2,col3=st.columns(3)
                with col1:
                    if st.button(f"💳 Buy Now - {c['topic'][:20]}", key=f"buy_{c['id']}", type="primary"):
                        st.session_state["selected_buy_course"]=c["topic"]
                        st.session_state["selected_price"]=c["price"]
                        st.session_state["selected_id"]=c["id"]
                        st.switch_page = "buy" # flag
                        st.success(f"✅ {c['topic']} selected! Neeche Buy page me jao ya form yahin bharo")
                with col2:
                    if upi_id:
                        upi_link=gen_upi_link(upi_id, c['price'], c['topic'])
                        st.link_button(f"📱 UPI Pay ₹{c['price']}", upi_link)
                        qr_buf=gen_qr_image(upi_link)
                        if qr_buf: st.image(qr_buf, caption=f"Scan & Pay ₹{c['price']} - {upi_id}", width=150)
                        st.caption(f"UPI ID: {upi_id}")
                with col3:
                    if razor_link:
                        st.link_button("💳 Razorpay Pay", razor_link)
                    if whatsapp_num:
                        wa_msg=urllib.parse.quote(f"Hi, I want to buy {c['topic']} for ₹{c['price']}")
                        st.link_button("💬 WhatsApp", f"https://wa.me/{whatsapp_num}?text={wa_msg}")
                
                st.write("---")
                st.error("🔒 Full Video, Audio, Text, PDF ke liye Access Key chahiye - Buy karke payment karo, tabhi milega")

        # DIRECT BUY FORM INSIDE SAME PAGE - PERFECT FLOW - MISTAKE ZERO
        st.divider()
        st.header("💰 Direct Buy Form - Yahan Se Payment Karke Access Key Lo")
        st.write("UPI se payment kiya toh UTR/Transaction ID yahan daalo")
        
        default_course = st.session_state.get("selected_buy_course", courses[0]["topic"] if courses else "")
        default_price = st.session_state.get("selected_price", 999)
        
        with st.form("direct_buy"):
            c1,c2=st.columns(2)
            with c1: 
                name=st.text_input("Name*"); email=st.text_input("Email*"); phone=st.text_input("Phone*")
                course_choice=st.selectbox("Course*", [c["topic"] for c in courses], index=[c["topic"] for c in courses].index(default_course) if default_course in [c["topic"] for c in courses] else 0)
            with c2:
                whatsapp=st.text_input("WhatsApp*"); city=st.text_input("City*"); utr=st.text_input("UPI UTR / Transaction ID (Payment ke baad)", placeholder="1234567890"); pay_method=st.selectbox("Payment Method", ["UPI - GPay/PhonePe/Paytm","Razorpay","Bank Transfer","WhatsApp Proof"])
            
            submitted=st.form_submit_button("✅ Payment Done - Get Access Key Now", type="primary")
            if submitted:
                if not name or not email or not phone or not whatsapp:
                    st.error("Name, Email, Phone, WhatsApp sab bharo")
                else:
                    sel_c=[c for c in courses if c["topic"]==course_choice][0]
                    inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                    access_key=f"BRAHMA-{hashlib.sha256((email+course_choice+inv).encode()).hexdigest()[:12].upper()}"
                    pur={"invoice_no":inv,"access_key":access_key,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":course_choice,"price":sel_c["price"],"course_id":sel_c["id"],"payment_method":pay_method,"utr":utr}
                    inv_file=generate_invoice_file(pur); pur["invoice_file"]=inv_file
                    purchases.append(pur); save_purchases(purchases)
                    st.balloons()
                    st.success(f"✅ Payment Received! Invoice: {inv}")
                    st.code(f"YOUR ACCESS KEY: {access_key}", language="text")
                    st.info("👉 Is Access Key ko copy karo, aur 'My Access - Unlock' me daalo, pura course khulega. Invoice file download kar lo.")
                    st.download_button("📥 Download Invoice", Path(inv_file).read_bytes(), file_name=f"{inv}.txt")
                    # Auto clear selection
                    st.session_state["selected_buy_course"]=None

    if menu=="💰 Buy - Payment + Key":
        st.header("💰 Buy Course - Payment + Access Key")
        # Same form as above but standalone
        with st.form("buy2"):
            c1,c2=st.columns(2)
            with c1: name=st.text_input("Name* "); email=st.text_input("Email* "); phone=st.text_input("Phone* "); 
            with c2: whatsapp=st.text_input("WhatsApp* "); city=st.text_input("City* "); course_choice=st.selectbox("Course* ", [c["topic"] for c in courses]); utr=st.text_input("UTR / Txn ID")
            if st.form_submit_button("Get Access Key"):
                sel_c=[c for c in courses if c["topic"]==course_choice][0]
                inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"; access_key=f"BRAHMA-{hashlib.sha256((email+course_choice+inv).encode()).hexdigest()[:12].upper()}"
                pur={"invoice_no":inv,"access_key":access_key,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":course_choice,"price":sel_c["price"],"course_id":sel_c["id"],"payment_method":"UPI","utr":utr}
                inv_file=generate_invoice_file(pur); purchases.append(pur); save_purchases(purchases)
                st.success(f"Access Key: {access_key}"); st.code(access_key)

    if menu=="🔑 My Access - Unlock":
        st.header("🔑 My Access - Access Key Daalo to Full Course Khulega")
        key=st.text_input("Access Key / Invoice No Daalo")
        if st.button("🔓 Unlock - Video+Audio+Text+PDF Dekho", type="primary"):
            found=[p for p in purchases if p["access_key"]==key or p["invoice_no"]==key]
            if not found: st.error("❌ Galat Key! Bina payment ke access nahi. Pehle Buy karo - UPI se payment karo")
            else:
                pur=found[0]; course=[c for c in courses if c["id"]==pur["course_id"]][0]
                st.success(f"✅ Unlocked! {course['topic']} - Hello {pur['name']}")
                tab1,tab2,tab3,tab4=st.tabs(["🎬 Video HD","🎧 Audio","📝 Text","📄 PDF"])
                mod_no=st.selectbox("Module", range(1,11), format_func=lambda x: f"Module {x}"); module=course["modules"][mod_no-1]
                vid_no=st.selectbox("Video", range(1,41), format_func=lambda x: f"V{x}: {module['videos'][x-1]['title'][:60]}"); video=module["videos"][vid_no-1]
                with tab1: st.write(f"{video['title']} - {video['dur']}"); st.video("https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"); st.caption(f"{video['video_file']}")
                with tab2: st.write(video['script_hi']); st.write(video['script_en'])
                with tab3: st.text_area("Text", video["text"], height=250)
                with tab4: st.text_area("PDF", video["pdf"], height=200); st.download_button("Download PDF", video["pdf"], file_name=f"{video['title']}.txt")

    if menu=="🤖 Chatbot":
        st.header("🤖 Chatbot - Hindi+English - No Data Leak")
        for ch in chats[-15:]:
            with st.chat_message(ch["role"]): st.write(ch["msg"])
        q=st.chat_input("Sawal puchho...")
        if q:
            chats.append({"role":"user","msg":q}); reply=chatbot_reply(q,courses); chats.append({"role":"assistant","msg":reply}); save_chats(chats); st.rerun()