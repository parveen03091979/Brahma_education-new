import streamlit as st
import json
import hashlib
import datetime
import urllib.parse
from pathlib import Path
import pandas as pd

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    PPTX_OK = True
except:
    PPTX_OK = False

st.set_page_config(page_title="Brahma Attractive PPT", layout="wide")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
PPT_DIR = DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)
AUTO_DIR = DATA_DIR / "automation"
AUTO_DIR.mkdir(exist_ok=True)

MY_UPI_ID = "parveen39179@okicici"
MY_NAME = "Parveen Kumar"

HUNDRED_COURSES = [
"AI Agent Automation 2026","Instagram Reels Mastery","YouTube Automation AI","Prompt Engineering Pro","Digital Marketing SEO Mastery",
"ChatGPT Mastery 2026","Facebook Ads Mastery","Google Ads Mastery","SEO Advanced 2026","Social Media Marketing Pro",
"Content Writing AI","Copywriting Mastery","Blogging Mastery 2026","Affiliate Marketing Pro","Dropshipping Business",
"E-commerce Mastery Shopify","Canva Design Mastery","Video Editing CapCut Pro","YouTube SEO Mastery","Instagram Growth Hack",
"LinkedIn Marketing Pro","Twitter X Growth Mastery","TikTok Viral Mastery","Pinterest Marketing","Quora Marketing",
"Email Marketing Automation","WhatsApp Marketing Pro","Telegram Channel Growth","Influencer Marketing","Personal Branding Mastery",
"Freelancing Mastery Upwork Fiverr","Agency Business Mastery","SaaS Business 2026","No-Code Business Bubble","Python Programming Mastery",
"JavaScript Mastery 2026","React JS Mastery","Next.js Mastery","Node.js Backend Mastery","Web Development Full Stack",
"WordPress Mastery","Shopify Store Design","UI UX Design Mastery","Figma Design Pro","Graphic Design Mastery",
"Logo Design Mastery","Thumbnail Design Viral","Video Animation Mastery","AI Image Generation Midjourney","AI Video Generation Sora",
"Voice Cloning ElevenLabs","Automation n8n Make","Zapier Automation Mastery","Notion Productivity Mastery","Excel Advanced Mastery",
"Google Sheets Automation","Data Analysis Python","Machine Learning Mastery","Deep Learning 2026","Data Science Mastery",
"Stock Market Trading AI","Crypto Trading Mastery","Forex Trading Pro","Real Estate Business","Motivational Speaking Mastery",
"Public Speaking Pro","Communication Skills Mastery","English Speaking Pro","Hindi Content Creation","Podcast Mastery",
"Music Production AI","Photography Mastery","Reels Editing Viral","Meme Marketing Mastery","Viral Content Formula",
"Lead Generation Mastery","Sales Funnel Mastery","Landing Page Design High Converting","CRO Conversion Optimization","Customer Support Automation",
"HR Recruitment AI","Business Plan Mastery","Startup Funding Mastery","Business Automation AI","Time Management Mastery",
"Mindset Mastery Millionaire","Meditation Mindfulness","Fitness Coaching Business","Diet Nutrition Business","Yoga Teaching Business",
"Cooking Channel Business","Travel Vlogging Business","Gaming Channel Growth","Education Channel Growth","Finance Channel Business",
"News Channel Automation","Meme Page Business","Affiliate Blog SEO","Amazon FBA Mastery","Etsy Store Mastery",
"Print on Demand Business","Stock Photography Business","Voice Over Business","Translation Business AI","Resume Writing Business",
"LinkedIn Profile Optimization Business","AI Tools Mastery 100 Tools","Chatbot Development","AI Voice Agent Mastery","AI Receptionist Business"
]

def load_json(p, default):
    try:
        if p.exists() and p.stat().st_size > 2:
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return default

def save_json(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def get_curriculum(topic):
    modules = []
    m1 = [
        "What is topic Definition with 5 real examples",
        "History of topic 2015 to 2026 timeline",
        "Types of topic Reactive Proactive Autonomous",
        "Topic vs Other Difference deep",
        "Why topic is future Market data 2026",
        "Career in topic Jobs Salary Freelancing",
        "Topic Mindset How to think like Builder",
        "Common myths about topic busted",
        "Success stories 5 millionaires",
        "Failure stories Why 90 percent fail",
        "Topic Roadmap 0 to Expert 400 lessons",
        "Tools needed Complete list 20 tools",
        "Industry overview Where topic used",
        "Market size growth data",
        "Skills needed Roadmap",
        "Learning path Step by step mastery",
        "Time management Learn in 90 days",
        "Best resources Books YouTube Courses",
        "Community Discord Reddit help",
        "Mentorship How to find mentor",
        "Architecture Brain Memory Tools Planning",
        "Core Tech behind topic GPT4 Claude Gemini",
        "RAG Retrieval Augmented Generation deep",
        "Memory types Short Long Vector DB",
        "Tools How to use external tools",
        "Planning ReAct Chain Thought Tree Thought",
        "Reasoning How to think step by step",
        "Action How to take action",
        "Observation How to learn from result",
        "Loop Working cycle Perceive Reason Act",
        "Case Study 1 Real business",
        "Case Study 2 Real business 10M ARR",
        "Case Study 3 Real business 10M users",
        "Case Study 4 Real business Workspace",
        "Case Study 5 Real business 5k month",
        "Assignment Build first simple project",
        "Assignment Research 10 examples sheet",
        "Assignment Draw Architecture diagram",
        "Module 1 Summary Checklist",
        "Module 1 Test 20 Questions"
    ]
    modules.append({"title": f"Module 1: {topic} Fundamentals", "lessons": m1})
    for m in range(2, 11):
        lessons = [f"Module {m} Lesson {i}: {topic} Real Topic {m}-{i} Deep unique - Practical" for i in range(1, 41)]
        modules.append({"title": f"Module {m}: {topic} Deep Module {m}", "lessons": lessons})
    curriculum = []
    lc = 1
    for mod in modules:
        vids = []
        for raw in mod["lessons"]:
            title = f"Lesson {lc}: {raw}"
            hi = f"""WHAT IS IT?
{raw} kya hai? Simple definition.

WHY IMPORTANT?
{topic} me ye sabse important hai. Iske bina kaam adhura.

HOW IT WORKS? Step by step:
1. Setup: Tool open karo
2. Action: Pehla step karo
3. Test: Result check karo
4. Improve: Galti sudharo

REAL EXAMPLE:
2026 me real company ne {raw} se 5 lakh per month kamaya. Kaise? Unhone daily practice kiya.

COMMON MISTAKES (90% log karte hain):
- Mistake 1: Basics skip karna
- Mistake 2: Direct advanced karna
- Mistake 3: Practice nahi karna

PRO TIP (Koi nahi batata):
Pro log {raw} ko roz 30 min practice karte hain. Aur notes banate hain.

ASSIGNMENT:
Aaj {raw} par ek chhota project banao. Kal tak submit karo.
"""
            en = f"""WHAT IS IT?
What is {raw}? Simple definition.

WHY IMPORTANT?
Most important in {topic}. Without this work is incomplete.

HOW IT WORKS? Step by step:
1. Setup: Open tool
2. Action: Do first step
3. Test: Check result
4. Improve: Fix mistake

REAL EXAMPLE:
Real company earned 5 lakh per month in 2026 using {raw}. How? Daily practice.

COMMON MISTAKES (90% do):
- Mistake 1: Skipping basics
- Mistake 2: Going direct advanced
- Mistake 3: No practice

PRO TIP (Nobody tells):
Pros practice {raw} 30 min daily. And make notes.

ASSIGNMENT:
Build small project on {raw} today. Submit by tomorrow.
"""
            vids.append({"no": lc, "title": title, "desc_hi": hi, "desc_en": en})
            lc += 1
        curriculum.append({"title": mod["title"], "videos": vids})
    return curriculum

def add_colored_shape(slide, left, top, width, height, fill_rgb, border_rgb=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(*fill_rgb)
    shape.line.fill.background()
    if border_rgb:
        shape.line.color.rgb = RGBColor(*border_rgb)
        shape.line.width = Pt(1.5)
    return shape

def create_attractive_ppt(course_id, course_topic):
    if not PPTX_OK:
        return None, "python-pptx missing"
    try:
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)

        curriculum = get_curriculum(course_topic)

        # Title Slide - Attractive Colorful
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        # Background light
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(245, 247, 255)
        # Top colorful bar
        add_colored_shape(slide, Inches(0), Inches(0), Inches(13.33), Inches(0.3), (79, 70, 229))
        # Main title box blue
        shape = add_colored_shape(slide, Inches(0.5), Inches(0.8), Inches(12.3), Inches(1.8), (79, 70, 229))
        tf = shape.text_frame
        tf.word_wrap = True
        tf.text = f"{course_topic}\nAttractive Deep Course - 400 Lessons - Har Lesson Alag"
        for para in tf.paragraphs:
            para.alignment = 1
            for run in para.runs:
                run.font.size = Pt(28)
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
        # Subtitle box white with border
        shape2 = add_colored_shape(slide, Inches(0.5), Inches(3.0), Inches(12.3), Inches(1.5), (255, 255, 255), (79, 70, 229))
        tf2 = shape2.text_frame
        tf2.word_wrap = True
        tf2.text = f"10 Modules x 40 Lessons = 400 Lessons\nHar lesson attractive colorful design - Bade fonts - Acchi explain - Practical + Assignment\nHindi + English - Puri learning - Interest banega"
        for para in tf2.paragraphs:
            para.alignment = 1
            for run in para.runs:
                run.font.size = Pt(16)
                run.font.color.rgb = RGBColor(55, 65, 81)
        # Bottom bar orange
        add_colored_shape(slide, Inches(0), Inches(7.2), Inches(13.33), Inches(0.3), (245, 158, 11))

        count = 0
        for mod in curriculum:
            # Module Slide - Attractive
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            fill = slide.background.fill
            fill.solid()
            fill.fore_color.rgb = RGBColor(255, 255, 255)
            add_colored_shape(slide, Inches(0), Inches(0), Inches(13.33), Inches(0.3), (79, 70, 229))
            # Module box
            shape = add_colored_shape(slide, Inches(0.5), Inches(1.0), Inches(12.3), Inches(2.5), (238, 242, 255), (79, 70, 229))
            tf = shape.text_frame
            tf.word_wrap = True
            tf.text = f"{mod['title']}\n40 Lessons - Har lesson attractive colorful - Bade fonts - Acchi explain"
            for para in tf.paragraphs:
                para.alignment = 1
                for run in para.runs:
                    run.font.size = Pt(24)
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(79, 70, 229)
            add_colored_shape(slide, Inches(0), Inches(7.2), Inches(13.33), Inches(0.3), (245, 158, 11))
            count += 1

            for vid in mod["videos"]:
                if count >= 80:
                    break
                slide = prs.slides.add_slide(prs.slide_layouts[6])
                fill = slide.background.fill
                fill.solid()
                fill.fore_color.rgb = RGBColor(249, 250, 251)
                # Top bar
                add_colored_shape(slide, Inches(0), Inches(0), Inches(13.33), Inches(0.15), (79, 70, 229))
                # Title bar - blue attractive
                title_shape = add_colored_shape(slide, Inches(0.2), Inches(0.25), Inches(12.9), Inches(0.7), (79, 70, 229))
                tf = title_shape.text_frame
                tf.word_wrap = True
                tf.text = vid["title"][:180]
                for para in tf.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(14)
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(255, 255, 255)

                # Hindi box - light orange attractive with border
                hindi_shape = add_colored_shape(slide, Inches(0.2), Inches(1.1), Inches(6.3), Inches(6.1), (255, 251, 235), (245, 158, 11))
                tf_h = hindi_shape.text_frame
                tf_h.word_wrap = True
                tf_h.text = f"🌟 HINDI - Acchi Explain - Attractive\n\n{vid['desc_hi']}"[:1300]
                for para in tf_h.paragraphs:
                    for run in para.runs:
                        run.font.size = Pt(11)
                        run.font.color.rgb = RGBColor(120