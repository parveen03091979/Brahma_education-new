import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
st.set_page_config(page_title="Brahma V106", layout="wide")
DATA=Path("data")
PPT_DIR=DATA/"ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)
CF=DATA/"courses.json"
PF=DATA/"purchases.json"
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
def init():
 data=load(CF,[])
 if len(data)<100:
  data=[]
  for i in range(100):
   data.append({"id":f"BRAHMA{1000+i}","topic":f"Course {i+1}","price":99})
  save(CF,data)
 for c in data:
  if c.get("price",999)>200:
   c["price"]=99
 save(CF,data)
 return data
courses=init()
purchases=load(PF,[])
MODS=[f"M{i}" for i in range(1,41)]
def english_txt(t,n):
 return f"{t} M{n} ENGLISH\nGOAL Master M{n}\nWHY Important\nSTEP1 Define\nSTEP2 Example\nSTEP3 Tool\nSTEP4 Practice\nSTEP5 Diary"
def hindi_txt(t,n):
 return f"{t} M{n} HINDI Translation\nLAKSHYA M{n} seekhna\nKYU Zaruri\nKADAM1 Paribhasha\nKADAM2 Udaharan\nKADAM3 Tool\nKADAM4 Abhyas\nKADAM5 Diary"
def make_bilingual(c):
 from pptx import Presentation
 from pptx.util import Inches, Pt
 cid=c["id"]
 top=c["topic"]
 en_p=PPT_DIR/(f"{cid}_ENGLISH_V100.pptx")
 hi_p=PPT_DIR/(f"{cid}_HINDI_V100.pptx")
 prs=Presentation()
 prs.slide_width=Inches(13.33)
 prs.slide_height=Inches(7.5)
 for n in range(1,41):
  s=prs.slides.add_slide(prs.slide_layouts[6])
  tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
  tf=tb.text_frame
  tf.word_wrap=True
  tf.text=f"M{n} {top} English Step By Step"
  tf.paragraphs[0].font.size=Pt(14)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=english_txt(top,n)
  bf.paragraphs[0].font.size=Pt(11)
 prs.save(str(en_p))
 prs2=Presentation()
 prs2.slide_width=Inches(13.33)
 prs2.slide_height=Inches(7.5)
 for n in range(1,41):
  s=prs2.slides.add_slide(prs2.slide_layouts[6])
  tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
  tf=tb.text_frame
  tf.word_wrap=True
  tf.text=f"M{n} {top} Hindi Translation"
  tf.paragraphs[0].font.size=Pt(14)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=hindi_txt(top,n)
  bf.paragraphs[0].font.size=Pt(11)
 prs2.save(str(hi_p))
 return en_p,hi_p
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
st.sidebar.title("Brahma V106 Fix")
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
  st.sidebar.success("Admin OK Bilingual Fixed")
  menu=st.sidebar.radio("Admin",["Dashboard","Price Manager 99","Deep Maker Bilingual","Course Library Bilingual","UPI QR Setup","Sales"])
  if st.sidebar.button("Logout"):
   st.session_state.admin_logged=False
   AS.unlink(missing_ok=True)
   st.rerun()
if st.session_state.admin_logged:
 if menu=="Dashboard":
  st.title("Dashboard Bilingual Fixed TypeError")
  st.success("Har Course 2 Files English+Hindi No TypeError Now")
  total=len(courses)
  en_c=len(list(PPT_DIR.glob("*ENGLISH*")))
  hi_c=len(list(PPT_DIR.glob("*HINDI*")))
  c1,c2,c3=st.columns(3)
  c1.metric("Total",total)
  c2.metric("English",en_c)
  c3.metric("Hindi",hi_c)
  if st.button("DELETE OLD"):
   for f in PPT_DIR.glob("*.*"):
    try:
     f.unlink()
    except:
     pass
   st.success("Done")
   st.rerun()
  if st.button("CREATE 100 BOOKS BILINGUAL", type="primary"):
   bar=st.progress(0)
   for idx,c in enumerate(courses):
    make_bilingual(c)
    bar.progress(int((idx+1)/len(courses)*100))
   st.success("Done - 2 Files Per Course Fixed")
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
 elif menu=="Deep Maker Bilingual":
  st.title("Deep Maker Bilingual Fixed")
  with st.form("add_new"):
   nt=st.text_input("New Course Name English")
   npr=st.number_input("New Price", value=99, min_value=1, max_value=10000, step=1)
   sub=st.form_submit_button("ADD COURSE BILINGUAL", type="primary")
   if sub:
    if len(nt)<3:
     st.error("Error")
    else:
     nid=f"BRAHMA{1000+len(courses)}"
     courses.append({"id":nid,"topic":nt,"price":int(npr)})
     save(CF,courses)
     make_bilingual({"id":nid,"topic":nt})
     st.success("Done")
     st.rerun()
  sel=st.selectbox("Select For PPT", [c["topic"]+" - "+c["id"] for c in courses])
  if st.button("Make Bilingual PPT", type="primary"):
   sid=sel.split(" - ")[-1]
   stopic=" - ".join(sel.split(" - ")[:-1])
   en_f,hi_f=make_bilingual({"id":sid,"topic":stopic})
   st.success("Done - English + Hindi Fixed")
   st.download_button("Download English", data=en_f.read_bytes(), file_name=en_f.name)
   st.download_button("Download Hindi", data=hi_f.read_bytes(), file_name=hi_f.name)
 elif menu=="Course Library Bilingual":
  st.title("Course Library Bilingual Fixed")
  for idx,co in enumerate(courses[:20]):
   en_files=list(PPT_DIR.glob(co["id"]+"*ENGLISH*"))
   hi_files=list(PPT_DIR.glob(co["id"]+"*HINDI*"))
   if en_files and hi_files:
    st.success(f"{idx+1}. {co['topic']} - Rs {co.get('price',99)} - 2 Files")
    col1,col2=st.columns(2)
    with col1:
     st.download_button("English", data=en_files[0].read_bytes(), file_name=en_files[0].name, key=f"en{idx}")
    with col2:
     st.download_button("Hindi", data=hi_files[0].read_bytes(), file_name=hi_files[0].name, key=f"hi{idx}")
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
     if st.button("APPROVE", key=f"ap{i}", type="primary"):
      p["status"]="APPROVED"
      p["access_key"]="BRAHMA-"+secrets.token_hex(5).upper()
      save(PF,purchases)
      st.success("Done")
      st.rerun()
else:
 if menu=="Browse Courses":
  st.title("Brahma Bilingual English+Hindi Fixed")
  st.success("Har Course 2 Files English+Hindi Price 99 No TypeError")
  for i,course in enumerate(courses[:15]):
   with st.expander(course["topic"]+" - Rs "+str(course["price"])+" - English+Hindi"):
    params={"pa":UID,"pn":OWNER,"am":str(course["price"]),"cu":"INR","tn":course["topic"][:20]}
    link="upi://pay?"+urllib.parse.urlencode(params)
    st.link_button(f"PAY Rs {course['price']} Get English+Hindi", link, type="primary")
    with st.form("buy_"+course["id"]):
     name=st.text_input("Name", key=f"n{course['id']}")
     email=st.text_input("Email", key=f"e{course['id']}")
     utr=st.text_input("UTR", key=f"u{course['id']}")
     if st.form_submit_button("SUBMIT"):
      if len(name)<3 or len(email)<5 or len(utr)<5:
       st.error("Error")
      else:
       purchases.append({"invoice_no":"INV"+datetime.datetime.now().strftime("%Y%m%d%H%M%S"),"access_key":"","name":name,"email":email,"course":course["topic"],"course_id":course["id"],"price":int(course["price"]),"utr":utr,"status":"PENDING","date":str(datetime.datetime.now())})
       save(PF,purchases)
       st.success("Done")
 elif menu=="My Access":
  st.title("My Learning Bilingual")
  k=st.text_input("Invoice or Key")
  if st.button("UNLOCK BILINGUAL", type="primary"):
   found=[p for p in purchases if (p.get("invoice_no")==k or p.get("access_key")==k) and p.get("status")=="APPROVED"]
   if not found:
    st.error("Error")
   else:
    pu=found[0]
    st.success("Welcome "+pu.get("name","Student"))
    en_files=list(PPT_DIR.glob(pu.get("course_id","")+"*ENGLISH*"))
    hi_files=list(PPT_DIR.glob(pu.get("course_id","")+"*HINDI*"))
    if en_files:
     st.download_button("DOWNLOAD ENGLISH FILE", data=en_files[0].read_bytes(), file_name=en_files[0].name, type="primary")
    if hi_files:
     st.download_button("DOWNLOAD HINDI FILE", data=hi_files[0].read_bytes(), file_name=hi_files[0].name, type="secondary")
st.caption("Brahma V106 Fix | Bilingual English+Hindi | No TypeError List Not Callable | No Cut | Stable 1.6KB")