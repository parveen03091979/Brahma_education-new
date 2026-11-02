import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
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
TOP50=["AI Product Mgmt","AI Project Mgmt","Gen AI Prompt","AI Agents","AI Eng LLM","ML MLOps","AI Strategy","LLM RAG","AI Auto n8n","Data Science","Data Analytics","Data Eng","CyberSec","Cloud AWS","DevOps","FullStack MERN","Python FullStack","Java FullStack","UI UX","Digital Mkt","SEO","Social Media","Video Edit","Graphic Design","Blockchain","FinTech","Stock Crypto","Product Mgmt","Project Mgmt","Biz Analytics","Robotics","Quantum","IoT","AR VR","Game Dev","Mobile Flutter","NoCode","Chatbot","SaaS","Ecom Shopify","YouTube Auto","Copywriting","Resume Interview","Communication","Leadership","EV Tech","Solar Energy","Digital Health","Bioinfo","Supply Chain"]
MODS=["WHAT IS","WHY IMP","WHERE USE","WHEN USE","WHO LEARN","HOW WORKS","TOOLS","EARN MONEY","PRACTICAL","RIGHT WAY","FOUNDATION","CORE","ADVANCED","STEP PROCESS","EXAMPLE","CLIENT REQ","REAL STORY","PLANNING","IMPLEMENT","MISTAKES","PRO TIP","EXPERT","COMPARE","FREE PAID","PORTFOLIO","FIND CLIENT","FREELANCING","AGENCY","MODEL","SCALING","SEO","LEAD","SALES","AUTO","OPTIMIZE","CASE STUDY","DAILY","HOMEWORK","REVISION","FINAL PROJECT"]
def en(topic,n):
 t=MODS[n-1]
 mk="Market 2026 56% premium "
 if "AI Product" in topic:
  mk="AI Product 600+ $180K-$320K $400K labs 300% YoY Top OpenAI Anthropic "
 if "AI Project" in topic:
  mk="AI Project $128K most in-demand 768 postings 56% premium "
 nxt=MODS[n] if n<40 else "COMPLETE"
 a=f"MASTER TEACHER FULL BOOK: {topic} | M{n:02d} {t} | {mk}Price 99 Only | Professional | Full Knowledge\n\n"
 b=f"1. GOAL: Master {t} in {topic}. Explain to 5 people real example. Define {t} own words 5 points.\n\n"
 c=f"2. WHY IMPORTANT: 2026 business needs {topic} {t}. Without fail salary low. With salary 3x $50/hr 80% save. Top demanding future proof.\n\n"
 d=f"3. CORE CONCEPT: {t} means main idea behind {topic}. Like engine car. {topic}=Perceive Reason Act WhatsApp check think reply. {t} engine of {topic}.\n\n"
 e=f"4. DEEP DIVE: Definition Types of {t} in {topic}. How {t} works Architecture behind scenes When use when not ecom health finance education.\n\n"
 f=f"5. STEP BY STEP 5 STEPS:\nStep1 Understand {t} definition {topic} write 5 points\nStep2 See 2 examples {topic} {t} success failure note why\nStep3 Open tools {t} {topic} Make.com n8n ChatGPT Sheet click 15m\nStep4 Build mini project 15m {topic} {t} save screenshot video\nStep5 Diary what learned doubt {t} tomorrow plan 15m theory practical\n\n"
 g=f"6. TOOLS: ChatGPT Make.com n8n Google Sheet WhatsApp API Canva Loom Free vs Paid comparison which free paid when use setup click by click.\n\n"
 h=f"7. REAL EXAMPLES: Success Company A used {t} in {topic} growth 3x 5h to 30m. Failure Company B skipped {t} fail. What success did right.\n\n"
 i=f"8. CASE STUDY: Rahul village Redmi 8 Jio 1GB no laptop daily 1h {topic} {t}. Before manual 4h daily after {t} automation 30m auto 90% auto shop owner paid 10k monthly 3 referrals ecom YouTuber.\n\n"
 j=f"9. MISTAKES + PRO TIPS: 90% fail {t} {topic}. M1 Skip foundation Fix M01-M10 twice M2 Only watch Fix 15m theory practical daily M3 Money chase Fix 30 days skill only M4 No diary Fix 10m diary 4 points M5 No mentor Fix community daily doubt. Pro Tip Extra value 2h extra 5 star referral.\n\n"
 k=f"10. PRACTICAL: Today 15m theory +15m practical {topic} {t}. Build mini project automate 1 task using {t}. Save screenshot.\n\n"
 l=f"11. HOMEWORK + QUIZ: Homework Teach {t} {topic} to friend voice note 2m submit. Quiz Q1 What is {t} in {topic}? Q2 When use {t}? Q3 Tools for {t}? Self check.\n\n"
 m=f"12. NEXT + RESOURCES + TEMPLATES: Next {nxt} builds on {t}. Resources YouTube docs communities LinkedIn Discord mentors. Checklist Daily 1h Weekly Portfolio Client onboarding. Templates Ready prompt Make blueprint Sheet template WhatsApp API Canva. Portfolio Minor Major Final Project. Interview Q&A Top 20 {topic} {t}. Freelancing Upwork Fiverr profile proposal 20 proposals 19 reject learn first client $15k 5 star 5 clients 75k agency 2L.\n\nFull Book Page Complete - Pura Page Bhara - Puri Knowledge - Market Best 100% - Professional - Price 99 Only - Distinct"
 return a+b+c+d+e+f+g+h+i+j+k+l+m
def hi(topic,n):
 t=MODS[n-1]
 nxt=MODS[n] if n<40 else "POORA"
 a=f"MASTER TEACHER FULL BOOK HINDI: {topic} | M{n:02d} {t} | Price 99 Only | Professional | Puri Knowledge\n\n"
 b=f"1. LAKSHYA: {t} ko {topic} me master karo 5 logo ko simple me samjhao Paribhasha 5 points.\n\n"
 c=f"2. KYU ZARURI: 2026 business ko {topic} {t} chahiye Bina fail salary kam Saath salary 3x $50/hr 80% bachega Top demanding future proof.\n\n"
 d=f"3. MUKHYA VICHAR: {t} ka matlab {topic} kaam karne ke peeche vichar Jaise car me engine {topic}=Perceive Reason Act WhatsApp check socho jawab {t} engine hai.\n\n"
 e=f"4. GEHRI THEORY: {t} ki paribhasha prakar kaise kaam karta hai Architecture kab upyog kab nahi ecom health finance education.\n\n"
 f=f"5. KADAM DAR KADAM 5 KADAM:\nKadam1 {t} paribhasha samjho {topic} 5 points\nKadam2 2 udaharan {topic} {t} safalta asafalta note kyu\nKadam3 Tools kholo {t} {topic} Make.com n8n ChatGPT Sheet 15m explore\nKadam4 Chhota project 15m {topic} {t} screenshot video\nKadam5 Diary kya seekha doubt {t} kal plan 15m theory practical\n\n"
 g=f"6. TOOLS: ChatGPT Make.com n8n Google Sheet WhatsApp API Canva Loom Free vs Paid tulna kaun free paid kab upyog setup.\n\n"
 h=f"7. UDAHARAN: Safalta Company A ne {t} {topic} me growth 3x 5h se 30m Asafalta B ne {t} chhoda fail Kya sahi kiya note.\n\n"
 i=f"8. CASE STUDY: Rahul gaon Redmi 8 Jio 1GB bina laptop roz 1h {topic} {t} Pehle manual 4h roz baad {t} automation 30m auto 90% auto malik 10k monthly 3 referral ecom YouTuber.\n\n"
 j=f"9. GALTIYA + PRO TIP: 90% fail {t} {topic} G1 Neenv chhodna Upay M01-M10 do baar G2 Sirf dekhna Upay 15m theory practical roz G3 Paisa peeche Upay 30 din skill G4 Diary nahi Upay 10m diary 4 points G5 Mentor nahi Upay community roz doubt Pro Tip Extra value 2h extra 5 star.\n\n"
 k=f"10. ABHYAAS: Aaj 15m theory +15m practical {topic} {t} Chhota project 1 kaam automate {t} se screenshot.\n\n"
 l=f"11. HOMEWORK + QUIZ: Homework {t} {topic} dost ko sikhao voice note 2m jama Quiz Q1 {t} kya hai {topic} me Q2 Kab upyog Q3 Tools kaun Self check.\n\n"
 m=f"12. AGLE KADAM + RESOURCES + TEMPLATES: Agla {nxt} is {t} par banega Resources YouTube docs communities LinkedIn Discord mentors Checklist Roz 1h Saptahik Portfolio Client onboarding Templates Ready prompt Make blueprint Sheet template WhatsApp API Canva Portfolio Minor Major Final Interview Q&A Top 20 {topic} {t} Freelancing Upwork Fiverr profile proposal 20 proposal 19 reject pehla client $15k 5 star 5 client 75k agency 2L.\n\nFull Book Page Poora - Pura Page Bhara - Puri Knowledge - Professional - Price 99 Only - Distinct"
 return a+b+c+d+e+f+g+h+i+j+k+l+m
def seo(topic):
 a=f"Brahma Super Agent Professional For {topic} | Market Best 100% Professional\n\n"
 b=f"SEO TITLE: {topic} Master Course 2026 | Top 50 High Level Demanding | Price 99 Only | Master Teacher Full Book 40 Modules 12 Sections\n\n"
 c=f"SEO DESCRIPTION: Learn {topic} scratch to advanced 2026 Most demanding high level AI Product $180K-$320K 600+ openings 300% growth AI Project $128K most in-demand Gen AI $200K 56% premium 40 modules WHAT IS WHY IMP REAL STORY MISTAKES FINAL PROJECT each 12 sections Goal Why Important Core Concept Deep Dive Step By Step Tools Real Examples Case Study Mistakes Pro Tips Practical Homework Quiz Next Steps Resources Templates Portfolio Interview Freelancing Rahul village Redmi 8 Jio 1GB story Tools ChatGPT Make.com n8n Price 99 only Brahma Super Agent handles SEO Digital Marketing Blogs Social Media Sales Chat Bot Professional.\n\n"
 d=f"KEYWORDS: {topic}, AI Product Management, AI Project Management, Generative AI, 2026 demanding courses, Price 99, Master Teacher Full Book 12 Sections, Step By Step Practical Case Study, ChatGPT Make.com Brahma Super Agent SEO Digital Marketing Professional\n\n"
 e=f"HASHTAGS: #{topic[:6]} #AIProductMgmt #GenAI #BrahmaAcademy #Price99 #MasterTeacher #FullBook #2026 Professional\n\n"
 f=f"BLOG POST: Why {topic} is Most Demanding in 2026? Market Data $180K-$320K 600+ openings 300% growth 56% premium What is {topic} 5 Steps master Case Study Rahul village Tools Mistakes Final Project 12 Sections Full Book Call to action Price 99 Brahma Super Agent auto handles blog creation SEO optimization professional.\n\n"
 g=f"FACEBOOK POST: {topic} Master Course 2026 | Most Demanding Future Proof | $180K-$320K Salary 600+ Openings | 40 Modules 12 Sections Step By Step Practical Case Study | Tools ChatGPT Make.com | Price 99 Only | Brahma Master Academy Professional\n\n"
 h=f"INSTAGRAM POST: {topic} Full Book | 40 Modules 12 Sections | WHAT IS WHY IMP REAL STORY MISTAKES FINAL | Rahul Redmi 8 Jio 1GB to Agency 2L Story | Practical Tools Case Study Full Knowledge | Price 99 Only | Brahma Master Academy Professional\n\n"
 i=f"MARKETING COPY: Master {topic} in 40 Days | Most Demanding 2026 $180K-$320K 600+ Openings 300% Growth | Benefits 40 Modules 12 Sections Goal Why Important Core Concept Deep Dive Step By Step Tools Real Examples Case Study Mistakes Pro Tips Practical Homework Quiz Next Steps Resources Templates Portfolio Interview Freelancing | Social Proof Rahul village Redmi 8 to Agency 2L | Price 99 Only Professional\n\n"
 j=f"SALES FUNNEL: Lead Magnet Free M01 WHAT IS module {topic} | Tripwire Rs 99 Full Course 40 Modules English + Hindi Full Book 12 Sections | Upsell Rs 999 Personal Mentorship + Portfolio Review | Brahma Super Agent Auto Handles Sales Funnel Email WhatsApp Follow Up Professional\n\n"
 k=f"CHAT BOT SCRIPT: Welcome to Brahma Master Academy {topic} Master Course 2026 Most Demanding Price 99 Only Professional | What is {topic}? {topic} is future proof high demanding 2026 $180K-$320K salary 600+ openings 300% growth Step by step practical case study Tools ChatGPT Make.com Full Book 12 Sections | Price? Rs 99 Only English + Hindi 2 Files 40 Modules Full Book Professional | How to buy? UPI Rs 99 pay UTR bhejo invoice milega approval ke baad English + Hindi download | Brahma Super Agent Chat Bot Auto Handles 24x7 Professional"
 return a+b+c+d+e+f+g+h+i+j+k
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
  tf.text=f"M{n:02d} {top} - {t} - EN - Full Book 12 Sections - Price 99 Professional"
  tf.paragraphs[0].font.size=Pt(11)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=en(top,n)
  bf.paragraphs[0].font.size=Pt(7)
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
  tf.text=f"M{n:02d} {top} - {t} - HI - Full Book 12 Sections - Price 99 Professional"
  tf.paragraphs[0].font.size=Pt(11)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=hi(top,n)
  bf.paragraphs[0].font.size=Pt(7)
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
 for i,name in enumerate(TOP50):
  d.append({"id":f"BRAHMA{1000+i}","topic":name.strip(),"price":99})
 save(CF,d)
 return d
courses=init50()
purchases=load(PF,[])
if st.session_state.admin_logged:
 if menu=="Dashboard":
  st.title("Dashboard - Brahma Master Academy - Professional Full Book")
  st.success("Top 50 High Level - Full Book Master Teacher - Har Module 12 Sections - Pura Page Bhara Puri Knowledge - Price 99 - Professional Academy - Crash Fixed Single File")
  c1,c2,c3=st.columns(3)
  c1.metric("Total Courses", len(courses))
  c2.metric("EN Full Book", len(list(PPT_DIR.glob("*EN.pptx"))))
  c3.metric("HI Full Book", len(list(PPT_DIR.glob("*HI.pptx"))))
  if st.button("DELETE OLD FILES"):
   for f in PPT_DIR.glob("*.*"):
    try:
     f.unlink()
    except:
     pass
   st.success("Done Old Deleted")
   st.rerun()
  if st.button("CREATE TOP 50 MASTER TEACHER FULL BOOK 12 SECTIONS", type="primary"):
   bar=st.progress(0)
   for idx,c in enumerate(courses):
    make(c)
    bar.progress(int((idx+1)/len(courses)*100))
   st.success("Done Full Book 12 Sections Top 50 Master Teacher Har Page Alag Distinct Pura Page Bhara Puri Knowledge Market Best 100% Professional Crash Fixed")
   st.balloons()
   st.rerun()
 elif menu=="Price Manager 99":
  st.title("Price Manager 99 - Professional")
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
     st.success("Done New Course Added Full Book 12 Sections English + Hindi 2 Files Professional")
     st.rerun()
  sel=st.selectbox("Select For PPT Full Book", [c["topic"]+" - "+c["id"] for c in courses])
  if st.button("Make Bilingual PPT Full Book 12 Sections", type="primary"):
   sid=sel.split(" - ")[-1]
   stopic=" - ".join(sel.split(" - ")[:-1])
   en_f,hi_f=make({"id":sid,"topic":stopic})
   st.success("Done Full Book 12 Sections Master Teacher Har Page Alag Distinct Pura Page Bhara Puri Knowledge Market Best Professional Crash Fixed")
   st.download_button("Download EN Full Book 12 Sections", data=en_f.read_bytes(), file_name=en_f.name)
   st.download_button("Download HI Full Book 12 Sections", data=hi_f.read_bytes(), file_name=hi_f.name)
 elif menu=="Course Library":
  st.title("Course Library - Top 50 Full Book Professional - 12 Sections")
  for idx,co in enumerate(courses):
   en_f=list(PPT_DIR.glob(co["id"]+"*EN.pptx"))
   hi_f=list(PPT_DIR.glob(co["id"]+"*HI.pptx"))
   if en_f and hi_f:
    st.success(f"{idx+1}. {co['topic']} - Rs {co.get('price',99)} - 2 Files Full Book 12 Sections Professional")
    a,b=st.columns(2)
    with a:
     st.download_button("EN Full Book 12 Sections", data=en_f[0].read_bytes(), file_name=en_f[0].name, key=f"en{idx}")
    with b:
     st.download_button("HI Full Book 12 Sections", data=hi_f[0].read_bytes(), file_name=hi_f[0].name, key=f"hi{idx}")
 elif menu=="UPI QR Setup":
  st.title("UPI QR Setup - Professional")
  st.write("UPI ID: "+UID+" Owner: "+OWNER+" Price 99 Only Professional")
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
  st.title("Brahma Super Agent - Professional - SEO + Marketing + Sales + Chat Bot - 12 Sections Full Book")
  for idx,co in enumerate(courses[:10]):
   with st.expander(f"{idx+1}. {co['topic']} - Brahma Super Agent Professional"):
    st.write(seo(co["topic"]))
    st.write("---")
    st.write("Brahma Super Agent Professional Tasks: SEO Title Description Keywords Hashtags Auto Digital Marketing Auto Post Content Blogs Auto Create SEO Optimized Blogs Facebook Instagram Auto Post Daily Reels Stories Hashtags Marketing Copy Sales Funnel Email WhatsApp Follow Up Sales Auto Follow Up Payment Reminder Invoice Access Key Chat Bot Auto 24x7 Handles Queries Full Book 12 Sections Goal Why Important Core Concept Deep Dive Step By Step Tools Real Examples Case Study Mistakes Pro Tips Practical Homework Quiz Next Steps Resources Templates Portfolio Interview Freelancing")
  st.success("Brahma Super Agent Active Professional - Crash Fixed - Professional Academy")
 elif menu=="Sales":
  st.title("Sales - Top 50 Full Book Professional - 12 Sections")
  for i,p in enumerate(purchases):
   with st.expander(f"{p.get('invoice_no','Order')} - {p.get('course','')} - Rs {p.get('price','')} - {p.get('status','')}"):
    st.write("Name:", p.get("name"))
    st.write("Email:", p.get("email"))
    st.write("Course:", p.get("course"))
    st.write("Price Rs 99 Only Professional:", p.get("price"))
    st.write("UTR:", p.get("utr"))
    st.write("Status:", p.get("status"))
    if p.get("status")=="PENDING":
     if st.button("APPROVE PAYMENT AND GIVE ACCESS", key=f"ap{i}", type="primary"):
      p["status"]="APPROVED"
      p["access_key"]="BRAHMA-"+secrets.token_hex(5).upper()
      save(PF,purchases)
      st.success(f"Done Approved - Key {p['access_key']}")
      st.rerun()
    else:
     st.success(f"Approved - Key {p.get('access_key')}")
else:
 if menu=="Browse Courses":
  st.title("Brahma Master Academy - Top 50 Master Courses - Market Best 100% - Price Rs 99 Only - Professional - Full Book 12 Sections")
  st.success("Top 50 High Level Demanding 2026 - Har Page Alag Distinct Full Book 12 Sections Pura Page Bhara Puri Knowledge - Jo Padhega Puri Tarah Seekh Jayega - Price Only Rs 99 - Professional Academy - Crash Fixed")
  for i,course in enumerate(courses):
   with st.expander(f"{i+1}. {course['topic']} - Rs {course['price']} - English + Hindi Full Book 12 Sections - Price 99 Only - Professional"):
    params={"pa":UID,"pn":OWNER,"am":str(course["price"]),"cu":"INR","tn":course["topic"][:20]}
    link="upi://pay?"+urllib.parse.urlencode(params)
    st.write(f"Course: {course['topic']} - Market Best 100% - Full Book 12 Sections - Har Page Alag Distinct Pura Page Bhara Puri Knowledge Professional")
    st.link_button(f"PAY Rs {course['price']} - Get English + Hindi Full Book 12 Sections - Price 99 Only Professional", link, type="primary")
    with st.form(f"buy_{course['id']}"):
     name=st.text_input("Your Name", key=f"n{course['id']}")
     email=st.text_input("Your Email", key=f"e{course['id']}")
     utr=st.text_input("UTR Number After Payment - 12 Digit", key=f"u{course['id']}")
     submit=st.form_submit_button(f"SUBMIT PAYMENT Rs {course['price']} - Get Access Full Book 12 Sections Professional")
     if submit:
      if len(name)<3 or len(email)<5 or len(utr)<5:
       st.error("Error - Fill All Details")
      else:
       purchases.append({"invoice_no":"INV"+datetime.datetime.now().strftime("%Y%m%d%H%M%S"),"access_key":"","name":name,"email":email,"course":course["topic"],"course_id":course["id"],"price":int(course["price"]),"utr":utr,"status":"PENDING","date":str(datetime.datetime.now())})
       save(PF,purchases)
       st.success(f"Done Payment Submitted - Invoice {purchases[-1]['invoice_no']} - After Admin Approval You Get English + Hindi Both Full Book 12 Sections Files Professional")
 elif menu=="My Access":
  st.title("My Learning - Top 50 Full Book Master Teacher - Price 99 Only - Professional - 12 Sections")
  k=st.text_input("Enter Invoice Number Or Access Key")
  if st.button("UNLOCK BILINGUAL FULL BOOK 12 SECTIONS - PRICE 99 ONLY - PROFESSIONAL", type="primary"):
   found=[p for p in purchases if (p.get("invoice_no")==k or p.get("access_key")==k) and p.get("status")=="APPROVED"]
   if not found:
    st.error("Error - Invoice Or Key Not Found Or Not Approved Yet")
   else:
    pu=found[0]
    st.success(f"Welcome {pu.get('name','Student')} - {pu.get('course')} - Price Rs {pu.get('price','99')} Only - Full Book 12 Sections Professional")
    en_f=list(PPT_DIR.glob(pu.get("course_id","")+"*EN.pptx"))
    hi_f=list(PPT_DIR.glob(pu.get("course_id","")+"*HI.pptx"))
    if en_f:
     st.download_button("DOWNLOAD ENGLISH FULL BOOK 12 SECTIONS - PRICE 99 ONLY - PROFESSIONAL", data=en_f[0].read_bytes(), file_name=en_f[0].name, type="primary")
    if hi_f:
     st.download_button("DOWNLOAD HINDI FULL BOOK 12 SECTIONS - PRICE 99 ONLY - PROFESSIONAL", data=hi_f[0].read_bytes(), file_name=hi_f[0].name, type="secondary")
    if not en_f:
     st.warning("Books Not Ready Yet - Admin Will Create Soon")
st.caption("Brahma Master Academy V118 Professional Full Book 12 Sections Crash Fixed Single File | Har Page Alag Distinct Full Book Pura Page Bhara Puri Knowledge | 12 Sections Goal Why Important Core Concept Deep Dive Step By Step Tools Real Examples Case Study Mistakes Pro Tips Practical Homework Quiz Next Steps Resources Templates | Top 50 High Level Price 99 | Full Dashboard API IDs QR Price Change New Course Super Agent SEO Marketing Blogs Social Media Marketing Sales Chat Bot | Single File No Import No White Screen | Professional Academy | No Retirement Wording")