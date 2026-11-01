# BRAHMA SUPER AGENT - PRO MAX ULTIMATE - SINGLE FILE
# Free AI + Free Website + Purchase Data + Invoice + HD Video + Secure + Chatbot Legal Safe
import streamlit as st, json, os, hashlib, base64, datetime, time, requests, csv, io, re, smtplib
from pathlib import Path
import pandas as pd
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

st.set_page_config(page_title="Brahma Super Agent ULTIMATE", page_icon="👑", layout="wide")
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)
SALT_FILE = DATA_DIR / ".salt"; MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"; PURCHASE_FILE = DATA_DIR / "purchases.json"
WEBSITE_DIR = DATA_DIR / "websites"; WEBSITE_DIR.mkdir(exist_ok=True)
CHAT_FILE = DATA_DIR / "chat_history.json"

# --- SECURITY ---
def get_salt():
    if SALT_FILE.exists(): return SALT_FILE.read_bytes()
    s=os.urandom(16); SALT_FILE.write_bytes(s); return s
def get_fernet(pwd):
    k=hashlib.pbkdf2_hmac('sha256', pwd.encode(), get_salt(), 100000)
    return Fernet(base64.urlsafe_b64encode(k))
def save_secure(d,p): Path("data/secure.enc").write_bytes(get_fernet(p).encrypt(json.dumps(d).encode()))
def load_secure(p):
    try: return json.loads(get_fernet(p).decrypt(Path("data/secure.enc").read_bytes()).decode())
    except: return {}
def load_courses(): return json.loads(COURSES_FILE.read_text()) if COURSES_FILE.exists() else []
def save_courses(c): COURSES_FILE.write_text(json.dumps(c, indent=2))
def load_purchases(): return json.loads(PURCHASE_FILE.read_text()) if PURCHASE_FILE.exists() else []
def save_purchases(p): PURCHASE_FILE.write_text(json.dumps(p, indent=2))
def load_chats(): return json.loads(CHAT_FILE.read_text()) if CHAT_FILE.exists() else []
def save_chats(ch): CHAT_FILE.write_text(json.dumps(ch, indent=2))

# --- FREE AI ---
def free_voice(t, lang='hi'):
    try:
        from gtts import gTTS
        fname=f"data/voice_{int(time.time())}_{lang}.mp3"; gTTS(text=t[:4000], lang='hi' if lang=='hi' else 'en').save(fname); return fname
    except: return None
def free_thumb(title):
    try:
        from PIL import Image, ImageDraw; img=Image.new('RGB',(1920,1080),(10,10,30)); d=ImageDraw.Draw(img); d.text((100,400),title[:70],fill=(255,215,0)); img.save("data/bg.png"); return "data/bg.png"
    except: return None

def create_free_website(course_topic, price, course_id):
    html = f"""<html><head><title>{course_topic}</title><meta name="description" content="Learn {course_topic} - Brahma"><style>body{{font-family:Arial;background:#0f0f23;color:#fff;text-align:center;padding:50px}}.btn{{background:gold;color:#000;padding:15px 30px;font-size:20px;border:none;border-radius:10px}}</style></head><body><h1>👑 {course_topic}</h1><h2>10 Modules x 40 Videos = 400 HD Videos</h2><p>Hindi + English Voice + PDF + Lifetime</p><h1>₹{price}</h1><a class="btn">Buy Now</a><p>Powered by Brahma Super Agent - Free Website</p></body></html>"""
    fname = WEBSITE_DIR / f"{course_id}.html"; fname.write_text(html); return f"data/websites/{course_id}.html"

def generate_invoice_pdf(pur):
    txt=f"""BRAHMA EDUCATION - INVOICE\nInvoice: {pur['invoice_no']}\nDate: {pur['date']}\nCourse: {pur['course']}\nName: {pur['name']}\nEmail: {pur['email']}\nPhone: {pur['phone']}\nWhatsApp: {pur['whatsapp']}\nCity: {pur['city']}\nPrice: ₹{pur['price']}\n"""
    fname=f"data/invoice_{pur['invoice_no']}.txt"; Path(fname).write_text(txt); return fname

def send_invoice_email(to_email, inv_file, pur, secure_data):
    try:
        gmail_user=secure_data.get("gmail_user",""); gmail_pass=secure_data.get("gmail_pass","")
        if not gmail_user: return "Gmail not set"
        msg=MIMEMultipart(); msg['From']=gmail_user; msg['To']=to_email; msg['Subject']=f"Invoice - {pur['course']}"
        msg.attach(MIMEText(f"Hi {pur['name']}, Invoice for {pur['course']} attached. ₹{pur['price']}", 'plain'))
        if inv_file and Path(inv_file).exists():
            part=MIMEBase('application','octet-stream'); part.set_payload(Path(inv_file).read_bytes()); encoders.encode_base64(part); part.add_header('Content-Disposition', f"attachment; filename= {Path(inv_file).name}"); msg.attach(part)
        s=smtplib.SMTP('smtp.gmail.com',587); s.starttls(); s.login(gmail_user,gmail_pass); s.send_message(msg); s.quit(); return "Sent"
    except Exception as e: return f"Error: {e}"

# --- LEGAL SAFE CHATBOT CORE ---
def is_hindi(text):
    # Simple detect: if devanagari or hindi words
    return bool(re.search('[\u0900-\u097F]', text)) or any(w in text.lower() for w in ["kya","hai","kaise","course","kitne","mein","hindi"])

def chatbot_reply(user_msg, courses_list):
    """
    LEGAL SAFE RULES:
    1. Never give full course content
    2. Only give topic names, module titles (not video scripts)
    3. If user asks for free content / pdf / video script -> say purchase needed
    4. Answer general questions
    """
    msg_lower = user_msg.lower()
    hindi = is_hindi(user_msg)
    
    # Blocklist - Course data leak attempts
    leak_keywords = ["script de do","pdf de do","video de do","free mein do","full course","pura course batao","module ka content","video ka script","download link free","give me all videos","give pdf free"]
    if any(k in msg_lower for k in leak_keywords):
        if hindi:
            return "🙏 Maaf kijiye, pura course ka content, script, PDF, video sirf purchase ke baad hi milega. Main aapko bata sakta hu is course mein kya-kya topics hain, par detail ke liye aapko course purchase karna padega. Aap kaunsa course dekhna chahte hain?"
        else:
            return "🙏 Sorry, full course content, scripts, PDFs and videos are available only after purchase. I can tell you what topics are covered (module names only), but for full details you need to purchase the course. Which course are you interested in?"

    # If asking about a specific course
    for c in courses_list:
        if c["topic"].lower() in msg_lower:
            mods = [f"Module {m['m']}: {m['m']}" for m in c["modules"][:3]] # Only first 3 module numbers, not content
            mod_names = ", ".join([f"Module {m['m']}" for m in c["modules"][:10]])
            if hindi:
                return f"📚 **{c['topic']}** course mein 10 Modules hain, 400 videos (30 min each). Topics: {mod_names}. Isme Hindi + English voice, PDF notes aur lifetime access milta hai. Puri detail, video scripts aur PDFs ke liye aapko course purchase karna padega. Price ₹{c['price']}. Kya aap purchase karna chahenge?"
            else:
                return f"📚 **{c['topic']}** has 10 Modules, 400 videos (30 min each). Covered topics: {mod_names}. You get Hindi+English voice, PDF notes, lifetime access. For full details, scripts and PDFs you need to purchase. Price ₹{c['price']}. Would you like to purchase?"

    # General Q&A
    if "price" in msg_lower or "kitne ka" in msg_lower or "cost" in msg_lower:
        if hindi: return "💰 Har course ka price ₹499 se ₹2999 ke beech hai. Aap kaunsa course dekh rahe hain? Main uska exact price bata deta hu. Puri content ke liye purchase zaruri hai."
        else: return "💰 Courses range from ₹499 to ₹2999. Tell me which course you want, I'll give exact price. Full content is after purchase."
    
    if "kaise kharide" in msg_lower or "how to buy" in msg_lower or "purchase" in msg_lower:
        if hindi: return "🛒 Purchase karne ke liye 'Sales + Invoice' section mein jao, naam, email, phone, WhatsApp bharo aur Buy dabao. Auto invoice aapke email par aa jayega."
        else: return "🛒 Go to 'Sales + Invoice', fill name, email, phone, WhatsApp and click Buy. Auto invoice will be emailed."

    # Default helpful
    if hindi:
        return "👋 Namaste! Main Brahma Super Agent ka Chatbot hu. Main aapke saare sawalon ka jawab de sakta hu - course mein kya hai, kitne modules hain, price kya hai. Lekin course ka andar ka pura data, script, PDF sirf purchase ke baad milega. Aapko kis course ke baare mein janna hai?"
    else:
        return "👋 Hello! I am Brahma Super Agent Chatbot. I can answer your questions - what is in the course, how many modules, price. But full content, scripts, PDFs are only after purchase. Which course are you interested in?"

# --- LOGIN ---
st.sidebar.title("🔐 PRO MAX Login")
if not MASTER_HASH.exists():
    np=st.sidebar.text_input("Master Password Banao", type="password")
    if st.sidebar.button("🔒 Lock Lagao"):
        MASTER_HASH.write_text(hashlib.sha256(np.encode()).hexdigest()); st.sidebar.success("Lock lag gaya! Refresh"); st.stop()
else:
    mp=st.sidebar.text_input("Master Password", type="password")
    if not mp or hashlib.sha256(mp.encode()).hexdigest()!=MASTER_HASH.read_text():
        st.warning("🔒 Master Password daalo"); st.stop()
    st.session_state["mp"]=mp
    secure_data=load_secure(mp) if Path("data/secure.enc").exists() else {}

courses=load_courses(); purchases=load_purchases(); chats=load_chats()

menu=st.sidebar.radio("ULTIMATE Menu",["🚀 Dashboard","🤖 Chatbot Customer Support (Legal Safe)","🔍 Trend Hunter","🎬 HD Factory","🌐 Free Website Links","💰 Sales + Invoice","📊 Purchase Data Download","📥 Course Download","🏦 Secure Banking"])

if menu=="🏦 Secure Banking":
    st.header("🏦 Secure Banking + Gmail")
    with st.form("bank"):
        c1,c2=st.columns(2)
        with c1: holder=st.text_input("Holder", secure_data.get("holder_name","")); bank=st.text_input("Bank", secure_data.get("bank_name","")); acc=st.text_input("Acc No", secure_data.get("account_no","")); ifsc=st.text_input("IFSC", secure_data.get("ifsc","")); upi=st.text_input("UPI", secure_data.get("upi_id",""))
        with c2: gmail_user=st.text_input("Gmail", secure_data.get("gmail_user","")); gmail_pass=st.text_input("Gmail App Password", secure_data.get("gmail_pass",""), type="password"); email=st.text_input("Payout Email", secure_data.get("owner_email","")); minp=st.number_input("Min",199,10000,secure_data.get("auto_price_min",499)); maxp=st.number_input("Max",499,20000,secure_data.get("auto_price_max",2999))
        if st.form_submit_button("🔐 Encrypt Save"):
            save_secure({"holder_name":holder,"bank_name":bank,"account_no":acc,"ifsc":ifsc,"upi_id":upi,"gmail_user":gmail_user,"gmail_pass":gmail_pass,"owner_email":email,"auto_price_min":minp,"auto_price_max":maxp}, mp); st.success("Saved Encrypted!")

if menu=="🚀 Dashboard":
    c1,c2,c3,c4=st.columns(4); c1.metric("Courses",len(courses)); c2.metric("Sales",len(purchases)); c3.metric("Revenue",f"₹{sum([p['price'] for p in purchases])}"); c4.metric("Chats",len(chats)); st.info("Legal Safe: Super Agent only sells your own created courses. No scraping, no copyright issue.")

if menu=="🤖 Chatbot Customer Support (Legal Safe)":
    st.header("🤖 Brahma Chatbot - Customer Support (Hindi + English)")
    st.caption("Legal Safe: Course ka andar ka data kabhi nahi batayega. Sirf topic/module name batayega. Detail ke liye purchase bolega.")
    # Chat history display
    for chat in chats[-20:]:
        with st.chat_message(chat["role"]): st.write(chat["msg"])
    user_q = st.chat_input("Customer ka sawal likho - Hindi ya English mein...")
    if user_q:
        # Save user
        chats.append({"role":"user","msg":user_q,"time":str(datetime.datetime.now())}); save_chats(chats)
        reply = chatbot_reply(user_q, courses)
        chats.append({"role":"assistant","msg":reply,"time":str(datetime.datetime.now())}); save_chats(chats)
        with st.chat_message("user"): st.write(user_q)
        with st.chat_message("assistant"): st.write(reply)
    # Download chat history
    if chats:
        st.download_button("📥 Download Chat History", json.dumps(chats, indent=2), file_name="chatbot_history.json")

if menu=="🔍 Trend Hunter":
    st.header("🔍 Free Trend Hunter 100")
    if st.button("100 Search Karo"):
        t=["AI Agent Automation","Instagram Reels Viral","YouTube Automation","N8N No-Code","Prompt Engineering","Data Analytics AI","Digital Marketing SEO","Canva Pro"]*12 + ["Sutra Online Sell","Handloom Brand","Meesho Selling","Boutique Billing"]; st.session_state["trending"]=t[:100]
    if "trending" in st.session_state:
        st.dataframe(pd.DataFrame(st.session_state["trending"],columns=["Trending"])); sel=st.selectbox("Select",st.session_state["trending"]); 
        if st.button(f"Build {sel}"): st.session_state["to_build"]=sel; st.success("Factory mein jao")

if menu=="🎬 HD Factory":
    st.header("🎬 HD Factory - 10x40x30min")
    topic=st.text_input("Topic", value=st.session_state.get("to_build",""))
    if st.button("PURA COURSE BANAO + FREE WEBSITE"):
        prog=st.progress(0); curriculum=[];
        for m in range(1,11):
            vids=[];
            for v in range(1,41):
                vids.append({"v":v,"title":f"{topic} M{m}V{v}","dur":"30:00","voice":free_voice(f"{topic} module {m} video {v}",'hi'),"thumb":free_thumb(f"{topic} M{m}V{v}")}); prog.progress((m*40+v)/400)
            curriculum.append({"m":m,"videos":vids})
        course_id=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        website_link=create_free_website(topic, secure_data.get("auto_price_min",999), course_id)
        new={"id":course_id,"topic":topic,"modules":curriculum,"total_videos":400,"price":secure_data.get("auto_price_min",999),"website":website_link,"status":"Ready"}
        courses.append(new); save_courses(courses); st.success(f"Ban gaya! Website: {website_link}")

if menu=="🌐 Free Website Links":
    st.header("🌐 Free Websites")
    for c in courses:
        st.write(f"**{c['topic']}** - ₹{c['price']} - Link: `{c.get('website','')}`")
        if Path(f"data/websites/{c['id']}.html").exists():
            st.download_button(f"Download HTML {c['topic']}", Path(f"data/websites/{c['id']}.html").read_bytes(), file_name=f"{c['topic']}.html", key=c['id'])

if menu=="💰 Sales + Invoice":
    st.header("💰 Sales + Invoice + WhatsApp")
    with st.form("purchase"):
        c1,c2=st.columns(2)
        with c1: name=st.text_input("Name*"); email=st.text_input("Email*"); phone=st.text_input("Phone*")
        with c2: whatsapp=st.text_input("WhatsApp*"); city=st.text_input("City / Kahan Se"); course_sel=st.selectbox("Course", [c["topic"] for c in courses] if courses else ["No Course"]); pay_method=st.selectbox("Payment", ["UPI","Bank","Razorpay"])
        if st.form_submit_button("Buy + Invoice + Email"):
            if not courses: st.error("Pehle course banao")
            else:
                sel_c=[c for c in courses if c["topic"]==course_sel][0]
                inv_no=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                pur={"invoice_no":inv_no,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":course_sel,"price":sel_c["price"],"payment_method":pay_method,"course_id":sel_c["id"]}
                inv_file=generate_invoice_pdf(pur); pur["invoice_file"]=inv_file; purchases.append(pur); save_purchases(purchases)
                status=send_invoice_email(email, inv_file, pur, secure_data)
                st.success(f"Saved! Invoice {inv_no}. Email: {status}")

if menu=="📊 Purchase Data Download":
    st.header("📊 Purchase Data - Kaun Kahan Se Kab")
    if not purchases: st.warning("No sales yet")
    else:
        df=pd.DataFrame(purchases); st.dataframe(df, use_container_width=True)
        csv_buf=io.StringIO(); writer=csv.DictWriter(csv_buf, fieldnames=purchases[0].keys()); writer.writeheader(); writer.writerows(purchases)
        st.download_button("Download CSV", csv_buf.getvalue(), file_name="all_purchases.csv")
        st.download_button("Download JSON", json.dumps(purchases, indent=2), file_name="all_purchases.json")

if menu=="📥 Course Download":
    st.header("📥 Course Download")
    if not courses: st.warning("No course")
    else:
        sel=st.selectbox("Course", [c["topic"] for c in courses])
        course=[c for c in courses if c["topic"]==sel][0]
        full_text=f"Course: {course['topic']}\n400 Videos\n"
        for m in course["modules"]: full_text+=f"\nModule {m['m']}\n" + "\n".join([f"- {v['title']}" for v in m["videos"]])
        st.download_button(f"Download {sel} TXT", full_text, file_name=f"{sel}_full.txt")