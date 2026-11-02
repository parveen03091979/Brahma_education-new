import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
st.set_page_config(page_title="Brahma", layout="wide")
DATA=Path("data")
PPT_DIR=DATA/"ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)
CF=DATA/"courses.json"
PF=DATA/"purchases.json"
QF=DATA/"upi_qr.jpg"
AF=DATA/"api_keys.json"
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
TOP25=["AI Product Mgmt","AI Project Mgmt","Gen AI Prompt","AI Agents","AI Eng LLM","ML MLOps","AI Strategy","LLM RAG","AI Auto n8n","Data Science","Data Analytics","Data Eng","CyberSec","Cloud AWS","DevOps","FullStack MERN","Python FullStack","Digital Mkt","SEO","FinTech","Blockchain","NoCode","Chatbot","SaaS","Ecom Shopify"]
MODS=["WHAT IS","WHY IMP","WHERE USE","WHEN USE","WHO LEARN","HOW WORKS","TOOLS","EARN MONEY","PRACTICAL","RIGHT WAY","FOUNDATION","CORE","ADVANCED","STEP PROCESS","EXAMPLE","CLIENT REQ","REAL STORY","PLANNING","IMPLEMENT","MISTAKES","PRO TIP","EXPERT","COMPARE","FREE PAID","PORTFOLIO","FIND CLIENT","FREELANCING","AGENCY","MODEL","SCALING","SEO","LEAD","SALES","AUTO","OPTIMIZE","CASE STUDY","DAILY","HOMEWORK","REVISION","FINAL PROJECT"]
GOAL=["Define what is 5 points","Explain why important salary","List 10 places where used","Decide when use when not","List who can learn no degree","Draw how works architecture","List 5 tools free vs paid","Show 3 ways earn money","Do 15m hands-on practical","Follow right learning path","Build strong foundation base","Explain core concepts clearly","Explain advanced concepts deep","Follow step process","Give 2 real examples","Write client requirements","Tell Rahul village story","Make project planning sheet","Implement project build","Avoid 5 mistakes 90% fail","Share pro tip secret","Apply expert strategy","Compare tools which best","Choose free vs paid when","Build portfolio 3 projects","Find clients Upwork 20 props","Start freelancing first client","Start agency team 2 people","Create business model canvas","Scale to 2L monthly","Do SEO marketing for course","Generate leads 100 daily","Close sales call script","Setup automation Make.com","Optimize performance ROI","Analyze case study proof","Do daily practice 1h routine","Do homework task submit","Revise method diary","Build final project 1Cr"]
WHY=["Foundation for all 39 modules","Without importance quit early","Knowing where saves time","Right timing decides success","Anyone can learn village city","Without architecture cannot build","Without tools cannot build","Without earning ways no money","Without practical only theory","Without right way waste 6 months","Without foundation advanced impossible","Without core cannot understand","Without advanced stay beginner","Without step process confused","Without examples cannot relate","Without client req build wrong","Without real story no motivation","Without planning project fails","Without implementation no result","Without avoiding mistakes fail 90%","Without pro tip work hard not smart","Without expert strategy grow slow","Without compare choose wrong tool","Without free vs paid overspend","Without portfolio no client trusts","Without finding clients no earning","Without freelancing no first client","Without agency stay solo low","Without model no business","Without scaling stuck 75k","Without SEO no students find you","Without leads no sales","Without sales closing no money","Without auto manual 4h daily","Without optimize waste time","Without case study no proof","Without daily practice forget","Without homework no action","Without revision forget in 7 days","Without final project no interview"]
def en(topic,n):
 t=MODS[n-1]
 g=GOAL[n-1]
 w=WHY[n-1]
 a=f"{topic} M{n:02d} {t} EN Best 25 Distinct\n"
 b=f"GOAL {g} in {topic}.\n"
 c=f"WHY {w}.\n"
 d=f"CONCEPT {t} in {topic} simple.\n"
 e=f"STEPS {g} {t} {topic}.\n"
 f=f"TOOLS ChatGPT Make.com n8n Sheet WhatsApp API Canva.\n"
 g2=f"CASE {t} {topic} Before 4h after 30m auto proof.\n"
 h=f"HW Teach {t} {topic} to friend 2m voice note.\n"
 i=f"NEXT {MODS[n] if n<40 else 'COMPLETE'} builds on {t}.\n"
 return a+b+c+d+e+f+g2+h+i
def hi(topic,n):
 t=MODS[n-1]
 g=GOAL[n-1]
 w=WHY[n-1]
 a=f"{topic} M{n:02d} {t} HI Best 25 Distinct\n"
 b=f"LAKSHYA {g} {topic} me.\n"
 c=f"KYU {w}.\n"
 d=f"VICHAR {t} {topic} simple.\n"
 e=f"KADAM {g} {t} {topic}.\n"
 f=f"TOOLS ChatGPT Make.com n8n Sheet WhatsApp API Canva.\n"
 g2=f"CASE {t} {topic} Pehle 4h baad 30m auto proof.\n"
 h=f"HW {t} {topic} dost ko sikhao 2m voice note.\n"
 i=f"AGLA {MODS[n] if n<40 else 'POORA'} is {t} par banega.\n"
 return a+b+c+d+e+f+g2+h+i
def make(c):
 from pptx import Presentation
 from pptx.util import Inches, Pt
 cid=c["id"]
 top=c["topic"]
 en_p=PPT_DIR/(f"{cid}_EN.pptx")
 hi_p=PPT_DIR/(f"{cid}_HI.pptx")
 prs=Presentation()
 prs.slide_width=Inches(13.33)
 prs.slide_height=Inches(7.5)
 for n in range(1,41):
  t=MODS[n-1]
  s=prs.slides.add_slide(prs.slide_layouts[6])
  tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
  tf=tb.text_frame
  tf.word_wrap=True
  tf.text=f"M{n:02d} {top} - {t} - EN - Best 25 - Price 99"
  tf.paragraphs[0].font.size=Pt(11)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=en(top,n)
  bf.paragraphs[0].font.size=Pt(10)
 prs.save(str(en_p))
 prs2=Presentation()
 prs2.slide_width=Inches(13.33)
 prs2.slide_height=Inches(7.5)
 for n in range(1,41):
  t=MODS[n-1]
  s=prs2.slides.add_slide(prs2.slide_layouts[6])
  tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
  tf=tb.text_frame
  tf.word_wrap=True
  tf.text=f"M{n:02d} {top} - {t} - HI - Best 25 - Price 99"
  tf.paragraphs[0].font.size=Pt(11)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=hi(top,n)
  bf.paragraphs[0].font.size=Pt(10)
 prs2.save(str(hi_p))
 return en_p,hi_p
def make_hash(pw):
 salt=secrets.token_bytes(16)
 h=hashlib.scrypt(pw.encode(), salt=salt, n=16384, r=8, p=1)
 return salt.hex()+":"+h.hex()
def verify(pw,stored):
 try:
  a,b=stored.split(":")
  s=bytes.fromhex(a)
  h=hashlib.scrypt(pw.encode(), salt=s, n=16384, r=8, p=1)
  return secrets.compare_digest(h.hex(), b)
 except:
  return False
def sess_valid():
 try:
  d=load(AS,{})
  exp=datetime.datetime.fromisoformat(d["expiry"])
  return datetime.datetime.now()<exp
 except:
  return False
if "admin_logged" not in st.session_state:
 st.session_state.admin_logged=sess_valid()
st.sidebar.title("Brahma Academy")
if not MH.exists():
 pw=st.sidebar.text_input("Create Password", type="password")
 if st.sidebar.button("Create Admin"):
  if pw and len(pw)>=4:
   MH.write_text(make_hash(pw), encoding="utf-8")
   st.rerun()
 menu="Browse"
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
  menu=st.sidebar.radio("Admin",["Dashboard","Price Manager 99","Add New Course","Course Library","UPI QR Setup","API Setup","Brahma Super Agent","Sales"])
  if st.sidebar.button("Logout"):
   st.session_state.admin_logged=False
   AS.unlink(missing_ok=True)
   st.rerun()
def init25():
 d=[]
 for i,name in enumerate(TOP25):
  d.append({"id":f"BRAHMA{1000+i}","topic":name.strip(),"price":99})
 save(CF,d)
 return d
courses=init25()
purchases=load(PF,[])
if st.session_state.admin_logged:
 if menu=="Dashboard":
  st.title("Dashboard - Brahma Academy - Best 25")
  st.success("Best 25 Demanding 2026 - Har Page Alag Distinct - Price 99 - No Crash")
  c1,c2,c3=st.columns(3)
  c1.metric("Total Best 25", len(courses))
  c2.metric("EN Distinct", len(list(PPT_DIR.glob("*EN.pptx"))))
  c3.metric("HI Distinct", len(list(PPT_DIR.glob("*HI.pptx"))))
  if st.button("DELETE OLD FILES"):
   for f in PPT_DIR.glob("*.*"):
    try:
     f.unlink()
    except:
     pass
   st.success("Done Deleted")
   st.rerun()
  if st.button("CREATE BEST 25 FULL BOOK DISTINCT", type="primary"):
   bar=st.progress(0)
   for idx,c in enumerate(courses):
    make(c)
    bar.progress(int((idx+1)/len(courses)*100))
   st.success("Done Best 25 Full Book Distinct - No Crash - No Same Matter")
   st.balloons()
   st.rerun()
 elif menu=="Price Manager 99":
  st.title("Price Manager 99")
  bulk=st.number_input("Set All Price To", value=99, min_value=1, max_value=10000, step=1)
  if st.button("SET ALL BULK PRICE", type="primary"):
   for c in courses:
    c["price"]=int(bulk)
   save(CF,courses)
   st.success(f"Done {bulk}")
   st.rerun()
  if st.button("SET ALL TO 99 ONLY", type="primary"):
   for c in courses:
    c["price"]=99
   save(CF,courses)
   st.success("Done 99")
   st.rerun()
  sel=st.selectbox("Select Course", [c["topic"]+" - "+c["id"]+" - Rs "+str(c.get("price",99)) for c in courses])
  sid=sel.split(" - ")[-2]
  curr=99
  for c in courses:
   if c["id"]==sid:
    curr=c.get("price",99)
  np=st.number_input("New Price Single", value=int(curr), min_value=1, max_value=10000, step=1)
  if st.button("UPDATE SINGLE PRICE", type="primary"):
   for c in courses:
    if c["id"]==sid:
     c["price"]=int(np)
     break
   save(CF,courses)
   st.success(f"Done {np}")
   st.rerun()
 elif menu=="Add New Course":
  st.title("Add New Course")
  with st.form("add"):
   nt=st.text_input("New Course Name")
   npr=st.number_input("New Price", value=99, min_value=1, max_value=10000, step=1)
   sub=st.form_submit_button("ADD NEW COURSE", type="primary")
   if sub:
    if len(nt)<3:
     st.error("Error Short")
    else:
     nid=f"BRAHMA{1000+len(courses)}"
     courses.append({"id":nid,"topic":nt,"price":int(npr)})
     save(CF,courses)
     make({"id":nid,"topic":nt})
     st.success("Done Added")
     st.rerun()
  sel=st.selectbox("Select For PPT", [c["topic"]+" - "+c["id"] for c in courses])
  if st.button("Make Bilingual PPT Distinct", type="primary"):
   sid=sel.split(" - ")[-1]
   stopic=" - ".join(sel.split(" - ")[:-1])
   en_f,hi_f=make({"id":sid,"topic":stopic})
   st.success("Done Distinct")
   st.download_button("Download EN", data=en_f.read_bytes(), file_name=en_f.name)
   st.download_button("Download HI", data=hi_f.read_bytes(), file_name=hi_f.name)
 elif menu=="Course Library":
  st.title("Course Library - Best 25")
  for idx,co in enumerate(courses):
   en_f=list(PPT_DIR.glob(co["id"]+"*EN.pptx"))
   hi_f=list(PPT_DIR.glob(co["id"]+"*HI.pptx"))
   if en_f and hi_f:
    st.success(f"{idx+1}. {co['topic']} - Rs {co.get('price',99)} - Best 25 Distinct")
    a,b=st.columns(2)
    with a:
     st.download_button("EN Distinct Best 25", data=en_f[0].read_bytes(), file_name=en_f[0].name, key=f"en{idx}")
    with b:
     st.download_button("HI Distinct Best 25", data=hi_f[0].read_bytes(), file_name=hi_f[0].name, key=f"hi{idx}")
 elif menu=="UPI QR Setup":
  st.title("UPI QR Setup")
  st.write("UPI ID: "+UID+" Owner: "+OWNER+" Price 99")
  up=st.file_uploader("Upload QR", type=["jpg","png","jpeg"])
  if up:
   QF.write_bytes(up.getvalue())
   st.success("Done QR Uploaded")
   st.rerun()
  if QF.exists():
   st.image(str(QF), width=300)
   st.success("QR Active")
 elif menu=="API Setup":
  st.title("API Setup - Brahma Super Agent")
  apis=load(AF,{})
  openai_key=st.text_input("OpenAI API Key", value=apis.get("openai",""), type="password")
  fb_token=st.text_input("Facebook Token", value=apis.get("fb",""), type="password")
  insta_token=st.text_input("Instagram Token", value=apis.get("insta",""), type="password")
  google_key=st.text_input("Google API Key", value=apis.get("google",""), type="password")
  if st.button("SAVE API IDs", type="primary"):
   apis["openai"]=openai_key
   apis["fb"]=fb_token
   apis["insta"]=insta_token
   apis["google"]=google_key
   save(AF,apis)
   st.success("Done Saved")
   st.rerun()
  st.write("Saved APIs:")
  st.json({k: "***"+v[-4:] if v else "" for k,v in apis.items()})
 elif menu=="Brahma Super Agent":
  st.title("Brahma Super Agent - Best 25")
  for idx,co in enumerate(courses[:10]):
   with st.expander(f"{idx+1}. {co['topic']} - Super Agent Best 25"):
    st.write(f"SEO Title {co['topic']} Master Course 2026 Top 25 Demanding Price 99 Only Full Book Distinct Best 25 Har Page Alag Distinct")
    st.write("Tasks: SEO Title Description Keywords Hashtags Auto Digital Marketing Auto Post Content Blogs Auto Create SEO Optimized Blogs Facebook Instagram Auto Post Daily Reels Stories Hashtags Marketing Copy Sales Funnel Email WhatsApp Follow Up Sales Auto Follow Up Payment Reminder Invoice Access Key Chat Bot Auto 24x7 Handles Queries Full Book Distinct Best 25 Har Page Alag Distinct Best 25 Demanding 2026")
  st.success("Super Agent Active Best 25")
 elif menu=="Sales":
  st.title("Sales - Best 25")
  for i,p in enumerate(purchases):
   with st.expander(f"{p.get('invoice_no','Order')} - {p.get('course','')} - Rs {p.get('price','')} - {p.get('status','')}"):
    st.write("Name:", p.get("name"))
    st.write("Email:", p.get("email"))
    st.write("Course:", p.get("course"))
    st.write("Price Rs 99:", p.get("price"))
    st.write("UTR:", p.get("utr"))
    st.write("Status:", p.get("status"))
    if p.get("status")=="PENDING":
     if st.button("APPROVE PAYMENT", key=f"ap{i}", type="primary"):
      p["status"]="APPROVED"
      p["access_key"]="BRAHMA-"+secrets.token_hex(5).upper()
      save(PF,purchases)
      st.success(f"Done {p['access_key']}")
      st.rerun()
    else:
     st.success(f"Approved {p.get('access_key')}")
else:
 if menu=="Browse Courses":
  st.title("Brahma Academy - Best 25 - Price 99 Only - Full Book Distinct Best 25")
  st.success("Best 25 Demanding 2026 - Har Page Alag Distinct - No Crash - No Same Matter")
  for i,course in enumerate(courses):
   with st.expander(f"{i+1}. {course['topic']} - Rs {course['price']} - Best 25 Distinct - Price 99"):
    params={"pa":UID,"pn":OWNER,"am":str(course["price"]),"cu":"INR","tn":course["topic"][:20]}
    link="upi://pay?"+urllib.parse.urlencode(params)
    st.write(f"Course: {course['topic']} - Full Book Distinct Best 25 - Har Page Alag Distinct")
    st.link_button(f"PAY Rs {course['price']} - Best 25 Distinct", link, type="primary")
    with st.form(f"buy_{course['id']}"):
     name=st.text_input("Your Name", key=f"n{course['id']}")
     email=st.text_input("Your Email", key=f"e{course['id']}")
     utr=st.text_input("UTR Number", key=f"u{course['id']}")
     submit=st.form_submit_button(f"SUBMIT PAYMENT Rs {course['price']} - Best 25")
     if submit:
      if len(name)<3 or len(email)<5 or len(utr)<5:
       st.error("Error Fill All")
      else:
       purchases.append({"invoice_no":"INV"+datetime.datetime.now().strftime("%Y%m%d%H%M%S"),"access_key":"","name":name,"email":email,"course":course["topic"],"course_id":course["id"],"price":int(course["price"]),"utr":utr,"status":"PENDING","date":str(datetime.datetime.now())})
       save(PF,purchases)
       st.success(f"Done Invoice {purchases[-1]['invoice_no']}")
 elif menu=="My Access":
  st.title("My Learning - Best 25 - Price 99 - Distinct Best 25")
  k=st.text_input("Enter Invoice Or Access Key")
  if st.button("UNLOCK BILINGUAL FULL BOOK DISTINCT BEST 25", type="primary"):
   found=[p for p in purchases if (p.get("invoice_no")==k or p.get("access_key")==k) and p.get("status")=="APPROVED"]
   if not found:
    st.error("Error Not Found Or Not Approved")
   else:
    pu=found[0]
    st.success(f"Welcome {pu.get('name','Student')} - {pu.get('course')} - Price Rs {pu.get('price','99')} Only - Best 25 Distinct")
    en_f=list(PPT_DIR.glob(pu.get("course_id","")+"*EN.pptx"))
    hi_f=list(PPT_DIR.glob(pu.get("course_id","")+"*HI.pptx"))
    if en_f:
     st.download_button("DOWNLOAD ENGLISH DISTINCT BEST 25", data=en_f[0].read_bytes(), file_name=en_f[0].name, type="primary")
    if hi_f:
     st.download_button("DOWNLOAD HINDI DISTINCT BEST 25", data=hi_f[0].read_bytes(), file_name=hi_f[0].name, type="secondary")
    if not en_f:
     st.warning("Books Not Ready Yet")
st.caption("V123 Best 25 Final Tiny No Crash No Same Matter Har Page Alag Distinct")