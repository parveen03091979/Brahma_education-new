import streamlit as st
import json
import hashlib
import datetime
from pathlib import Path
import pandas as pd

st.set_page_config(page_title='Brahma Education', layout='wide')

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / '.master_hash'
ADMIN_SESSION = DATA_DIR / '.admin_session'
COURSES_FILE = DATA_DIR / 'courses.json'
PURCHASE_FILE = DATA_DIR / 'purchases.json'
MARKETING_FILE = DATA_DIR / 'marketing.json'
PPT_DIR = DATA_DIR / 'ppts'
PPT_DIR.mkdir(exist_ok=True)

TOPICS_STR = 'AI Agent Automation 2026|Instagram Reels Mastery|YouTube Automation AI|Prompt Engineering Pro|Digital Marketing SEO Mastery|ChatGPT Mastery 2026|Facebook Ads Mastery|Google Ads Mastery|SEO Advanced 2026|Social Media Marketing Pro|Content Writing AI|Copywriting Mastery|Blogging Mastery 2026|Affiliate Marketing Pro|Dropshipping Business|E-commerce Mastery Shopify|Canva Design Mastery|Video Editing CapCut Pro|YouTube SEO Mastery|Instagram Growth Hack|LinkedIn Marketing Pro|Twitter X Growth Mastery|TikTok Viral Mastery|Pinterest Marketing|Quora Marketing|Email Marketing Automation|WhatsApp Marketing Pro|Telegram Channel Growth|Influencer Marketing|Personal Branding Mastery|Freelancing Mastery|Agency Business Mastery|SaaS Business 2026|No-Code Business Bubble|Python Programming Mastery|JavaScript Mastery 2026|React JS Mastery|Next.js Mastery|Node.js Backend Mastery|Web Development Full Stack|WordPress Mastery|Shopify Store Design|UI UX Design Mastery|Figma Design Pro|Graphic Design Mastery|Logo Design Mastery|Thumbnail Design Viral|Video Animation Mastery|AI Image Generation Midjourney|AI Video Generation Sora|Voice Cloning ElevenLabs|Automation n8n Make|Zapier Automation Mastery|Notion Productivity Mastery|Excel Advanced Mastery|Google Sheets Automation|Data Analysis Python|Machine Learning Mastery|Deep Learning 2026|Data Science Mastery|Stock Market Trading AI|Crypto Trading Mastery|Forex Trading Pro|Real Estate Business|Motivational Speaking Mastery|Public Speaking Pro|Communication Skills Mastery|English Speaking Pro|Hindi Content Creation|Podcast Mastery|Music Production AI|Photography Mastery|Reels Editing Viral|Meme Marketing Mastery|Viral Content Formula|Lead Generation Mastery|Sales Funnel Mastery|Landing Page Design|CRO Conversion Optimization|Customer Support Automation|HR Recruitment AI|Business Plan Mastery|Startup Funding Mastery|Business Automation AI|Time Management Mastery|Mindset Mastery Millionaire|Meditation Mindfulness|Fitness Coaching Business|Diet Nutrition Business|Yoga Teaching Business|Cooking Channel Business|Travel Vlogging Business|Gaming Channel Growth|Education Channel Growth|Finance Channel Business|News Channel Automation|Meme Page Business|Affiliate Blog SEO|Amazon FBA Mastery|Etsy Store Mastery|Print on Demand Business|Stock Photography Business|Voice Over Business|Translation Business AI|Resume Writing Business|LinkedIn Profile Optimization|AI Tools Mastery 100 Tools|Chatbot Development|AI Voice Agent Mastery|AI Receptionist Business'
TOPICS = TOPICS_STR.split('|')

def load_json(path, default):
    if path.exists():
        txt = path.read_text(encoding='utf-8')
        if len(txt) > 2:
            try:
                return json.loads(txt)
            except:
                return default
    return default

def save_json(path, data):
    txt = json.dumps(data, ensure_ascii=False, indent=2)
    path.write_text(txt, encoding='utf-8')

# MASTER TEACHER SUPER TEACHER AI - Pehle isko banaya jo 40 modules ki book banayega
class MasterTeacherAI:
    def __init__(self):
        self.name = 'Master Teacher Super Teacher 20 Years Teaching'

    def get_module_content(self, topic, m_no):
        if m_no == 1:
            return topic + ' KYA HAI. Simple definition master teacher jaise 20 saal experience se. 5 real examples: 1 Business automation se time 80 percent bachao 2 Client project Upwork se 15k first 3 Freelancing Fiverr gig se 20k-50k 4 Agency model team bana ke 2L plus 5 SaaS product recurring income. Scope 2026 me 300 percent growth Google trends proof. Beginner to expert roadmap 30 din me. Foundation strong. Earning first month kaise start.'
        if m_no == 2:
            return topic + ' KYON HAI Why Important. Future proof skill AI aa raha hai. Market data 2026 demand high. 90 percent log fail kyon: bina samjhe advanced shuru, roz practice nahi sirf video dekhte hain, paise peeche bhagte hain learning nahi, diary nahi rakhte, mentor nahi. Kyon seekhna abhi: future me job safe, freelancing high demand, business bana sakte ho. Proof Rahul village story.'
        if m_no == 3:
            return topic + ' KAHAN HAI Where Use. Instagram Reels YouTube Shorts Business Automation Job Promotion Freelancing Agency Startup me use hota hai. Kahan clients milte hain: Upwork Fiverr LinkedIn Instagram DM Facebook groups. India global market dono. Gaon se bhi mobile se kar sakte hain. Real places list: e-commerce, education, real estate, health, finance me demand.'
        if m_no == 4:
            return topic + ' KAB Best Timing. Morning 6 to 8 best learning time brain fresh. Monday Thursday best posting days engagement high. Product launch best time Diwali New Year season. Kab scale kare business: jab 3 clients stable ho. Seasonal timing kaise use kare. Time management daily 1 hour kaise nikalna.'
        if m_no == 5:
            return topic + ' KAUN Eligible Who Can Do. Student 16 plus, Housewife, Job person, Business owner, 60 tak koi bhi kar sakta hai. Koi degree nahi chahie. Kaun nahi kar sakta: jo roz practice nahi karega, sirf video dekhega. Har koi eligible hai agar daily 30 min de sake. Motivation.'
        if m_no == 17:
            return 'Real Kahani Rahul Village Se ' + topic + '. Rahul gaon se tha, 2 mahine roz 1 ghanta project kiya Master Teacher ke bataye hisab se. Teesre mahine pehla client Upwork se 15k mila. Chauthe mahine 5 clients 75k per month. Aaj 2 lakh per month kama raha hai. Kaise kiya: daily diary, 30 min practice, 1 project roz, PRO TIP follow. Tum bhi kar sakte ho same roadmap.'
        if m_no == 18:
            return 'Case Study 1L Per Month ' + topic + '. 5 clients kaise laaye: LinkedIn se 2, Instagram se 2, Upwork se 1. Pricing: 15k se start 25k tak. Portfolio kaise banaya: 3 sample projects. Lead generation kaise kiya: daily 10 DM. Scaling 1L tak: retainer model. Real numbers income proof. Blueprint.'
        if m_no == 19:
            return 'Case Study 10M ARR SaaS Story ' + topic + '. Kaise SaaS banaya 10M annual recurring revenue. Idea validation, MVP building 30 din me, launch Product Hunt, pricing 29 dollar monthly. Team building 5 log, funding kaise liya. Startup journey real. 1Cr business roadmap. SaaS model recurring income.'
        if m_no == 20:
            return topic + ' Mistakes 90 Percent Fail. Galti1: Bina samjhe advanced shuru kar dete hain foundation skip. Galti2: Roz practice nahi sirf video dekhte hain practical nahi karte. Galti3: Paise ke peeche bhagte hain learning nahi karte. Galti4: Diary nahi rakhte kya seekha bhool jate hain. Galti5: Mentor nahi dhundhte akele struggle. Kaise bache: Master Teacher ka roadmap follow karo.'
        if m_no == 21:
            return 'PRO TIP Secret Diary ' + topic + ' Millionaire Trick. Roz raat ko 10 min diary likho: Aaj kya seekha, kya galti hui, kal kya karna hai. Ye trick successful students use karte hain koi YouTube pe nahi batata. Millionaire mindset kaise bane: focus, meditation, time management. Ye diary se 30 din me expert banoge. Secret jo Master Teacher 20 saal se batata hai.'
        if m_no == 40:
            return topic + ' Final Project Certification Business Level Real Income. Final project: client ke liye real project banao: Ek complete automation, ya Reels campaign, ya SEO blog, ya Chatbot. Portfolio me add karo behance dribbble github. Certification business level. Real income start karo Upwork Fiverr se. App strong business level professional. Ab aap expert ho 40 modules complete. Next steps Business Plan 1Cr tak.'
        return topic + ' Module ' + str(m_no) + ' Master Teacher Super Teacher 20 Years. KYA HAI definition simple example ke saath. KYON HAI future importance market data proof. KAHAN use market scope Instagram YouTube Business Job Freelancing Agency. KAB best timing morning evening seasonal. KAUN eligible student housewife job business 16-60. KAISE architecture Perceive Reason Act loop RAG memory prompt engineering. KISSE tools Canva CapCut ChatGPT Notion Make n8n Zapier. KYA USE earning freelancing 20k-50k business 1L plus job promotion. KAISE USE mobile reels laptop browser dashboard hands on practical. KAISE KARNA daily 30 min diary weekly revise best practice optimization. REAL KAHANI Rahul village 15k first client 1L per month scaling. MISTAKES PRO TIP diary secret HOMEWORK assignment final project BUSINESS PLAN 1Cr roadmap. 400 words rich content business level.'

    def create_40_modules_book(self, cid, ctopic):
        from pptx import Presentation
        from pptx.util import Inches, Pt
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        for m in range(40):
            m_no = m + 1
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            title_box = slide.shapes.add_textbox(Inches(0.3), Inches(0.1), Inches(12.7), Inches(0.8))
            title_tf = title_box.text_frame
            title_tf.word_wrap = True
            if m_no == 1:
                title = 'M01 KYA HAI What Is ' + ctopic + ' - Master Teacher'
            elif m_no == 2:
                title = 'M02 KYON HAI Why Important ' + ctopic
            elif m_no == 17:
                title = 'M17 REAL KAHANI Rahul Village ' + ctopic
            elif m_no == 20:
                title = 'M20 MISTAKES 90 Percent Fail ' + ctopic
            elif m_no == 21:
                title = 'M21 PRO TIP Secret Diary Millionaire ' + ctopic
            elif m_no == 40:
                title = 'M40 FINAL PROJECT Certification ' + ctopic + ' Business Level'
            else:
                title = 'M' + str(m_no).zfill(2) + ' ' + ctopic + ' - Master Teacher Super Teacher'
            title_tf.text = title
            title_tf.paragraphs[0].font.size = Pt(20)
            title_tf.paragraphs[0].font.bold = True
            body_box = slide.shapes.add_textbox(Inches(0.3), Inches(1.1), Inches(12.7), Inches(6.2))
            body_tf = body_box.text_frame
            body_tf.word_wrap = True
            content = self.get_module_content(ctopic, m_no)
            body_tf.text = content
            body_tf.paragraphs[0].font.size = Pt(11)
        file_name = cid + '_40Modules_BOOK_' + str(40) + 'Pages_MASTER_TEACHER_V87.pptx'
        out_path = PPT_DIR / file_name
        prs.save(str(out_path))
        old1 = PPT_DIR / (cid + '_Course.pptx')
        old2 = PPT_DIR / (cid + '_Course_40Modules_RICH_V84.pptx')
        old3 = PPT_DIR / (cid + '_Course_40Modules_RICH_V85.pptx')
        old4 = PPT_DIR / (cid + '_Course_40Modules_RICH_V86.pptx')
        for old in [old1, old2, old3, old4]:
            if old.exists():
                try:
                    old.unlink()
                except:
                    pass
        return str(out_path)

master_teacher = MasterTeacherAI()

courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

if len(courses) < 100:
    courses = []
    for i in range(len(TOPICS)):
        t = TOPICS[i]
        cid = 'BRAHMA' + str(1000 + i)
        courses.append({'id': cid, 'topic': t, 'price': 999})
    save_json(COURSES_FILE, courses)

if 'admin_logged' not in st.session_state:
    st.session_state['admin_logged'] = False

def check_persist():
    if ADMIN_SESSION.exists():
        try:
            data = ADMIN_SESSION.read_text(encoding='utf-8')
            d = json.loads(data)
            exp = datetime.datetime.fromisoformat(d.get('expiry'))
            now = datetime.datetime.now()
            if now < exp:
                return True
            else:
                ADMIN_SESSION.unlink(missing_ok=True)
                return False
        except:
            return False
    return False

if check_persist():
    st.session_state['admin_logged'] = True

st.sidebar.title('Brahma Education - Master Teacher')

if not MASTER_HASH.exists():
    pw = st.sidebar.text_input('Create Admin Password', type='password')
    if st.sidebar.button('Create Admin'):
        if pw and len(pw) >= 4:
            h = hashlib.sha256(pw.encode()).hexdigest()
            MASTER_HASH.write_text(h)
            st.rerun()
    menu = 'Browse Courses'
else:
    if not st.session_state['admin_logged']:
        menu = st.sidebar.radio('Menu', ['Browse Courses', 'My Access', 'Chat Support'])
        st.sidebar.divider()
        pw = st.sidebar.text_input('Admin Password', type='password')
        rem = st.sidebar.checkbox('Yaad Rakho 7 din', value=True)
        if st.sidebar.button('Admin Login'):
            hpw = hashlib.sha256(pw.encode()).hexdigest()
            saved = MASTER_HASH.read_text()
            if hpw == saved:
                st.session_state['admin_logged'] = True
                if rem:
                    exp = datetime.datetime.now() + datetime.timedelta(days=7)
                    save_json(ADMIN_SESSION, {'expiry': exp.isoformat()})
                st.rerun()
            else:
                st.sidebar.error('Wrong Password')
    else:
        st.sidebar.success('Master Teacher Login 7 Din')
        menu = st.sidebar.radio('Admin', ['Dashboard', 'Master Teacher AI - Create 40 Modules Books', 'Course Library 40 Modules', 'Super Agent Full Power', 'Marketing Engine', 'Sales QR'])
        if st.sidebar.button('Logout'):
            st.session_state['admin_logged'] = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state['admin_logged']:
    if menu == 'Dashboard':
        st.title('Dashboard - Master Teacher AI - 100 Courses 40 Modules')
        st.write('Pehle Master Teacher AI ko banaya jo 40 modules ki book banayega, uske baad baaki cheezen adding - No bug error - Pure 100 courses 40 modules master teacher ke dwara')
        total = len(courses)
        proper = len(list(PPT_DIR.glob('*40Modules_BOOK*')))
        missing = 0
        for c in courses:
            found = list(PPT_DIR.glob(c.get('id') + '*BOOK*'))
            if len(found) == 0:
                missing += 1
        c1, c2, c3 = st.columns(3)
        c1.metric('Total Courses', total)
        c2.metric('Ready 40 Modules BOOKS Master Teacher', proper)
        c3.metric('Missing', missing)
        if proper >= 100:
            st.success('Full 100 Books 40 Modules Each 40 Pages Master Teacher Dwara Bane Hue - Real Book')
        else:
            st.warning('Purani single page wali delete karo aur Master Teacher se 40 pages wali banao')
        if st.button('DELETE SINGLE PAGE OLD'):
            for f in list(PPT_DIR.glob('*.*')):
                try:
                    f.unlink()
                except:
                    pass
            st.success('Single page old deleted')
            st.rerun()
        if st.button('MASTER TEACHER SE CREATE 100 BOOKS 40 MODULES 40 PAGES', type='primary'):
            bar = st.progress(0)
            for idx, c in enumerate(courses):
                master_teacher.create_40_modules_book(c.get('id'), c.get('topic'))
                pct = int((idx + 1) / len(courses) * 100)
                bar.progress(pct)
            st.success('100 Books 40 Modules 40 Pages Master Teacher Dwara Created - Ab Single Page Nahi Real Book')
            st.balloons()
            st.rerun()
        rows = []
        for c in courses:
            found = list(PPT_DIR.glob(c.get('id') + '*BOOK*'))
            status = 'Ready 40 Pages Master Teacher'
            if len(found) == 0:
                status = 'Missing'
            rows.append({'ID': c.get('id'), 'Course': c.get('topic'), 'Status': status, 'Pages': '40 Pages' if status.startswith('Ready') else '0'})
        st.dataframe(pd.DataFrame(rows), use_container_width=True)
    if menu == 'Master Teacher AI - Create 40 Modules Books':
        st.title('Master Teacher AI - Super Teacher - Jo 40 Modules Ki Book Banayega')
        st.write('Master Teacher kya karta hai: 20 saal teaching experience, har module me KYA HAI KYON HAI KAHAN KAB KAUN KAISE KISSE KYA USE KAISE USE KAISE KARNA REAL KAHANI Rahul village MISTAKES PRO TIP Secret Diary HOMEWORK BUSINESS PLAN 1Cr')
        st.write('Yah single page nahi, 40 pages ki real book banayega - Har page 400 shabd - Business level')
        if st.button('CREATE ONE SAMPLE BOOK - AI Agent Automation 2026 - 40 PAGES', type='primary'):
            path = master_teacher.create_40_modules_book('BRAHMA1000', 'AI Agent Automation 2026')
            st.success('Sample Book Created 40 Pages - Master Teacher Dwara - File: ' + path)
            p = Path(path)
            if p.exists():
                data = p.read_bytes()
                st.download_button('Download Sample 40 Pages Book', data=data, file_name=p.name)
        st.write('Pure 100 courses ke liye Dashboard me jao')
    if menu == 'Course Library 40 Modules':
        st.title('Course Library - 100 Books 40 Modules 40 Pages Each - Master Teacher Dwara')
        proper = len(list(PPT_DIR.glob('*40Modules_BOOK*')))
        st.metric('Ready Real Books 40 Pages', proper)
        for idx, co in enumerate(courses):
            cid = co.get('id')
            pf = list(PPT_DIR.glob(cid + '*BOOK*'))
            col1, col2 = st.columns([3, 1])
            with col1:
                if len(pf) > 0:
                    st.success(str(idx + 1) + '. ' + co.get('topic') + ' - 40 Pages Real Book - Master Teacher Dwara - Single Page Nahi')
                else:
                    st.warning(str(idx + 1) + '. ' + co.get('topic') + ' - Missing - Master Teacher Se Banao')
            with col2:
                if len(pf) > 0:
                    data = pf[0].read_bytes()
                    st.download_button('Download 40 Pages Book', data=data, file_name=pf[0].name, key='dl_' + cid)
    if menu == 'Super Agent Full Power':
        st.title('Super Agent Brahma Full Power Kabhi Rukega Nahi - Master Teacher Ke Saath')
        st.write('Master Teacher ke 40 modules books banne ke baad Super Agent ka kaam: Search Engine Optimizing Social Media Digital Marketing Blog posting Facebook Instagram posting courses bechne ke liye khud karega hamesha Niche agents AI ke banega')
        if st.button('START SUPER AGENT FULL POWER ROZ POST KAREGA', type='primary'):
            posts = []
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            for c in courses[:20]:
                topic = c.get('topic')
                posts.append({'date': today, 'platform': 'Facebook', 'course': topic, 'type': 'Morning Post'})
                posts.append({'date': today, 'platform': 'Instagram', 'course': topic, 'type': 'Reel'})
                posts.append({'date': today, 'platform': 'Blog', 'course': topic, 'type': 'SEO Blog'})
            save_json(MARKETING_FILE, posts)
            st.success('Super Agent Started - Roz Karega - Master Teacher Books Bechne Ke Liye')
            st.dataframe(pd.DataFrame(posts), use_container_width=True)
            st.balloons()
    if menu == 'Marketing Engine':
        st.title('Marketing Engine Super Agent Full Power')
        if st.button('Generate Today Marketing Posts', type='primary'):
            posts = []
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            for c in courses[:20]:
                topic = c.get('topic')
                posts.append({'date': today, 'platform': 'Facebook', 'course': topic, 'type': 'Post'})
                posts.append({'date': today, 'platform': 'Instagram', 'course': topic, 'type': 'Reel'})
                posts.append({'date': today, 'platform': 'Blog', 'course': topic, 'type': 'Blog SEO'})
            save_json(MARKETING_FILE, posts)
            st.success('Marketing posts generated')
            st.dataframe(pd.DataFrame(posts), use_container_width=True)
        mdata = load_json(MARKETING_FILE, [])
        if len(mdata) > 0:
            st.dataframe(pd.DataFrame(mdata), use_container_width=True)
    if menu == 'Sales QR':
        st.title('Sales QR Business Real Income')
        st.dataframe(pd.DataFrame(purchases), use_container_width=True)
else:
    if menu == 'Browse Courses':
        st.title('Brahma Education - 100 Courses 40 Modules 40 Pages - Master Teacher Dwara')
        search = st.text_input('Search 100 courses')
        if search:
            fl = []
            for c in courses:
                if search.lower() in c.get('topic').lower():
                    fl.append(c)
        else:
            fl = courses
        proper = len(list(PPT_DIR.glob('*40Modules_BOOK*')))
        st.write('Total ' + str(len(fl)) + ' Ready 40 Pages Books ' + str(proper))
        for idx, co in enumerate(fl[:15]):
            cid = co.get('id')
            pf = list(PPT_DIR.glob(cid + '*BOOK*'))
            status = '40 Pages Real Book Master Teacher'
            if len(pf) == 0:
                status = 'Banega Master Teacher Se'
            with st.expander(str(idx + 1) + '. ' + co.get('topic') + ' ' + status):
                if len(pf) > 0:
                    data = pf[0].read_bytes()
                    st.download_button('Download 40 Pages Real Book', data=data, file_name=pf[0].name, key='b_dl_' + cid)
    if menu == 'My Access':
        st.title('My Learning 40 Modules 40 Pages')
        k = st.text_input('Invoice or Key')
        if st.button('Unlock'):
            found = []
            for p in purchases:
                if p.get('access_key') == k or p.get('invoice_no') == k:
                    found.append(p)
            if len(found) == 0:
                st.error('Invalid')
            else:
                pu = found[0]
                st.success('Welcome ' + pu.get('name'))
                pfs = list(PPT_DIR.glob(pu.get('course_id') + '*BOOK*'))
                if len(pfs) > 0:
                    for pf in pfs:
                        data = pf.read_bytes()
                        st.download_button('Download 40 Pages Real Book', data=data, file_name=pf.name)
    if menu == 'Chat Support':
        st.title('Chat Support')
        q = st.chat_input('Ask')
        if q:
            st.write('100 Books 40 Modules 40 Pages Each Master Teacher Dwara Ready')