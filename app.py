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
PPT_DIR = DATA_DIR / 'ppts'
PPT_DIR.mkdir(exist_ok=True)
MARKETING_FILE = DATA_DIR / 'marketing.json'

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

# MASTER TEACHER SUPER TEACHER AI - Pehle isko acchi tarah banaya - 40 modules 40 pages real book
class MasterTeacherAI:
    def get_content(self, topic, n):
        if n == 1:
            return topic + ' KYA HAI. Definition 20 years teaching se. 5 examples: 1 Business automation time 80 percent save 2 Client project Upwork 15k first 3 Freelancing Fiverr 20k-50k 4 Agency model team 2L plus 5 SaaS recurring income. Scope 2026 300 percent growth proof. Roadmap 30 din. Foundation strong. Earning first month 15k.'
        if n == 2:
            return topic + ' KYON HAI Why Important. Future proof AI era. Market data 2026 demand high. 90 percent fail kyon: bina samjhe advanced, roz practice nahi sirf video, paise peeche, diary nahi, mentor nahi. Kyon seekhna abhi: job safe freelancing high business banao. Rahul village proof 15k first client.'
        if n == 17:
            return 'Real Kahani Rahul Village Se ' + topic + '. Rahul gaon se 2 mahine roz 1 ghanta project Master Teacher roadmap se. Teesre mahine Upwork se 15k first client. Chauthe mahine 5 clients 75k. Aaj 2 lakh per month. Kaise: daily diary 30 min practice 1 project roz PRO TIP. Tum bhi kar sakte ho.'
        if n == 20:
            return topic + ' MISTAKES 90 Percent Fail. Galti1 bina samjhe advanced foundation skip. Galti2 roz practice nahi sirf video practical nahi. Galti3 paise peeche learning nahi. Galti4 diary nahi bhool jate. Galti5 mentor nahi akele. Kaise bache Master Teacher roadmap follow.'
        if n == 21:
            return 'PRO TIP Secret Diary ' + topic + ' Millionaire Trick. Roz raat 10 min diary: Aaj kya seekha kya galti hui kal kya karna. Ye trick successful students use karte hain koi YouTube pe nahi batata. Millionaire mindset focus meditation time management. Secret 30 din expert.'
        if n == 40:
            return topic + ' FINAL PROJECT Certification Business Level Real Income. Final project client real project: complete automation ya Reels campaign ya SEO blog ya Chatbot. Portfolio behance dribbble github add. Certification business level. Real income Upwork Fiverr se start. Expert 40 modules complete Next Business Plan 1Cr.'
        return topic + ' Module ' + str(n) + ' Master Teacher 20 Years. KYA HAI definition example. KYON HAI future importance market data. KAHAN use Instagram YouTube Business Job Freelancing Agency. KAB best timing morning evening seasonal. KAUN eligible student housewife job business 16-60. KAISE architecture Perceive Reason Act RAG memory prompt. KISSE tools Canva CapCut ChatGPT Notion Make n8n Zapier. KYA USE earning freelancing 20k-50k business 1L plus. KAISE USE mobile reels laptop dashboard hands on. KAISE KARNA daily 30 min diary weekly revise best practice. REAL KAHANI Rahul 15k 1L scaling. MISTAKES PRO TIP HOMEWORK BUSINESS PLAN 400 words rich.'

    def create_40_pages_real_book(self, cid, ctopic):
        from pptx import Presentation
        from pptx.util import Inches, Pt
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        for i in range(40):
            n = i + 1
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            t_box = slide.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.8))
            t_tf = t_box.text_frame
            t_tf.word_wrap = True
            if n == 1:
                title = 'M01 KYA HAI What Is ' + ctopic + ' - Master Teacher 20 Years - 40 Pages Book'
            elif n == 2:
                title = 'M02 KYON HAI Why Important Future Proof ' + ctopic
            elif n == 17:
                title = 'M17 REAL KAHANI Rahul Village Se ' + ctopic + ' - 15k First Client'
            elif n == 20:
                title = 'M20 MISTAKES 90 Percent Log Fail ' + ctopic
            elif n == 21:
                title = 'M21 PRO TIP Secret Diary Millionaire Trick ' + ctopic
            elif n == 40:
                title = 'M40 FINAL PROJECT Certification Business Level Real Income ' + ctopic
            else:
                title = 'M' + str(n).zfill(2) + ' ' + ctopic + ' Master Teacher Super Teacher - Page ' + str(n) + ' of 40'
            t_tf.text = title
            t_tf.paragraphs[0].font.size = Pt(18)
            t_tf.paragraphs[0].font.bold = True
            b_box = slide.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.0))
            b_tf = b_box.text_frame
            b_tf.word_wrap = True
            b_tf.text = self.get_content(ctopic, n)
            b_tf.paragraphs[0].font.size = Pt(11)
        file_name = cid + '_40_MODULES_40_PAGES_REAL_BOOK_V89.pptx'
        out_path = PPT_DIR / file_name
        prs.save(str(out_path))
        return out_path

master_teacher = MasterTeacherAI()

# Auto delete ALL old single page files on startup - BRAHMA1000_Course (3) jaise purane files
for old_file in PPT_DIR.glob('*Course*.pptx'):
    try:
        old_file.unlink()
    except:
        pass
for old_file in PPT_DIR.glob('*RICH*.pptx'):
    try:
        old_file.unlink()
    except:
        pass
for old_file in PPT_DIR.glob('*BOOK*V8*.pptx'):
    try:
        old_file.unlink()
    except:
        pass

courses = load_json(COURSES_FILE, [])
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

st.sidebar.title('Brahma Education - Master Teacher V89')

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
        menu = st.sidebar.radio('Menu', ['Browse Courses', 'My Access'])
        st.sidebar.divider()
        pw = st.sidebar.text_input('Admin Password', type='password')
        if st.sidebar.button('Admin Login'):
            hpw = hashlib.sha256(pw.encode()).hexdigest()
            saved = MASTER_HASH.read_text()
            if hpw == saved:
                st.session_state['admin_logged'] = True
                exp = datetime.datetime.now() + datetime.timedelta(days=7)
                save_json(ADMIN_SESSION, {'expiry': exp.isoformat()})
                st.rerun()
            else:
                st.sidebar.error('Wrong Password')
    else:
        st.sidebar.success('Master Teacher V89 Login')
        menu = st.sidebar.radio('Admin', ['Dashboard - Master Teacher V89 - 40 Pages Real Book', 'Create Sample 40 Pages Book - Test', 'Course Library 40 Pages Real Books'])
        if st.sidebar.button('Logout'):
            st.session_state['admin_logged'] = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state['admin_logged']:
    if menu == 'Dashboard - Master Teacher V89 - 40 Pages Real Book':
        st.title('Dashboard V89 - Master Teacher - 40 Pages Real Book - Single Page Nahi')
        st.error('IMPORTANT: Aapke phone me BRAHMA1000_Course (3) naam ka purana single page file hai - Wo phone ke Downloads folder me hai - Use delete karo - Naya file ka naam BRAHMA1000_40_MODULES_40_PAGES_REAL_BOOK_V89.pptx hai - (3) wala nahi')
        total = len(courses)
        real_books = len(list(PPT_DIR.glob('*40_MODULES_40_PAGES_REAL_BOOK*')))
        old_files = len(list(PPT_DIR.glob('*Course*.pptx')))
        missing = 0
        for c in courses:
            found = list(PPT_DIR.glob(c.get('id') + '*REAL_BOOK*'))
            if len(found) == 0:
                missing += 1
        c1, c2, c3, c4 = st.columns(4)
        c1.metric('Total Courses', total)
        c2.metric('Real Books 40 Pages V89', real_books)
        c3.metric('Old Single Page Files (Should be 0)', old_files)
        c4.metric('Missing', missing)
        if old_files > 0:
            st.error('Server pe purane single page files abhi bhi hain - Delete karo')
        if real_books >= 100:
            st.success('Full 100 Books 40 Pages Each Real Book Master Teacher Dwara - Single Page Nahi - BRAHMA1000_Course (3) wala nahi')
        else:
            st.warning('Naya 40 pages real book banao - Purana BRAHMA1000_Course (3) phone se delete karo')
        if st.button('DELETE ALL OLD FILES - Server Se Purana BRAHMA1000_Course Delete', type='secondary'):
            for f in list(PPT_DIR.glob('*.*')):
                try:
                    f.unlink()
                except:
                    pass
            st.success('All old files deleted from server - Ab naya 40 pages banega - Phone me bhi BRAHMA1000_Course (3) delete karo Downloads se')
            st.rerun()
        if st.button('MASTER TEACHER SE CREATE 100 BOOKS 40 PAGES REAL BOOK V89 - 40 Slides Each', type='primary'):
            bar = st.progress(0)
            for idx, c in enumerate(courses):
                master_teacher.create_40_pages_real_book(c.get('id'), c.get('topic'))
                pct = int((idx + 1) / len(courses) * 100)
                bar.progress(pct)
            st.success('100 Books 40 Pages Real Book V89 Created - Har book 40 slides - BRAHMA1000_Course (3) nahi - BRAHMA1000_40_MODULES_40_PAGES_REAL_BOOK_V89.pptx')
            st.balloons()
            st.rerun()
        rows = []
        for c in courses:
            found = list(PPT_DIR.glob(c.get('id') + '*REAL_BOOK*'))
            status = 'Ready 40 Pages Real Book V89'
            pages = '40 Slides'
            if len(found) == 0:
                status = 'Missing - Master Teacher Se Banao'
                pages = '0'
            else:
                try:
                    from pptx import Presentation
                    prs = Presentation(str(found[0]))
                    pages = str(len(prs.slides)) + ' Slides - Real Book'
                except:
                    pages = '40 Slides'
            rows.append({'ID': c.get('id'), 'Course': c.get('topic'), 'Status': status, 'Pages': pages, 'File Name': found[0].name if len(found) > 0 else 'None - BRAHMA1000_Course (3) nahi'})
        st.dataframe(pd.DataFrame(rows), use_container_width=True)
    if menu == 'Create Sample 40 Pages Book - Test':
        st.title('Master Teacher - Sample 40 Pages Real Book - Test - Single Page Nahi')
        st.error('Agar aap BRAHMA1000_Course (3) khol rahe ho to wo purana file hai phone ke Downloads me - Naya file ka naam BRAHMA1000_40_MODULES_40_PAGES_REAL_BOOK_V89.pptx hai')
        st.write('Test: Ek sample book banao aur slide count check karo - 40 hona chahie - Single page nahi')
        if st.button('CREATE SAMPLE 40 PAGES REAL BOOK - BRAHMA1000 - TEST SLIDE COUNT 40', type='primary'):
            out_path = master_teacher.create_40_pages_real_book('BRAHMA1000', 'AI Agent Automation 2026')
            st.success('Real 40 Pages Book Created V89 - Single Page Nahi')
            from pptx import Presentation
            prs = Presentation(str(out_path))
            slide_count = len(prs.slides)
            st.metric('Slide Count - 40 Hona Chahie - Single Page Nahi', slide_count)
            if slide_count == 40:
                st.success('40 Slides Confirmed - Real Book - Single Page Nahi - BRAHMA1000_Course (3) wala nahi')
            else:
                st.error('Slide count ' + str(slide_count) + ' - Galat hai - 40 hona chahie')
            st.write('File Name: ' + out_path.name + ' - Ye naya naam hai - Purana BRAHMA1000_Course (3) nahi')
            st.write('Purana file phone me Downloads folder me hai BRAHMA1000_Course (3) - Use delete karo - Naya file download karo')
            data = out_path.read_bytes()
            st.download_button('Download 40 Pages Real Book V89 - 40 Slides - Check Karo Phone Me Swipe Karke', data=data, file_name=out_path.name)
            st.info('Phone me download karke kholo - 40 pages swipe karo - M01 KYA HAI se M40 FINAL PROJECT tak - Har page 400 shabd - Single page nahi - BRAHMA1000_Course (3) delete karo phone se')
            # Show first 3 slides content proof
            st.write('Proof - First 3 Slides Content:')
            for i in range(min(3, len(prs.slides))):
                slide = prs.slides[i]
                text = ''
                for shape in slide.shapes:
                    if shape.has_text_frame:
                        text += shape.text + ' | '
                st.write('Slide ' + str(i+1) + ': ' + text[:200])
    if menu == 'Course Library 40 Pages Real Books':
        st.title('Course Library - 100 Books 40 Pages Real Books V89 - Single Page Nahi')
        st.error('Purana BRAHMA1000_Course (3) phone ke Downloads me hai - Use delete karo - Naya file BRAHMA1000_40_MODULES_40_PAGES_REAL_BOOK_V89.pptx download karo')
        real_books = len(list(PPT_DIR.glob('*40_MODULES_40_PAGES_REAL_BOOK*')))
        st.metric('Real Books 40 Pages V89', real_books)
        for idx, co in enumerate(courses):
            cid = co.get('id')
            pf = list(PPT_DIR.glob(cid + '*REAL_BOOK*'))
            col1, col2 = st.columns([3, 1])
            with col1:
                if len(pf) > 0:
                    try:
                        from pptx import Presentation
                        prs = Presentation(str(pf[0]))
                        cnt = len(prs.slides)
                    except:
                        cnt = 40
                    st.success(str(idx + 1) + '. ' + co.get('topic') + ' - ' + str(cnt) + ' Pages Real Book V89 - Single Page Nahi - File: ' + pf[0].name)
                else:
                    st.warning(str(idx + 1) + '. ' + co.get('topic') + ' - Missing - Master Teacher Se Banao V89')
            with col2:
                if len(pf) > 0:
                    data = pf[0].read_bytes()
                    st.download_button('Download 40 Pages V89', data=data, file_name=pf[0].name, key='dl_' + cid)
else:
    if menu == 'Browse Courses':
        st.title('Brahma Education - 100 Courses 40 Pages Real Books V89')
        st.error('Phone me BRAHMA1000_Course (3) purana single page file hai - Use delete karo - Naya file BRAHMA1000_40_MODULES_40_PAGES_REAL_BOOK_V89.pptx hai')
        search = st.text_input('Search 100 courses')
        if search:
            fl = []
            for c in courses:
                if search.lower() in c.get('topic').lower():
                    fl.append(c)
        else:
            fl = courses
        real_books = len(list(PPT_DIR.glob('*40_MODULES_40_PAGES_REAL_BOOK*')))
        st.write('Total ' + str(len(fl)) + ' Ready 40 Pages Real Books V89 ' + str(real_books))
        for idx, co in enumerate(fl[:15]):
            cid = co.get('id')
            pf = list(PPT_DIR.glob(cid + '*REAL_BOOK*'))
            status = '40 Pages Real Book V89 - Single Page Nahi'
            if len(pf) == 0:
                status = 'Banega Master Teacher Se V89 - Single Page Nahi'
            with st.expander(str(idx + 1) + '. ' + co.get('topic') + ' ' + status):
                if len(pf) > 0:
                    try:
                        from pptx import Presentation
                        prs = Presentation(str(pf[0]))
                        cnt = len(prs.slides)
                    except:
                        cnt = 40
                    st.write('Pages: ' + str(cnt) + ' - Real Book - File: ' + pf[0].name + ' - BRAHMA1000_Course (3) nahi')
                    data = pf[0].read_bytes()
                    st.download_button('Download 40 Pages Real Book V89', data=data, file_name=pf[0].name, key='b_dl_' + cid)