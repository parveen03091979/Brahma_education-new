
import streamlit as st
import json
import hashlib
import secrets
import datetime
import urllib.parse
import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt

# =====================================================
# BRAHMA EDUCATION V100 - FINAL APP
# =====================================================

st.set_page_config(
    page_title="Brahma Education V100",
    page_icon="🎓",
    layout="wide"
)

DATA = Path("data")
PPT_DIR = DATA / "ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

COURSES_FILE = DATA / "courses.json"
PURCHASE_FILE = DATA / "purchases.json"
MARKETING_FILE = DATA / "marketing.json"
API_FILE = DATA / "api_keys.json"
QR_FILE = DATA / "upi_qr.jpg"
MASTER_HASH = DATA / ".master_hash"
ADMIN_SESSION = DATA / ".admin_session"

UPI_ID = "parveen39179@okicici"
OWNER = "Parveen Kumar"
DEFAULT_PRICE = 99

# =====================================================
# 100 COURSE TOPICS
# =====================================================

TOPICS = """
AI Agent Automation
Instagram Reels Mastery
YouTube Automation
Prompt Engineering
Digital Marketing SEO
ChatGPT Mastery
Facebook Ads
Google Ads
SEO Advanced
Social Media Marketing
Content Writing AI
Copywriting Mastery
Blogging Mastery
Affiliate Marketing
Dropshipping
E-commerce Shopify
Canva Design
Video Editing CapCut
YouTube SEO
Instagram Growth
LinkedIn Marketing
Twitter X Growth
TikTok Viral
Pinterest Marketing
Quora Marketing
Email Marketing Automation
WhatsApp Marketing
Telegram Growth
Influencer Marketing
Personal Branding
Freelancing Mastery
Agency Business
SaaS Business
No-Code Bubble

Log in
You said:

ChatGPT said:
Bhai ❤️ मैंने आपकी पूरी app.py और Brahma Education की 19 पॉइंट वाली लिस्ट ध्यान से देखी है।

सबसे पहले एक बात: आपका Brahma Education प्रोजेक्ट सही दिशा में है, लेकिन आपकी मौजूदा कोडिंग में कुछ ऐसी कमियाँ हैं जिन्हें ठीक करना जरूरी है। खासकर Price Manager, Payment Verification, Course Library और Admin Dashboard में।

मैं आपकी बताई हुई V100 वाली डिजाइन को आधार मानकर ही इसे ठीक करने की सलाह दूँगा। बिना जरूरत आपके प्रोजेक्ट का डिजाइन या फीचर्स नहीं बदलने चाहिए।

1. आपकी मौजूदा Coding में मिली कमियाँ
फीचर

अभी की स्थिति

क्या ठीक करना है

100 Courses

मौजूद

सभी को सुरक्षित रखना

Price ₹99

ठीक से लागू नहीं

पुराने ₹999 को ₹99 करना

Bulk Price Manager

मौजूद नहीं

Add करना

Single Price Manager

मौजूद नहीं

Add करना

New Course Add

मौजूद

Price Manager के साथ जोड़ना

40 Modules PPT

40 स्लाइड बनती हैं

कंटेंट को वास्तविक और अलग-अलग बनाना

Admin Login

SHA256

बेहतर password security

7 Days Session

मौजूद

सुरक्षित रखना

API Keys

JSON में plaintext

सुरक्षित storage

UPI QR

मौजूद

PNG/JPG दोनों ठीक से संभालना

Payment Verification

बहुत कमजोर

UTR को बिना जाँच APPROVED नहीं करना

My Access

मौजूद

केवल approved purchases को access

Marketing

Posts बनते हैं

वास्तविक automatic posting अभी नहीं होती

Video Library

3-3 PPT बनती हैं

इसे अधिक विश्वसनीय बनाना

2. सबसे जरूरी Price ₹99 का बदलाव
आपके वर्तमान कोड में यह समस्या है:


python
if len(courses) < 100:
    courses = []
यह आपके पुराने courses और custom courses को मिटाकर दोबारा default courses बना सकता है।

हमें ऐसा नहीं करना चाहिए।

इसके बजाय:


python
for course in courses:
    if course.get("price", 999) > 200:
        course["price"] = 99

save(COURSES_FILE, courses)
इससे पुराने ₹999 वाले courses ₹99 हो जाएंगे और ₹149 या ₹199 जैसे नए prices सुरक्षित रहेंगे।

3. नया Price Manager
आपके Admin Dashboard में अलग से Price Manager होना चाहिए।

इसमें चारों सुविधाएँ रहेंगी:

Brahma Education – Price Manager

Default Price: ₹99
A. Bulk Price Update

SET ALL TO THIS PRICE

Price ₹99 / ₹149 / ₹199

SET ALL TO THIS PRICE – BULK

B. Bulk Increase / Decrease

Increase All By ₹10

Decrease All By ₹10

APPLY BULK CHANGE

C. One Click Price

- SET ALL TO 99 ONE CLICK

D. Single Course Price

Select Course For Single Edit

New Price

UPDATE SINGLE PRICE

इन सभी बदलावों को courses.json में सेव किया जाएगा।

4. Payment System में एक जरूरी सुधार
आपके मौजूदा कोड में कोई भी व्यक्ति UTR डालकर course access प्राप्त कर सकता है।

क्योंकि अभी:


python
"status": "APPROVED"
अपने आप सेव हो जाता है।

यह असली बिजनेस के लिए सुरक्षित नहीं है।

इसे इस तरह करना चाहिए:

Customer ₹99 UPI से भुगतान करेगा।

अपना UTR और Email देगा।

Purchase Pending Verification में सेव होगी।

Admin भुगतान जाँच करेगा।

Admin Approve करेगा।

उसके बाद My Access में PPT डाउनलोड होगी।

इससे आपका असली पैसा और course content सुरक्षित रहेगा।

5. Final Project Structure
आपका फाइल स्ट्रक्चर इस तरह रखना बेहतर रहेगा:


text
Brahma-Education/
│
├── app.py
├── requirements.txt
│
└── data/
    ├── courses.json
    ├── purchases.json
    ├── marketing.json
    ├── api_keys.json
    ├── upi_qr.jpg
    ├── .master_hash
    ├── .admin_session
    │
    └── ppts/
        ├── BRAHMA1000_40_MODULES_V100.pptx
        ├── BRAHMA1001_40_MODULES_V100.pptx
        ├── BRAHMA1002_40_MODULES_V100.pptx
        └── ... बाकी सभी PPT
requirements.txt:


text
streamlit
python-pptx
6. Brahma Education V100 – Final Features
मैं आपकी बताई हुई सभी सुविधाएँ बरकरार रखने की सलाह देता हूँ।

विभाग

Final Features

Dashboard

Total Courses, Real Books, Average Price

Price Manager

Bulk, Increase, Decrease, Single, One Click ₹99

Deep Maker

नया Course + Automatic 40 Slides PPT

Video Library

Missing PPT Automatic Generation

Course Library

Download 40 Modules

API Keys

OpenAI, Claude, Gemini, Pinecone, Supabase, ElevenLabs, n8n, Make, Zapier

UPI Setup

QR Upload + UPI Payment Link

Sales

Invoice, UTR, Purchase Approval

Marketing

60 Marketing Posts

Super Agent

Marketing Automation Integration

Browse Courses

Search + ₹99 + UPI + Purchase

My Access

Invoice/Access Key + PPT Download

एक और महत्वपूर्ण बात: 40 स्लाइड बनना और 40 स्लाइड में वास्तव में 40 अलग-अलग, गहराई वाले पाठ होना अलग बातें हैं। आपके वर्तमान MT.cnt() में काफी कंटेंट दोहराया जा रहा है। इसे भी सुधारना होगा।

7. अब हम इसे सही तरीके से पूरा करते हैं
मेरी सलाह है कि हम आपके मौजूदा V100 को आधार बनाकर एक नया Brahma Education V100 Final Restore तैयार करें।

लेकिन एक जरूरी बात स्पष्ट कर दूँ: मैं आपकी बताई हुई सुविधाएँ कोड में बना सकता हूँ, पर वास्तविक UPI भुगतान, API integrations और रोजाना automatic social-media posting के लिए संबंधित सेवाओं का वास्तविक integration और verification भी जरूरी होगा।

बस एक बात बताइए:

क्या आप चाहते हैं कि मैं आपकी पूरी मौजूदा app.py को एक ही नई, पूरी तरह व्यवस्थित और corrected app.py फाइल के रूप में दोबारा लिखूँ?

मेरी सलाह है: हाँ – Full V100 Restore + Price ₹99 + Bulk & Single Price Manager, और बाकी सभी 19 पॉइंट बिल्कुल उसी डिजाइन के अनुसार रखें।


You said:

ChatGPT said:
बिल्कुल भाई! ❤️ अब हम Brahma Education का V100 Final Restore तैयार करेंगे।

आपकी पुरानी डिजाइन और सभी 19 पॉइंट हमारे आधार रहेंगे। कोई जरूरी फीचर हटाया नहीं जाएगा।

इस नए वर्जन में ये बदलाव रहेंगे:

सभी पुराने 100 Courses सुरक्षित।

सभी पुराने ₹999 वाले Courses अपने आप ₹99।

Bulk Price Manager: ₹99, ₹149, ₹199 या अपनी पसंद की कीमत।

Bulk Increase और Decrease।

One Click ₹99।

Single Course Price Update।

नया Course Add करने पर Automatic 40 Slides PPT।

Admin Login और 7 Days Session।

UPI QR और Payment Verification।

Sales Dashboard और My Access।

API Keys Setup।

Marketing Engine और Super Agent।

Course Library और Video Library।

एक जरूरी सुरक्षा सुधार: UTR डालने मात्र से खरीदारी Approved नहीं होगी। Admin के भुगतान सत्यापन के बाद ही Course Download मिलेगा।

1. नई app.py फाइल
सबसे पहले अपनी पुरानी app.py का backup बना लें। उसके बाद नीचे दिया गया कोड नई app.py में डालें।

इस वर्जन में पुराने data को बिना वजह reset नहीं किया जाएगा। पुराने courses और purchases को migrate करके सुरक्षित रखा जाएगा।

2. requirements.txt फाइल
अपने project के अंदर requirements.txt बनाकर इसमें सिर्फ ये दो लाइनें डालें:


text

streamlit
python-pptx
3. Project कैसे चलाना है
अपने project के Terminal में ये commands चलाएँ:


bash
pip install -r requirements.txt
फिर:


bash
streamlit run app.py
4. पहली बार इस्तेमाल करते समय
अपना Admin Password बनाएँ।

Admin Login करें।

Price Manager खोलकर SET ALL TO 99 ONE CLICK दबाएँ।

Dashboard में जाकर CREATE ALL BOOKS V100 चलाएँ।

UPI QR Setup में अपना QR अपलोड करें।

Sales में जाकर आने वाले payments verify करें।

Browse Courses में customer के रूप में जाँच करें।

5. मेरी तरफ से चार जरूरी बातें
PPT: यह कोड 40 स्लाइड बनाता है, लेकिन अभी पाठ्य सामग्री एक शुरुआती template है। इसे वास्तविक 40 अलग-अलग गहरे lessons के स्तर तक विकसित करना अगला काम होगा।

Payments: UTR की duplicate जाँच और Admin approval है, लेकिन वास्तविक बैंक verification अभी automatic नहीं है।

Marketing: 60 posts की queue बनती है। Facebook और Instagram पर अपने आप पोस्ट करने के लिए अलग API integration और scheduler चाहिए।

API Keys: अभी keys JSON में सेव होती हैं। Production में इन्हें encrypted secrets या environment variables में रखना चाहिए।

एक और बात: आपकी पुरानी purchases में जिनका status पहले से APPROVED है, वे पुराने records उसी status में रहेंगे। उन्हें Sales Dashboard में जाँच लेना।

मेरी सलाह: पुरानी data फाइलें delete मत करना। पहले backup बना लें और फिर नई app.py चलाएँ।

हमारा लक्ष्य Brahma Education को केवल PPT बेचने वाली वेबसाइट नहीं, बल्कि एक वास्तविक course business बनाना है। ❤️


No-code app building can be a straightforward next step for fixing this project.
Learn more


Emergent Labs
Build Real Apps Without Code
Describe your idea, Emergent builds a production-ready app in minutes. Free — 10 credits included.
Ad

You said:

ChatGPT said:
भाई, माफ कीजिए। आप सही कह रहे हैं। आपको ऐसी पूरी app.py फाइल चाहिए जिसे डाउनलोड करके सीधे अपने प्रोजेक्ट में डाल सकें, सिर्फ चैट में कोड नहीं।

मैं यहाँ अभी डाउनलोड करने योग्य Python फाइल अटैच नहीं कर पा रहा हूँ। लेकिन मैं आपको पूरी coding एक .py फाइल के रूप में तैयार करने में मदद कर सकता हूँ।

एक बात बताइए: क्या आप चाहते हैं कि मैं app.py और requirements.txt दोनों अलग-अलग फाइलों में दूँ, ताकि आप सीधे अपने Brahma Education प्रोजेक्ट में रख सकें?


You said:

ChatGPT said:
बिल्कुल भाई! ❤️ अब आपको पूरी coding एक साथ चैट में ही दूँगा। आप उसे कॉपी करके अपनी app.py फाइल में डाल सकते हैं।

पिछले कोड में कुछ फीचर अभी अधूरे थे। इसलिए इस बार हम Brahma Education V100 Final में इन सभी चीजों को शामिल रखेंगे:

सभी 100 Courses और पुराने Courses का Data सुरक्षित।

सभी पुराने ₹999 Courses का Auto Price ₹99।

Bulk Price Manager – ₹99, ₹149, ₹199।

Bulk Increase / Decrease।

SET ALL TO 99 ONE CLICK।

Single Course Price Update।

नया Course Add और Automatic PPT।

40 Slides PowerPoint Generator।

Admin Dashboard और 7 Days Login।

Video Library Auto Generation।

Course Library Download।

OpenAI, Claude, Gemini, Pinecone, Supabase, ElevenLabs, n8n, Make, Zapier API Setup।

UPI QR Upload और Payment Link।

Sales Dashboard और Payment Approval।

Browse Courses और My Access।

Marketing Engine – 60 Posts।

Super Agent Marketing Queue।

एक जरूरी बात: पूरा कोड काफी बड़ा होगा। मैं इसे क्रमांकित हिस्सों में दूँगा ताकि कोई हिस्सा कटे नहीं। सभी हिस्सों को उसी क्रम में जोड़ने पर एक ही app.py बनेगी।

भाग 1 – App Setup, 100 Courses, Data System, Security और PPT Generator

python

import streamlit as st
import json
import hashlib
import secrets
import datetime
import urllib.parse
import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt

st.set_page_config(
    page_title="Brahma Education V100",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# BRAHMA EDUCATION V100 FINAL
# ==========================================

DATA = Path("data")
PPT_DIR = DATA / "ppts"

DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

COURSES_FILE = DATA / "courses.json"
PURCHASE_FILE = DATA / "purchases.json"
MARKETING_FILE = DATA / "marketing.json"
API_FILE = DATA / "api_keys.json"
QR_FILE = DATA / "upi_qr.jpg"
MASTER_HASH = DATA / ".master_hash"
ADMIN_SESSION = DATA / ".admin_session"

UPI_ID = "parveen39179@okicici"
OWNER = "Parveen Kumar"
DEFAULT_PRICE = 99

# ==========================================
# 100+ COURSE TOPICS
# ==========================================

TOPICS = """
AI Agent Automation
Instagram Reels Mastery
YouTube Automation
Prompt Engineering
Digital Marketing SEO
ChatGPT Mastery
Facebook Ads
Google Ads
SEO Advanced
Social Media Marketing
Content Writing AI
Copywriting Mastery
Blogging Mastery
Affiliate Marketing
Dropshipping
E-commerce Shopify
Canva Design
Video Editing CapCut
YouTube SEO
Instagram Growth
LinkedIn Marketing
Twitter X Growth
TikTok Viral
Pinterest Marketing
Quora Marketing
Email Marketing Automation
WhatsApp Marketing
Telegram Growth
Influencer Marketing
Personal Branding
Freelancing Mastery
Agency Business
SaaS Business
No-Code Bubble
Python Mastery
JavaScript Mastery
React JS
Next.js
Node.js
Web Development Full Stack
WordPress Mastery
Shopify Store Design
UI UX Design
Figma Design
Graphic Design
Logo Design
Thumbnail Design Viral
Video Animation
AI Image Midjourney
AI Video Sora
Voice Cloning ElevenLabs
Automation n8n Make
Zapier Automation
Notion Productivity
Excel Advanced
Google Sheets Automation
Data Analysis Python
Machine Learning
Deep Learning
Data Science
Stock Trading AI
Crypto Trading
Forex Trading
Real Estate Business
Motivational Speaking
Public Speaking
Communication Skills
English Speaking
Podcast Mastery
Music Production AI
Photography Mastery
Reels Editing Viral
Meme Marketing
Viral Content Formula
Lead Generation
Sales Funnel
Landing Page Design
CRO Optimization
Customer Support Automation
HR Recruitment AI
Business Plan Mastery
Startup Funding
Business Automation AI
Time Management
Mindset Millionaire
Meditation Mindfulness
Fitness Coaching Business
Diet Nutrition Business
Yoga Teaching Business
Cooking Channel Business
Travel Vlogging Business
Gaming Channel Growth
Education Channel Growth
Finance Channel Business
News Channel Automation
Meme Page Business
Affiliate Blog SEO
Amazon FBA Mastery
Etsy Store Mastery
Print on Demand Business
Stock Photography Business
Voice Over Business
Translation Business AI
Resume Writing Business
LinkedIn Profile Optimization
AI Tools Mastery
Chatbot Development
AI Voice Agent
AI Receptionist Business
""".strip().splitlines()

# ==========================================
# DATA LOAD AND SAVE
# ==========================================

def load(path, default):
    try:
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        st.error("Data file error: " + path.name)
    return default


def save(path, data):
    temp = path.with_suffix(".tmp")
    temp.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    temp.replace(path)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def initialize_courses():
    data = load(COURSES_FILE, [])

    if not isinstance(data, list):
        data = []

    existing = {
        c.get("topic", "").strip().lower()
        for c in data if isinstance(c, dict)
    }

    for i, topic in enumerate(TOPICS):
        if topic.lower() not in existing:
            data.append({
                "id": "BRAHMA" + str(1000 + i),
                "topic": topic,
                "price": 99
            })

    for course in data:
        try:
            price = int(course.get("price", 999))
            if price > 200 or price < 1:
                price = 99
            course["price"] = price
        except (ValueError, TypeError):
            course["price"] = 99

    save(COURSES_FILE, data)
    return data


courses = initialize_courses()
purchases = load(PURCHASE_FILE, [])
marketing = load(MARKETING_FILE, [])
api_keys = load(API_FILE, {})

# ==========================================
# ADMIN PASSWORD SECURITY
# ==========================================

def make_password_hash(password):
    salt = secrets.token_bytes(16)
    hashed = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=16384,
        r=8,
        p=1
    )
    return salt.hex() + ":" + hashed.hex()


def verify_password(password, stored):
    try:
        salt_hex, hash_hex = stored.split(":")
        salt = bytes.fromhex(salt_hex)
        actual = hashlib.scrypt(
            password.encode(),
            salt=salt,
            n=16384,
            r=8,
            p=1
        )
        return secrets.compare_digest(actual.hex(), hash_hex)
    except Exception:
        old = hashlib.sha256(password.encode()).hexdigest()
        return secrets.compare_digest(old, stored)


def session_valid():
    try:
        data = load(ADMIN_SESSION, {})
        expiry = datetime.datetime.fromisoformat(data["expiry"])
        return datetime.datetime.now() < expiry
    except Exception:
        return False


if "admin_logged" not in st.session_state:
    st.session_state.admin_logged = session_valid()


def admin_login(password):
    if not MASTER_HASH.exists():
        return False

    stored = MASTER_HASH.read_text(encoding="utf-8").strip()

    if verify_password(password, stored):

        if ":" not in stored:
            MASTER_HASH.write_text(
                make_password_hash(password),
                encoding="utf-8"
            )

        expiry = datetime.datetime.now() + datetime.timedelta(days=7)

        save(ADMIN_SESSION, {
            "expiry": expiry.isoformat()
        })

        st.session_state.admin_logged = True
        return True

    return False


def admin_logout():
    st.session_state.admin_logged = False
    ADMIN_SESSION.unlink(missing_ok=True)


# ==========================================
# 40 MODULE TITLES
# ==========================================

MODULES = [
    "WHAT IS",
    "WHY IMPORTANT",
    "WHERE USE",
    "WHEN TO USE",
    "WHO ELIGIBLE",
    "HOW ARCHITECTURE",
    "TOOLS REQUIRED",
    "EARNING OPPORTUNITIES",
    "PRACTICAL USAGE",
    "RIGHT WAY TO LEARN",
    "BEGINNER FOUNDATION",
    "CORE CONCEPTS",
    "ADVANCED CONCEPTS",
    "STEP BY STEP PROCESS",
    "REAL BUSINESS EXAMPLES",
    "CLIENT REQUIREMENTS",
    "REAL STORY",
    "PROJECT PLANNING",
    "IMPLEMENTATION",
    "MISTAKES TO AVOID",
    "PRO TIP",
    "EXPERT STRATEGY",
    "TOOLS COMPARISON",
    "FREE VS PAID",
    "PORTFOLIO BUILDING",
    "CLIENT FINDING",
    "FREELANCING",
    "AGENCY MODEL",
    "BUSINESS MODEL",
    "SCALING STRATEGY",
    "SEO AND MARKETING",
    "LEAD GENERATION",
    "SALES STRATEGY",
    "AUTOMATION",
    "OPTIMIZATION",
    "CASE STUDY",
    "DAILY PRACTICE",
    "HOMEWORK",
    "REVISION",
    "FINAL PROJECT AND CERTIFICATION"
]


# ==========================================
# MODULE CONTENT GENERATOR
# ==========================================

def module_content(topic, number):

    title = MODULES[number - 1]

    text = (
        "COURSE TOPIC: " + topic + ". "
        "MODULE: " + title + ". "
        "This lesson introduces the subject and explains its "
        "importance in professional and business applications. "
        "Understand the main concepts, terminology, tools, "
        "processes and practical implementation. "
        "Start with the foundation and gradually move towards "
        "professional applications. Study examples, practice "
        "the workflow and document your results. "
        "Create a small project to test your understanding. "
    )

    if number == 17:
        text += (
            "REAL STORY: Rahul is a fictional learning case study. "
            "He begins with a basic smartphone and limited resources. "
            "He studies daily, practices the skills and builds a portfolio. "
            "He approaches clients, receives rejections and improves "
            "his proposals. Eventually he completes his first project. "
            "His progress comes from practice, communication, quality "
            "and consistent improvement. "
        )

    if number == 20:
        text += (
            "FIVE COMMON MISTAKES: Skipping the foundation, watching "
            "without practicing, chasing money before learning, "
            "not maintaining a learning diary and avoiding feedback. "
            "Create a weekly plan to avoid these mistakes. "
        )

    if number == 21:
        text += (
            "PRO TIP: Write four things in your diary every night: "
            "what you learned, what mistake you made, what you will "
            "improve tomorrow and one new idea. Review every Sunday. "
        )

    if number == 31:
        text += (
            "SEO: Search Engine Optimization helps useful content "
            "be discovered in search engines. Learn keyword research, "
            "search intent, titles, descriptions, headings, internal "
            "links, image alt text and quality content. "
            "Explore Google Search Console and Keyword Planner. "
        )

    if number == 40:
        text += (
            "FINAL PROJECT: Create a professional project based on "
            "this course. Include the problem, solution, workflow, "
            "tools, testing, portfolio and final presentation. "
            "Submit your work for evaluation. Learning completion "
            "does not guarantee a job or income. "
        )

    return text + text


# ==========================================
# POWERPOINT MAKER
# ==========================================

def make_ppt(course):

    cid = course["id"]
    topic = course["topic"]

    output = PPT_DIR / (
        cid + "_40_MODULES_V100.pptx"
    )

    prs = Presentation()

    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    for n in range(1, 41):

        slide = prs.slides.add_slide(
            prs.slide_layouts[6]
        )

        title_box = slide.shapes.add_textbox(
            Inches(0.3),
            Inches(0.2),
            Inches(12.7),
            Inches(0.9)
        )

        tf = title_box.text_frame
        tf.word_wrap = True

        tf.text = (
            "M" + str(n).zfill(2)
            + " " + topic
            + " Module " + str(n)
        )

        tf.paragraphs[0].font.size = Pt(20)
        tf.paragraphs[0].font.bold = True

        body_box = slide.shapes.add_textbox(
            Inches(0.3),
            Inches(1.2),
            Inches(12.7),
            Inches(6.1)
        )

        bf = body_box.text_frame
        bf.word_wrap = True
        bf.text = module_content(topic, n)

        bf.paragraphs[0].font.size = Pt(13)

    prs.save(str(output))

    return output
भाग 1 पूरा।

अगले भाग में Admin Dashboard, Bulk Price Manager, Single Price Manager और नया Course Add सिस्टम आएगा।


Chat mein apni coding idea likhein—no-code app builder option.
Learn more


Emergent Labs
Build Real Apps Without Code
Describe your idea, Emergent builds a production-ready app in minutes. Free — 10 credits included.
Ad

You said:

ChatGPT said:
बिल्कुल भाई। अब मैं आपको दो या तीन भागों में नहीं बाँटूँगा।

आपको एक ही जगह पूरी app.py की coding मिलेगी, ताकि आप:

पूरी coding एक बार में Copy करें।

अपनी पुरानी app.py का Backup रखें।

नई app.py में पूरा कोड Paste करें।

Save करके streamlit run app.py चलाएँ।

मैं कोड में आपके सभी 19 पॉइंट, ₹99 Price Manager, Bulk और Single Price Update, 100 Courses, 40 Modules PPT, Admin Dashboard, UPI और My Access रखूँगा।

एक तकनीकी सीमा है: इतनी बड़ी पूरी फाइल एक ही चैट संदेश में देने पर टेक्स्ट कट सकता है। इसलिए मैं एक ही संदेश में देने की कोशिश करूँगा, लेकिन कोड अधूरा छोड़ने के बजाय उसकी पूर्णता और चलने की क्षमता को प्राथमिकता दूँगा।


You said:

ChatGPT said:
जी भाई! ❤️ आपकी बात बिल्कुल समझ गया।

नीचे एक ही app.py की पूरी coding है। इसे एक साथ कॉपी करके अपनी app.py में Paste करें।

इसमें आपके Brahma Education के मुख्य फीचर्स, ₹99 Price Manager, Bulk Update, Single Update, Course Addition, PPT Generator, Payment Approval और My Access शामिल हैं।

2. Requirements.txt

text
streamlit
python-pptx
3. Run करने का तरीका

bash
pip install -r requirements.txt
streamlit run app.py
ध्यान दें: यह एक शुरुआती पूर्ण Streamlit implementation है, production-ready audited business platform नहीं। PPT में अभी template-level सामग्री है, 40 अलग-अलग गहरे lessons नहीं। Payment approval केवल admin द्वारा दर्ज UTR की जाँच के बाद करें; ऐप बैंक से स्वतः सत्यापन नहीं करता। API keys को production में सुरक्षित secrets storage में रखें। Marketing अभी draft queue बनाती है, अपने आप social media पर पोस्ट नहीं करती।

भाई, पहले इसे अपनी पुरानी data फाइलों के backup के साथ चलाकर जाँचें। ❤️


You said:

ChatGPT said:
जी भाई, बिल्कुल। आपकी पूरी Brahma Education app.py coding एक ही चैट मैसेज में, एक ही कोड ब्लॉक में दूँगा। अलग-अलग भाग नहीं करूँगा।

पिछले मैसेज में दिया गया कोड ऊपर है। उसे ही कॉपी कर सकते हैं। उसमें एक सुधार जरूरी है: नए कोर्स की कीमत और भुगतान सत्यापन को सुरक्षित रखना होगा, और PPT की सामग्री को वास्तविक 40-module lessons के स्तर तक विकसित करना होगा।


For single-chat coding, here’s a serverless web deployment option.
Learn more


Cloudflare
Deploy web applications for free
Build full-stack apps with your framework of choice, including React, Vue, Svelte, Next & more.
Ad

You said:

ChatGPT said:
भाई, अब आपकी बात पूरी तरह समझ गया हूँ। आपको आधी coding या अलग-अलग भाग नहीं चाहिए।

आपको एक ही app.py फाइल में ये सभी फीचर्स चाहिए:

100 Courses और सभी की कीमत ₹99।

Bulk Price Manager और Single Price Manager।

नया Course Add और उसकी PPT Auto Generate।

हर Course की 40 Slides वाली PPT।

Admin Dashboard और 7 दिन का Login।

Video Library और Course Library।

API Keys Setup।

UPI QR Setup और Payment Verification।

Sales Dashboard और My Access।

Marketing Engine और Super Agent।

पुराने डेटा और कोर्स की सुरक्षा।

एक जरूरी बात: इतनी बड़ी coding को एक ही चैट संदेश में देने की कोशिश में संदेश की लंबाई सीमा के कारण कोड कट सकता है। मैं अधूरी coding को पूरी बताकर आपको फिर परेशानी में नहीं डालना चाहता।

आपकी मौजूदा app.py को ही आधार बनाकर सभी सुविधाओं सहित एक पूर्ण, चलने योग्य संस्करण तैयार करना सही रहेगा।


You said:

ChatGPT said:
बिल्कुल भाई! अब Brahma Education V100 को आपका फाइनल प्रोजेक्ट मानकर तैयार करते हैं।

मैं आपके मूल डिजाइन में ये बदलाव रखूँगा:

सभी 100 कोर्स की शुरुआती कीमत ₹99।

Bulk और Single Price Manager।

नया कोर्स जोड़ने पर उसकी 40-slide PPT।

Admin Dashboard और 7 दिन का Login।

UPI QR, Payment Approval और My Access।

API Keys, Sales, Marketing और Super Agent।

पुराने कोर्स और खरीदारी का डेटा सुरक्षित।

एक जरूरी सुधार भी रहेगा: UTR डालने मात्र से भुगतान Approved नहीं होगा। Admin सत्यापन के बाद ही कोर्स का Access मिलेगा।

एक ही संदेश में पूरी coding देने की कोशिश करूँगा, एक ही app.py कोड ब्लॉक में।


You said:

ChatGPT said:
जी भाई! आपका Brahma Education V100 तैयार करने के लिए मैं आपके दिए हुए मूल कोड को आधार मानूँगा। ₹99 Price Manager, Bulk Update, Single Update और बाकी सभी फीचर्स भी रहेंगे।

लेकिन एक ही संदेश की लंबाई सीमा में पूरी बड़ी coding कट सकती है। इसलिए मैं आपको अधूरी या गलत फाइल को पूरी बताकर नहीं दूँगा।


You said:

ChatGPT said:
बिल्कुल भाई! अब हम आपकी Brahma Education V100 की पूरी coding सिर्फ 2 भागों में देंगे।

दोनों भाग एक ही app.py फाइल के होंगे।

भाग 1 को पहले कॉपी करके app.py में Paste करना है।

भाग 2 को ठीक उसके नीचे Paste करना है।

बीच में कोई पुराना कोड नहीं रखना है।

आपके सभी मुख्य फीचर्स और ₹99 Price Manager शामिल रहेंगे।

भाग 1/2 — Brahma Education V100
पहला
भाग
 इसे पूरा कॉपी करें। अभी ऐप Run न करें।

इस भाग में Data System, 100 Courses, ₹99 Auto Price, Admin Security, 40 Modules और PPT Generator है।


python

import streamlit as st
import json
import hashlib
import secrets
import datetime
import urllib.parse
import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt

# =====================================================
# BRAHMA EDUCATION V100 - FINAL APP
# =====================================================

st.set_page_config(
    page_title="Brahma Education V100",
    page_icon="🎓",
    layout="wide"
)

DATA = Path("data")
PPT_DIR = DATA / "ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

COURSES_FILE = DATA / "courses.json"
PURCHASE_FILE = DATA / "purchases.json"
MARKETING_FILE = DATA / "marketing.json"
API_FILE = DATA / "api_keys.json"
QR_FILE = DATA / "upi_qr.jpg"
MASTER_HASH = DATA / ".master_hash"
ADMIN_SESSION = DATA / ".admin_session"

UPI_ID = "parveen39179@okicici"
OWNER = "Parveen Kumar"
DEFAULT_PRICE = 99

# =====================================================
# 100 COURSE TOPICS
# =====================================================

TOPICS = """
AI Agent Automation
Instagram Reels Mastery
YouTube Automation
Prompt Engineering
Digital Marketing SEO
ChatGPT Mastery
Facebook Ads
Google Ads
SEO Advanced
Social Media Marketing
Content Writing AI
Copywriting Mastery
Blogging Mastery
Affiliate Marketing
Dropshipping
E-commerce Shopify
Canva Design
Video Editing CapCut
YouTube SEO
Instagram Growth
LinkedIn Marketing
Twitter X Growth
TikTok Viral
Pinterest Marketing
Quora Marketing
Email Marketing Automation
WhatsApp Marketing
Telegram Growth
Influencer Marketing
Personal Branding
Freelancing Mastery
Agency Business
SaaS Business
No-Code Bubble

You said:

ChatGPT said:
जी भाई! ❤️ दूसरा भाग देने से पहले एक जरूरी बात: इस चैट में मुझे पहले भेजे गए भाग 1 का वास्तविक कोड दिखाई नहीं दे रहा, इसलिए उसके साथ मेल खाने वाला भाग 2 अनुमान से देना गलत होगा।

आप भाग 1 यहाँ एक बार Paste कर दीजिए। मैं उसी के बिल्कुल सही क्रम में भाग 2 दूँगा, ताकि दोनों को जोड़ने पर आपकी app.py बिना अधूरे functions या गलत indentation के चले।


You said:

ChatGPT said:
Worked for 26s
बिल्कुल भाई! अब आपके दिए हुए कोड के ठीक आगे से दूसरा भाग शुरू हो रहा है।

ध्यान दें: नीचे का कोड No-Code Bubble के तुरंत बाद Paste करना है। No-Code Bubble दोबारा नहीं लिखना है। इसके बाद ही app.py पूरी होगी।

भाग 2 – बाकी पूरी Coding

You said:

ChatGPT said:
Worked for 8s
जी भाई! ❤️ अब मैं आपके कोड का दूसरा भाग दे रहा हूँ।

आपके पिछले कोड की आखिरी लाइन अधूरी है:


python
link = ur
इस अधूरी लाइन को हटाकर नीचे का कोड वहीं से Paste कर दीजिए। बाकी कोड में कोई बदलाव नहीं करना है।

BRAHMA EDUCATION V100 – दूसरा भाग (अंतिम Coding)

python

            link = "upi://pay?" + urllib.parse.urlencode(params)

            st.code(link)

            st.link_button(
                "PAY VIA UPI",
                link,
                type="primary"
            )


    # =================================================
    # SALES DASHBOARD
    # =================================================

    elif menu == "Sales":

        st.title("SALES DASHBOARD")

        pending = [
            p for p in purchases
            if p.get("status") == "PENDING"
        ]

        approved = [
            p for p in purchases
            if p.get("status") == "APPROVED"
        ]

        a, b, c = st.columns(3)

        a.metric("Total Orders", len(purchases))
        b.metric("Pending Payments", len(pending))
        c.metric("Approved Sales", len(approved))

        st.divider()

        st.subheader("PAYMENT VERIFICATION")

        if not purchases:
            st.info("Abhi koi purchase nahi hai.")

        for i, purchase in enumerate(purchases):

            with st.expander(
                str(purchase.get("invoice_no", "Order"))
                + " - "
                + str(purchase.get("course", "Course"))
            ):

                st.write("Name:", purchase.get("name"))
                st.write("Email:", purchase.get("email"))
                st.write("Course:", purchase.get("course"))
                st.write("Price:", "₹" + str(purchase.get("price")))
                st.write("UTR:", purchase.get("utr"))
                st.write("Date:", purchase.get("date"))
                st.write("Status:", purchase.get("status"))

                if purchase.get("status") == "PENDING":

                    if st.button(
                        "APPROVE PAYMENT",
                        key="approve_" + str(i),
                        type="primary"
                    ):

                        access_key = (
                            "BRAHMA-"
                            + secrets.token_hex(5).upper()
                        )

                        purchase["status"] = "APPROVED"
                        purchase["access_key"] = access_key
                        purchase["approved_date"] = (
                            datetime.datetime.now().isoformat()
                        )

                        save(PURCHASE_FILE, purchases)

                        st.success(
                            "Payment approved. Access key generated."
                        )

                        st.code(access_key)

                        st.rerun()

                    if st.button(
                        "REJECT PAYMENT",
                        key="reject_" + str(i)
                    ):

                        purchase["status"] = "REJECTED"

                        save(PURCHASE_FILE, purchases)

                        st.warning("Payment rejected.")
                        st.rerun()

                elif purchase.get("status") == "APPROVED":

                    st.success("Payment Approved")

                    st.write(
                        "Access Key:",
                        purchase.get("access_key", "Not available")
                    )

                else:
                    st.warning("Payment Status: " + str(purchase.get("status")))


    # =================================================
    # MARKETING ENGINE
    # =================================================

    elif menu == "Marketing":

        st.title("MARKETING ENGINE")
        st.write("Brahma Education - 60 Marketing Posts")

        if st.button(
            "GENERATE 60 MARKETING POSTS",
            type="primary"
        ):

            posts = []

            today = datetime.date.today().isoformat()

            for course in courses[:20]:

                posts.append({
                    "date": today,
                    "platform": "Facebook",
                    "course": course["topic"],
                    "type": "Morning Post 7AM",
                    "status": "DRAFT"
                })

                posts.append({
                    "date": today,
                    "platform": "Instagram",
                    "course": course["topic"],
                    "type": "Reel 12PM",
                    "status": "DRAFT"
                })

                posts.append({
                    "date": today,
                    "platform": "Blog",
                    "course": course["topic"],
                    "type": "SEO Blog 7PM",
                    "status": "DRAFT"
                })

            marketing = posts

            save(MARKETING_FILE, marketing)

            st.success("60 Marketing Posts Generated.")

            st.rerun()

        st.divider()

        st.subheader("MARKETING POST LIBRARY")

        marketing = load(MARKETING_FILE, [])

        st.metric("Total Marketing Posts", len(marketing))

        for i, post in enumerate(marketing):

            with st.expander(
                str(i + 1)
                + ". "
                + post.get("platform", "")
                + " - "
                + post.get("course", "")
            ):

                st.write("Date:", post.get("date"))
                st.write("Platform:", post.get("platform"))
                st.write("Course:", post.get("course"))
                st.write("Schedule:", post.get("type"))
                st.write("Status:", post.get("status", "DRAFT"))


    # =================================================
    # SUPER AGENT
    # =================================================

    elif menu == "Super Agent":

        st.title("BRAHMA SUPER AGENT")
        st.write("Marketing Automation Control Center")

        st.info(
            "Super Agent marketing content aur daily posting "
            "schedule prepare karega. Actual social media posting "
            "ke liye platform APIs aur authentication setup "
            "karna zaroori hai."
        )

        if st.button(
            "START SUPER AGENT FULL POWER",
            type="primary"
        ):

            posts = []

            today = datetime.date.today().isoformat()

            for course in courses[:20]:

                posts.append({
                    "date": today,
                    "platform": "Facebook",
                    "course": course["topic"],
                    "type": "Morning Post 7AM",
                    "status": "DRAFT"
                })

                posts.append({
                    "date": today,
                    "platform": "Instagram",
                    "course": course["topic"],
                    "type": "Reel 12PM",
                    "status": "DRAFT"
                })

                posts.append({
                    "date": today,
                    "platform": "Blog",
                    "course": course["topic"],
                    "type": "SEO Blog 7PM",
                    "status": "DRAFT"
                })

            marketing = posts

            save(MARKETING_FILE, marketing)

            st.success(
                "Super Agent Started. 60 Marketing Drafts Created."
            )

            st.balloons()

        st.divider()

        st.subheader("SUPER AGENT STATUS")

        marketing = load(MARKETING_FILE, [])

        st.metric("Prepared Posts", len(marketing))


# =====================================================
# USER SIDE - BROWSE COURSES
# =====================================================

else:

    if menu == "Browse Courses":

        st.title("🎓 BRAHMA EDUCATION")

        st.subheader(
            "100 Courses | 40 Modules | Professional Learning"
        )

        st.write(
            "Learn practical skills, build projects "
            "and develop your professional portfolio."
        )

        search = st.text_input(
            "SEARCH COURSES",
            placeholder="Search your favourite course..."
        )

        filtered = [
            course for course in courses
            if search.lower() in course["topic"].lower()
        ]

        ready = sum(
            1 for course in filtered
            if (
                PPT_DIR / (
                    course["id"]
                    + "_40_MODULES_V100.pptx"
                )
            ).exists()
        )

        a, b, c = st.columns(3)

        a.metric("Total Courses", len(filtered))
        b.metric("Ready PPT Books", ready)
        c.metric("Starting Price", "₹99")

        st.divider()

        for i, course in enumerate(filtered):

            with st.expander(
                course["topic"]
                + " - ₹"
                + str(course["price"])
            ):

                st.subheader(course["topic"])

                st.write(
                    "Course Price: ₹"
                    + str(course["price"])
                )

                st.write("40 Learning Modules")

                if QR_FILE.exists():

                    st.image(
                        str(QR_FILE),
                        width=220
                    )

                else:

                    st.info(
                        "UPI QR will be available after admin uploads it."
                    )

                params = {
                    "pa": UPI_ID,
                    "pn": OWNER,
                    "am": str(course["price"]),
                    "cu": "INR",
                    "tn": course["topic"][:40]
                }

                payment_link = (
                    "upi://pay?"
                    + urllib.parse.urlencode(params)
                )

                st.link_button(
                    "PAY ₹" + str(course["price"]) + " VIA UPI",
                    payment_link,
                    type="primary"
                )

                st.divider()

                st.subheader("GET YOUR COURSE ACCESS")

                with st.form(
                    "purchase_" + course["id"]
                ):

                    name = st.text_input(
                        "Full Name",
                        key="name_" + course["id"]
                    )

                    email = st.text_input(
                        "Email Address",
                        key="email_" + course["id"]
                    )

                    utr = st.text_input(
                        "UPI Transaction UTR",
                        key="utr_" + course["id"],
                        max_chars=30
                    )

                    submitted = st.form_submit_button(
                        "SUBMIT PAYMENT DETAILS",
                        type="primary"
                    )

                    if submitted:

                        if len(name.strip()) < 3:

                            st.error("Enter your full name.")

                        elif "@" not in email or "." not in email:

                            st.error("Enter a valid email address.")

                        elif len(utr.strip()) < 5:

                            st.error("Enter your UPI transaction UTR.")

                        elif any(
                            p.get("utr", "").strip() == utr.strip()
                            and p.get("status") in ["PENDING", "APPROVED"]
                            for p in purchases
                        ):

                            st.error(
                                "This UTR has already been submitted."
                            )

                        else:

                            invoice = (
                                "INV"
                                + datetime.datetime.now().strftime(
                                    "%Y%m%d%H%M%S"
                                )
                                + secrets.token_hex(2).upper()
                            )

                            purchase = {
                                "invoice_no": invoice,
                                "access_key": "",
                                "name": name.strip(),
                                "email": email.strip().lower(),
                                "course": course["topic"],
                                "course_id": course["id"],
                                "price": int(course["price"]),
                                "utr": utr.strip(),
                                "status": "PENDING",
                                "date": datetime.datetime.now().isoformat()
                            }

                            purchases.append(purchase)

                            save(PURCHASE_FILE, purchases)

                            st.success(
                                "Payment details submitted successfully."
                            )

                            st.info(
                                "Your payment is pending admin verification. "
                                "After approval, your course access will be activated."
                            )

                            st.code(invoice)

                            st.rerun()


    # =================================================
    # MY ACCESS - MY LEARNING
    # =================================================

    elif menu == "My Access":

        st.title("📚 MY LEARNING")

        st.write(
            "Enter your approved Invoice Number "
            "or Access Key to unlock your course."
        )

        access_input = st.text_input(
            "INVOICE NUMBER OR ACCESS KEY"
        )

        if st.button(
            "UNLOCK MY COURSE",
            type="primary"
        ):

            found = [
                p for p in purchases
                if (
                    p.get("invoice_no") == access_input.strip()
                    or p.get("access_key") == access_input.strip()
                )
                and p.get("status") == "APPROVED"
            ]

            if not found:

                st.error(
                    "Access not found or payment not approved yet."
                )

            else:

                purchase = found[0]

                st.success(
                    "WELCOME "
                    + purchase.get("name", "Student")
                )

                st.subheader(
                    purchase.get("course", "Your Course")
                )

                st.write(
                    "Course Price: ₹"
                    + str(purchase.get("price", 99))
                )

                st.write(
                    "Invoice: "
                    + purchase.get("invoice_no", "")
                )

                st.write("40 Learning Modules")

                course_id = purchase.get("course_id", "")

                ppt_path = (
                    PPT_DIR
                    / (
                        course_id
                        + "_40_MODULES_V100.pptx"
                    )
                )

                if ppt_path.exists():

                    st.success("Your Course PPT is Ready.")

                    st.download_button(
                        "DOWNLOAD YOUR 40 MODULE COURSE",
                        data=ppt_path.read_bytes(),
                        file_name=ppt_path.name,
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                        type="primary"
                    )

                else:

                    st.warning(
                        "Course book is being prepared. "
                        "Please contact the administrator."
                    )

# =====================================================
# APPLICATION FOOTER
# =====================================================

st.divider()

st.caption(
    "© Brahma Education | V100 | Professional Learning Platform"
)