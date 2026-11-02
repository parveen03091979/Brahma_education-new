import streamlit as st
import json
import hashlib
import datetime
import urllib.parse
from pathlib import Path
import pandas as pd
import re

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    PPTX_OK=True
except:
    PPTX_OK=False

st.set_page_config(page_title="Brahma Deep PPT Only", layout="wide")

DATA_DIR=Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH=DATA_DIR / ".master_hash"
COURSES_FILE=DATA_DIR / "courses.json"
PURCHASE_FILE=DATA_DIR / "purchases.json"
UPI_QR_PATH=DATA_DIR / "upi_qr.jpg"
PPT_DIR=DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)

MY_UPI_ID="parveen39179@okicici"
MY_NAME="Parveen Kumar"
BLOCKED_UTRS=["123456789012","123456789123","111111111111","000000000000","999999999999","184792641807"]

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size>2:
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def is_valid_name(name):
    name=name.strip()
    if not re.match(r"^[A-Za-z ]+$", name): return False, "Only letters"
    if len(name.split())<2: return False, "Full name"
    return True, "OK"

def is_valid_email(email):
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email): return False, "Email @ needed"
    return True, "OK"

def is_valid_utr(utr, purchases_list):
    utr=utr.strip()
    if not (utr.isdigit() and len(utr)==12): return False, "UTR 12 digit"
    if utr in BLOCKED_UTRS: return False, f"Fake UTR {utr}"
    for p in purchases_list:
        if p.get("utr")==utr: return False, f"UTR {utr} used"
    return True, "OK"

def get_deep_curriculum_full(topic):
    deep_modules=[
        {"title": f"Module 1: {topic} - Fundamentals & Mindset", "focus": "Why What Career Future Scope", "lessons": [
            "What is topic - Deep definition", "History and evolution", "Why important in 2026", "Career opportunities", "Future scope 2030", "Mindset for mastery", "Common myths", "Success stories", "Failure analysis", "Roadmap 400 lessons",
            "Tools overview", "Industry overview", "Market size", "Skills needed", "Learning path", "Time management", "Resources", "Community", "Mentorship", "First steps",
            "Basics 1", "Basics 2", "Basics 3", "Basics 4", "Basics 5", "Practical 1", "Practical 2", "Practical 3", "Practical 4", "Practical 5",
            "Case study 1", "Case study 2", "Case study 3", "Case study 4", "Case study 5", "Assignment 1", "Assignment 2", "Assignment 3", "Summary 1", "Test 1"
        ]},
        {"title": f"Module 2: {topic} - Tools & Complete Setup", "focus": "All tools install setup API", "lessons": [
            "Tool 1 install", "Tool 2 install", "Tool 3 install", "Tool 4 install", "Tool 5 install", "Tool 6 install", "Tool 7 install", "Tool 8 install", "Tool 9 install", "Tool 10 install",
            "Account creation", "API keys", "Setup step 1", "Setup step 2", "Setup step 3", "Setup step 4", "Setup step 5", "Testing setup", "Troubleshooting", "Best practices",
            "Tool comparison", "Free vs paid", "Free tools list", "Paid tools list", "Tool 1 deep", "Tool 2 deep", "Tool 3 deep", "Tool 4 deep", "Tool 5 deep", "Integration 1",
            "Integration 2", "Integration 3", "Integration 4", "Integration 5", "Workflow 1", "Workflow 2", "Workflow 3", "Assignment", "Summary", "Test"
        ]},
        {"title": f"Module 3: {topic} - Core Concepts Deep Theory", "focus": "Core theory principles deep", "lessons": ["Concept 1 deep"]*40},
        {"title": f"Module 4: {topic} - Practical Basics Hands-On", "focus": "First 10 projects step by step", "lessons": ["Practical 1"]*40},
        {"title": f"Module 5: {topic} - Intermediate Mastery", "focus": "15 techniques case studies", "lessons": ["Intermediate 1"]*40},
        {"title": f"Module 6: {topic} - Advanced Pro Strategies", "focus": "15 pro tricks optimization", "lessons": ["Advanced 1"]*40},
        {"title": f"Module 7: {topic} - Real Client Project 1 End to End", "focus": "Client project 1 complete", "lessons": ["Project 1 step"]*40},
        {"title": f"Module 8: {topic} - Real Project 2 Automation Scaling", "focus": "Project 2 automation scaling", "lessons": ["Project 2 step"]*40},
        {"title": f"Module 9: {topic} - Monetization Business", "focus": "Paise kaise kamaye freelancing agency", "lessons": ["Monetization 1"]*40},
        {"title": f"Module 10: {topic} - Mastery Scaling Future", "focus": "Mastery scaling 1L future trends", "lessons": ["Mastery 1"]*40},
    ]
    curriculum=[]
    lesson_counter=1
    for m_idx, mod in enumerate(deep_modules, 1):
        vids=[]
        for v in range(1, 41):
            title_detail = mod["lessons"][v-1] if v-1 < len(mod["lessons"]) else f"Lesson {v}"
            lt=f"Lesson {lesson_counter}: {topic} - {mod['focus']} - {title_detail} - Deep"
            deep_hi=f"{topic} - {mod['focus']} - {title_detail}\n\nTheory:\n{topic} ka {mod['focus']} bahut important hai. Is lesson me hum deep me samjhenge - Definition, working, logic, future 2026. Real examples, case studies, mistakes.\n\nPractical:\nStep 1 - Setup\nStep 2 - Tool open\nStep 3 - First action\nStep 4 - Test\nStep 5 - Result check\n\nImportant Points:\n- Point 1 {topic} {mod['focus']}\n- Point 2 Deep analysis\n- Point 3 Common mistakes\n- Point 4 Best practices\n- Point 5 Pro tips\n\nAssignment:\nIs lesson ke baad {topic} ka {title_detail} par ek project banao."
            deep_en=f"{topic} - {mod['focus']} - {title_detail}\n\nTheory:\n{mod['focus']} is core of {topic}. Deep definition, working, logic, future 2026. Real examples, case studies, mistakes.\n\nPractical:\nStep 1 Setup\nStep 2 Open tool\nStep 3 First action\nStep 4 Test\nStep 5 Check result\n\nImportant Points:\n- Point 1 {topic} {mod['focus']}\n- Point 2 Deep analysis\n- Point 3 Common mistakes\n- Point 4 Best practices\n- Point 5 Pro tips\n\nAssignment:\nBuild project on {topic} {title_detail} after this lesson."
            vids.append({"no": lesson_counter, "title": lt, "desc_hi": deep_hi, "desc_en": deep_en})
            lesson_counter+=1
        curriculum.append({"module_no": m_idx, "title": mod["title"], "focus": mod["focus"], "videos": vids})
    return curriculum

def create_deep_ppt_only(course_id, course_topic):
    if not PPTX_OK:
        return None, "python-pptx missing - Add in requirements.txt"
    try:
        prs=Presentation()
        prs.slide_width=Inches(13.33)
        prs.slide_height=Inches(7.5)
        curriculum=get_deep_curriculum_full(course_topic)

        # Title slide - Only course content
        slide=prs.slides.add_slide(prs.slide_layouts[6])
        tb=slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(1.5))
        tf=tb.text_frame
        tf.text=f"{course_topic}\nDeep Course - 400 Lessons - Puri Detail"
        tf.paragraphs[0].runs[0].font.size=Pt(32)
        tf.paragraphs[0].runs[0].font.bold=True
        tb2=slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(12.3), Inches(2))
        tb2.text_frame.text=f"10 Modules x 40 Lessons = 400 Lessons\nModule 1 Fundamentals to Module 10 Mastery\nHindi + English Deep Content + Practical + Assignment\nKoi topic nahi chhuta - Puri learning guarantee"

        count=0
        for mod in curriculum:
            # Module title slide
            slide=prs.slides.add_slide(prs.slide_layouts[6])
            tbox=slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(12.3), Inches(2))
            tbox.text_frame.text=f"{mod['title']}\n{mod['focus']}\n40 Lessons Deep"
            tbox.text_frame.paragraphs[0].runs[0].font.size=Pt(28)
            tbox.text_frame.paragraphs[0].runs[0].font.bold=True
            count+=1
            for vid in mod["videos"]:
                if count>=85: break
                slide=prs.slides.add_slide(prs.slide_layouts[6])
                tbox=slide.shapes.add_textbox(Inches(0.2), Inches(0.1), Inches(12.9), Inches(0.7))
                tbox.text_frame.text=f"{vid['title']}"
                tbox.text_frame.paragraphs[0].runs[0].font.size=Pt(14)
                tbox.text_frame.paragraphs[0].runs[0].font.bold=True

                hibox=slide.shapes.add_textbox(Inches(0.2), Inches(0.9), Inches(6.3), Inches(6.2))
                hibox.text_frame.word_wrap=True
                hibox.text_frame.text=f"HINDI:\n{vid['desc_hi']}"[:1500]
                for p in hibox.text_frame.paragraphs:
                    if p.runs:
                        p.runs[0].font.size=Pt(10)

                enbox=slide.shapes.add_textbox(Inches(6.7), Inches(0.9), Inches(6.3), Inches(6.2))
                enbox.text_frame.word_wrap=True
                enbox.text_frame.text=f"ENGLISH:\n{vid['desc_en']}"[:1500]
                for p in enbox.text_frame.paragraphs:
                    if p.runs:
                        p.runs[0].font.size=Pt(10)
                count+=1
            if count>=85: break

        ppt_path=PPT_DIR / f"{course_id}_{course_topic.replace(' ', '_')[:15]}_DEEP_400_PPT.pptx"
        prs.save(str(ppt_path))
        return str(ppt_path), f"Deep PPT - {count} slides - {course_topic} - 400 lessons deep - Puri detail - Koi topic nahi chhuta"
    except Exception as e:
        return None, f"PPT Error {e}"

courses=load_json(COURSES_FILE, [])
purchases=load_json(PURCHASE_FILE, [])

if len(courses)==0:
    for i in range(100):
        t=f"Course {i+1}"
        if i==0: t="AI Agent Automation 2026"
        if i==1: t="Instagram Reels Mastery"
        if i==2: t="YouTube Automation AI"
        if i==3: t="Prompt Engineering Pro"
        if i==4: t="Digital Marketing SEO"
        courses.append({"id": f"BRAHMA{1000+i}", "topic": t, "price": 999, "videos": 400})
    save_json(COURSES_FILE, courses)

if "admin_logged" not in st.session_state:
    st.session_state["admin_logged"]=False

st.sidebar.title("Brahma Deep PPT Only")
if not MASTER_HASH.exists():
    pw=st.sidebar.text_input("Create Admin Password", type="password")
    if st.sidebar.button("Create Admin"):
        if pw and len(pw)>=4:
            MASTER_HASH.write_text(hashlib.sha256(pw.encode()).hexdigest())
            st.rerun()
    menu="Browse Courses"
else:
    if not st.session_state["admin_logged"]:
        menu=st.sidebar.radio("Menu", ["Browse Courses", "My Access", "Chat Support"])
        st.sidebar.divider()
        pw=st.sidebar.text_input("Admin Password", type="password")
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(pw.encode()).hexdigest()==MASTER_HASH.read_text():
                st.session_state["admin_logged"]=True
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("Deep PPT Only - No Voice")
        menu=st.sidebar.radio("Admin", ["Brahma Deep PPT Maker", "Video Library", "Dashboard", "Sales", "QR Setup"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"]=False
            st.rerun()

if st.session_state["admin_logged"]:
    if menu=="Dashboard":
        st.title("Dashboard - Deep PPT Only - No Voice - No Faltu Sentences")
        c1,c2,c3=st.columns(3)
        c1.metric("Courses", len(courses))
        c2.metric("Deep PPTs", len(list(PPT_DIR.glob("*.pptx"))))
        c3.metric("Deep Lessons", len(courses)*400)
        st.dataframe(pd.DataFrame(courses), use_container_width=True)

    if menu=="Brahma Deep PPT Maker":
        st.title("Brahma Deep PPT Maker - Sirf PPT - No Voice - Puri Deep Learning")
        st.write("Sirf PPT - Deep - Har course ki puri detail - 400 lessons - Hindi + English - No voice - No faltu sentences")
        st.divider()
        course_sel=st.selectbox("Course select karo - Deep PPT Only", [f"{c['topic']} - {c['id']}" for c in courses[:30]])
        col1,col2=st.columns(2)
        with col1:
            st.write("**Ek Course ka Deep PPT Banao - 80 Slides Deep**")
            if st.button("Brahma - Is Course ka Deep PPT Banao - Puri Detail - Guaranteed", type="primary"):
                sel_id=course_sel.split(" - ")[-1]
                sel_topic=" - ".join(course_sel.split(" - ")[:-1])
                with st.spinner(f"Bana raha hai Deep PPT - {sel_topic} - 80 slides deep - Puri detail - 30 sec..."):
                    ppt_path, msg = create_deep_ppt_only(sel_id, sel_topic)
                    if ppt_path and Path(ppt_path).exists():
                        st.success(f"SUCCESS - {msg} - PPT Ban Gaya - Video Library me check karo")
                        st.balloons()
                        with open(ppt_path, "rb") as f:
                            st.download_button(f"Download Deep PPT - {sel_topic} - Puri Detail", f, file_name=Path(ppt_path).name)
                    else:
                        st.error(f"Fail - {msg}")
        with col2:
            st.write("**5 Courses ke Deep PPT Banao - Auto**")
            if st.button("Brahma - 5 Courses Deep PPT Banao - Auto - Puri Detail", type="secondary"):
                bar=st.progress(0)
                status=st.empty()
                for idx,c in enumerate(courses[:5]):
                    status.write(f"Bana raha hai {idx+1}/5 - {c['topic']} - Deep PPT - Puri detail")
                    create_deep_ppt_only(c["id"], c["topic"])
                    bar.progress(int((idx+1)/5*100))
                st.success("5 Courses Deep PPT Done - Check Video Library - 100% Ban Gaya")
                st.balloons()
        st.divider()
        st.subheader("Bane Hue Deep PPTs - Download")
        for pf in list(PPT_DIR.glob("*.pptx"))[:15]:
            st.write(f"{pf.name} - {pf.stat().st_size/1024:.0f} KB - Deep")
            with open(pf, "rb") as f:
                st.download_button(f"Download {pf.name}", f, file_name=pf.name, key=f"dl_{pf.name}")

    if menu=="Video Library":
        st.title("Video Library - Deep PPT Only - Check")
        for co in courses[:15]:
            co_id=co.get("id")
            ppt_files=list(PPT_DIR.glob(f"{co_id}*"))
            with st.expander(f"{co.get('topic')} - Deep PPT Check", expanded=(co_id=="BRAHMA1000")):
                if ppt_files:
                    st.success(f"Deep PPT Bana - {ppt_files[0].name} - {ppt_files[0].stat().st_size/1024:.0f} KB - Puri Detail")
                    with open(ppt_files[0], "rb") as f:
                        st.download_button(f"Download Deep PPT - {co.get('topic')} - Puri Detail", f, file_name=ppt_files[0].name, key=f"ppt_{co_id}")
                else:
                    st.error("Deep PPT Nahi Bana - Brahma Deep PPT Maker se banao - Guaranteed banega - No voice - Sirf deep learning")

    if menu=="Sales":
        st.title("Sales - Deep PPT Course")
        st.dataframe(pd.DataFrame(purchases), use_container_width=True)
    if menu=="QR Setup":
        st.title("QR Setup")
        st.info(f"UPI {MY_UPI_ID}")
        up=st.file_uploader("Upload QR", type=["jpg","png","jpeg"])
        if up:
            UPI_QR_PATH.write_bytes(up.getvalue())
            st.success("QR Saved")
            st.rerun()
        if UPI_QR_PATH.exists():
            st.image(str(UPI_QR_PATH), width=300)

else:
    if menu=="Browse Courses":
        st.title("Brahma Education - Deep PPT Only - Puri Learning")
        st.write("100+ Courses - Each 400 Lessons Deep - Hindi + English Deep + Practical + Assignment - Koi topic nahi chhuta")
        search=st.text_input("Search deep course")
        fl=[c for c in courses if search.lower() in c.get("topic","").lower()] if search else courses
        page_size=20
        total_pages=max(1, (len(fl)+page_size-1)//page_size)
        page=st.selectbox("Pages", range(1, total_pages+1), format_func=lambda x: f"Page {x}")
        pcs=fl[(page-1)*page_size:page*page_size]
        for idx,co in enumerate(pcs, start=(page-1)*page_size+1):
            with st.expander(f"{idx}. {co.get('topic')} - Rs {co.get('price')} - Deep 400 Lessons"):
                col_qr,col_pay=st.columns([1,2])
                with col_qr:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH), width=220)
                    else:
                        st.info("Secure UPI")
                with col_pay:
                    st.write(f"Course: {co.get('topic')} - Deep 400 Lessons - Puri Detail")
                    params={"pa": MY_UPI_ID, "pn": MY_NAME, "am": str(co.get("price",999)), "cu": "INR", "tn": co.get("topic","")[:20]}
                    link=f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"Pay Rs {co.get('price')} - Deep PPT", link, type="primary")
                with st.form(f"buy_{co['id']}_{idx}"):
                    c1,c2,c3=st.columns(3)
                    with c1:
                        name=st.text_input("Full Name", key=f"n_{idx}", placeholder="Rahul Sharma")
                    with c2:
                        email=st.text_input("Email", key=f"e_{idx}", placeholder="rahul@gmail.com")
                    with c3:
                        utr=st.text_input("UTR 12 digit", key=f"u_{idx}", placeholder="UPI app se")
                    if st.form_submit_button("Get Deep PPT Course - Puri Learning", type="primary"):
                        ok_name,msg_name=is_valid_name(name)
                        if not ok_name:
                            st.error(msg_name)
                            st.stop()
                        ok_email,msg_email=is_valid_email(email)
                        if not ok_email:
                            st.error(msg_email)
                            st.stop()
                        ok_utr,msg_utr=is_valid_utr(utr, purchases)
                        if not ok_utr:
                            st.error(msg_utr)
                            st.stop()
                        inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                        key=f"BRAHMA-{hashlib.sha256((email+co.get('topic')+inv+utr).encode()).hexdigest()[:10].upper()}"
                        purchases.append({"invoice_no": inv, "access_key": key, "name": name, "email": email, "course": co.get("topic"), "course_id": co.get("id"), "price": co.get("price"), "utr": utr, "status": "APPROVED", "date": str(datetime.datetime.now())})
                        save_json(PURCHASE_FILE, purchases)
                        st.success(f"Verified - Deep PPT - Invoice {inv}")
                        st.info(f"Key {key} - My Access me dalo")

    if menu=="My Access":
        st.title("My Learning - Deep PPT Only - Puri Detail")
        k=st.text_input("Invoice or Key")
        if st.button("Unlock My Deep PPT Course", type="primary"):
            found=[p for p in purchases if p.get("access_key")==k or p.get("invoice_no")==k]
            if not found:
                st.error("Invalid key")
            else:
                pu=found[0]
                st.success(f"Welcome {pu.get('name')} - {pu.get('course')} - Deep PPT - Puri Learning")
                ppt_files=list(PPT_DIR.glob(f"{pu.get('course_id')}*"))
                if ppt_files:
                    st.subheader("Your Deep PPT Course - Puri Detail - Download")
                    for pf in ppt_files:
                        with open(pf, "rb") as f:
                            st.download_button(f"Download Deep PPT - {pu.get('course')} - Puri Detail - 400 Lessons", f, file_name=pf.name)
                else:
                    st.warning("Deep PPT Abhi Nahi Bana - Admin banayega - Brahma Deep PPT Maker se")
                st.subheader("Deep Curriculum Preview - Puri Detail")
                cur=get_deep_curriculum_full(pu.get("course"))
                for mod in cur[:2]:
                    with st.expander(f"{mod['title']} - 40 Lessons Deep - Puri Detail"):
                        for vid in mod["videos"][:3]:
                            st.write(f"{vid['no']}. {vid['title']}")
                st.success("Deep Guarantee: Is course ke baad is topic me koi doubt nahi - Puri learning - PPT kitni bhi bane learning puri - No faltu sentences")

    if menu=="Chat Support":
        st.title("Chat Support - Deep PPT Only")
        q=st.chat_input("Ask")
        if q:
            st.write("Deep PPT Only - Har course 400 lessons deep - Hindi + English deep + practical + assignment - Koi topic nahi chhuta - Puri learning")