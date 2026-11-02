import streamlit as st, json, hashlib, secrets, datetime
from pathlib import Path
st.set_page_config(page_title="Brahma Top 50 AI", layout="wide")
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
TOP50="AI Product Management Hottest 2026,AI Project Management,Generative AI Prompt Engineering,AI Agents Automation,AI Engineering LLM Engineering,Machine Learning MLOps,AI Strategy Consulting,LLM Fine Tuning RAG,AI Automation n8n Make Zapier,Data Science Big Data,Data Analytics Power BI,Data Engineering,Cybersecurity Ethical Hacking,Cloud Computing AWS Azure GCP,DevOps Kubernetes,Full Stack MERN,Python Full Stack,Java Full Stack,UI UX Product Design,Digital Marketing Performance,SEO Content Marketing,Social Media Influencer,Video Editing Motion Graphics,Graphic Design Branding,Blockchain Web3,FinTech Analytics,Stock Crypto Trading,Product Management,Project Management PMP Agile,Business Analytics,Robotics Human Robot,Quantum Computing,IoT Embedded Systems,AR VR Metaverse,Game Development Unity,Mobile App Flutter,No Code Low Code,Chatbot Development,SaaS Product Building,Ecommerce Shopify,YouTube Automation,Copywriting Sales Funnel,Resume Interview Skills,Communication Public Speaking,Leadership Management,EV Technology,Renewable Solar Energy,Digital Health Telemedicine,Bioinformatics,Supply Chain Logistics,HR Analytics,Accounting Tally GST".split(",")
def init50():
 data=[]
 for i,name in enumerate(TOP50):
  data.append({"id":f"BRAHMA{1000+i}","topic":name.strip(),"price":99})
 save(CF,data)
 return data
courses=init50()
MODS="WHAT IS,WHY IMP,WHERE USE,WHEN USE,WHO LEARN,HOW WORKS,TOOLS,EARNING,PRACTICAL,RIGHT WAY,FOUNDATION,CORE,ADVANCED,STEP,EXAMPLE,CLIENT,STORY,PLANNING,IMPLEMENT,MISTAKES,PRO TIP,EXPERT,COMPARE,FREE PAID,PORTFOLIO,FIND CLIENT,FREELANCING,AGENCY,MODEL,SCALING,SEO,LEAD,SALES,AUTO,OPTIMIZE,CASE,DAILY,HOMEWORK,REVISION,FINAL".split(",")
def en_txt(t,n,topic):
 if n==1:
  return f"{topic} WHAT IS EN Master Teacher Top Demanding 2026\nGOAL Explain {topic} to 5 people simple\nWHY 2026 hottest 56 percent wage premium 300 percent YoY growth\nCONCEPT Perceive Reason Act like WhatsApp check think reply\nS1 Choose 1 task in {topic}\nS2 ChatGPT prompt You are {topic} expert\nS3 Connect Make.com tool\nS4 Test second account\nS5 Diary"
 if n==17:
  return f"{topic} REAL STORY EN Master Teacher\nRahul village Redmi 8 Jio 1GB no laptop 1h daily {topic}\nS1 Month1-2 foundation only\nS2 Portfolio 3 projects {topic}\nS3 Upwork 20 proposals 19 reject learn\nS4 1 USA client 15k 5 star\nS5 Month4 5 clients 75k Month6 agency 2L"
 if n==20:
  return f"{topic} MISTAKES EN Master Teacher\nM1 Skip foundation Fix M1-M10 twice {topic}\nM2 Only watch no practice Fix 15m theory 15m practical {topic}\nM3 Money chase Fix 30 days skill only {topic}\nM4 No diary Fix night 10m diary\nM5 No mentor Fix community doubt {topic}"
 if n==40:
  return f"{topic} FINAL PROJECT EN Master Teacher\nS1 Choose business problem {topic}\nS2 Plan tools workflow paper\nS3 Build test 10 times fix bug {topic}\nS4 Result screenshot before 2h after 10m\nS5 Portfolio Behance GitHub case study {topic}\nS6 Next freelancing agency SaaS 1Cr {topic}"
 return f"{topic} {t} EN Master Teacher Distinct Top Demanding\nGOAL Master {t} in {topic} step by step\nWHY Foundation for next important {topic}\nCONCEPT Core idea of {t} example {topic}\nS1 Define own words {t}\nS2 2 examples success failure {topic}\nS3 Open tool click options {t}\nS4 15m practical task {topic}\nS5 Diary"
def hi_txt(t,n,topic):
 if n==1:
  return f"{topic} WHAT IS HI Translation Master Teacher Top\nLAKSHYA 5 logo ko {topic} simple me samjhao\nKYU 2026 sabse zyada demanding 56 percent premium 300 percent growth\nAVADHARNA Perceive Reason Act jaise WhatsApp dekho socho jawab\nK1 1 kaam chuno {topic} me\nK2 ChatGPT kholo Tum {topic} expert ho\nK3 Make.com jodo\nK4 Dusra account test\nK5 Diary"
 if n==17:
  return f"{topic} STORY HI Translation Master Teacher\nRahul gaon Redmi 8 Jio 1GB bina laptop roz 1h {topic}\nK1 Mahina1-2 neenv only\nK2 Portfolio 3 project {topic}\nK3 Upwork 20 proposal 19 reject\nK4 1 USA client 15k 5 star\nK5 Mahina4 5 client 75k Mahina6 agency 2L"
 if n==20:
  return f"{topic} MISTAKES HI Translation Master Teacher\nG1 Neenv skip Upay M1-M10 do baar {topic}\nG2 Sirf dekho practice nahi Upay 15m theory practical {topic}\nG3 Paisa peeche Upay 30 din skill only {topic}\nG4 Diary nahi Upay raat 10m diary\nG5 Mentor nahi Upay community doubt {topic}"
 if n==40:
  return f"{topic} FINAL HI Translation Master Teacher\nK1 {topic} me samasya chuno\nK2 Yojana tools kagaj par banao\nK3 Banao 10 baar test karo bug theek {topic}\nK4 Result screenshot pehle 2h baad 10m\nK5 Portfolio Behance GitHub case study {topic}\nK6 Agla freelancing agency SaaS 1Cr {topic}"
 return f"{topic} {t} HI Translation Master Teacher Distinct Top\nLAKSHYA {t} ko {topic} me kadam dar kadam\nKYU Agle ki neenv zaruri {topic}\nAVADHARNA {t} ka vichar example {topic}\nK1 Paribhasha likho {t}\nK2 2 udaharan dekho {topic}\nK3 Tool kholo click karo {t}\nK4 15m abhyas karo {topic}\nK5 Diary me likho {t}"
def make(c):
 from pptx import Presentation
 from pptx.util import Inches, Pt
 cid=c["id"]
 top=c["topic"]
 en_p=PPT_DIR/(f"{cid}_ENGLISH.pptx")
 hi_p=PPT_DIR/(f"{cid}_HINDI.pptx")
 prs=Presentation()
 prs.slide_width=Inches(13.33)
 prs.slide_height=Inches(7.5)
 for n in range(1,41):
  t=MODS[n-1]
  s=prs.slides.add_slide(prs.slide_layouts[6])
  tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
  tf=tb.text_frame
  tf.word_wrap=True
  tf.text=f"M{n} {top} {t} EN Master Teacher Top Demanding"
  tf.paragraphs[0].font.size=Pt(11)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=en_txt(t,n,top)
  bf.paragraphs[0].font.size=Pt(9)
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
  tf.text=f"M{n} {top} {t} HI Master Teacher Top Demanding Translation"
  tf.paragraphs[0].font.size=Pt(11)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=hi_txt(t,n,top)
  bf.paragraphs[0].font.size=Pt(9)
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
st.sidebar.title("Brahma Top 50 AI")
if not MH.exists():
 pw=st.sidebar.text_input("Create Password", type="password")
 if st.sidebar.button("Create Admin"):
  if pw and len(pw)>=4:
   MH.write_text(make_hash(pw), encoding="utf-8")
   st.rerun()
 menu="Browse"
else:
 if not st.session_state.admin_logged:
  menu=st.sidebar.radio("Menu",["Browse"])
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
  st.sidebar.success("OK")
  menu=st.sidebar.radio("Admin",["Dashboard Top 50 AI","Library Top 50 AI"])
  if st.sidebar.button("Logout"):
   st.session_state.admin_logged=False
   AS.unlink(missing_ok=True)
   st.rerun()
if st.session_state.admin_logged:
 if menu=="Dashboard Top 50 AI":
  st.title("Top 50 AI Demanding 2026 - AI PM Project Management Included")
  st.success("AI Product Management AI Project Management Top 1-2 - 300 percent growth 56 percent premium - More demanding than old 50")
  total=len(courses)
  en_c=len(list(PPT_DIR.glob("*ENGLISH*")))
  hi_c=len(list(PPT_DIR.glob("*HINDI*")))
  c1,c2,c3=st.columns(3)
  c1.metric("Total 50",total)
  c2.metric("EN",en_c)
  c3.metric("HI",hi_c)
  if st.button("DELETE OLD"):
   for f in PPT_DIR.glob("*.*"):
    try:
     f.unlink()
    except:
     pass
   st.success("Done")
   st.rerun()
  if st.button("CREATE TOP 50 AI BOOKS MASTER TEACHER", type="primary"):
   bar=st.progress(0)
   for idx,c in enumerate(courses):
    make(c)
    bar.progress(int((idx+1)/len(courses)*100))
   st.success("Done Top 50 AI Master Teacher")
   st.balloons()
   st.rerun()
  st.write("New Top 50 List 2026 - AI Courses More Demanding:")
  for i,co in enumerate(courses):
   st.write(f"{i+1}. {co['topic']}")
 elif menu=="Library Top 50 AI":
  st.title("Library Top 50 AI Master Teacher")
  for idx,co in enumerate(courses):
   en_f=list(PPT_DIR.glob(co["id"]+"*ENGLISH*"))
   hi_f=list(PPT_DIR.glob(co["id"]+"*HINDI*"))
   if en_f and hi_f:
    st.success(f"{idx+1}. {co['topic']} - 2 Files Master Teacher Top Demanding")
    col1,col2=st.columns(2)
    with col1:
     st.download_button("EN Master Top", data=en_f[0].read_bytes(), file_name=en_f[0].name, key=f"en{idx}")
    with col2:
     st.download_button("HI Master Top", data=hi_f[0].read_bytes(), file_name=hi_f[0].name, key=f"hi{idx}")
else:
 if menu=="Browse":
  st.title("Brahma Top 50 AI Demanding 2026")
  st.success("AI Product Management AI Project Management Included - More Demanding Than Old 50")
  st.write("Top 50 AI Demanding 2026")
st.caption("V110 Top 50 AI | AI PM AI Project Management Top Demanding | 56 percent premium 300 percent growth | Master Teacher Distinct Bilingual | Stable")