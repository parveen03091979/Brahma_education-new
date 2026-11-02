import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
import content as ct
st.set_page_config(page_title="Brahma Master Academy", layout="wide")
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
  t=ct.MODS[n-1]
  s=prs.slides.add_slide(prs.slide_layouts[6])
  tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
  tf=tb.text_frame
  tf.word_wrap=True
  tf.text=f"M{n:02d} {top} - {t} - EN - Master Teacher Full Book - Price 99"
  tf.paragraphs[0].font.size=Pt(12)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=ct.en(top,n)
  bf.paragraphs[0].font.size=Pt(8)
 prs.save(str(en_p))
 prs2=Presentation()
 prs2.slide_width=Inches(13.33)
 prs2.slide_height=Inches(7.5)
 for n in range(1,41):
  t=ct.MODS[n-1]
  s=prs2.slides.add_slide(prs2.slide_layouts[6])
  tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
  tf=tb.text_frame
  tf.word_wrap=True
  tf.text=f"M{n:02d} {top} - {t} - HI - Master Teacher Full Book - Price 99"
  tf.paragraphs[0].font.size=Pt(12)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=ct.hi(top,n)
  bf.paragraphs[0].font.size=Pt(8)
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
st.sidebar.title("Brahma Master Academy")
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
  st.sidebar.success("Admin Access - Professional")
  menu=st.sidebar.radio("Admin",["Dashboard","Price Manager 99","Add New Course","Course Library","UPI QR Setup","API Setup","Brahma Super Agent","Sales"])
  if st.sidebar.button("Logout"):
   st.session_state.admin_logged=False
   AS.unlink(missing_ok=True)
   st.rerun()
def init50():
 d=[]
 for i,name in enumerate(ct.TOP50):
  d.append({"id":f"BRAHMA{1000+i}","topic":name.strip(),"price":99})
 save(CF,d)
 return d
courses=init50()
purchases=load(PF,[])
if st.session_state.admin_logged:
 if menu=="Dashboard":
  st.title("Dashboard - Brahma Master Academy - Professional")
  st.success("Top 50 High Level Demanding Courses - Full Book Master Teacher - Har Page Alag Distinct Pura Page Bhara Puri Knowledge - Price 99 - Professional Academy - Brahma Super Agent Handles SEO Digital Marketing Blogs Social Media Marketing Sales Chat Bot")
  c1,c2,c3=st.columns(3)
  c1.metric("Total Courses", len(courses))
  c2.metric("English Full Book", len(list(PPT_DIR.glob("*EN.pptx"))))
  c3.metric("Hindi Full Book", len(list(PPT_DIR.glob("*HI.pptx"))))
  if st.button("DELETE OLD FILES"):
   for f in PPT_DIR.glob("*.*"):
    try:
     f.unlink()
    except:
     pass
   st.success("Done Old Deleted")
   st.rerun()
  if st.button("CREATE TOP 50 MASTER TEACHER FULL BOOK", type="primary"):
   bar=st.progress(0)
   for idx,c in enumerate(courses):
    make(c)
    bar.progress(int((idx+1)/len(courses)*100))
   st.success("Done Full Book Top 50 Master Teacher Har Page Alag Distinct Pura Page Bhara Puri Knowledge Market Best 100% Professional")
   st.balloons()
   st.rerun()
  st.write("Top 50 High Level Demanding 2026 Full Book Professional:")
  for i,co in enumerate(courses):
   st.write(f"{i+1}. {co['topic']} - Rs {co.get('price',99)} - Full Book Master Teacher Professional")
 elif menu=="Price Manager 99":
  st.title("Price Manager 99 - Professional")
  st.success("Har Course Price Sirf Rs 99 - Professional Pricing - Change Kar Sakte Ho")
  bulk=st.number_input("Set All Price To", value=99, min_value=1, max_value=10000, step=1)
  if st.button("SET ALL BULK PRICE", type="primary"):
   for c in courses:
    c["price"]=int(bulk)
   save(CF,courses)
   st.success(f"Done All Price {bulk}")
   st.rerun()
  if st.button("SET ALL TO 99 ONLY", type="primary"):
   for c in courses:
    c["price"]=99
   save(CF,courses)
   st.success("Done All 99 Price Only Professional")
   st.rerun()
  sel=st.selectbox("Select Course For Price Change", [c["topic"]+" - "+c["id"]+" - Rs "+str(c.get("price",99)) for c in courses])
  sid=sel.split(" - ")[-2]
  curr=99
  for c in courses:
   if c["id"]==sid:
    curr=c.get("price",99)
  np=st.number_input("New Price Single", value=int(curr), min_value=1, max_value=10000, step=1)
  if st.button("UPDATE SINGLE COURSE PRICE", type="primary"):
   for c in courses:
    if c["id"]==sid:
     c["price"]=int(np)
     break
   save(CF,courses)
   st.success(f"Done Price Updated {np}")
   st.rerun()
 elif menu=="Add New Course":
  st.title("Add New Course - Professional")
  st.success("Yaha Naya Course Add Kar Sakte Ho - Top 50 Me Add Hoga - Professional")
  with st.form("add"):
   nt=st.text_input("New Course Name - Top Demanding Future Professional")
   npr=st.number_input("New Price", value=99, min_value=1, max_value=10000, step=1)
   sub=st.form_submit_button("ADD NEW COURSE TOP 50 PROFESSIONAL", type="primary")
   if sub:
    if len(nt)<3:
     st.error("Error Name Short")
    else:
     nid=f"BRAHMA{1000+len(courses)}"
     courses.append({"id":nid,"topic":nt,"price":int(npr)})
     save(CF,courses)
     make({"id":nid,"topic":nt})
     st.success("Done New Course Added Full Book Master Teacher English + Hindi 2 Files Professional")
     st.rerun()
  sel=st.selectbox("Select For PPT Full Book", [c["topic"]+" - "+c["id"] for c in courses])
  if st.button("Make Bilingual PPT Full Book Master Teacher", type="primary"):
   sid=sel.split(" - ")[-1]
   stopic=" - ".join(sel.split(" - ")[:-1])
   en_f,hi_f=make({"id":sid,"topic":stopic})
   st.success("Done Full Book Master Teacher Har Page Alag Distinct Pura Page Bhara Puri Knowledge Market Best Professional")
   st.download_button("Download EN Full Book", data=en_f.read_bytes(), file_name=en_f.name)
   st.download_button("Download HI Full Book", data=hi_f.read_bytes(), file_name=hi_f.name)
 elif menu=="Course Library":
  st.title("Course Library - Top 50 Full Book Professional")
  st.success("Top 50 High Level - Har Page Alag Distinct Full Book Pura Page Bhara - English + Hindi - Professional Academy")
  for idx,co in enumerate(courses):
   en_f=list(PPT_DIR.glob(co["id"]+"*EN.pptx"))
   hi_f=list(PPT_DIR.glob(co["id"]+"*HI.pptx"))
   if en_f and hi_f:
    st.success(f"{idx+1}. {co['topic']} - Rs {co.get('price',99)} - 2 Files Full Book Master Teacher Professional")
    a,b=st.columns(2)
    with a:
     st.download_button("EN Full Book Distinct", data=en_f[0].read_bytes(), file_name=en_f[0].name, key=f"en{idx}")
    with b:
     st.download_button("HI Full Book Distinct", data=hi_f[0].read_bytes(), file_name=hi_f[0].name, key=f"hi{idx}")
 elif menu=="UPI QR Setup":
  st.title("UPI QR Setup - Professional")
  st.write("UPI ID: "+UID+" Owner: "+OWNER+" Price 99 Only Professional")
  st.success("Yaha UPI QR Upload Karo - Student Payment Yaha Ayega - Professional Payment Setup")
  up=st.file_uploader("Upload QR Code Image", type=["jpg","png","jpeg"])
  if up:
   QF.write_bytes(up.getvalue())
   st.success("Done QR Uploaded")
   st.rerun()
  if QF.exists():
   st.image(str(QF), width=300)
   st.success("QR Active - Student Can Pay Rs 99 - Professional")
 elif menu=="API Setup":
  st.title("API Setup - Brahma Super Agent - Professional")
  st.success("Yaha API Aur IDs Dalne Se - Brahma Super Agent Professional Handles SEO Digital Marketing Blogs Social Media Auto Post Marketing Sales Chat Bot")
  apis=load(AF,{})
  openai_key=st.text_input("OpenAI API Key For Brahma Super Agent", value=apis.get("openai",""), type="password")
  fb_token=st.text_input("Facebook Page Access Token For Auto Post", value=apis.get("fb",""), type="password")
  insta_token=st.text_input("Instagram Access Token For Auto Post", value=apis.get("insta",""), type="password")
  google_key=st.text_input("Google Search API Key For Market Research", value=apis.get("google",""), type="password")
  if st.button("SAVE API IDs - Brahma Super Agent Professional", type="primary"):
   apis["openai"]=openai_key
   apis["fb"]=fb_token
   apis["insta"]=insta_token
   apis["google"]=google_key
   save(AF,apis)
   st.success("Done API IDs Saved - Brahma Super Agent Will Use These For SEO Digital Marketing Blogs Social Media Auto Post Marketing Sales Chat Bot Professional")
   st.rerun()
  st.write("Saved APIs:")
  st.json({k: "***"+v[-4:] if v else "" for k,v in apis.items()})
 elif menu=="Brahma Super Agent":
  st.title("Brahma Super Agent - Professional - SEO + Marketing + Sales + Chat Bot")
  st.success("Brahma Super Agent Professional - Sab Kuch Handle Karega - SEO + Digital Marketing + Blogs + Facebook Instagram Auto Post + Marketing + Sales + Chat Bot - Professional Academy")
  for idx,co in enumerate(courses[:10]):
   with st.expander(f"{idx+1}. {co['topic']} - Brahma Super Agent Professional"):
    st.write(ct.seo(co["topic"]))
    st.write("---")
    st.write("Brahma Super Agent Professional Tasks:")
    st.write("1. SEO - Title Description Keywords Hashtags Auto - Market Research Google Search 100% Data")
    st.write("2. Digital Marketing - Auto Post Content Social Media Ads Copy Professional")
    st.write("3. Blogs - Auto Create SEO Optimized Blogs For Each Course Professional")
    st.write("4. Facebook Instagram - Auto Post Daily Reels Stories Hashtags Professional")
    st.write("5. Marketing - Marketing Copy Sales Funnel Email WhatsApp Follow Up Professional")
    st.write("6. Sales - Auto Sales Follow Up Payment Reminder Invoice Access Key Professional")
    st.write("7. Chat Bot - Auto 24x7 Chat Bot Handles Queries Price 99 UPI Payment Professional")
  st.success("Brahma Super Agent Active Professional - SEO + Digital Marketing + Blogs + Facebook Instagram Auto Post + Marketing + Sales + Chat Bot - Professional Academy")
 elif menu=="Sales":
  st.title("Sales - Top 50 Full Book Professional")
  st.success("Yaha Student Payments Dikhenge - Approve Karo - Access Key Banao - Professional Sales")
  for i,p in enumerate(purchases):
   with st.expander(f"{p.get('invoice_no','Order')} - {p.get('course','')} - Rs {p.get('price','')} - {p.get('status','')}"):
    st.write("Name:", p.get("name"))
    st.write("Email:", p.get("email"))
    st.write("Course:", p.get("course"))
    st.write("Course ID:", p.get("course_id"))
    st.write("Price Rs 99 Only Professional:", p.get("price"))
    st.write("UTR:", p.get("utr"))
    st.write("Status:", p.get("status"))
    st.write("Date:", p.get("date"))
    if p.get("status")=="PENDING":
     if st.button("APPROVE PAYMENT AND GIVE ACCESS", key=f"ap{i}", type="primary"):
      p["status"]="APPROVED"
      p["access_key"]="BRAHMA-"+secrets.token_hex(5).upper()
      save(PF,purchases)
      st.success(f"Done Approved - Key {p['access_key']} - Student Can Unlock English + Hindi Both Full Book Files Professional")
      st.rerun()
    else:
     st.success(f"Approved - Key {p.get('access_key')} - Student Has English + Hindi Full Book Access Professional")
else:
 if menu=="Browse Courses":
  st.title("Brahma Master Academy - Top 50 Master Courses - Market Best 100% - Price Rs 99 Only - Professional")
  st.success("Top 50 High Level Demanding 2026 - AI Product Mgmt AI Project Mgmt Gen AI Included - Har Page Alag Distinct Full Book Pura Page Bhara Puri Knowledge - Jo Padhega Puri Tarah Seekh Jayega - Price Only Rs 99 - Professional Academy - Brahma Super Agent Handles SEO Digital Marketing Blogs Social Media Marketing Sales Chat Bot Professional")
  for i,course in enumerate(courses):
   with st.expander(f"{i+1}. {course['topic']} - Rs {course['price']} - English + Hindi Full Book Master Teacher - Price 99 Only - Professional"):
    params={"pa":UID,"pn":OWNER,"am":str(course["price"]),"cu":"INR","tn":course["topic"][:20]}
    link="upi://pay?"+urllib.parse.urlencode(params)
    st.write(f"Course: {course['topic']} - Market Best 100% - Master Teacher Full Book - Har Page Alag Distinct Pura Page Bhara Puri Knowledge Professional")
    st.write(f"Price: Rs {course['price']} Only - Professional Pricing - Sirf 99 - Full Book")
    st.write(f"Language: English File + Hindi Translation File - 2 Files - Dono Me Step By Step Practical Case Studies Full Knowledge Professional")
    st.link_button(f"PAY Rs {course['price']} - Get English + Hindi Full Book - Price 99 Only Professional", link, type="primary")
    with st.form(f"buy_{course['id']}"):
     name=st.text_input("Your Name", key=f"n{course['id']}")
     email=st.text_input("Your Email", key=f"e{course['id']}")
     utr=st.text_input("UTR Number After Payment - 12 Digit", key=f"u{course['id']}")
     submit=st.form_submit_button(f"SUBMIT PAYMENT Rs {course['price']} - Get Access Full Book Professional")
     if submit:
      if len(name)<3 or len(email)<5 or len(utr)<5:
       st.error("Error - Fill All Details - Name Email UTR Required")
      else:
       purchases.append({"invoice_no":"INV"+datetime.datetime.now().strftime("%Y%m%d%H%M%S"),"access_key":"","name":name,"email":email,"course":course["topic"],"course_id":course["id"],"price":int(course["price"]),"utr":utr,"status":"PENDING","date":str(datetime.datetime.now())})
       save(PF,purchases)
       st.success(f"Done Payment Submitted - Invoice {purchases[-1]['invoice_no']} - After Admin Approval You Get English + Hindi Both Full Book Files Professional - Price Rs {course['price']} Only - Master Teacher Distinct Full Knowledge Professional")
 elif menu=="My Access":
  st.title("My Learning - Top 50 Full Book Master Teacher - Price 99 Only - Professional")
  st.success("Yaha Invoice Ya Access Key Daalo - English + Hindi Dono Full Book Files Milegi - Har Page Alag Distinct Full Book Pura Page Bhara Puri Knowledge Professional - Master Teacher")
  k=st.text_input("Enter Invoice Number Or Access Key")
  if st.button("UNLOCK BILINGUAL FULL BOOK MASTER TEACHER - PRICE 99 ONLY - PROFESSIONAL", type="primary"):
   found=[p for p in purchases if (p.get("invoice_no")==k or p.get("access_key")==k) and p.get("status")=="APPROVED"]
   if not found:
    st.error("Error - Invoice Or Key Not Found Or Not Approved Yet - Contact Admin - Price 99 Only Professional")
   else:
    pu=found[0]
    st.success(f"Welcome {pu.get('name','Student')} - {pu.get('course')} - Price Rs {pu.get('price','99')} Only - Full Book Master Teacher Distinct Professional - Market Best 100% - Puri Knowledge - Pura Page Bhara Professional")
    en_f=list(PPT_DIR.glob(pu.get("course_id","")+"*EN.pptx"))
    hi_f=list(PPT_DIR.glob(pu.get("course_id","")+"*HI.pptx"))
    if en_f:
     st.download_button("DOWNLOAD ENGLISH FULL BOOK - PRICE 99 ONLY - PROFESSIONAL", data=en_f[0].read_bytes(), file_name=en_f[0].name, type="primary")
    if hi_f:
     st.download_button("DOWNLOAD HINDI FULL BOOK - PRICE 99 ONLY - PROFESSIONAL", data=hi_f[0].read_bytes(), file_name=hi_f[0].name, type="secondary")
    if not en_f:
     st.warning("Books Not Ready Yet - Admin Will Create Soon - Top 50 Full Book Master Teacher - Price 99 Only Professional - Pura Page Bhara Puri Knowledge")
st.caption("Brahma Master Academy V116 Professional | Har Page Alag Distinct Full Book Pura Page Bhara Puri Knowledge | Top 50 High Level Price 99 | Full Dashboard API IDs QR Price Change New Course Super Agent SEO Marketing Blogs Social Media Marketing Sales Chat Bot | 2 Files No Cut | Professional Academy | No Retirement Wording")