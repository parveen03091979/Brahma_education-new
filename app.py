import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path

st.set_page_config(page_title="Brahma V104 Step By Step", layout="wide")

DATA=Path("data")
PPT_DIR=DATA/"ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

CF=DATA/"courses.json"
PF=DATA/"purchases.json"
MF=DATA/"marketing.json"
QF=DATA/"upi_qr.jpg"
MH=DATA/".master_hash"
AS=DATA/".admin_session"

UID="parveen39179@okicici"
OWNER="Parveen Kumar"

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
    if len(data)<100:
        data=[]
        for i in range(100):
            data.append({"id":"BRAHMA"+str(1000+i),"topic":"Course "+str(i+1),"price":99})
        save(CF,data)
    for c in data:
        if c.get("price",999)>200:
            c["price"]=99
    save(CF,data)
    return data

courses=init_courses()
purchases=load(PF,[])

MODS=["WHAT IS","WHY IMPORTANT","WHERE USE","WHEN TO USE","WHO CAN LEARN","HOW IT WORKS ARCHITECTURE","TOOLS YOU NEED","HOW YOU EARN MONEY","HOW TO USE PRACTICALLY","RIGHT WAY TO LEARN","BEGINNER FOUNDATION","CORE CONCEPTS","ADVANCED CONCEPTS","STEP BY STEP PROCESS","REAL BUSINESS EXAMPLES","CLIENT REQUIREMENTS","REAL STORY OF SUCCESS","PROJECT PLANNING","IMPLEMENTATION","MISTAKES 90 PERCENT FAIL","PRO TIP SECRET","EXPERT STRATEGY","TOOLS COMPARISON","FREE VS PAID","PORTFOLIO BUILDING","HOW TO FIND CLIENTS","FREELANCING START","AGENCY BUSINESS","BUSINESS MODEL","HOW TO SCALE","SEO AND MARKETING","LEAD GENERATION","SALES CLOSING","AUTOMATION SETUP","OPTIMIZATION","CASE STUDY ANALYSIS","DAILY PRACTICE ROUTINE","HOMEWORK TASK","REVISION METHOD","FINAL PROJECT AND NEXT STEPS"]

def step_content(topic,num):
    title=MODS[num-1]
    base="COURSE: "+topic+" | MODULE "+str(num)+" - "+title+"\n\n"
    
    if num==1:
        return base+"GOAL: After this module you can explain "+topic+" to 5 people in simple words.\nWHY LEARN: Every business in 2026 needs to save 80 percent time. Salary 3x growth. Future proof skill.\nCONCEPT: "+topic+" is like a helper. Example: You check message (Perceive), think what to reply (Reason), then type reply (Act). Same logic in automation.\nSTEP BY STEP:\nStep 1: Choose one daily boring task. Example: Reply to Instagram comments.\nStep 2: Open ChatGPT. Write prompt: You are social media manager, reply friendly.\nStep 3: Connect tool: Make.com Instagram trigger + ChatGPT action.\nStep 4: Test with your second account. Comment and see auto reply.\nStep 5: Write in diary: What learned, what mistake, tomorrow plan.\nPRACTICE: Today make 1 automation. HOMEWORK: Write 3 tasks you can automate."
    
    if num==2:
        return base+"GOAL: Understand why "+topic+" is important for job and business.\nWHY: Market data 2026 shows 90 percent businesses want automation. 3x salary. No future risk.\nCONCEPT: Without "+topic+" you work 8 hours manual. With "+topic+" same work in 1 hour. Example: Manual reels 4 hours vs automated 30 min.\nSTEP BY STEP:\nStep 1: Google Trends open. Search "+topic+". See growth graph.\nStep 2: Upwork open. Search "+topic+" jobs. Count jobs and price.\nStep 3: Talk to 1 shop owner. Ask daily time waste problem.\nStep 4: Note 5 places where "+topic+" saves time.\nStep 5: Diary: Why you must learn this in next 30 days.\nPRACTICE: Find 5 job posts. HOMEWORK: Write why you need this skill."
    
    if num==17:
        return base+"GOAL: Learn from real person Rahul story and avoid his mistakes.\nWHY: Real story gives you hope and exact roadmap.\nCONCEPT: Rahul from village, Redmi 8 phone, Jio 1GB, no laptop. No degree. Only daily 1 hour practice.\nSTEP BY STEP:\nStep 1: Month 1-2: Daily 1 hour learning. No earning focus. Only foundation.\nStep 2: Month 3: Make portfolio 3 projects. No client yet.\nStep 3: Upwork: Write 20 proposals. 19 reject. Learn from reject reason.\nStep 4: 1 USA client agrees Rs 15k. Deliver extra value. Get 5 star.\nStep 5: Month 4: 5 clients Rs 75k. Month 6: Agency 2L. Build house for parents.\nPRACTICE: Write your 6 month roadmap like Rahul. HOMEWORK: What will you do daily 1 hour?"
    
    if num==20:
        return base+"GOAL: Avoid 5 mistakes that make 90 percent people fail in "+topic+".\nWHY: If you avoid mistakes you save 6 months time.\nCONCEPT: Mistakes are not failure but signals.\nSTEP BY STEP - 5 MISTAKES:\nMistake 1: Foundation skip. You jump to advanced. Fix: Do M01 to M10 twice.\nMistake 2: Only watching videos no practice. Fix: 15 min theory 15 min practical daily.\nMistake 3: Money chase before learning. Fix: First 30 days only skill no money.\nMistake 4: No diary. You forget. Fix: Night 10 min diary 4 points.\nMistake 5: No mentor alone. Fix: Join community ask doubt daily.\nPRACTICE: Check which mistake you do. HOMEWORK: Write your mistake correction plan."
    
    if num==21:
        return base+"GOAL: Use secret pro tip that toppers use.\nWHY: This diary method makes you 10x faster.\nCONCEPT: Toppers dont have extra time. They have extra clarity.\nSTEP BY STEP - PRO TIP DIARY:\nStep 1: Night 10 PM take diary.\nStep 2: Write 4 things: 1) What I learned today in "+topic+" 2) What mistake I made 3) What I will improve tomorrow 4) One new business idea.\nStep 3: Sunday 1 hour review all 7 days diary.\nStep 4: Monday plan based on review.\nStep 5: Repeat 30 days.\nPRACTICE: Tonight write diary. HOMEWORK: Share diary photo tomorrow."
    
    if num==40:
        return base+"GOAL: Create final project and get next steps for 1Cr roadmap.\nWHY: Project is your job interview. No certificate needed if project strong.\nCONCEPT: Final project = Problem + Solution + Workflow + Tools + Result + Portfolio.\nSTEP BY STEP - FINAL PROJECT:\nStep 1: Choose one business problem in "+topic+". Example: Shop owner needs auto reply to WhatsApp.\nStep 2: Plan solution: Tools list, workflow diagram on paper.\nStep 3: Build: Make automation, test 10 times, fix bugs.\nStep 4: Result: Screenshot video record. Before automation 2 hours, after 10 min.\nStep 5: Portfolio: Upload to Behance GitHub LinkedIn with case study.\nStep 6: Next steps: Freelancing profile, agency plan, SaaS idea.\nPRACTICE: Start final project today. HOMEWORK: Submit in 7 days for review. Certificate after review."
    
    # For other modules generic step by step template
    return base+"GOAL: Master "+title+" in "+topic+" clearly.\nWHY: This module is foundation for next module. Skip this you fail next.\nCONCEPT: "+title+" means core idea behind "+topic+" working. Example: Like engine in car.\nSTEP BY STEP:\nStep 1: Understand definition. Write in your own words.\nStep 2: See 2 examples. One success one failure.\nStep 3: Open tool related to this module. Click each option.\nStep 4: Do small task 15 min practical.\nStep 5: Write in diary what learned and what doubt.\nPRACTICE: Today 15 min theory + 15 min practical. HOMEWORK: Teach this to one friend. If you can teach you learned."

def make_ppt(course):
    from pptx import Presentation
    from pptx.util import Inches, Pt
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
        tf.text="M"+str(n).zfill(2)+" "+topic+" - "+MODS[n-1]+" - Step By Step"
        tf.paragraphs[0].font.size=Pt(16)
        tf.paragraphs[0].font.bold=True
        bb=slide.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
        bf=bb.text_frame
        bf.word_wrap=True
        bf.text=step_content(topic,n)
        bf.paragraphs[0].font.size=Pt(11)
    prs.save(str(out))
    return out

def make_hash(pw):
    salt=secrets.token_bytes(16)
    h=hashlib.scrypt(pw.encode(), salt=salt, n=16384, r=8, p=1)
    return salt.hex()+":"+h.hex()

def verify(pw,stored):
    try:
        s_hex,h_hex=stored.split(":")
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

st.sidebar.title("Brahma V104 Step By Step")
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
            if verify(pw,stored):
                exp=datetime.datetime.now()+datetime.timedelta(days=7)
                save(AS,{"expiry":exp.isoformat()})
                st.session_state.admin_logged=True
                st.rerun()
            else:
                st.sidebar.error("Wrong")
    else:
        st.sidebar.success("Admin OK - Step By Step")
        menu=st.sidebar.radio("Admin",["Dashboard","Price Manager 99","Deep Maker","Course Library","UPI QR Setup","Sales"])
        if st.sidebar.button("Logout"):
            st.session_state.admin_logged=False
            AS.unlink(missing_ok=True)
            st.rerun()

if st.session_state.admin_logged:
    if menu=="Dashboard":
        st.title("Dashboard - Step By Step Teaching")
        st.success("40 Modules - Har Module Me Goal Why Concept Step1-5 Practice Homework - Jaise Samne Sikha Rahe Ho")
        total=len(courses)
        ready=len(list(PPT_DIR.glob("*.pptx")))
        c1,c2=st.columns(2)
        c1.metric("Total",total)
        c2.metric("Ready",ready)
        if st.button("DELETE OLD SAME MATTER"):
            for f in PPT_DIR.glob("*.*"):
                try:
                    f.unlink()
                except:
                    pass
            st.success("Done")
            st.rerun()
        if st.button("CREATE 100 BOOKS STEP BY STEP", type="primary"):
            bar=st.progress(0)
            for idx,c in enumerate(courses):
                make_ppt(c)
                bar.progress(int((idx+1)/len(courses)*100))
            st.success("Done - Har Module Step By Step")
            st.balloons()
            st.rerun()

    elif menu=="Price Manager 99":
        st.title("Price Manager")
        bulk=st.number_input("Set All Price", value=99, min_value=1, max_value=10000, step=1)
        if st.button("SET ALL BULK", type="primary"):
            for c in courses:
                c["price"]=int(bulk)
            save(CF,courses)
            st.success("Done")
            st.rerun()
        if st.button("SET ALL TO 99", type="primary"):
            for c in courses:
                c["price"]=99
            save(CF,courses)
            st.success("Done")
            st.rerun()
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
        st.title("Deep Maker - Step By Step Teaching")
        with st.form("add_new"):
            nt=st.text_input("New Course Name")
            npr=st.number_input("New Price", value=99, min_value=1, max_value=10000, step=1)
            sub=st.form_submit_button("ADD COURSE STEP BY STEP", type="primary")
            if sub:
                if len(nt)<3:
                    st.error("Error")
                else:
                    nid="BRAHMA"+str(1000+len(courses))
                    courses.append({"id":nid,"topic":nt,"price":int(npr)})
                    save(CF,courses)
                    make_ppt({"id":nid,"topic":nt})
                    st.success("Done - Step By Step Course")
                    st.rerun()
        sel=st.selectbox("Select For PPT", [c["topic"]+" - "+c["id"] for c in courses])
        if st.button("Make PPT Step By Step", type="primary"):
            sid=sel.split(" - ")[-1]
            stopic=" - ".join(sel.split(" - ")[:-1])
            out=make_ppt({"id":sid,"topic":stopic})
            st.success("Done - Goal Why Concept Step1-5 Practice Homework")
            st.download_button("Download Step By Step", data=out.read_bytes(), file_name=out.name)

    elif menu=="Course Library":
        st.title("Course Library - Step By Step")
        for idx,co in enumerate(courses[:20]):
            pf=list(PPT_DIR.glob(co["id"]+"*"))
            if pf:
                st.success(str(idx+1)+". "+co["topic"]+" - Rs "+str(co.get("price",99))+" - Step By Step")
                st.download_button("Download Step By Step", data=pf[0].read_bytes(), file_name=pf[0].name, key="dlc"+str(idx))

    elif menu=="UPI QR Setup":
        st.title("UPI QR Setup")
        st.write("UPI ID: "+UID)
        up=st.file_uploader("Upload QR", type=["jpg","png","jpeg"])
        if up:
            QF.write_bytes(up.getvalue())
            st.success("Done")
            st.rerun()
        if QF.exists():
            st.image(str(QF), width=300)

    elif menu=="Sales":
        st.title("Sales")
        for i,p in enumerate(purchases):
            with st.expander(str(p.get("invoice_no","Order"))):
                st.write("Name:", p.get("name"))
                st.write("Price:", "Rs "+str(p.get("price")))
                st.write("UTR:", p.get("utr"))
                st.write("Status:", p.get("status"))
                if p.get("status")=="PENDING":
                    if st.button("APPROVE", key="ap"+str(i), type="primary"):
                        p["status"]="APPROVED"
                        p["access_key"]="BRAHMA-"+secrets.token_hex(5).upper()
                        save(PF,purchases)
                        st.success("Done")
                        st.rerun()

else:
    if menu=="Browse Courses":
        st.title("Brahma Education - Step By Step Sikhane Ka Tarika")
        st.success("Har Module Me Goal Why Concept Step1 Step2 Step3 Step4 Step5 Practice Homework - Jaise Samne Sikha Rahe Ho")
        for i,course in enumerate(courses[:15]):
            with st.expander(course["topic"]+" - Rs "+str(course["price"])):
                params={"pa":UID,"pn":OWNER,"am":str(course["price"]),"cu":"INR","tn":course["topic"][:20]}
                link="upi://pay?"+urllib.parse.urlencode(params)
                st.link_button("PAY Rs "+str(course["price"]), link, type="primary")
                with st.form("buy_"+course["id"]):
                    name=st.text_input("Name", key="n"+course["id"])
                    email=st.text_input("Email", key="e"+course["id"])
                    utr=st.text_input("UTR", key="u"+course["id"])
                    if st.form_submit_button("SUBMIT"):
                        if len(name)<3 or len(email)<5 or len(utr)<5:
                            st.error("Error")
                        else:
                            purchases.append({"invoice_no":"INV"+datetime.datetime.now().strftime("%Y%m%d%H%M%S"),"access_key":"","name":name,"email":email,"course":course["topic"],"course_id":course["id"],"price":int(course["price"]),"utr":utr,"status":"PENDING","date":str(datetime.datetime.now())})
                            save(PF,purchases)
                            st.success("Done")

    elif menu=="My Access":
        st.title("My Learning - Step By Step")
        k=st.text_input("Invoice or Key")
        if st.button("UNLOCK", type="primary"):
            found=[p for p in purchases if (p.get("invoice_no")==k or p.get("access_key")==k) and p.get("status")=="APPROVED"]
            if not found:
                st.error("Error")
            else:
                pu=found[0]
                st.success("Welcome "+pu.get("name","Student")+" - Step By Step Course")
                pf=list(PPT_DIR.glob(pu.get("course_id","")+"*"))
                if pf:
                    st.download_button("DOWNLOAD STEP BY STEP 40 MODULES", data=pf[0].read_bytes(), file_name=pf[0].name, type="primary")

st.caption("Brahma V104 | Step By Step Teaching | Goal Why Concept Step1-5 Practice Homework | Price 99 | No Same Matter")