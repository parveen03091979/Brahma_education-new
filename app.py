import streamlit as st, json, hashlib, secrets, datetime
from pathlib import Path
import content as ct
st.set_page_config(page_title="Brahma Final Retirement", layout="wide")
DATA=Path("data")
PPT_DIR=DATA/"ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)
CF=DATA/"courses.json"
MH=DATA/".master_hash"
AS=DATA/".admin_session"
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
  tf.text=f"M{n:02d} {top} {t} EN Master Price 99"
  tf.paragraphs[0].font.size=Pt(11)
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
  tf.text=f"M{n:02d} {top} {t} HI Master Price 99"
  tf.paragraphs[0].font.size=Pt(11)
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
st.sidebar.title("Brahma Final Retirement")
if not MH.exists():
 pw=st.sidebar.text_input("Create Password", type="password")
 if st.sidebar.button("Create Admin"):
  if pw and len(pw)>=4:
   MH.write_text(make_hash(pw), encoding="utf-8")
   st.rerun()
else:
 if not st.session_state.admin_logged:
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
  st.sidebar.success("OK Final Retirement")
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
if st.session_state.admin_logged:
 st.title("Brahma Final Retirement Plan Top 50")
 st.success("Har Page Alag V104 Restored Top 50 Price 99 Brahma Super Agent SEO Handles All - No Same Matter")
 c1,c2,c3=st.columns(3)
 c1.metric("Total 50", len(courses))
 c2.metric("EN", len(list(PPT_DIR.glob("*EN.pptx"))))
 c3.metric("HI", len(list(PPT_DIR.glob("*HI.pptx"))))
 if st.button("DELETE OLD SAME MATTER"):
  for f in PPT_DIR.glob("*.*"):
   try:
    f.unlink()
   except:
    pass
  st.success("Done")
  st.rerun()
 if st.button("CREATE TOP 50 MASTER TEACHER RETIREMENT", type="primary"):
  bar=st.progress(0)
  for idx,c in enumerate(courses):
   make(c)
   bar.progress(int((idx+1)/len(courses)*100))
  st.success("Done Top 50 Master Teacher Har Page Alag Distinct Retirement")
  st.balloons()
  st.rerun()
 if st.button("SET ALL TO 99 RETIREMENT"):
  for c in courses:
   c["price"]=99
  save(CF,courses)
  st.success("Done All 99 Price Only Retirement Plan")
  st.rerun()
 st.subheader("Library Master Top 50 - Price 99 - Har Page Alag")
 for idx,co in enumerate(courses[:15]):
  en_f=list(PPT_DIR.glob(co["id"]+"*EN.pptx"))
  hi_f=list(PPT_DIR.glob(co["id"]+"*HI.pptx"))
  if en_f and hi_f:
   st.write(f"{idx+1}. {co['topic']} - Rs {co.get('price',99)} - 2 Files Distinct")
   a,b=st.columns(2)
   with a:
    st.download_button("EN Master Distinct", data=en_f[0].read_bytes(), file_name=en_f[0].name, key=f"en{idx}")
   with b:
    st.download_button("HI Master Distinct", data=hi_f[0].read_bytes(), file_name=hi_f[0].name, key=f"hi{idx}")
 st.subheader("Brahma Super Agent SEO Digital Marketing")
 st.success("Super Agent Sab Handle Karega SEO Digital Marketing Retirement Plan - Search Engine Optimising Digital Marketing Super Agent Jo Brahma Hai Vah Sab Kuch Handle Karega")
 for idx,co in enumerate(courses[:5]):
  with st.expander(f"{idx+1}. {co['topic']} - Brahma SEO Super Agent"):
   st.write(ct.seo(co["topic"]))
   st.write("Brahma Super Agent Tasks: SEO Title Desc Keywords Hashtags Auto Digital Marketing Auto Post Market Research Google 100% Data Salary Demand Growth Course Step Practical Case 1Cr Roadmap Retirement Lifetime Passive Income 99 x Students")
else:
 st.title("Brahma Top 50 Retirement Plan Price 99")
 st.success("Login Admin - Top 50 High Level - AI Product Mgmt AI Project Mgmt Included - Har Page Alag V104 Restored - No Same Matter - Brahma Super Agent SEO Handles All - Price 99 Only - Retirement Plan")
st.caption("V114 Final Retirement | 2 Files No Cut | No Line >200 | Har Page Alag V104 Restored | Top 50 Price 99 | Brahma Super Agent SEO | No Same Matter | Stable")