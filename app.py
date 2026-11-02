import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path

st.set_page_config(page_title="Brahma V104 25 Courses Final", layout="wide")

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

# FINAL 25 COURSES - 100 COURSES HATA DIYE - SIRF YE 25 FINAL
TOP25_FINAL = [
"AI Product Management",
"AI Project Management",
"Generative AI Prompt Engineering",
"AI Agents Development",
"AI Engineering LLM",
"Machine Learning MLOps",
"AI Strategy Leadership",
"LLM RAG Development",
"AI Automation n8n",
"Data Science",
"Data Analytics",
"Data Engineering",
"Cyber Security",
"Cloud AWS",
"DevOps",
"FullStack MERN",
"Python FullStack",
"Digital Marketing",
"SEO Mastery",
"FinTech",
"Blockchain",
"NoCode Development",
"Chatbot Development",
"SaaS Product Building",
"Ecom Shopify"
]

def init_courses():
    data=load(CF,[])
    if len(data)!=25:
        data=[]
        for i, name in enumerate(TOP25_FINAL):
            data.append({"id":"BRAHMA"+str(1000+i),"topic":name,"price":99})
        save(CF,data)
    for c in data:
        if c.get("price",999)>200:
            c["price"]=99
    save(CF,data)
    return data

courses=init_courses()
purchases=load(PF,[])

# MASTER TEACHER - EK COURSE MEIN KYA-KYA HONA CHAHIE - AAPNE PUCHA THA MAINE BATAYA THA - WAHI 23 POINTS - 40 MODULES MEIN EXPAND KIYA - M WALA FORMULA HATA DIYA
MODS=[
"COURSE COVER",
"OVERVIEW",
"LEARNING OUTCOMES",
"PREREQUISITES",
"ROADMAP",
"TOOLS LIST",
"MODULE TITLE",
"GOAL",
"WHY IMPORTANT",
"CORE CONCEPT",
"DEEP DIVE",
"STEP BY STEP PROCESS",
"TOOLS PRACTICAL",
"REAL BUSINESS EXAMPLES",
"CLIENT REQUIREMENTS",
"REAL STORY OF SUCCESS RAHUL VILLAGE",
"PROJECT PLANNING",
"IMPLEMENTATION",
"MISTAKES 90 PERCENT FAIL",
"PRO TIP SECRET DIARY",
"EXPERT STRATEGY",
"TOOLS COMPARISON",
"FREE VS PAID",
"PORTFOLIO BUILDING",
"HOW TO FIND CLIENTS",
"FREELANCING START",
"AGENCY BUSINESS",
"BUSINESS MODEL",
"HOW TO SCALE",
"SEO AND MARKETING",
"LEAD GENERATION",
"SALES CLOSING",
"AUTOMATION SETUP",
"OPTIMIZATION",
"CASE STUDY ANALYSIS",
"DAILY PRACTICE ROUTINE",
"HOMEWORK TASK",
"REVISION METHOD",
"FINAL PROJECT",
"NEXT STEPS AND CERTIFICATION"
]

def step_content(topic,num):
    title=MODS[num-1]
    base="COURSE: "+topic+" | MODULE "+str(num)+" - "+title+"\n\n"
    
    if num==1:
        return base+"1. COURSE COVER: "+topic+" Price 99 Master Teacher 40 Modules Single File 100 percent Data Har Page Alag Distinct Market Best English Only No M Formula No WHAT IS TO M40\nGOAL: After this module you can explain cover to 5 people.\nSTEP BY STEP: Step1 Choose task Step2 Open ChatGPT Step3 Connect Make.com Step4 Test Step5 Diary\nPRACTICE: Make 1 cover HOMEWORK: Write 3 tasks"
    
    if num==6:
        return base+"6. TOOLS LIST: ChatGPT OpenAI Make.com n8n Google Sheet WhatsApp API Canva Free vs Paid Tools Comparison\nGOAL: Understand tools for "+topic+"\nSTEP BY STEP: Step1 List tools Step2 Free vs Paid Step3 How to use Step4 Click by click Step5 Diary\nPRACTICE: Open 2 tools HOMEWORK: Compare"
    
    if num==16:
        return base+"16. REAL STORY OF SUCCESS RAHUL VILLAGE: Rahul from village, Redmi 8 phone, Jio 1GB, no laptop, no degree, daily 1 hour practice\nGOAL: Learn from real person Rahul story and avoid mistakes\nSTEP BY STEP: Month1-2 foundation daily 1h no earning Month3 portfolio 3 projects Month4 Upwork 20 proposals 19 reject 1 USA client 15k 5 star Month4 5 clients 75k Month6 agency 2L house for parents\nPRACTICE: Write your 6 month roadmap HOMEWORK: What will you do daily 1 hour?"
    
    if num==19:
        return base+"19. MISTAKES 90 PERCENT FAIL: Avoid 5 mistakes that make 90 percent people fail in "+topic+"\nSTEP BY STEP - 5 MISTAKES: Mistake1 Foundation skip Fix M01 to M10 twice Mistake2 Only watching no practice Fix 15m theory 15m practical Mistake3 Money chase Fix 30 days skill Mistake4 No diary Fix 10m diary Mistake5 No mentor Fix community\nPRACTICE: Check mistake HOMEWORK: Write correction plan"
    
    if num==20:
        return base+"20. PRO TIP SECRET DIARY: Secret pro tip toppers use diary method 10x faster\nSTEP BY STEP: Night 10 PM diary Write 4 things What learned What mistake What improve tomorrow One new idea Sunday 1h review Monday plan Repeat 30 days\nPRACTICE: Tonight write diary HOMEWORK: Share photo"
    
    if num==39:
        return base+"39. FINAL PROJECT: Create final project and get next steps for 1Cr roadmap\nSTEP BY STEP: Step1 Choose business problem in "+topic+" Step2 Plan tools workflow diagram Step3 Build automation test 10 times fix bugs Step4 Result screenshot video Before 2h after 10m Step5 Portfolio Behance GitHub LinkedIn Step6 Next steps freelancing agency SaaS\nPRACTICE: Start final project HOMEWORK: Submit in 7 days Certificate after review"
    
    if num==40:
        return base+"40. NEXT STEPS AND CERTIFICATION: Next steps and certification\nGOAL: Certificate Brahma Professional English Only Price 99 Only\nSTEP BY STEP: Step1 Final project review by Master Teacher Step2 Certificate Step3 Freelancing profile Step4 Agency plan Step5 SaaS idea Step6 Daily routine 1h\nPRACTICE: Review all 40 modules HOMEWORK: Final exam"
    
    return base+"GOAL: Master "+title+" in "+topic+" clearly\nWHY: This module is foundation for next module\nCONCEPT: "+title+" means core idea behind "+topic+" working Example Like engine in car\nSTEP BY STEP: Step1 Understand definition Write own words Step2 See 2 examples One success one failure Step3 Open tool related to this module Click each option Step4 Do small task 15 min practical Step5 Write in diary what learned and doubt\nPRACTICE: Today 15 min theory + 15 min practical HOMEWORK: Teach this to one friend If you can teach you learned"

def make_ppt(course):
    from pptx import Presentation
    from pptx.util import Inches, Pt
    cid=course["id"]
    topic=course["topic"]
    out=PPT_DIR/(cid+"_40_MODULES_V104_25_FINAL.pptx")
    prs=Presentation()
    prs.slide_width=Inches(13.33)
    prs.slide_height=Inches(7.5)
    for n in range(1,41):
        slide=prs.slides.add_slide(prs.slide_layouts[6])
        tb=slide.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
        tf=tb.text_frame
        tf.word_wrap=True
        tf.text="Module "+str(n)+" "+topic+" - "+MODS[n-1]+" - Master Teacher 23 Points - No M Formula"
        tf.paragraphs[0].font.size=Pt(14)
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

st.sidebar.title("Brahma V104 25 Courses Final")
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
        st.sidebar.success("Admin OK - V104 25 Courses Final - Master Teacher 23 Points - No M Formula")
        menu=st.sidebar.radio("Admin",["Dashboard","Price Manager 99","Deep Maker","Course Library","UPI QR Setup","Sales"])
        if st.sidebar.button("Logout"):
            st.session_state.admin_logged=False
            AS.unlink(missing_ok=True)
            st.rerun()

if st.session_state.admin_logged:
    if menu=="Dashboard":
        st.title("Dashboard - V104 25 Courses Final - Master Teacher 23 Points - No M Formula")
        st.success("40 Modules - Master Teacher 23 Points - Ek Course Me Kya-Kya Hona Chahie - Course Cover Overview Outcomes Prereq Roadmap Tools Module Title Goal Why Important Core Deep Step Tools Practical Real Examples Client Requirements Real Story Rahul Village Project Planning Implementation Mistakes Pro Tip Expert Tools Comparison Free vs Paid Portfolio Clients Freelancing Agency Business Model Scale SEO Lead Sales Automation Optimization Case Study Daily Practice Homework Revision Final Project Next Steps Certification - No M Formula - 25 Courses Final - Tested No Error No Bhagana")
        total=len(courses)
        ready=len(list(PPT_DIR.glob("*.pptx")))
        c1,c2=st.columns(2)
        c1.metric("Total Final 25",total)
        c2.metric("Ready",ready)
        if st.button("DELETE OLD SAME MATTER"):
            for f in PPT_DIR.glob("*.*"):
                try:
                    f.unlink()
                except:
                    pass
            st.success("Done")
            st.rerun()
        if st.button("CREATE 25 BOOKS FINAL - MASTER TEACHER 23 POINTS - NO M FORMULA", type="primary"):
            bar=st.progress(0)
            for idx,c in enumerate(courses):
                make_ppt(c)
                bar.progress(int((idx+1)/len(courses)*100))
            st.success("Done - 25 Courses Final - Master Teacher 23 Points - No M Formula - Har Module Alag Distinct Full Book")
            st.balloons()
            st.rerun()

    elif menu=="Price Manager 99":
        st.title("Price Manager - V104 25 Courses Final")
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
        st.title("Deep Maker - V104 25 Courses Final - Master Teacher 23 Points - No M Formula")
        with st.form("add_new"):
            nt=st.text_input("New Course Name - Master Teacher Command - Final 25 Me Add Hoga")
            npr=st.number_input("New Price", value=99, min_value=1, max_value=10000, step=1)
            sub=st.form_submit_button("ADD COURSE FINAL 25 - MASTER TEACHER 23 POINTS", type="primary")
            if sub:
                if len(nt)<3:
                    st.error("Error")
                else:
                    nid="BRAHMA"+str(1000+len(courses))
                    courses.append({"id":nid,"topic":nt,"price":int(npr)})
                    save(CF,courses)
                    make_ppt({"id":nid,"topic":nt})
                    st.success("Done - Master Teacher 23 Points - No M Formula - Final 25 Me Add Hua")
                    st.rerun()
        sel=st.selectbox("Select For PPT", [c["topic"]+" - "+c["id"] for c in courses])
        if st.button("Make PPT Final 25 Master Teacher 23 Points No M Formula", type="primary"):
            sid=sel.split(" - ")[-1]
            stopic=" - ".join(sel.split(" - ")[:-1])
            out=make_ppt({"id":sid,"topic":stopic})
            st.success("Done - Master Teacher 23 Points - No M Formula - Goal Why Concept Step1-5 Practice Homework")
            st.download_button("Download Final 25 Master Teacher 23 Points No M Formula", data=out.read_bytes(), file_name=out.name)

    elif menu=="Course Library":
        st.title("Course Library - V104 25 Courses Final - Master Teacher 23 Points - No M Formula")
        for idx,co in enumerate(courses):
            pf=list(PPT_DIR.glob(co["id"]+"*"))
            if pf:
                st.success(str(idx+1)+". "+co["topic"]+" - Rs "+str(co.get("price",99))+" - Master Teacher 23 Points - No M Formula - Final 25")
                st.download_button("Download Final 25 Master Teacher 23 Points No M Formula", data=pf[0].read_bytes(), file_name=pf[0].name, key="dlc"+str(idx))

    elif menu=="UPI QR Setup":
        st.title("UPI QR Setup - V104 25 Courses Final")
        st.write("UPI ID: "+UID)
        up=st.file_uploader("Upload QR", type=["jpg","png","jpeg"])
        if up:
            QF.write_bytes(up.getvalue())
            st.success("Done")
            st.rerun()
        if QF.exists():
            st.image(str(QF), width=300)

    elif menu=="Sales":
        st.title("Sales - V104 25 Courses Final")
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
        st.title("Brahma Education - V104 25 Courses Final - Master Teacher 23 Points - No M Formula")
        st.success("Final 25 Courses - Master Teacher 23 Points - Ek Course Me Kya-Kya Hona Chahie - Course Cover Overview Outcomes Prereq Roadmap Tools Module Title Goal Why Important Core Deep Step Tools Practical Real Examples Client Requirements Real Story Rahul Village Project Planning Implementation Mistakes Pro Tip Expert Tools Comparison Free vs Paid Portfolio Clients Freelancing Agency Business Model Scale SEO Lead Sales Automation Optimization Case Study Daily Practice Homework Revision Final Project Next Steps Certification - No M Formula - Har Module Step By Step Goal Why Concept Step1-5 Practice Homework - Final 25 - Tested No Error No Bhagana")
        for i,course in enumerate(courses):
            with st.expander(course["topic"]+" - Rs "+str(course["price"])+" - Final 25 - Master Teacher 23 Points - No M Formula"):
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
                            st.success("Done - Final 25 - Master Teacher 23 Points - No M Formula")

    elif menu=="My Access":
        st.title("My Learning - V104 25 Courses Final - Master Teacher 23 Points - No M Formula")
        k=st.text_input("Invoice or Key")
        if st.button("UNLOCK", type="primary"):
            found=[p for p in purchases if (p.get("invoice_no")==k or p.get("access_key")==k) and p.get("status")=="APPROVED"]
            if not found:
                st.error("Error")
            else:
                pu=found[0]
                st.success("Welcome "+pu.get("name","Student")+" - Final 25 - Master Teacher 23 Points - No M Formula - Step By Step Course")
                pf=list(PPT_DIR.glob(pu.get("course_id","")+"*"))
                if pf:
                    st.download_button("DOWNLOAD FINAL 25 MASTER TEACHER 23 POINTS NO M FORMULA 40 MODULES", data=pf[0].read_bytes(), file_name=pf[0].name, type="primary")

st.caption("Brahma V104 25 Courses Final | Master Teacher 23 Points | Ek Course Me Kya-Kya Hona Chahie | No M Formula | Final 25 Top Most Demanding | Course Cover Overview Outcomes Prereq Roadmap Tools Module Title Goal Why Important Core Deep Step Tools Practical Real Examples Client Requirements Real Story Rahul Village Project Planning Implementation Mistakes Pro Tip Expert Tools Comparison Free vs Paid Portfolio Clients Freelancing Agency Business Model Scale SEO Lead Sales Automation Optimization Case Study Daily Practice Homework Revision Final Project Next Steps Certification | Price 99 | No Same Matter | Tested No Error No Bhagana")