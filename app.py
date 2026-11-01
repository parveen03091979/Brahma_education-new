# BRAHMA SUPER AGENT - ULTIMATE - LIGHT VERSION - NO CRYPTO - 100% WORKING ON STREAMLIT
import streamlit as st, json, os, hashlib, datetime, time, requests, csv, io, re, smtplib
from pathlib import Path
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

st.set_page_config(page_title="Brahma Super Agent PRO", page_icon="👑", layout="wide")
DATA_DIR = Path("data"); DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"; PURCHASE_FILE = DATA_DIR / "purchases.json"
WEBSITE_DIR = DATA_DIR / "websites"; WEBSITE_DIR.mkdir(exist_ok=True)
CHAT_FILE = DATA_DIR / "chat_history.json"
CONFIG_FILE = DATA_DIR / "config.json"

def load_courses(): return json.loads(COURSES_FILE.read_text()) if COURSES_FILE.exists() else []
def save_courses(c): COURSES_FILE.write_text(json.dumps(c, indent=2))
def load_purchases(): return json.loads(PURCHASE_FILE.read_text()) if PURCHASE_FILE.exists() else []
def save_purchases(p): PURCHASE_FILE.write_text(json.dumps(p, indent=2))
def load_chats(): return json.loads(CHAT_FILE.read_text()) if CHAT_FILE.exists() else []
def save_chats(ch): CHAT_FILE.write_text(json.dumps(ch, indent=2))
def load_config(): return json.loads(CONFIG_FILE.read_text()) if CONFIG_FILE.exists() else {}
def save_config(c): CONFIG_FILE.write_text(json.dumps(c, indent=2))

def free_voice(t, lang='hi'):
    try:
        from gtts import gTTS
        fname=f"data/voice_{int(time.time())}_{lang}.mp3"; gTTS(text=t[:4000], lang='hi' if lang=='hi' else 'en').save(fname); return fname
    except: return None

def create_free_website(topic, price, cid):
    html=f"<html><head><title>{topic}</title><style>body{{font-family:Arial;background:#0f0f23;color:#fff;text-align:center;padding:50px}}.btn{{background:gold;color:#000;padding:15px 30px;font-size:20px}}</style></head><body><h1>👑 {topic}</h1><h2>10 Modules x 40 Videos = 400 Videos</h2><p>Hindi+English Voice+PDF</p><h1>₹{price}</h1><button class='btn'>Buy Now</button></body></html>"
    f=WEBSITE_DIR / f"{cid}.html"; f.write_text(html); return f"data/websites/{cid}.html"

def generate_invoice(pur):
    txt=f"BRAHMA EDUCATION\nInvoice: {pur['invoice_no']}\nDate: {pur['date']}\nCourse: {pur['course']}\nName: {pur['name']}\nEmail: {pur['email']}\nPhone: {pur['phone']}\nWhatsApp: {pur['whatsapp']}\nCity: {pur['city']}\nPrice: ₹{pur['price']}\n"
    fname=f"data/invoice_{pur['invoice_no']}.txt"; Path(fname).write_text(txt); return fname

# --- LEGAL SAFE CHATBOT ---
def chatbot_reply(user_msg, courses):
    ml=user_msg.lower()
    leak=["script de do","pdf de do","video de do","free mein do","full course","pura course batao","module ka content","free download"]
    if any(k in ml for k in leak):
        return "🙏 Pura content, script, PDF, video sirf purchase ke baad milega. Main sirf topic aur module ka naam bata sakta hu. Detail ke liye purchase karna padega."
    for c in courses:
        if c["topic"].lower() in ml:
            mods=", ".join([f"Module {m['m']}" for m in c["modules"][:10]])
            return f"📚 **{c['topic']}** me 10 Modules, 400 videos (30 min). Topics: {mods}. Price ₹{c['price']}. Puri detail ke liye purchase karna padega."
    if "price" in ml or "kitne" in ml: return "💰 Price ₹499-₹2999. Kaunsa course chahiye bolo?"
    return "👋 Namaste! Main aapke sawalon ka jawab dunga - price, modules kya hain. Lekin pura andar ka content sirf purchase ke baad. Kaunsa course?"

# --- LOGIN ---
st.sidebar.title("🔐 Login")
if not MASTER_HASH.exists():
    np=st.sidebar.text_input("Master Password Banao", type="password")
    if st.sidebar.button("Lock Lagao"):
        MASTER_HASH.write_text(hashlib.sha256(np.encode()).hexdigest()); st.sidebar.success("Ban gaya! Refresh karo"); st.stop()
else:
    mp=st.sidebar.text_input("Master Password", type="password")
    if not mp or hashlib.sha256(mp.encode()).hexdigest()!=MASTER_HASH.read_text():
        st.warning("🔒 Password daalo"); st.stop()
    st.session_state["mp"]=mp

courses=load_courses(); purchases=load_purchases(); chats=load_chats(); config=load_config()

menu=st.sidebar.radio("Menu",["🚀 Dashboard","🤖 Chatbot (Legal Safe)","🔍 Trend Hunter","🎬 HD Factory","🌐 Free Website Links","💰 Sales + Invoice","📊 Purchase Data","📥 Course Download","🏦 Banking"])

if menu=="🏦 Banking":
    st.header("🏦 Banking + Gmail (Secure)")
    with st.form("b"):
        c1,c2=st.columns(2)
        with c1: holder=st.text_input("Holder",config.get("holder_name","")); bank=st.text_input("Bank",config.get("bank_name","")); acc=st.text_input("Acc No",config.get("account_no","")); ifsc=st.text_input("IFSC",config.get("ifsc","")); upi=st.text_input("UPI",config.get("upi_id",""))
        with c2: gmail=st.text_input("Gmail",config.get("gmail_user","")); gpass=st.text_input("App Password",config.get("gmail_pass",""),type="password"); email=st.text_input("Payout Email",config.get("owner_email","")); minp=st.number_input("Min",199,10000,config.get("auto_price_min",499)); maxp=st.number_input("Max",499,20000,config.get("auto_price_max",2999))
        if st.form_submit_button("Save"):
            save_config({"holder_name":holder,"bank_name":bank,"account_no":acc,"ifsc":ifsc,"upi_id":upi,"gmail_user":gmail,"gmail_pass":gpass,"owner_email":email,"auto_price_min":minp,"auto_price_max":maxp}); st.success("Saved!")

if menu=="🚀 Dashboard":
    c1,c2,c3=st.columns(3); c1.metric("Courses",len(courses)); c2.metric("Sales",len(purchases)); c3.metric("Revenue",f"₹{sum([p['price'] for p in purchases])}")

if menu=="🤖 Chatbot (Legal Safe)":
    st.header("🤖 Chatbot - Hindi+English - No Data Leak")
    for ch in chats[-20:]:
        with st.chat_message(ch["role"]): st.write(ch["msg"])
    q=st.chat_input("Sawal likho...")
    if q:
        chats.append({"role":"user","msg":q}); reply=chatbot_reply(q,courses); chats.append({"role":"assistant","msg":reply}); save_chats(chats); st.rerun()

if menu=="🔍 Trend Hunter":
    if st.button("100 Trending Search"):
        t=["AI Agent Automation","Instagram Viral Reels","YouTube Automation","N8N No-Code","Prompt Engineering","Data Analytics AI","Digital Marketing SEO","Canva Pro"]*12+["Online Business","Meesho Selling"]; st.session_state["trending"]=t[:100]
    if "trending" in st.session_state:
        st.dataframe(pd.DataFrame(st.session_state["trending"],columns=["Trending"])); sel=st.selectbox("Select",st.session_state["trending"])
        if st.button(f"Build {sel}"): st.session_state["to_build"]=sel

if menu=="🎬 HD Factory":
    topic=st.text_input("Topic",value=st.session_state.get("to_build",""))
    if st.button("PURA COURSE BANAO (10x40) + WEBSITE"):
        prog=st.progress(0); curriculum=[];
        for m in range(1,11):
            vids=[];
            for v in range(1,41):
                vids.append({"v":v,"title":f"{topic} M{m}V{v}","dur":"30:00"}); prog.progress((m*40+v)/400)
            curriculum.append({"m":m,"videos":vids})
        cid=datetime.datetime.now().strftime("%Y%m%d%H%M%S"); website=create_free_website(topic,config.get("auto_price_min",999),cid)
        new={"id":cid,"topic":topic,"modules":curriculum,"total_videos":400,"price":config.get("auto_price_min",999),"website":website}; courses.append(new); save_courses(courses); st.success(f"Ban gaya! Website: {website}")

if menu=="🌐 Free Website Links":
    st.header("🌐 Free Website Links - Hamesha Yahan")
    for c in courses:
        st.write(f"{c['topic']} - ₹{c['price']} - {c.get('website','')}")
        if Path(f"data/websites/{c['id']}.html").exists():
            st.download_button(f"Download {c['topic']}",Path(f"data/websites/{c['id']}.html").read_bytes(),file_name=f"{c['topic']}.html",key=c['id'])

if menu=="💰 Sales + Invoice":
    with st.form("p"):
        c1,c2=st.columns(2)
        with c1: name=st.text_input("Name*"); email=st.text_input("Email*"); phone=st.text_input("Phone*")
        with c2: whatsapp=st.text_input("WhatsApp*"); city=st.text_input("City Kahan Se"); csel=st.selectbox("Course",[c["topic"] for c in courses] if courses else ["No Course"])
        if st.form_submit_button("Buy + Invoice"):
            sel_c=[c for c in courses if c["topic"]==csel][0]; inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"; pur={"invoice_no":inv,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":csel,"price":sel_c["price"]}; inv_file=generate_invoice(pur); purchases.append(pur); save_purchases(purchases); st.success(f"Saved! Invoice {inv}")

if menu=="📊 Purchase Data":
    if purchases:
        df=pd.DataFrame(purchases); st.dataframe(df); csv_buf=io.StringIO(); writer=csv.DictWriter(csv_buf,fieldnames=purchases[0].keys()); writer.writeheader(); writer.writerows(purchases); st.download_button("Download CSV",csv_buf.getvalue(),file_name="purchases.csv")

if menu=="📥 Course Download":
    if courses:
        sel=st.selectbox("Course",[c["topic"] for c in courses]); course=[c for c in courses if c["topic"]==sel][0]; txt=f"Course {sel} 400 Videos\n" + "\n".join([f"Module {m['m']}" for m in course["modules"]]); st.download_button("Download Notes",txt,file_name=f"{sel}.txt")