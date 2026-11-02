import os
import json
import hashlib
import time
from datetime import datetime, timedelta
import streamlit as st
from pptx import Presentation
from pptx.util import Inches, Pt

# Ensure required folders exist
os.makedirs("data/ppts", exist_ok=True)

# 17. FILE STRUCTURE DEFINE PATHS
COURSES_FILE = "data/courses.json"
PURCHASES_FILE = "data/purchases.json"
MARKETING_FILE = "data/marketing.json"
API_KEYS_FILE = "data/api_keys.json"
HASH_FILE = "data/master_hash"
SESSION_FILE = "data/admin_session"
QR_IMAGE_PATH = "data/upi_qr.jpg"

# 18. STABLE COMPACT 100 COURSES ARRAY GENERATION (Prevents UI syntax crash & large string limits)
RAW_TOPICS = [
    "AI Agent Automation", "Instagram Reels Mastery", "YouTube Automation", "Prompt Engineering",
    "Digital Marketing SEO", "ChatGPT Mastery", "Facebook Ads", "Google Ads", "SEO Advanced",
    "Social Media Marketing", "Content Writing AI", "Copywriting", "Blogging", "Affiliate Marketing",
    "Dropshipping", "E-commerce Shopify", "Canva Design", "Video Editing CapCut", "YouTube SEO",
    "Instagram Growth", "LinkedIn Marketing", "Twitter X Growth", "TikTok Viral", "Pinterest",
    "Quora", "Email Marketing Automation", "WhatsApp Marketing", "Telegram Growth", "Influencer Marketing",
    "Personal Branding", "Freelancing Mastery", "Agency Business", "SaaS Business", "No-Code Bubble",
    "Python", "JavaScript", "React", "Next.js", "Node.js", "Full Stack Web Dev", "WordPress",
    "Shopify Store", "UI UX Design", "Figma", "Graphic Design", "Logo Design", "Thumbnail Design Viral",
    "Video Animation", "AI Image Midjourney", "AI Video Sora", "Voice Cloning ElevenLabs",
    "Automation n8n Make", "Zapier", "Notion", "Excel Advanced", "Google Sheets Automation",
    "Data Analysis Python", "Machine Learning", "Deep Learning", "Data Science", "Stock Trading AI",
    "Crypto Trading", "Forex Trading", "Real Estate Business", "Motivational Speaking", "Public Speaking",
    "Communication Skills", "English Speaking", "Podcast Mastery", "Music Production AI", "Photography",
    "Reels Editing Viral", "Meme Marketing", "Viral Content Formula", "Lead Generation", "Sales Funnel",
    "Landing Page Design", "CRO", "Customer Support Automation", "HR Recruitment AI", "Business Plan Mastery",
    "Startup Funding", "Business Automation AI", "Time Management", "Mindset Millionaire", "Meditation",
    "Fitness Coaching Business", "Diet Nutrition Business", "Yoga Teaching Business", "Cooking Channel Business",
    "Travel Vlogging Business", "Gaming Channel Growth", "Education Channel Growth", "Finance Channel Business",
    "News Channel Automation", "Meme Page Business", "Affiliate Blog SEO", "Amazon FBA", "Etsy Store",
    "Print on Demand", "Stock Photography Business", "Voice Over Business", "Translation Business AI",
    "Resume Writing Business", "LinkedIn Profile Optimization", "AI Tools Mastery", "Chatbot Development",
    "AI Voice Agent", "AI Receptionist Business"
]

def load_courses():
    if not os.path.exists(COURSES_FILE):
        courses_list = []
        for i, topic in enumerate(RAW_TOPICS):
            courses_list.append({
                "id": "BRAHMA" + str(1000 + i),
                "topic": topic,
                "price": 99
            })
        save_courses(courses_list)
        return courses_list
    try:
        with open(COURSES_FILE, "r") as f:
            data = json.load(f)
            # 5. AUTO FIX FOR PRICE > 200 TO 99
            for c in data:
                if c.get("price", 99) > 200:
                    c["price"] = 99
            return data
    except:
        return []

def save_courses(data):
    with open(COURSES_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_purchases():
    if os.path.exists(PURCHASES_FILE):
        try:
            with open(PURCHASES_FILE, "r") as f: return json.load(f)
        except: return []
    return []

def save_purchases(data):
    with open(PURCHASES_FILE, "w") as f: json.dump(data, f, indent=4)

def load_api_keys():
    if os.path.exists(API_KEYS_FILE):
        try:
            with open(API_KEYS_FILE, "r") as f: return json.load(f)
        except: return {}
    return {"openai": "", "claude": "", "gemini": "", "pinecone": "", "supabase": "", "elevenlabs": "", "n8n": "", "make": "", "zapier": ""}

def save_api_keys(data):
    with open(API_KEYS_FILE, "w") as f: json.dump(data, f, indent=4)

# 7. ADMIN SECURITY PROTOCOLS
def get_master_hash():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f: return f.read().strip()
    default_hash = hashlib.sha256("brahma123".encode()).hexdigest()
    with open(HASH_FILE, "w") as f: f.write(default_hash)
    return default_hash

def check_admin_session():
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, "r") as f:
                sess = json.load(f)
            if time.time() < sess.get("expiry", 0): return True
        except: pass
    return False

def create_admin_session():
    expiry = time.time() + (7 * 24 * 60 * 60) # 7 Days Remember Session
    with open(SESSION_FILE, "w") as f:
        json.dump({"expiry": expiry}, f)

def clear_admin_session():
    if os.path.exists(SESSION_FILE): os.remove(SESSION_FILE)

# 4. DEEP V100 PPT GENERATION MODULE (40 Detailed Slides, Fixed Pt Formats, High-Stability Concatenations)
def generate_course_ppt(course_title, course_id):
    prs = Presentation()
    prs.slide_width = Inches(13.33)  # 13.33 x 7.5 Wide Screen Setup
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # 3. HIGH VALUE 40 ARCHITECTURE MODULE DATA
    modules_info = [
        ("M01 WHAT IS", "Definition: Advanced systemic operational scaling engine. 5 Corporate automation workflows. Saves up to 80% baseline execution times."),
        ("M02 WHY IMPORTANT", "Future Proof Strategy: Critical global shifts. 2026 market demands show extreme technical shortage. Multiplies career target salary metrics by 3x."),
        ("M03 WHERE USE", "Omnichannel Execution Ecosystem: Scales high viral output channels including Instagram Reels, YouTube Shorts, Enterprise Automations. Boosts job positions & freelancing."),
        ("M04 WHEN TIMING", "Peak Human Efficiency Window: Deploy assets daily morning 6 to 8 AM when psychological focus metrics peak. Standard Monday and Thursday postings drive 40% higher traffic spikes."),
        ("M05 WHO ELIGIBLE", "Universal Enrollment Framework: Open globally to student brackets age 16 plus, technical working professionals, core brick-and-mortar business owners, up to 60 years. Zero baseline degrees required. Consumes 30 mins daily tracking."),
        ("M06 HOW ARCHITECTURE", "Core Loop Engine Model: Operates via persistent Perceive-Reason-Act frameworks. Uses explicit ReAct patterns, deep Chain of Thought routing systems, secure RAG vector stores, prompt engineering memory layers."),
        ("M07 WITH WHAT TOOLS", "Integrated Ecosystem Infrastructure: Seamlessly shifts across zero-cost assets (Canva, CapCut, ChatGPT app framework, Notion dashboard, Google Sheets automation) to advanced enterprise tools (Paid ElevenLabs APIs, n8n webhook routing, Make ecosystem infrastructure, Zapier pipelines)."),
        ("M08 WHAT EARN", "Monetization Scale & Pipelines: Launch independent freelance agencies via online platforms like Upwork and Fiverr. Captures Rs 20k to 50k first month. Scales up to 1L monthly recurring inside 3 months. Corporate agency growth unlocks Rs 2L plus monthly tiers."),
        ("M09 HOW TO USE", "Operational Device Strategy: Complete portable optimization across smartphones via native applications (InShot editing suites, mobile CapCut layers, Canva viewports, native ChatGPT applications). Absolute browser synchronization on laptops via dashboard suites."),
        ("M10 HOW TO DO RIGHT WAY", "Daily Optimization Routine: Enforce deep 30 mins daily practice block. Allocate 15 mins structural theory review and 15 mins live manual build. Maintain dedicated engineering log diaries. Execute comprehensive end-to-end revisions every Sunday."),
        ("M17 REAL STORY", "Inspirational Narrative of Rahul: Based in remote tier-3 village sector. Operated with single outdated Redmi 8 mobile device backed by basic Jio 1GB standard tier connection. Absolute lack of primary desktop computing architecture. Enrolled under Brahma Master Teacher framework. Invested 1 hour regular daily practice over 2 months. Unlocked Upwork freelance pipelines by month three. Submitted 20 competitive custom pipeline proposals. Faced 19 consecutive automated corporate rejections. Secured 1 premium high-paying USA enterprise account generating Rs 15k upfront. Month four expanded workspace portfolio to capture 5 high-yield steady retainers yielding Rs 75k monthly stack. Reached month six establishing multi-seat automation consulting agency mapping Rs 2 Lakhs predictable clean margin. Managed to build high-end residential real estate architecture for parents. Secured absolute financial freedom metrics."),
        ("M20 MISTAKES 90% FAIL", "Critical Attrition Pitfalls: Mistake 1: Attempting high-level engineering without mastering foundational basics. Mistake 2: Consuming passive video guides without performing active manual code validation. Mistake 3: Tunnel vision targeting rapid short-term monetary targets over raw technical capability stack. Mistake 4: Skipping historical logging logbooks causing rapid concept loss. Mistake 5: Solo engineering journeys void of professional advisory mentorship loops."),
        ("M21 PRO TIP", "Elite Execution Secrets: Maintain physical target diary logbook. Log every single night for 10 minutes tracking 4 vital metrics: core engineering takeaways achieved, negative implementation mistakes recorded, absolute micro-execution roadmap for tomorrow morning, disruptive high-growth business concepts."),
" + str(p.get("price")) + " | Gateway Reference UTR Number: " + str(p.get("utr")) + "")
st.write("📅 Timeline Log Matrix: " + str(p.get("date")) + " | System Validation Core Flag: " + str(p.get("status")))
st.write("---")
else:
st.info("System has verified zero standard inbound consumer conversions logged inside current cycles database files.")
st.write("---")
# 16. OMNICHANNEL MARKETING ENGINE AUTOMATION CONTROLS
st.subheader("🤖 Omnichannel Automated Marketing Campaigns Engine")
if st.button("GENERATE 60 MARKETING POSTS"):
marketing_manifest = []
current_time = datetime.now()
# Map daily 20 course profiles systematically to generate exactly 60 targeted contextual distribution posts
for idx in range(min(20, len(courses))):
target_c = courses[idx]
c_title = target_c.get("topic")
# Platform 1 Distribution Block - Facebook Morning Platform Target 7AM
marketing_manifest.append({
"timestamp": (current_time + timedelta(hours=7)).strftime("%Y-%m-%d 07:00:00"),
"platform": "Facebook",
"post_type": "Morning Post",
"content": "Scale your execution architecture. Master " + str(c_title) + " inside our comprehensive elite master class track today. Complete production level 40 detailed models layout blueprint. Price only Rs 99."
})
# Platform 2 Distribution Block - Instagram Optimization Target 12PM
marketing_manifest.append({
"timestamp": (current_time + timedelta(hours=12)).strftime("%Y-%m-%d 12:00:00"),
"platform": "Instagram",
"post_type": "Reel Video Script Template",
"content": "[Visual Anchor Hook: Extreme performance dashboard workflows showing 80% time compression factors.] Stop wasting execution hours blindly manually structuring operations layers. Access the ultimate systemic blueprint to automate " + str(c_title) + " workflows now. Link embedded inside biography profiles."
})
# Platform 3 Distribution Block - Digital Content Engine Target 7PM
marketing_manifest.append({
"timestamp": (current_time + timedelta(hours=19)).strftime("%Y-%m-%d 19:00:00"),
"platform": "Blog SEO",
"post_type": "Authority Positioning Article Content",
"content": "Core analysis metrics inside modern corporate optimization frameworks focus explicitly on strategic tool adoption metrics. Review the full definitive study mapping " + str(c_title) + " deployment roadmaps to fast track target revenue pipelines."
})
with open(MARKETING_FILE, "w") as f:
json.dump(marketing_manifest, f, indent=4)
st.success("⚡ Campaign Pipelines Activated! 60 Targeted Distribution Framework Assets Saved to local storage database maps.")
if os.path.exists(MARKETING_FILE):
st.write("Active Queue Distribution Records: Logged operational tracks verified.")
with open(MARKETING_FILE, "r") as f:
mk_data = json.load(f)
st.json(mk_data[:3]) # Display sample distribution manifest snippet configurations for verification

### 📋 `requirements.txt`
```text
streamlit
python-pptx