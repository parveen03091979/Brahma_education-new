import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
st.set_page_config(page_title="Brahma V107", layout="wide")
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
MODS=["WHAT IS","WHY IMPORTANT","WHERE USE","WHEN USE","WHO LEARN","HOW WORKS","TOOLS","EARNING","PRACTICAL","RIGHT WAY","FOUNDATION","CORE CONCEPT","ADVANCED","STEP PROCESS","EXAMPLE","CLIENT REQ","REAL STORY","PLANNING","IMPLEMENT","MISTAKES","PRO TIP","EXPERT","COMPARE","FREE PAID","PORTFOLIO","CLIENT FIND","FREELANCING","AGENCY","MODEL","SCALING","SEO","LEAD GEN","SALES","AUTOMATION","OPTIMIZE","CASE STUDY","DAILY PRACTICE","HOMEWORK","REVISION","FINAL PROJECT"]
def english_txt(t,n,topic):
 if n==1:
  return f"{topic} M{n} WHAT IS ENGLISH\nGOAL Explain {topic} to 5 people\nWHY 2026 need 80 percent time save salary 3x\nCONCEPT Perceive Reason Act like WhatsApp check think reply\nSTEP1 Choose task Instagram reply\nSTEP2 ChatGPT prompt friendly\nSTEP3 Make.com trigger action\nSTEP4 Test second account\nSTEP5 Diary"
 if n==17:
  return f"{topic} M{n} REAL STORY ENGLISH\nGOAL Learn from Rahul real roadmap\nCONCEPT Village Redmi 8 Jio 1GB no laptop daily 1h\nSTEP1 Month1-2 foundation only\nSTEP2 Portfolio 3 projects\nSTEP3 Upwork 20 proposals 19 reject learn\nSTEP4 1 USA client 15k 5 star\nSTEP5 Month4 5 clients 75k Month6 agency 2L house"
 if n==20:
  return f"{topic} M{n} MISTAKES ENGLISH\nGOAL Avoid 5 mistakes 90 percent fail\nM1 Skip foundation Fix M1-M10 twice\nM2 Only watch no practice Fix 15m theory 15m practical\nM3 Money chase Fix 30 days skill only\nM4 No diary Fix night 10m diary 4 points\nM5 No mentor Fix community doubt"
 if n==40:
  return f"{topic} M{n} FINAL PROJECT ENGLISH\nGOAL Final portfolio 1Cr roadmap\nSTEP1 Choose business problem {topic}\nSTEP2 Plan tools workflow paper\nSTEP3 Build test 10 times fix bug\nSTEP4 Result screenshot before 2h after 10m\nSTEP5 Portfolio Behance GitHub LinkedIn\nSTEP6 Next freelancing agency SaaS"
 return f"{topic} M{n} {t} ENGLISH\nGOAL Master {t} in {topic}\nWHY Foundation for next module important\nCONCEPT Core idea of {t} like engine in car\nSTEP1 Write definition own words\nSTEP2 See 2 examples success failure\nSTEP3 Open tool click options\nSTEP4 15m practical task\nSTEP5 Diary what learned"
def hindi_txt(t,n,topic):
 if n==1:
  return f"{topic} M{n} WHAT IS HINDI Translation\nLAKSHYA 5 logo ko {topic} samjhao\nKYU 2026 me 80 percent samay bachega salary 3x\nAVADHARNA Perceive Reason Act jaise WhatsApp dekho socho jawab do\nKADAM1 Kaam chuno Instagram reply\nKADAM2 ChatGPT prompt friendly\nKADAM3 Make.com jodo\nKADAM4 Test dusra account\nKADAM5 Diary"
 if n==17:
  return f"{topic} M{n} REAL STORY HINDI Translation\nLAKSHYA Rahul kahani se seekho\nAVADHARNA Gaon Redmi 8 Jio 1GB bina laptop roz 1 ghanta\nKADAM1 Mahina1-2 neenv only\nKADAM2 Portfolio 3 project\nKADAM3 Upwork 20 proposal 19 reject seekho\nKADAM4 1 USA client 15k 5 star\nKADAM5 Mahina4 5 client 75k Mahina6 agency 2L ghar"
 if n==20:
  return f"{topic} M{n} MISTAKES HINDI Translation\nLAKSHYA 5 galti se bacho 90 fail\nG1 Neenv skip Upay M1-M10 do baar\nG2 Sirf dekho practice nahi Upay 15m theory 15m practical\nG3 Paisa peeche Upay 30 din skill only\nG4 Diary nahi Upay raat 10m diary 4 points\nG5 Mentor nahi Upay community doubt"
 if n==40:
  return f"{topic} M{n} FINAL PROJECT HINDI Translation\nLAKSHYA Antim portfolio 1Cr roadmap\nKADAM1 {topic} me samasya chuno\nKADAM2 Yojana tools workflow kagaj par\nKADAM3 Banao 10 baar test karo bug theek\nKADAM4 Result screenshot pehle 2h baad 10m\nKADAM5 Portfolio Behance GitHub LinkedIn\nKADAM6 Agla freelancing agency SaaS"
 return f"{topic} M{n} {t} HINDI Translation\nLAKSHYA {t} ko {topic} me seekhna\nKYU Agle module ki neenv zaruri\nAVADHARNA {t} ka mukhya vichar\nKADAM1 Paribhasha apne shabdon me likho\nKADAM2 2 udaharan safalta asafalta dekho\nKADAM3 Tool kholo har option click karo\nKADAM4 15m abhyas karo\nKADAM5 Diary me kya seekha likho"
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
  t=MODS[n-1]
  s=prs.slides.add_slide(prs.slide_layouts[6])
  tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
  tf=tb.text_frame
  tf.word_wrap=True
  tf.text=f"M{n} {top} {t} English Step By Step Distinct"
  tf.paragraphs[0].font.size=Pt(13)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=english_txt(t,n,top)
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
  tf.text=f"M{n} {top} {t} Hindi Translation Distinct"
  tf.paragraphs[0].font.size=Pt(13)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=hindi_txt(t,n,top)
  bf.paragraphs[0].font.size=Pt(10)
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
st.sidebar.title("Brahma V107 Distinct")
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
  st.sidebar.success("Admin OK Distinct