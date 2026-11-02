import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path
st.set_page_config(page_title='Brahma AI', layout='wide')
DATA=Path('data')
PPT_DIR=DATA/'ppts'
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)
CF=DATA/'courses.json'
PF=DATA/'purchases.json'
MH=DATA/'.master_hash'
AS=DATA/'.admin_session'
QF=DATA/'upi_qr.jpg'
AF=DATA/'api_keys.json'
UID='parveen39179@okicici'
OWNER='Parveen Kumar'
def load(p,d):
 try:
  if p.exists():
   return json.loads(p.read_text(encoding='utf-8'))
 except:
  pass
 return d
def save(p,d):
 t=p.with_suffix('.tmp')
 t.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
 t.replace(p)
TOP25=['AI Product Mgmt','AI Project Mgmt','Gen AI Prompt','AI Agents','AI Eng LLM','ML MLOps','AI Strategy','LLM RAG','AI Auto n8n','Data Science','Data Analytics','Data Eng','CyberSec','Cloud AWS','DevOps','FullStack MERN','Python FullStack','Digital Mkt','SEO','FinTech','Blockchain','NoCode','Chatbot','SaaS','Ecom Shopify']
MODS=['WHAT IS','WHY IMP','WHERE USE','WHEN USE','WHO LEARN','HOW WORKS','TOOLS','EARN MONEY','PRACTICAL','RIGHT WAY','FOUNDATION','CORE','ADVANCED','STEP PROCESS','EXAMPLE','CLIENT REQ','REAL STORY','PLANNING','IMPLEMENT','MISTAKES','PRO TIP','EXPERT','COMPARE','FREE PAID','PORTFOLIO','FIND CLIENT','FREELANCING','AGENCY','MODEL','SCALING','SEO','LEAD','SALES','AUTO','OPTIMIZE','CASE STUDY','DAILY','HOMEWORK','REVISION','FINAL PROJECT']
def writer(topic,n):
 t=MODS[n-1]
 nxt=MODS[n] if n<40 else 'COMPLETE'
 a=f'ENGLISH ONLY SINGLE FILE 100% DATA {topic} M{n:02d} {t}\n'
 b=f'COVER {topic} Tagline Most Demanding 2026 Price 99 Master Teacher 40 Modules\n'
 c=f'OVERVIEW What is {topic} {t}? Who for? What learn? Future salary $180K-$320K 600+ openings 300% growth\n'
 d=f'OUTCOMES 10 After M{n:02d} you can define {t} explain to 5 people build project save 2h use tools find clients earn $50/hr portfolio avoid mistakes final project\n'
 e=f'PREREQ Phone internet 1h daily No laptop No degree 10th fail village city Redmi 8 Jio 1GB Rahul 1h daily 2L\n'
 f=f'ROADMAP Month1-2 foundation M01-M10 {t} Month3 portfolio 3 projects Month4 5 clients 75k Month6 agency 2L Next {nxt}\n'
 g=f'TOOLS ChatGPT Make.com n8n Sheet WhatsApp API Canva Loom Free vs Paid\n'
 h=f'MODULE M{n:02d} {topic} - {t} - ENGLISH ONLY - Master Teacher Writer Teacher Style - Price 99 - No Ulta Sidha\n'
 i=f'GOAL After this you can {t} in {topic} explain to 5 people real example\n'
 j=f'WHY IMPORTANT Salary demand 56% premium $180K-$320K Without {t} fail With {t} salary 3x $50/hr 80% save Top demanding 2026\n'
 k=f'CORE CONCEPT {t} simple Perceive Reason Act Engine car WhatsApp check think reply {topic}=Perceive+Reason+Act\n'
 l=f'DEEP DIVE Definition Types How {t} works Architecture Input Process Output Frontend Backend API When use when not ecom health finance education\n'
 m=f'STEP BY STEP 5 STEPS Choose task {topic} {t} Open ChatGPT prompt You are {t} expert reply friendly Connect Make.com Test second account Diary 15m theory 15m practical\n'
 n2=f'TOOLS PRACTICAL Which tools {t} {topic} Free vs Paid How use click by click 15m explore each\n'
 o=f'REAL EXAMPLES Success Company A used {t} {topic} growth 3x 5h to 30m Failure Company B skipped fail Note why\n'
 p=f'CASE STUDY Rahul village Redmi 8 Jio 1GB no laptop 1h daily {topic} {t} Before manual 4h after 30m auto 90% auto shop owner paid 10k monthly 3 referrals proof screenshot video\n'
 q=f'MISTAKES PRO TIPS 90% fail {t} {topic} M1 Skip foundation Fix M01-M10 twice M2 Only watch Fix 15m theory practical daily M3 Money chase Fix 30 days skill only M4 No diary Fix 10m diary 4 points M5 No mentor Fix community daily doubt Pro Tip Extra value 2h extra 5 star referral shortcut save 6 months\n'
 r=f'PRACTICAL HOMEWORK QUIZ Today 15m theory +15m practical Build mini project {t} {topic} automate 1 task screenshot Teach {t} {topic} to friend voice note 2m Quiz What is {t}? When use? Tools?\n'
 s=f'NEXT STEPS Next {nxt} builds on {t} Link next module Previous M{n-1:02d} Next {nxt}\n'
 t2=f'PROJECTS 5 Minor every 8 modules 1 small project {t} {topic} 2 Major after M20 M30 Real client Before After ROI 1 Final M40 Full portfolio Problem choose Plan workflow Build Test 10x Result screenshot Portfolio upload Behance GitHub LinkedIn 1Cr roadmap This is interview\n'
 u=f'EXTRA Templates prompts Make.com blueprints Sheet templates WhatsApp API Canva Checklists Daily 1h Weekly Portfolio Client onboarding Cheat Sheets Tools comparison Free vs Paid Pricing Salary $180K-$320K Case Studies 10 Rahul story Shop owner Ecom YouTuber Freelancer Interview Q&A Top 20 Answer Freelancing Upwork Fiverr profile proposal 20 proposals 19 reject First client $15k 5 star Referral 5 clients 75k Agency 2L Resources YouTube Docs Communities LinkedIn Discord Mentors\n'
 v=f'ASSESSMENT Quiz 3-5 self check Assignment practical screenshot video submit Final Exam M40 final project review Certificate Brahma Professional English Only\n'
 w=f'SUPER AGENT SEO Title {topic} {t} Master Course 2026 Top 25 Demanding Price 99 Only Master Teacher Writer Teacher Style English Only Single File 100% Data Har Page Alag Distinct Market Best 100% Blog Why {topic} {t} is Most Demanding 2026 Market Data $180K-$320K 600+ openings Facebook Instagram post {topic} Master Course 2026 Most Demanding Future Proof $180K-$320K Salary 600+ Openings 40 Modules Har Page Alag Distinct Full Book Pura Page Bhara Puri Knowledge Price 99 Only Brahma Master Academy Marketing Copy Sales Funnel Email WhatsApp Chat Bot Price 99 UPI UTR Invoice Access Key Welcome to Brahma Master Academy {topic} {t} Master Course 2026 Most Demanding Price 99 Only English Only Single File Master Teacher Writer Teacher Style 100% Data\n'
 x=f'FULL BOOK PAGE COMPLETE DISTINCT Pura Page Bhara Puri Knowledge Market Best 100% Price 99 Only Har Page Alag Distinct Good Writer Good Teacher Style Proper Arrange No Ulta Sidha 7 Points Structure Complete Master Teacher AI Writer Teacher Style English Only Single File Best 25 Demanding 2026 100% Data Collected Online Har Course Ka Data Har Course Me'
 return a+b+c+d+e+f+g+h+i+j+k+l+m+n2+o+p+q+r+s+t2+u+v+w+x
def make(c):
 from pptx import Presentation
 from pptx.util import Inches, Pt
 cid=c['id']
 top=c['topic']
 en_p=PPT_DIR/(f'{cid}_EN.pptx')
 prs=Presentation()
 prs.slide_width=Inches(13.33)
 prs.slide_height=Inches(7.5)
 for n in range(1,41):
  t=MODS[n-1]
  s=prs.slides.add_slide(prs.slide_layouts[6])
  tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
  tf=tb.text_frame
  tf.word_wrap=True
  tf.text=f'M{n:02d} {top} - {t} - ENGLISH ONLY - Writer Teacher - 100% Data - Price 99'
  tf.paragraphs[0].font.size=Pt(10)
  tf.paragraphs[0].font.bold=True
  bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
  bf=bb.text_frame
  bf.word_wrap=True
  bf.text=writer(top,n)
  bf.paragraphs[0].font.size=Pt(6)
 prs.save(str(en_p))
 return en_p
def make_hash(pw):
 return hashlib.sha256(pw.encode()).hexdigest()
def verify(pw,stored):
 return hashlib.sha256(pw.encode()).hexdigest()==stored
def sess_valid():
 try:
  d=load(AS,{})
  exp=datetime.datetime.fromisoformat(d['expiry'])
  return datetime.datetime.now()<exp
 except:
  return False
if 'admin_logged' not in st.session_state:
 st.session_state.admin_logged=sess_valid()
st.sidebar.title('Brahma AI Writer')
if not MH.exists():
 pw=st.sidebar.text_input('Create Password', type='password')
 if st.sidebar.button('Create Admin'):
  if pw and len(pw)>=4:
   MH.write_text(make_hash(pw), encoding='utf-8')
   st.rerun()
 menu='Browse'
else:
 if not st.session_state.admin_logged:
  menu=st.sidebar.radio('Menu',['Browse Courses','My Access'])
  pw=st.sidebar.text_input('Password', type='password')
  if st.sidebar.button('Login'):
   stored=MH.read_text(encoding='utf-8').strip()
   if verify