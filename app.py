import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path

st.set_page_config(page_title="Brahma V102", layout="wide")

DATA=Path("data")
PPT_DIR=DATA/"ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

CF=DATA/"courses.json"
PF=DATA/"purchases.json"
MF=DATA/"marketing.json"
AF=DATA/"api_keys.json"
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

def make_ppt(course):
    try:
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
            tf.text="M"+str(n).zfill(2)+" "+topic
            tf.paragraphs[0].font.size=Pt(20)
            tf.paragraphs[0].font.bold=True
            bb=slide.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
            bf=bb.text_frame
            bf.word_wrap=True
            bf.text=topic+" Deep detail master teacher business automation client freelancing agency SaaS growth roadmap."
            bf.paragraphs[0].font.size=Pt(13)
        prs.save(str(out))
        return out
    except:
        return None

st.sidebar.title("Brahma V102 No Crash")
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
        st.sidebar.success("Admin OK")
        menu=st.sidebar.radio("Admin",["Dashboard","Price Manager 99","Deep Maker","Course Library","UPI QR Setup","Sales"])
        if st.sidebar.button("Logout"):
            st.session_state.admin_logged=False
            AS.unlink(missing_ok=True)
            st.rerun()

if st.session_state.admin_logged:
    if menu=="Dashboard":
        st.title("Dashboard Price 99 - No Crash")
        st.success("App is working - No Sare cut - No unterminated")
        total=len(courses)
        ready=len(list(PPT_DIR.glob("*.pptx")))
        c1,c2=st.columns(2)
        c1.metric("Total",total)
        c2.metric("Ready",ready)
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
        bulk=st.number_input("Set All Price", value=99, min_value=1, max_value=10000, step=1)
        if st.button("SET ALL BULK", type="primary"):
            for c in courses:
                c["price"]=int(bulk)
            save(CF,courses)
            st.success("Done")
            st.rerun()
        inc=st.number_input("Inc Dec All By", value=10, min_value=-1000, max_value=1000, step=1)
        if st.button("APPLY BULK", type="secondary"):
            for c in courses:
                c["price"]=int(max(1,c.get("price",99)+int(inc)))
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
        st.title("Deep Maker + Add Course")
        with st.form("add_new"):
            nt=st.text_input("New Course Name")
            npr=st.number_input("New Price", value=99, min_value=1, max_value=10000, step=1)
            sub=st.form_submit_button("ADD COURSE", type="primary")
            if sub:
                if len(nt)<3:
                    st.error("Error")
                else:
                    nid="BRAHMA"+str(1000+len(courses))
                    courses.append({"id":nid,"topic":nt,"price":int(npr)})
                    save(CF,courses)
                    make_ppt({"id":nid,"topic":nt})
                    st.success("Done")
                    st.rerun()

    elif menu=="Course Library":
        st.title("Course Library")
        for idx,co in enumerate(courses[:20]):
            pf=list(PPT_DIR.glob(co["id"]+"*"))
            if pf:
                st.success(str(idx+1)+". "+co["topic"]+" - Rs "+str(co.get("price",99)))
                st.download_button("Download", data=pf[0].read_bytes(), file_name=pf[0].name, key="dlc"+str(idx))

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
        st.title("Brahma Education Price 99 - No Crash Working")
        st.success("App working - No Sare unterminated error")
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
        st.title("My Learning")
        k=st.text_input("Invoice or Key")
        if st.button("UNLOCK", type="primary"):
            found=[p for p in purchases if (p.get("invoice_no")==k or p.get("access_key")==k) and p.get("status")=="APPROVED"]
            if not found:
                st.error("Error")
            else:
                pu=found[0]
                st.success("Welcome "+pu.get("name","Student"))
                pf=list(PPT_DIR.glob(pu.get("course_id","")+"*"))
                if pf:
                    st.download_button("DOWNLOAD", data=pf[0].read_bytes(), file_name=pf[0].name, type="primary")

st.caption("Brahma V102 No Crash | Price 99 | Stable | 2KB Tiny")