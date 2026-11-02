import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path

st.set_page_config(page_title="Brahma V100 25 Courses Final Master Teacher", layout="wide")

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

# MASTER TEACHER - EK COURSE MEIN KYA-KYA HONA CHAHIE - AAPNE GUIDE KIYA - M POINT CHHODKAR - WAHI 23 POINTS + 40 MODULES EXPAND
MODS=[
"COURSE COVER",
"OVERVIEW WHAT IS",
"LEARNING OUTCOMES",
"PREREQUISITES",
"ROADMAP",
"TOOLS LIST",
"MODULE TITLE",
"GOAL",
"WHY IMPORTANT",
"CORE CONCEPT",
"DEEP DIVE ARCHITECTURE",
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
    
    # MASTER TEACHER 23 POINTS - EK COURSE MEIN KYA-KYA HONA CHAHIE - M POINT HATA DIYA - WHAT IS TO M40 HATA DIYA - M01-M10 HATA DIYA
    if num==1:
        return base+"1. COURSE COVER: "+topic+" Price 99 Master Teacher 40 Modules Single File 100 percent Data Har Page Alag Distinct Market Best English Only No M Point\n2. OVERVIEW: What is "+topic+" Future Market $180K-$320K 600 openings 2026 Most Demanding Top 25 Final Me Se Ek\nGOAL: After this module you can explain "+topic+" to 5 people in simple words\nWHY LEARN: Every business 2026 needs 80 percent time save Salary 3x Future proof\nCONCEPT: "+topic+" is like helper Example Check message Perceive Think Reason Type reply Act Same automation logic\nSTEP BY STEP: Step1 Choose 1 boring task Example Reply Instagram comments Step2 Open ChatGPT prompt You are social media manager friendly Step3 Connect Make.com Instagram trigger + ChatGPT Step4 Test second account comment auto reply Step5 Diary What learned What mistake Tomorrow plan\nPRACTICE: Today make 1 automation HOMEWORK: Write 3 tasks you can automate\n3. LEARNING OUTCOMES: 10 outcomes define explain build project save 2h tools clients earn portfolio final\n4. PREREQUISITES: Phone internet 1h daily No laptop No degree Village Redmi 8 Jio Rahul 1h daily 2L possible\n5. ROADMAP: Month1-2 foundation Month3 portfolio Month4 5 clients 75k Month6 agency 2L Next Module builds on previous\n6. TOOLS LIST: ChatGPT Make.com n8n Sheet WhatsApp API Canva Free vs Paid"
    
    if num==6:
        return base+"6. TOOLS LIST FOR "+topic+": ChatGPT OpenAI Make.com n8n Google Sheet WhatsApp API Canva Free vs Paid Tools Comparison\nGOAL: Understand tools for "+topic+"\nWHY: Without tools manual 8h With tools 1h Example Manual reels 4h automated 30m\nCONCEPT: Tools are engine like car engine\nSTEP BY STEP: Step1 List tools Step2 Free vs Paid Step3 How to use Step4 Click by click Step5 Diary\nPRACTICE: Open 2 tools HOMEWORK: Compare Free Paid\n12. STEP BY STEP: 5 steps Choose task Open ChatGPT prompt You are "+topic+" expert 10 years experience Connect Make.com n8n Test Diary 15m theory 15m practical daily\n13. TOOLS PRACTICAL: Which tools Free vs Paid How use click by click\n20. EXTRA TEMPLATES: prompts Make.com blueprints Sheet templates WhatsApp Canva Checklists Daily 1h Weekly Portfolio Client onboarding Cheat Sheets Tools comparison Salary Case Studies Freelancer Interview Q Freelancing Upwork Fiverr profile proposal First client 15k 5 star Referral 5 clients 75k Agency 2L Resources YouTube Docs Communities LinkedIn Discord Mentors\n21. ASSESSMENT CERTIFICATION: Quiz Assignment Final Exam Module 40 final project review Certificate Brahma Professional English Only Price 99\n22. SUPER AGENT SEO BLOG SOCIAL MEDIA: SEO Title "+topic+" Master Course 2026 Top 25 Final Price 99 Only Writer Teacher Single File Har Page Alag Distinct Blog Why Most Demanding Facebook Instagram post Marketing Copy Sales Funnel Email WhatsApp Chat Bot Price 99 UPI UTR Invoice Access Key Auto Post Daily Always Automatically Khud Karega Hamesha\n23. FULL BOOK COMPLETE DISTINCT: Pura Page Bhara Puri Knowledge Market Best 100 percent Price 99 Only Har Page Alag Distinct Good Writer Good Teacher Proper Arrange No Ulta Sidha Complete English Only Best 25 Final 100 percent Data Master Teacher Inside All Things Decided No M Formula"
    
    if num==16:
        return base+"16. REAL STORY OF SUCCESS RAHUL VILLAGE: Rahul village Redmi 8 phone Jio 1GB no laptop no degree daily 1 hour practice "+topic+"\nGOAL: Learn from real person Rahul story and avoid mistakes\nWHY: Real story gives hope exact roadmap\nCONCEPT: Rahul from village no resources only daily 1h practice\nSTEP BY STEP: Month1-2 daily 1h learning no earning focus only foundation Month3 Make portfolio 3 projects no client yet Month4 Upwork Write 20 proposals 19 reject Learn from reject reason Month4 1 USA client agrees Rs 15k Deliver extra value Get 5 star Month4 5 clients Rs 75k Month6 Agency 2L Build house for parents\nPRACTICE: Write your 6 month roadmap like Rahul HOMEWORK: What will you do daily 1 hour?\n15. CASE STUDY: Rahul village Redmi 8 Jio No Laptop 1h Daily Before Manual 4h daily After Auto 30m daily Auto 90 percent Shop Owner Client 10k per month 3 referrals proof screenshot\n19. PROJECTS: 5 Minor every 8 modules 1 small 2 Major after Module 20 Module 30 Real client ROI 1 Final Module 40 Full portfolio Behance GitHub LinkedIn 1Cr interview"
    
    if num==19:
        return base+"19. MISTAKES 90 PERCENT FAIL: Avoid 5 mistakes that make 90 percent people fail in "+topic+"\nWHY: If you avoid mistakes you save 6 months time\nCONCEPT: Mistakes are not failure but signals\nSTEP BY STEP - 5 MISTAKES: Mistake1 Foundation skip You jump to advanced Fix Do Module 1 to Module 10 twice Mistake2 Only watching videos no practice Fix 15m theory 15m practical daily Mistake3 Money chase before learning Fix First 30 days only skill no money Mistake4 No diary You forget Fix Night 10m diary 4 points Mistake5 No mentor alone Fix Join community ask doubt daily\nPRACTICE: Check which mistake you do HOMEWORK: Write your mistake correction plan\n16. MISTAKES PRO TIPS: 90 percent fail Skip foundation Fix foundation twice Only watch no practical Fix 15m theory + 15m practical Money chase Fix 30 days skill build No diary Fix 10m daily diary No mentor Fix community join Pro Tip Extra value give 2h extra work 5 star rating shortcut 6 months journey\n10. CORE CONCEPT: "+topic+" simple Perceive Reason Act Engine Example Car Engine Petrol Air Move Same AI WhatsApp check think reply auto\n11. DEEP DIVE: Definition Types How "+topic+" works Input Output Frontend Backend API When use When not use Difference"
    
    if num==20:
        return base+"20. PRO TIP SECRET DIARY: Secret pro tip toppers use diary method 10x faster\nWHY: This diary method makes you 10x faster\nCONCEPT: Toppers dont have extra time They have extra clarity\nSTEP BY STEP - PRO TIP DIARY: Step1 Night 10 PM take diary Step2 Write 4 things 1) What I learned today in "+topic+" 2) What mistake I made 3) What I will improve tomorrow 4) One new business idea Step3 Sunday 1 hour review all 7 days diary Step4 Monday plan based on review Step5 Repeat 30 days\nPRACTICE: Tonight write diary HOMEWORK: Share diary photo tomorrow\n16. PRO TIPS: Diary method Extra 2h work 5 star rating shortcut\n17. HOMEWORK: Today 15m theory + 15m practical Build mini project automate 1 task screenshot Teach to friend voice note Quiz What is "+topic+" When use Which tools\n18. NEXT STEPS: Next Module builds on Module "+str(num)+" Previous Module Revision Previous Homework"
    
    if num==39:
        return base+"39. FINAL PROJECT: Create final project and get next steps for 1Cr roadmap\nWHY: Project is your job interview No certificate needed if project strong\nCONCEPT: Final project = Problem + Solution + Workflow + Tools + Result + Portfolio Problem Identify Plan Build Test Result 10x Portfolio Behance GitHub LinkedIn This is 1Cr interview portfolio\nSTEP BY STEP - FINAL PROJECT: Step1 Choose one business problem in "+topic+" Example Shop owner needs auto reply to WhatsApp Step2 Plan solution Tools list workflow diagram on paper Step3 Build Make automation test 10 times fix bugs Step4 Result Screenshot video record Before automation 2 hours after 10 min Step5 Portfolio Upload to Behance GitHub LinkedIn with case study Step6 Next steps Freelancing profile agency plan SaaS idea\nPRACTICE: Start final project today HOMEWORK: Submit in 7 days for review Certificate after review\n19. PROJECTS: 5 Minor every 8 modules 1 small project 2 Major after Module 20 Module 30 Real client work with ROI proof 1 Final Module 40 Full portfolio Problem Identify Plan Build Test Result 10x Portfolio Behance GitHub LinkedIn 1Cr interview\n20. EXTRA: Templates prompts blueprints templates checklists cheat sheets salary case studies interview Q freelancing resources mentors"
    
    if num==40:
        return base+"40. NEXT STEPS AND CERTIFICATION: Next steps and certification for "+topic+"\nGOAL: Certificate Brahma Professional English Only Price 99 Only After final project\nWHY: Certificate is proof of skill But project is real job interview\nCONCEPT: Next steps = Freelancing Agency SaaS Daily routine\nSTEP BY STEP: Step1 Final project review by Master Teacher Step2 Certificate Step3 Freelancing profile Upwork Fiverr 20 proposals Step4 Agency plan 5 clients 75k Step5 SaaS idea Step6 Daily routine 1h learning 1h building 1h clients Step7 Weekly review Monthly scaling\nPRACTICE: Review all 40 modules HOMEWORK: Final exam Certificate after final project review\n21. ASSESSMENT CERTIFICATION: Quiz 3 to 5 questions self check Assignment practical screenshot video proof Final Exam Module 40 final project review by Master Teacher Certificate Brahma Professional English Only Price 99 Only\n22. SUPER AGENT: SEO Blog Social Media Marketing Copy Sales Funnel Email WhatsApp Chat Bot Auto Post Daily Always\n23. FULL BOOK: Pura Page Bhara Puri Knowledge Market Best 100 percent Price 99 Only Har Page Alag Distinct Good Writer Good Teacher Proper Arrange No Ulta Sidha Complete English Only Best 25 Final 100 percent Data Master Teacher Inside All Things Decided For One Course No M Formula No WHAT IS TO M40"
    
    return base+"GOAL: Master "+title+" in "+topic+" clearly\nWHY: This module is foundation for next module Skip this you fail next\nCONCEPT: "+title+" means core idea behind "+topic+" working Example Like engine in car\nSTEP BY STEP:\nStep 1: Understand definition Write in your own words\nStep 2: See 2 examples One success one failure\nStep 3: Open tool related to this module Click each option\nStep 4: Do small task 15 min practical\nStep 5: Write in diary what learned and what doubt\nPRACTICE: Today 15 min theory + 15 min practical HOMEWORK: Teach this to one friend If you can teach you learned\nMASTER TEACHER 23 POINTS: Course Cover Overview Outcomes Prereq Roadmap Tools Module Title Goal Why Important Core Deep Step Tools Practical Real Examples Client Requirements Real Story Rahul Village Project Planning Implementation Mistakes Pro Tip Expert Tools Comparison Free vs Paid Portfolio Clients Freelancing Agency Business Model Scale SEO Lead Sales Automation Optimization Case Study Daily Practice Homework Revision Final Project Next Steps Certification\nFULL BOOK: Pura Page Bhara Puri Knowledge Market Best Price 99 Only Har Page Alag Distinct Good Writer Good Teacher Proper Arrange No Ulta Sidha Complete English Only Best 25 Final No M Formula"

def make_ppt(course):
    from pptx import Presentation
    from pptx.util import Inches, Pt
    cid=course["id"]
    topic=course["topic"]
    out=PPT_DIR/(cid+"_40_MODULES_V100_25_FINAL_MASTER_TEACHER_NO_M.pptx")
    prs=Presentation()
    prs.slide_width=Inches(13.33)
    prs.slide_height=Inches(7.5)
    for n in range(1,41):
        slide=prs.slides.add_slide(prs.slide_layouts[6])
        tb=slide.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
        tf=tb.text_frame
        tf.word_wrap=True
        tf.text="Module "+str(n)+" "+topic+" - "+MODS[n-1]+" - Master Teacher 23 Points - No M Point - Final 25"
        tf.paragraphs[0].font.size=Pt(14)
        tf.paragraphs[0].font.bold=True
        bb=slide.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
        bf=bb.text_frame
        bf.word_wrap=True
        bf.text=step_content(topic,n)
        bf.paragraphs[0].font.size=Pt(10)
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

st.sidebar.title("Brahma V100 25 Courses Final Master Teacher No M")
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
        st.sidebar.success("Admin OK - V100 25 Courses Final Master Teacher No M Point")
        menu=st.sidebar.radio("Admin",["Dashboard","Price Manager 99","Deep Maker","Course Library","UPI QR Setup","Sales"])
        if st.sidebar.button("Logout"):
            st.session_state.admin_logged=False
            AS.unlink(missing_ok=True)
            st.rerun()

if st.session_state.admin_logged:
    if menu=="Dashboard":
        st.title("Dashboard - V100 25 Courses Final - Master Teacher 23 Points - No M Point")
        st.success("V100 Base Utani Hi - Sirf 100 Ki Jagah 25 Courses Final Add Kiye - Master Teacher 23 Points Add Kiye Jo Aapne Guide Kiya Ek Course Me Kya-Kya Hona Chahie - M Point Hata Diya - WHAT IS TO M40 M01-M10 Sab Hata Diya - Tested No Error No Bhagana - 25 Courses Final - Master Teacher Inside All Things - Har Module Alag Distinct Full Book Pura Page Bhara Market Best")
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
        if st.button("CREATE 25 BOOKS FINAL MASTER TEACHER 23 POINTS NO M POINT", type="primary"):
            bar=st.progress(0)
            for idx,c in enumerate(courses):
                make_ppt(c)
                bar.progress(int((idx+1)/len(courses)*100))
            st.success("Done - 25 Courses Final - Master Teacher 23 Points - No M Point - Har Module Alag Distinct Full Book Pura Page Bhara")
            st.balloons()
            st.rerun()

    elif menu=="Price Manager 99":
        st.title("Price Manager - V100 25 Courses Final")
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
        st.title("Deep Maker - V100 25 Courses Final - Master Teacher 23 Points - No M Point")
        with st.form("add_new"):
            nt=st.text_input("New Course Name - Master Teacher Command - Final 25 Me Add Hoga")
            npr=st.number_input("New Price", value=99, min_value=1, max_value=10000, step=1)
            sub=st.form_submit_button("ADD COURSE FINAL 25 MASTER TEACHER 23 POINTS NO M POINT", type="primary")
            if sub:
                if len(nt)<3:
                    st.error("Error")
                else:
                    nid="BRAHMA"+str(1000+len(courses))
                    courses.append({"id":nid,"topic":nt,"price":int(npr)})
                    save(CF,courses)
                    make_ppt({"id":nid,"topic":nt})
                    st.success("Done - Master Teacher 23 Points No M Point - Final 25 Me Add Hua")
                    st.rerun()
        sel=st.selectbox("Select For PPT", [c["topic"]+" - "+c["id"] for c in courses])
        if st.button("Make PPT Final 25 Master Teacher 23 Points No M Point", type="primary"):
            sid=sel.split(" - ")[-1]
            stopic=" - ".join(sel.split(" - ")[:-1])
            out=make_ppt({"id":sid,"topic":stopic})
            st.success("Done - Master Teacher 23 Points No M Point - Goal Why Concept Step1-5 Practice Homework")
            st.download_button("Download Final 25 Master Teacher 23 Points No M Point", data=out.read_bytes(), file_name=out.name)

    elif menu=="Course Library":
        st.title("Course Library - V100 25 Courses Final - Master Teacher 23 Points - No M Point")
        for idx,co in enumerate(courses):
            pf=list(PPT_DIR.glob(co["id"]+"*"))
           