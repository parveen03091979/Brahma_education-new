import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt

st.set_page_config(page_title="Brahma Education V100", page_icon="🎓", layout="wide")

DATA = Path("data")
PPT_DIR = DATA / "ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

CF = DATA / "courses.json"
PF = DATA / "purchases.json"
MF = DATA / "marketing.json"
AF = DATA / "api_keys.json"
QF = DATA / "upi_qr.jpg"
MH = DATA / ".master_hash"
AS = DATA / ".admin_session"

UID = "parveen39179@okicici"
OWNER = "Parveen Kumar"

TOPICS = """
AI Agent Automation
Instagram Reels Mastery
YouTube Automation
Prompt Engineering
Digital Marketing SEO
ChatGPT Mastery
Facebook Ads
Google Ads
SEO Advanced
Social Media Marketing
Content Writing AI
Copywriting Mastery
Blogging Mastery
Affiliate Marketing
Dropshipping
E-commerce Shopify
Canva Design
Video Editing CapCut
YouTube SEO
Instagram Growth
LinkedIn Marketing
Twitter X Growth
TikTok Viral
Pinterest Marketing
Quora Marketing
Email Marketing Automation
WhatsApp Marketing
Telegram Growth
Influencer Marketing
Personal Branding
Freelancing Mastery
Agency Business
SaaS Business
No-Code Bubble
Python Mastery
JavaScript Mastery
React JS
Next.js
Node.js
Web Development Full Stack
WordPress Mastery
Shopify Store Design
UI UX Design
Figma Design
Graphic Design
Logo Design
Thumbnail Design Viral
Video Animation
AI Image Midjourney
AI Video Sora
Voice Cloning ElevenLabs
Automation n8n Make
Zapier Automation
Notion Productivity
Excel Advanced
Google Sheets Automation
Data Analysis Python
Machine Learning
Deep Learning
Data Science
Stock Trading AI
Crypto Trading
Forex Trading
Real Estate Business
Motivational Speaking
Public Speaking
Communication Skills
English Speaking
Podcast Mastery
Music Production AI
Photography Mastery
Reels Editing Viral
Meme Marketing
Viral Content Formula
Lead Generation
Sales Funnel
Landing Page Design
CRO Optimization
Customer Support Automation
HR Recruitment AI
Business Plan Mastery
Startup Funding
Business Automation AI
Time Management
Mindset Millionaire
Meditation Mindfulness
Fitness Coaching Business
Diet Nutrition Business
Yoga Teaching Business
Cooking Channel Business
Travel Vlogging Business
Gaming Channel Growth
Education Channel Growth
Finance Channel Business
News Channel Automation
Meme Page Business
Affiliate Blog SEO
Amazon FBA Mastery
Etsy Store Mastery
Print on Demand Business
Stock Photography Business
Voice Over Business
Translation Business AI
Resume Writing Business
LinkedIn Profile Optimization
AI Tools Mastery
Chatbot Development
AI Voice Agent
AI Receptionist Business
""".strip().splitlines()

def load(p,d):
    try:
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return d

def save(p,d):
    t=p.with_suffix(".tmp")
    t.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
    t.replace(p)

def init_courses():
    data=load(CF,[])
    if not isinstance(data,list):
        data=[]
    exist={c.get("topic","").strip().lower() for c in data if isinstance(c, dict)}
    for i,topic in enumerate(TOPICS):
        if topic.lower() not in exist:
            data.append({"id":"BRAHMA"+str(1000+i),"topic":topic,"price":99})
    for c in data:
        try:
            pr=int(c.get("price",999))
            if pr>200 or pr<1:
                pr=99
            c["price"]=pr
        except:
            c["price"]=99
    save(CF,data)
    return data

courses=init_courses()
purchases=load(PF,[])
api_keys=load(AF,{})

MODS=["WHAT IS","WHY IMPORTANT","WHERE USE","WHEN TO USE","WHO ELIGIBLE","HOW ARCH","TOOLS REQUIRED","EARNING","PRACTICAL USE","RIGHT WAY","FOUNDATION","CORE CONCEPT","ADVANCED","STEP BY STEP","BUSINESS EXAMPLE","CLIENT REQ","REAL STORY","PLANNING","IMPLEMENTATION","MISTAKES","PRO TIP","EXPERT","TOOLS COMPARE","FREE VS PAID","PORTFOLIO","CLIENT FINDING","FREELANCING","AGENCY","BUSINESS MODEL","SCALING","SEO MARKETING","LEAD GEN","SALES","AUTOMATION","OPTIMIZATION","CASE STUDY","DAILY PRACTICE","HOMEWORK","REVISION","FINAL PROJECT"]

def mod_content(topic,num):
    title=MODS[num-1]
    txt="COURSE TOPIC: "+topic+". MODULE: "+title+". This lesson explains importance in professional and business applications. Understand main concepts, terminology, tools, processes and practical implementation. Start with foundation and move towards professional applications. "
    return txt+txt

def make_ppt(course):
    cid=course["id"]
    topic=course["topic"]
    out=PPT_DIR/(cid+"_40_MODULES_V100.pptx")
    prs=Presentation()
    prs.slide_width=Inches(13.33)
    prs.slide_height=Inches(7.5)
    for n in range(1,41):
        slide=prs.slides.add_slide(prs.slide_layouts[6])
        tb=slide.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
        tf=tb.text_frame
        tf.word_wrap=True
        tf.text="M"+str(n).zfill(2)+" "+topic+" Module "+str(n)
        tf.paragraphs[0].font.size=Pt(20)
        tf.paragraphs[0].font.bold=True
        bb=slide.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
        bf=bb.text_frame
        bf.word_wrap=True
        bf.text=mod_content(topic,n)
        bf.paragraphs[0].font.size=Pt(13)
    prs.save(str(out))
    return out

def make_hash(pw):
    salt=secrets.token_bytes(16)
    h=hashlib.scrypt(pw.encode(), salt=salt, n=16384, r=8, p=1)
    return salt.hex()+":"+h.hex()

def verify(pw, stored):
    try:
        s_hex, h_hex = stored.split(":")
        s=bytes.fromhex(s_hex)
        a=hashlib.scrypt(pw.encode(), salt=s, n=16384, r=8, p=1)
        return secrets.compare_digest(a.hex(), h_hex)
    except:
        old=hashlib.sha256(pw.encode()).hexdigest()
        return secrets.compare_digest(old, stored)

def sess_valid():
    try:
        d=load(AS,{})
        exp=datetime.datetime.fromisoformat(d["expiry"])
        return datetime.datetime.now()<exp
    except:
        return False

if "admin_logged" not in st.session_state:
    st.session_state.admin_logged=sess_valid()

st.sidebar.title("Brahma V100")
if not MH.exists():
    pw=st.sidebar.text_input("Create Password", type="password")
    if st.sidebar.button("Create Admin"):
        if pw and len(pw)>=4:
            MH.write_text(make_hash(pw), encoding="utf-8")
            st.rerun()
    menu="Browse Courses"
else:
    if not st.session_state.admin_logged:
        menu=st.sidebar.radio("Menu",["Browse Courses","My Access"])
        pw=st.sidebar.text_input("Password", type="password")
        if st.sidebar.button("Login"):
            stored=MH.read_text(encoding="utf-8").strip()
            if verify(pw, stored):
                if ":" not in stored:
                    MH.write_text(make_hash(pw), encoding="utf-8")
                exp=datetime.datetime.now()+datetime.timedelta(days=7)
                save(AS,{"expiry":exp.isoformat()})
                st.session_state.admin_logged=True
                st.rerun()
            else:
                st.sidebar.error("Wrong")
    else:
        st.sidebar.success("Admin OK Price 99")
        menu=st.sidebar.radio("Admin",["Dashboard","Price Manager 99","Deep Maker","Course Library","Video Library","API Keys","UPI QR Setup","Sales","Marketing","Super Agent"])
        if st.sidebar.button("Logout"):
            st.session_state.admin_logged=False
            AS.unlink(missing_ok=True)
            st.rerun()

if st.session_state.admin_logged:
    if menu=="Dashboard":
        st.title("Dashboard Price 99")
        total=len(courses)
        ready=len(list(PPT_DIR.glob("*_40_MODULES_V100.pptx")))
        avg=sum([c.get("price",99) for c in courses])//max(1,total)
        c1,c2,c3=st.columns(3)
        c1.metric("Total",total)
        c2.metric("Ready",ready)
        c3.metric("Avg",avg)
        if st.button("DELETE OLD"):
            for f in PPT_DIR.glob("*.*"):
                try:
                    f.unlink()
                except:
                    pass
            st.success("Done")
            st.rerun()
        if st.button("CREATE 100 BOOKS", type="primary"):
            bar=st.progress(0)
            for idx,c in enumerate(courses):
                make_ppt(c)
                bar.progress(int((idx+1)/len(courses)*100))
            st.success("Done")
            st.balloons()
            st.rerun()

    elif menu=="Price Manager 99":
        st.title("Price Manager")
        st.success("All price 99 - Bulk and Single option")
        bulk=st.number_input("Set All Price Rs", value=99, min_value=1, max_value=10000, step=1)
        if st.button("SET ALL BULK", type="primary"):
            for c in courses:
                c["price"]=int(bulk)
            save(CF,courses)
            st.success("Done")
            st.rerun()
        inc=st.number_input("Increase Decrease All By Rs", value=10, min_value=-1000, max_value=1000, step=1)
        if st.button("APPLY BULK", type="secondary"):
            for c in courses:
                np=c.get("price",99)+int(inc)
                c["price"]=int(max(1,np))
            save(CF,courses)
            st.success("Done")
            st.rerun()
        if st.button("SET ALL TO 99", type="primary"):
            for c in courses:
                c["price"]=99
            save(CF,courses)
            st.success("Done")
            st.balloons()
            st.rerun()
        st.divider()
        sel=st.selectbox("Select Course", [c["topic"]+" - "+c["id"]+" - Rs "+str(c.get("price",99)) for c in courses])
        sid=sel.split(" - ")[-2]
        curr=99
        for c in courses:
            if c["id"]==sid:
                curr=c.get("price",99)
        np=st.number_input("New Price", value=int(curr), min_value=1, max_value=10000, step=1)
        if st.button("UPDATE SINGLE", type="primary"):
            for c in courses:
                if c["id"]==sid:
                    c["price"]=int(np)
                    break
            save(CF,courses)
            st.success("Done")
            st.rerun()

    elif menu=="Deep Maker":
        st.title("Deep Maker + Add Course")
        with st.form("add_new"):
            nt=st.text_input("New Course Name")
            npr=st.number_input("New Course Price", value=99, min_value=1, max_value=10000, step=1)
            sub=st.form_submit_button("ADD COURSE", type="primary")
            if sub:
                if len(nt)<5:
                    st.error("Error")
                else:
                    nid="BRAHMA"+str(1000+len(courses))
                    courses.append({"id":nid,"topic":nt,"price":int(npr)})
                    save(CF,courses)
                    make_ppt({"id":nid,"topic":nt})
                    st.success("Done")
                    st.rerun()
        sel=st.selectbox("Select For PPT", [c["topic"]+" - "+c["id"] for c in courses])
        if st.button("Make PPT", type="primary"):
            sid=sel.split(" - ")[-1]
            stopic=" - ".join(sel.split(" - ")[:-1])
            out=make_ppt({"id":sid,"topic":stopic})
            st.success("Done")
            st.download_button("Download", data=out.read_bytes(), file_name=out.name)

    elif menu=="Course Library":
        st.title("Course Library Price 99")
        for idx,co in enumerate(courses[:20]):
            pf=list(PPT_DIR.glob(co["id"]+"*V100*"))
            if pf:
                st.success(str(idx+1)+". "+co["topic"]+" - Rs "+str(co.get("price",99)))
                st.download_button("Download", data=pf[0].read_bytes(), file_name=pf[0].name, key="dlc"+str(idx))

    elif menu=="Video Library":
        st.title("Video Library")
        total=len(courses)
        made=len(list(PPT_DIR.glob("*.pptx")))
        missing=total-made
        st.metric("Missing", missing)
        if missing>0:
            ml=[c for c in courses if not list(PPT_DIR.glob(c["id"]+"*"))][:3]
            for c in ml:
                make_ppt(c)
                st.success("Done")
            st.rerun()

    elif menu=="API Keys":
        st.title("API Keys")
        ok=st.text_input("OpenAI", value=api_keys.get("openai",""), type="password")
        ck=st.text_input("Claude", value=api_keys.get("claude",""), type="password")
        gk=st.text_input("Gemini", value=api_keys.get("gemini",""), type="password")
        if st.button("SAVE", type="primary"):
            api_keys["openai"]=ok
            api_keys["claude"]=ck
            api_keys["gemini"]=gk
            save(AF, api_keys)
            st.success("Done")
            st.balloons()

    elif menu=="UPI QR Setup":
        st.title("UPI QR Setup Price 99")
        st.write("UPI ID: "+UID+" Name: "+OWNER)
        up=st.file_uploader("Upload QR", type=["jpg","png","jpeg"])
        if up:
            QF.write_bytes(up.getvalue())
            st.success("Done")
            st.rerun()
        if QF.exists():
            st.image(str(QF), width=300)
        amount=st.number_input("Amount INR", value=99, min_value=1)
        topic_sel=st.selectbox("Course For Link", [c["topic"] for c in courses[:20]])
        if st.button("Generate Link", type="primary"):
            params={"pa":UID,"pn":OWNER,"am":str(amount),"cu":"INR","tn":topic_sel[:20]}
            link="upi://pay?"+urllib.parse.urlencode(params)
            st.code(link)

    elif menu=="Sales":
        st.title("Sales Dashboard")
        pending=[p for p in purchases if p.get("status")=="PENDING"]
        approved=[p for p in purchases if p.get("status")=="APPROVED"]
        a,b,c=st.columns(3)
        a.metric("Total", len(purchases))
        b.metric("Pending", len(pending))
        c.metric("Approved", len(approved))
        for i,p in enumerate(purchases):
            with st.expander(str(p.get("invoice_no","Order"))+" - "+str(p.get("course","Course"))):
                st.write("Name:", p.get("name"))
                st.write("Email:", p.get("email"))
                st.write("Price:", "Rs "+str(p.get("price")))
                st.write("UTR:", p.get("utr"))
                st.write("Status:", p.get("status"))
                if p.get("status")=="PENDING":
                    if st.button("APPROVE", key="approve_"+str(i), type="primary"):
                        ak="BRAHMA-"+secrets.token_hex(5).upper()
                        p["status"]="APPROVED"
                        p["access_key"]=ak
                        p["approved_date"]=datetime.datetime.now().isoformat()
                        save(PF, purchases)
                        st.success("Done")
                        st.rerun()
                    if st.button("REJECT", key="reject_"+str(i)):
                        p["status"]="REJECTED"
                        save(PF, purchases)
                        st.success("Done")
                        st.rerun()

    elif menu=="Marketing":
        st.title("Marketing Engine")
        if st.button("GENERATE 60 POSTS", type="primary"):
            posts=[]
            today=datetime.date.today().isoformat()
            for course in courses[:20]:
                posts.append({"date":today,"platform":"Facebook","course":course["topic"],"type":"Morning Post 7AM","status":"DRAFT"})
                posts.append({"date":today,"platform":"Instagram","course":course["topic"],"type":"Reel 12PM","status":"DRAFT"})
                posts.append({"date":today,"platform":"Blog","course":course["topic"],"type":"SEO Blog 7PM","status":"DRAFT"})
            save(MF, posts)
            st.success("Done")
            st.rerun()
        st.metric("Posts", len(load(MF, [])))

    elif menu=="Super Agent":
        st.title("Super Agent")
        if st.button("START SUPER AGENT", type="primary"):
            posts=[]
            today=datetime.date.today().isoformat()
            for course in courses[:20]:
                posts.append({"date":today,"platform":"Facebook","course":course["topic"],"type":"Morning Post 7AM","status":"DRAFT"})
                posts.append({"date":today,"platform":"Instagram","course":course["topic"],"type":"Reel 12PM","status":"DRAFT"})
                posts.append({"date":today,"platform":"Blog","course":course["topic"],"type":"SEO Blog 7PM","status":"DRAFT"})
            save(MF, posts)
            st.success("Done")
            st.balloons()

else:
    if menu=="Browse Courses":
        st.title("Brahma Education V100 Price 99")
        search=st.text_input("Search")
        filtered=[c for c in courses if search.lower() in c["topic"].lower()] if search else courses
        ready=len(list(PPT_DIR.glob("*_40_MODULES_V100.pptx")))
        st.write("Total "+str(len(filtered))+" courses - Ready "+str(ready)+" - Price Only 99")
        for i,course in enumerate(filtered[:15]):
            with st.expander(course["topic"]+" - Rs "+str(course["price"])):
                if QF.exists():
                    st.image(str(QF), width=220)
                params={"pa":UID,"pn":OWNER,"am":str(course["price"]),"cu":"INR","tn":course["topic"][:40]}
                link="upi://pay?"+urllib.parse.urlencode(params)
                st.link_button("PAY Rs "+str(course["price"])+" VIA UPI", link, type="primary")
                with st.form("purchase_"+course["id"]):
                    name=st.text_input("Full Name", key="name_"+course["id"])
                    email=st.text_input("Email", key="email_"+course["id"])
                    utr=st.text_input("UTR", key="utr_"+course["id"], max_chars=30)
                    submitted=st.form_submit_button("SUBMIT PAYMENT", type="primary")
                    if submitted:
                        if len(name.strip())<3:
                            st.error("Error")
                        elif "@" not in email or "." not in email:
                            st.error("Error")
                        elif len(utr.strip())<5:
                            st.error("Error")
                        elif any(p.get("utr","").strip()==utr.strip() and p.get("status") in ["PENDING","APPROVED"] for p in purchases):
                            st.error("Error")
                        else:
                            invoice="INV"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+secrets.token_hex(2).upper()
                            purchase={"invoice_no":invoice,"access_key":"","name":name.strip(),"email":email.strip().lower(),"course":course["topic"],"course_id":course["id"],"price":int(course["price"]),"utr":utr.strip(),"status":"PENDING","date":datetime.datetime.now().isoformat()}
                            purchases.append(purchase)
                            save(PF, purchases)
                            st.success("Done")
                            st.code(invoice)
                            st.rerun()

    elif menu=="My Access":
        st.title("My Learning Price 99")
        access_input=st.text_input("INVOICE OR ACCESS KEY")
        if st.button("UNLOCK", type="primary"):
            found=[p for p in purchases if (p.get("invoice_no")==access_input.strip() or p.get("access_key")==access_input.strip()) and p.get("status")=="APPROVED"]
            if not found:
                st.error("Error")
            else:
                purchase=found[0]
                st.success("WELCOME "+purchase.get("name","Student"))
                ppt_path=PPT_DIR/(purchase.get("course_id","")+"_40_MODULES_V100.pptx")
                if ppt_path.exists():
                    st.download_button("DOWNLOAD COURSE", data=ppt_path.read_bytes(), file_name=ppt_path.name, type="primary")
                else:
                    st.warning("Not ready")

st.divider()
st.caption("Brahma Education | V100.9 Final | Price 99 | No Error | Stable")