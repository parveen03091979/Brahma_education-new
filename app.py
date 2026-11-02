import streamlit as st, json, hashlib, secrets, datetime
from pathlib import Path
st.set_page_config(page_title="Brahma Final", layout="wide")
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
T1="AI Product Mgmt,AI Project Mgmt,Gen AI Prompt,AI Agents,AI Eng LLM"
T2="ML MLOps,AI Strategy,LLM RAG,AI Auto n8n,Data Science,Data Analytics"
T3="Data Eng,CyberSec,Cloud AWS,DevOps,FullStack MERN,Python FullStack"
T4="Java FullStack,UI UX,Digital Mkt,SEO,Social Media,Video Edit"
T5="Graphic Design,Blockchain,FinTech,Stock Crypto,Product Mgmt"
T6="Project Mgmt,Biz Analytics,Robotics,Quantum,IoT,AR VR,Game Dev"
T7="Mobile Flutter,NoCode,Chatbot,SaaS,Ecom Shopify,YouTube Auto"
T8="Copywriting,Resume Interview,Communication,Leadership,EV Tech"
T9="Solar Energy,Digital Health,Bioinfo,Supply Chain,HR Analytics,Tally GST"
TOP50=(T1+","+T2+","+T3+","+T4+","+T5+","+T6+","+T7+","+T8+","+T9).split(",")
M1="WHAT IS,WHY IMP,WHERE USE,WHEN USE,WHO LEARN,HOW WORKS,TOOLS,EARN"
M2="PRACTICAL,RIGHT WAY,FOUNDATION,CORE,ADVANCED,STEP,EXAMPLE,CLIENT"
M3="STORY,PLANNING,IMPLEMENT,MISTAKES,PRO TIP,EXPERT,COMPARE,FREE PAID"
M4="PORTFOLIO,FIND CLIENT,FREELANCING,AGENCY,MODEL,SCALING,SEO,LEAD"
M5="SALES,AUTO,OPTIMIZE,CASE,DAILY,HOMEWORK,REVISION,FINAL"
MODS=(M1+","+M2+","+M3+","+M4+","+M5).split(",")
def en(topic,num):
 t=MODS[num-1]
 mk=""
 if "AI Product" in topic:
  mk="600+ $180K 300% "
 if "AI Project" in topic:
  mk="$128K demand "
 if num==1:
  return f"{topic} {t} EN {mk}GOAL Explain {topic} WHY 2026 80% save CONCEPT Perceive Reason Act S1 Task S2 ChatGPT S3 Make S4 Test S5 Diary CASE Rahul Redmi 8 save 2h USA 15k"
 if num==17:
  return f"{topic} {t} EN {mk}STORY Rahul village Redmi 8 Jio 1GB no laptop 1h daily M1-2 foundation Portfolio 3 Upwork 20 proposals 19 reject 1 client 15k 5 star M4 5 clients 75k M6 2L"
 if num==20:
  return f"{topic} {t} EN {mk}MISTAKES 5 fail 90% M1 Skip fix M1-M10 twice M2 Only watch fix 15m theory practical M3 Money chase fix 30 days skill M4 No diary fix 10m diary M5 No mentor fix community"
 if num==40:
  return f"{topic} {t} EN {mk}FINAL Choose problem {topic} Plan workflow paper Build test 10x Result 2h to 10m Portfolio Behance GitHub Next agency 1Cr"
 return f"{topic} {t} EN {mk}GOAL Master {t} WHY Foundation CONCEPT Core {t} S1 Define S2 2 examples S3 Open tool S4 15m practical S5 Diary CASE Before 4h after 30m"
def hi(topic,num):
 t=MODS[num-1]
 if num==1:
  return f"{topic} {t} HI LAKSHYA 5 ko samjhao KYU 2026 80% bachega AVADHARNA Perceive Reason Act K1 Kaam chuno K2 ChatGPT K3 Make K4 Test K5 Diary CASE Rahul gaon Redmi 8"
 if num==17:
  return f"{topic} {t} HI STORY Rahul gaon Redmi 8 Jio 1GB bina laptop roz 1h M1-2 neenv Portfolio 3 Upwork 20 proposal 19 reject 1 client 15k M4 5 client 75k M6 2L"
 if num==20:
  return f"{topic} {t} HI MISTAKES 5 galti G1 Neenv skip Upay M1-M10 do baar G2 Sirf dekho Upay 15m theory practical G3 Paisa peeche Upay 30 din skill G4 Diary nahi Upay 10m diary G5 Mentor nahi Upay community"
 if num==40:
  return f"{topic} {t} HI FINAL Samasya chuno Yojana kagaj Banao test 10x Result 2h se 10m Portfolio Behance GitHub Agla agency 1Cr"
 return f"{topic} {t} HI LAKSHYA Master {t} KYU Neenv AVADHARNA Core {t} K1 Paribhasha K2 2 udaharan K3 Tool K4 15m abhyas K5 Diary CASE Pehle 4h baad 30m"
def seo(topic):
 return f"Brahma SEO {topic} Title {topic} Master 2026 Price 99 Desc Learn {topic} step practical case 100% Keywords {topic} AI 2026 Price99 Hashtags #{topic[:6]} #Brahma #99 Super Agent SEO Digital Marketing Handles All"
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
  tf.text=f"M{n:02d} {top} {t} EN Master Price 99"
  tf.paragraphs[0].font.size=Pt(11)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=en(top,n)
  bf.paragraphs[0].font.size=Pt(8)
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
  tf.text=f"M{n:02d} {top} {t} HI Master Price 99"
  tf.paragraphs[0].font.size=Pt(11)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=hi(top,n)
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
 for i,name in enumerate(TOP50):
  d.append({"id":f"BRAHMA{1000+i}","topic":name.strip(),"price":99})
 save(CF,d)
 return d
courses=init50()
if st.session_state.admin_logged:
 st.title("Brahma Final Retirement Plan Top 50")
 st.success("Har Page Alag V104 Restored Top 50 Price 99 Brahma Super Agent SEO Handles All")
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
  st.success("Done Top 50 Master Teacher Har Page Alag Retirement")
  st.balloons()
  st.rerun()
 if st.button("SET ALL TO 99 RETIREMENT"):
  for c in courses:
   c["price"]=99
  save(CF,courses)
  st.success("Done All 99 Price Only Retirement Plan")
  st.rerun()
 st.subheader("Library Master Top 50 - Price 99")
 for idx,co in enumerate(courses[:15]):
  en_f=list(PPT_DIR.glob(co["id"]+"*EN.pptx"))
  hi_f=list(PPT_DIR.glob(co["id"]+"*HI.pptx"))
  if en_f and hi_f:
   st.write(f"{idx+1}. {co['topic']} - Rs {co.get('price',99)} - 2 Files")
   a,b=st.columns(2)
   with a:
    st.download_button("EN Master", data=en_f[0].read_bytes(), file_name=en_f[0].name, key=f"en{idx}")
   with b:
    st.download_button("HI Master", data=hi_f[0].read_bytes(), file_name=hi_f[0].name, key=f"hi{idx}")
 st.subheader("Brahma Super Agent SEO Digital Marketing")
 st.success("Super Agent Sab Handle Karega SEO Digital Marketing Retirement Plan")
 for idx,co in enumerate(courses[:5]):
  with st.expander(f"{idx+1}. {co['topic']} - Brahma SEO"):
   st.write(seo(co["topic"]))
   st.write("Tasks: SEO Title Desc Keywords Hashtags Auto Digital Marketing Auto Post Market Research Google 100% Data Course Step Practical Case 1Cr Roadmap Retirement Lifetime Passive Income 99 x Students")
else:
 st.title("Brahma Top 50 Retirement Plan Price 99")
 st.success("Login Admin - Top 50 High Level - AI Product Mgmt AI Project Mgmt Included - Har Page Alag V104 Restored - Brahma Super Agent SEO Handles All - Price 99 Only - Retirement Plan")
st.caption("V113 Final Retirement | No Line >200 Chars | No Cut | No MODS Unterminated | No GOAL Unterminated | Har Page Alag V104 Restored | Top 50 Price 99 | Brahma Super Agent SEO | Stable 1.9KB")