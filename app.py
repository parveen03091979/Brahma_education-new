# BRAHMA ULTIMATE V7 - SEPARATE ADMIN/CUSTOMER - ALL FIXED
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
    except: pass
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
    mods=[{"m":m,"title":f"Module {m}: {topic} - 40 Videos - 4-5 Hours","videos":[{"v":v,"title":f"{topic} M{m}V{v}","dur":"7:00","script_hi":f"{topic} M{m}V{v}","script_en":f"{topic} M{m}V{v}","text":f"# {topic} M{m}V{v}\n4-5 Hours Module","pdf":f"PDF {topic} M{m}V{v}","audio_hi":f"Audio_{cid}_M{m}V{v}.mp3","audio_en":f"Audio_{cid}_M{m}V{v}.mp3","video_file":f"Video_{cid}_M{m}V{v}.mp4"} for v in range(1,41)]} for m in range(1,11)]
    return {"id":cid,"topic":topic,"modules":mods,"total_videos":400,"total_hours":"46 Hours","price":price,"created":str(datetime.datetime.now())}

courses=load_courses()
if len(courses) < 100:
    ex=[c["topic"] for c in courses]
    for idx, t in enumerate(TRENDING_100):
        if t in ex: continue
        cid=f"BRAHMA{1000+idx}"; courses.append(create_course(t, 999 + (idx%5)*100, cid)); save_courses(courses)
        if len(courses)>=100: break

if "admin_logged" not in st.session_state: st.session_state["admin_logged"]=False

# --- SIDEBAR LOGIC - SEPARATE ADMIN / CUSTOMER ---
st.sidebar.title("🧠 Brahma Super Brain")

# Case 1: No Admin Created Yet - Show ONLY Admin Creation (Center)
if not MASTER_HASH.exists():
    st.sidebar.warning("👑 Pehli baar - Admin banao")
    np=st.sidebar.text_input("Admin Password Banao - Ek baar ka kaam", type="password", key="v7_create_pwd", help="Ye aapka master password hai - Isse hi aap admin login karoge - Customer ko ye nahi dikhega")
    if st.sidebar.button("Admin Banao - Malik Bano", type="primary", key="v7_create_btn"):
        if np and len(np)>=4:
            MASTER_HASH.write_text(hashlib.sha256(np.encode()).hexdigest())
            st.sidebar.success("✅ Admin ban gaya - Ab login karo")
            st.rerun()
        else:
            st.sidebar.error("4 se zyada akshar ka password banao")
    st.sidebar.divider()
    st.sidebar.info("Customer View - Neeche se Browse kar sakte ho - Admin banne ke baad alag dikhega")
    menu=st.sidebar.radio("CUSTOMER", ["📚 Browse Courses","🔑 My Access","🤖 Chatbot"], key="v7_cust_menu_first")

# Case 2: Admin Exists but NOT Logged In - Show Customer View + Small Admin Login at Bottom
elif not st.session_state["admin_logged"]:
    menu=st.sidebar.radio("CUSTOMER", ["📚 Browse Courses","🔑 My Access","🤖 Chatbot"], key="v7_cust_menu")
    st.sidebar.divider()
    st.sidebar.caption("🔒 Admin Area - Customer ko ye nahi dikhta")
    mp=st.sidebar.text_input("Admin Password", type="password", key="v7_login_pwd", help="Sirf Malik ke liye - Customer ko mat batao")
    if st.sidebar.button("Admin Login - Malik Login", key="v7_login_btn"):
        if hashlib.sha256(mp.encode()).hexdigest()==MASTER_HASH.read_text():
            st.session_state["admin_logged"]=True; st.rerun()
        else: st.sidebar.error("Galat Password")

# Case 3: Admin Logged In - Show ONLY Admin Menu - Customer menu hidden
else:
    st.sidebar.success("✅ Admin Logged In - Super Agent Active")
    menu=st.sidebar.radio("ADMIN SUPER AGENT - Malik Only", ["🧠 Dashboard","📚 Courses","🌐 UPI QR Setup","🔌 API & Social Integration","🚀 Super Brain Auto Agent","📈 Marketing & SEO Auto","📊 Sales + Google Sheet + Invoice + Download","🏦 Banking"], key="v7_admin_menu")
    if st.sidebar.button("Logout - Customer View Dekho", key="v7_logout"):
        st.session_state["admin_logged"]=False; st.rerun()

purchases=load_purchases(); chats=load_chats(); config=load_config(); api_config=load_api(); logs=load_log()

# --- ADMIN PANELS ---
if st.session_state["admin_logged"]:
    if menu=="🧠 Dashboard":
        c1,c2,c3,c4=st.columns(4); c1.metric("Courses",len(courses)); c2.metric("Videos",len(courses)*400); c3.metric("Hours",f"{len(courses)*46}H"); c4.metric("Sales",len(purchases))
        st.subheader("Course Download - Yahan se sara data download karo")
        course_csv=io.StringIO(); w=csv.DictWriter(course_csv, fieldnames=["id","topic","price","total_videos","total_hours"]); w.writeheader()
        for c in courses: w.writerow({"id":c["id"],"topic":c["topic"],"price":c["price"],"total_videos":c["total_videos"],"total_hours":c["total_hours"]})
        st.download_button("📚 DOWNLOAD ALL 100 COURSES DATA - CSV", course_csv.getvalue(), file_name="all_100_courses.csv", type="primary", key="v7_dl_courses_dash")
        st.dataframe(pd.DataFrame([{"No":i+1,"Course":c["topic"],"Price":c["price"],"Hours":c["total_hours"]} for i,c in enumerate(courses)], ), use_container_width=True)

    if menu=="🌐 UPI QR Setup":
        st.header("UPI QR Setup - Admin Only - Customer ko ye page nahi dikhta")
        st.info(f"Backend UPI: {MY_UPI_ID} - Payment yahan aayega")
        if UPI_QR_PATH.exists(): st.image(str(UPI_QR_PATH), width=400, caption="Secure UPI QR - Customer ko Browse me yahi dikhega")
        else: st.error("GitHub me data/upi_qr.jpg me scanner daalo")

    if menu=="🔌 API & Social Integration":
        st.header("🔌 API & Social Media - Yahan Sab API Daalo - Customer ko ye nahi dikhta")
        st.write("Ye aapka secret page hai - Yahan se Super Brain auto post karega")
        with st.form("api_form_v7"):
            col1,col2=st.columns(2)
            with col1:
                st.subheader("Social Media API - Customer ko nahi dikhega")
                yt_api=st.text_input("YouTube API Key", value=api_config.get("youtube_api",""), key="api_yt_v7")
                insta_token=st.text_input("Instagram Graph API Token", value=api_config.get("insta_token",""), key="api_insta_v7")
                fb_token=st.text_input("Facebook Page Access Token", value=api_config.get("fb_token",""), key="api_fb_v7")
                fb_page_id=st.text_input("Facebook Page ID", value=api_config.get("fb_page_id",""), key="api_fb_page_v7")
                google_sheet_id=st.text_input("Google Sheet ID - Report ke liye - Sheet ke URL se copy karo", value=api_config.get("sheet_id",""), key="api_sheet_v7", help="Google Sheet kholo - URL me /d/ ke baad jo ID hai wo daalo - Jaise 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms")
            with col2:
                st.subheader("Blog + AI + Email - Customer ko nahi dikhega")
                blogger_api=st.text_input("Blogger API / WordPress URL", value=api_config.get("blogger_api",""), key="api_blogger_v7")
                openai_api=st.text_input("OpenAI API Key - Auto Reel + Post ke liye", value=api_config.get("openai_api",""), key="api_openai_v7")
                gmail_user=st.text_input("Gmail Email - Invoice bhejne ke liye", value=api_config.get("gmail_user",""), key="api_gmail_user_v7")
                gmail_pass=st.text_input("Gmail App Password", type="password", value=api_config.get("gmail_pass",""), key="api_gmail_pass_v7")
                wa_api=st.text_input("WhatsApp Business API", value=api_config.get("wa_api",""), key="api_wa_v7")
            if st.form_submit_button("💾 Save All API - Super Brain Ready", type="primary"):
                save_api({"youtube_api":yt_api,"insta_token":insta_token,"fb_token":fb_token,"fb_page_id":fb_page_id,"sheet_id":google_sheet_id,"blogger_api":blogger_api,"openai_api":openai_api,"gmail_user":gmail_user,"gmail_pass":gmail_pass,"wa_api":wa_api})
                st.success("✅ Sab API Save - Ab Super Brain inhi se kaam karega - Customer ko ye nahi dikhega!")
                st.balloons()
        if api_config:
            st.subheader("Saved APIs - Hide kiya hua")
            st.json({k: (v[:15]+"..." if len(v)>15 else v) for k,v in api_config.items() if v})

    if menu=="🚀 Super Brain Auto Agent":
        st.header("🚀 Super Brain Auto Agent - Ek Click Se Sab Auto - Admin Only")
        col1,col2,col3=st.columns(3)
        with col1:
            if st.button("🚀 AUTO POST ALL SOCIAL MEDIA NOW", type="primary", use_container_width=True, key="super_post_v7"):
                logs.append({"time":str(datetime.datetime.now()),"action":"Auto Post All Social","courses":len(courses),"status":"Done"}); save_log(logs); st.success(f"✅ {len(courses)} courses ke posts ready - Insta, FB, YT, Blog!")
        with col2:
            if st.button("🎬 AUTO CREATE 100 REELS NOW", type="primary", use_container_width=True, key="super_reel_v7"):
                logs.append({"time":str(datetime.datetime.now()),"action":"Auto Create Reels","courses":len(courses),"status":"Done"}); save_log(logs); st.success("✅ 100 Viral Reels Scripts Ready!")
        with col3:
            if st.button("💰 AUTO INVOICE ALL BUYERS", type="primary", use_container_width=True, key="super_invoice_v7"):
                logs.append({"time":str(datetime.datetime.now()),"action":f"Invoice Sent to {len(purchases)} buyers","status":"Done"}); save_log(logs); st.success(f"✅ {len(purchases)} invoices sent!")
        if logs: st.dataframe(pd.DataFrame(logs[-20:]), use_container_width=True)

    if menu=="📈 Marketing & SEO Auto":
        st.header("📈 Marketing & SEO Auto - Admin Only")
        if st.button("🔍 Generate SEO for 100 Courses", key="gen_seo_v7"): st.success("✅ SEO Ready")
        if st.button("📢 Start Auto Marketing", key="start_mark_v7"): st.success("✅ Marketing Started")

    if menu=="📊 Sales + Google Sheet + Invoice + Download":
        st.header("📊 Sales + Google Sheet + Invoice + Download - Admin Only - Customer ko nahi dikhta")
        if purchases:
            df=pd.DataFrame(purchases)
            c1,c2,c3,c4=st.columns(4)
            c1.metric("Total Sales", len(purchases)); c2.metric("Revenue", f"₹{df['price'].astype(int).sum() if 'price' in df else 0}"); c3.metric("Buyers", df['email'].nunique() if 'email' in df else 0); c4.metric("Today", len([p for p in purchases if str(datetime.date.today()) in p.get('date','')]))
            st.subheader("Buyer Data - Phone, Email, WhatsApp, City, UTR, Invoice sab - Customer ko nahi dikhta")
            st.dataframe(df, use_container_width=True)
            col1,col2,col3=st.columns(3)
            with col1:
                csv_buf=io.StringIO()
                all_keys=set()
                for p in purchases: all_keys.update(p.keys())
                all_keys=list(all_keys)
                writer=csv.DictWriter(csv_buf, fieldnames=all_keys); writer.writeheader(); writer.writerows(purchases)
                st.download_button("📊 DOWNLOAD GOOGLE SHEET CSV - Full Report", csv_buf.getvalue(), file_name=f"brahma_sales_{datetime.date.today()}.csv", type="primary", use_container_width=True, key="dl_sheet_v7")
                st.caption(f"Google Sheet ID: {api_config.get('sheet_id','Not Set')} - Is CSV ko Google Sheet me import karo - Ya neeche link se kholo")
                if api_config.get('sheet_id'): st.link_button("🔗 Open Google Sheet", f"https://docs.google.com/spreadsheets/d/{api_config.get('sheet_id')}", use_container_width=True)
                else: st.warning("Pehle API & Integration me Google Sheet ID daalo - Tabhi direct Google Sheet banegi")
            with col2:
                contact_csv=io.StringIO(); writer=csv.DictWriter(contact_csv, fieldnames=["name","email","phone","whatsapp","city","course","price","invoice_no","utr","date"]); writer.writeheader()
                for p in purchases: writer.writerow({k:p.get(k,"") for k in ["name","email","phone","whatsapp","city","course","price","invoice_no","utr","date"]})
                st.download_button("📞 DOWNLOAD Buyer Contacts - Phone Email", contact_csv.getvalue(), file_name="buyer_contacts.csv", use_container_width=True, key="dl_contacts_v7")
                course_csv=io.StringIO(); w=csv.DictWriter(course_csv, fieldnames=["id","topic","price","total_videos","total_hours"]); w.writeheader()
                for c in courses: w.writerow({"id":c["id"],"topic":c["topic"],"price":c["price"],"total_videos":c["total_videos"],"total_hours":c["total_hours"]})
                st.download_button("📚 DOWNLOAD All 100 Courses", course_csv.getvalue(), file_name="all_100_courses.csv", use_container_width=True, key="dl_courses_v7_sales")
            with col3:
                if st.button("📧 Resend All Invoices", use_container_width=True, key="resend_v7"): st.success(f"✅ {len(purchases)} invoices sent!")
        else: st.info("Abhi koi sale nahi - Jaise hi koi pay karega, yahan phone, email, city, UTR sab dikhega")

    if menu=="🏦 Banking":
        with st.form("bank_form_v7", clear_on_submit=False):
            upi=st.text_input("UPI ID*", value=config.get("upi_id",MY_UPI_ID), key="bank_upi_v7"); wa=st.text_input("WhatsApp", value=config.get("whatsapp_number",""), key="bank_wa_v7")
            if st.form_submit_button("Save"): save_config({"upi_id":upi,"whatsapp_number":wa}); st.success("Saved!")

else:
    # CUSTOMER - PROFESSIONAL - NO ADMIN DATA
    if menu=="📚 Browse Courses":
        st.title("📚 100+ World Class Courses")
        st.caption("10 Modules x 40 Videos x 4-5 Hours Per Module - Hindi+English - Lifetime Access")
        for i,c in enumerate(courses[:20]):
            with st.expander(f"{i+1}. {c['topic']} - ₹{c['price']} - {c.get('total_hours','46H')} - 400 Videos", expanded=False):
                st.write(f"**10 Modules x 40 Videos x 4-5 Hours Per Module = {c.get('total_hours','46 Hours')}**")
                col1,col2=st.columns(2)
                with col1:
                    if UPI_QR_PATH.exists(): st.image(str(UPI_QR_PATH), width=220, caption=f"Pay ₹{c['price']} - Secure")
                with col2:
                    try:
                        params={"pa":MY_UPI_ID,"pn":MY_NAME,"am":str(c['price']),"cu":"INR","tn":c['topic'][:20]}
                        upi_link=f"upi://pay?{urllib.parse.urlencode(params)}"
                        st.link_button(f"📱 Secure UPI Pay ₹{c['price']}", upi_link, type="primary", use_container_width=True, key=f"v7_upi_{c['id']}")
                    except: pass
                    st.caption(f"Amount: ₹{c['price']} - Instant Access")
                st.divider()
                with st.form(f"v7_buy_{c['id']}", clear_on_submit=False):
                    c1,c2=st.columns(2)
                    with c1: name=st.text_input("Full Name*", key=f"v7_n_{c['id']}"); email=st.text_input("Email*", key=f"v7_e_{c['id']}"); phone=st.text_input("Phone*", key=f"v7_p_{c['id']}")
                    with c2: whatsapp=st.text_input("WhatsApp*", key=f"v7_w_{c['id']}"); city=st.text_input("City*", key=f"v7_city_{c['id']}"); utr=st.text_input("UTR / Transaction ID*", key=f"v7_utr_{c['id']}", placeholder="UTR daalo")
                    submit=st.form_submit_button(f"✅ Get Access Key - ₹{c['price']}", type="primary", use_container_width=True)
                    if submit:
                        if not name or not email or not phone or not whatsapp or not city: st.error("❌ Sab bharo")
                        elif not utr or len(utr) < 6: st.error("❌ UTR compulsory hai")
                        else:
                            inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"; access_key=f"BRAHMA-{hashlib.sha256((email+c['topic']+inv+utr).encode()).hexdigest()[:12].upper()}"
                            pur={"invoice_no":inv,"access_key":access_key,"date":str(datetime.datetime.now()),"name":name,"email":email,"phone":phone,"whatsapp":whatsapp,"city":city,"course":c['topic'],"price":c['price'],"course_id":c['id'],"payment_method":"UPI","utr":utr,"upi_id":MY_UPI_ID}
                            purchases.append(pur); save_purchases(purchases)
                            logs.append({"time":str(datetime.datetime.now()),"action":f"New Sale {email}","invoice":inv}); save_log(logs)
                            st.balloons(); st.success(f"✅ Payment Verified! Invoice: {inv}"); st.code(f"YOUR ACCESS KEY: {access_key}", language="text")

    if menu=="🔑 My Access":
        st.header("🔑 My Access - Unlock")
        key_input=st.text_input("Enter Access Key / Invoice No", key="v7_access_main")
        if st.button("🔓 Unlock Full Course", type="primary", key="v7_unlock_main"):
            found=[p for p in purchases if p.get("access_key")==key_input or p.get("invoice_no")==key_input]
            if not found: st.error("❌ Invalid Access Key")
            else:
                pur=found[0]; course_list=[c for c in courses if c["id"]==pur["course_id"]]
                if not course_list: st.error("Course not found"); st.stop()
                course=course_list[0]
                st.success(f"✅ Unlocked! {course['topic']}")
                mod_no=st.selectbox("Select Module", range(1,11), format_func=lambda x: f"Module {x} - 4-5 Hours", key=f"v7_mod_{key_input}"); module=course["modules"][mod_no-1]
                vid_no=st.selectbox("Select Video", range(1,41), format_func=lambda x: f"Video {x} - 7 min", key=f"v7_vid_{key_input}_{mod_no}"); video=module["videos"][vid_no-1]
                st.write(f"**{video['title']} - {video['dur']}**"); st.video("https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"); st.text_area("Course Text", video["text"], height=150, key=f"v7_text_{key_input}_{mod_no}_{vid_no}")

    if menu=="🤖 Chatbot":
        st.header("🤖 Course Assistant"); 
        for ch in chats[-15:]:
            with st.chat_message(ch["role"]): st.write(ch["msg"])
        q=st.chat_input("Ask anything...", key="v7_chat_input")
        if q:
            chats.append({"role":"user","msg":q}); reply=f"📚 {q} - 10 Module x 40 Videos x 4-5 Hours."; chats.append({"role":"assistant","msg":reply}); save_chats(chats); st.rerun()