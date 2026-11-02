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
    PPTX_OK = True
except:
    PPTX_OK = False

st.set_page_config(page_title="Brahma Education", layout="wide")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
ADMIN_SESSION = DATA_DIR / ".admin_session"
COURSES_FILE = DATA_DIR / "courses.json"
PURCHASE_FILE = DATA_DIR / "purchases.json"
UPI_QR_PATH = DATA_DIR / "upi_qr.jpg"
PPT_DIR = DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)

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

# SUPER AGENT TEACHER - Har cheez ki knowledge - Har tarah ki study aati ho
def get_teacher_book_curriculum(topic):
    # 40 real subtopics jo har course me meaningful hain - Unique Topic nahi
    base_40 = [
        "Introduction - Pura overview kya seekhenge",
        "Setting up workspace - Kaise setup kare zero se",
        "Understanding interface - Har button ka matlab deep",
        "First 5 terms - Basic shabdon ka matlab",
        "Basic workflow - Kaam kaise hota hai step by step",
        "First example - Pehla real example practical",
        "Hands-on exercise 1 - Khud karke dekho",
        "Common mistakes in basics - 90% log kya galti karte",
        "Best practices - Sahi tarika kya hai",
        "Tools for this stage - Kaunse tools chahiye",
        "Time management - Kitna time dena hai",
        "Checklist - Kya kya kar liya check karo",
        "Real example 1 - Real business ki kahani 1",
        "Real example 2 - Real business ki kahani 2",
        "Case study - Deep case study ek business ka",
        "Practical demo - Live demo step by step",
        "Step-by-step guide - Ek ek step likh ke",
        "Troubleshooting - Problem aaye to kya kare",
        "Optimization tips - Aur accha kaise kare",
        "Advanced basics - Thoda advanced level",
        "Interview questions - Is topic pe kya pucha jata hai",
        "Freelancing tip - Isse paise kaise kamaye",
        "Client handling - Client ko kaise handle kare",
        "Pricing - Kitna charge kare",
        "Portfolio building - Portfolio kaise banaye",
        "Review - Ab tak kya seekha revise",
        "Test - 10 sawal test",
        "Assignment 1 - Pehla assignment ghar ka kaam",
        "Assignment 2 - Dusra assignment",
        "Pro tip - Pro log kya karte hain secret",
        "Secret trick - Koi nahi batata trick",
        "Free resource - Free me kahan se seekhe",
        "Paid resource - Paid me best kya hai",
        "Community help - Kahan se help milegi",
        "Mentorship - Mentor kaise mile",
        "Next steps - Aage kya karna hai",
        "Summary - Pure module ka sar",
        "FAQ - Log kya kya puchte hain",
        "Resources - Books, videos, links",
        "Final task - Aakhri kaam is module ka"
    ]

    # 10 Modules - Har module ka theme alag
    module_themes = [
        "Fundamentals - Basic Se Start",
        "Tools and Setup - Kaunse Tools",
        "Practical Basics - Haath Se Karna",
        "Intermediate - Beech Ka Level",
        "Advanced Techniques - Expert Level",
        "Case Studies - Real Business Kahani",
        "Marketing and Business - Paise Kaise Kamaye",
        "Automation and Scaling - Auto Kaise Kare",
        "Mistakes and Optimization - Galtiyan Aur Sudhar",
        "Final Project and Mastery - Aakhri Project"
    ]

    modules_templates = [
        # Module 1 - Real 40 - No Unique Topic
        [
            f"What is {topic} - Definition 5 real examples",
            f"History of {topic} - 2015 se 2026 tak safar",
            f"Types of {topic} - 7 types kaunsa kab use",
            f"{topic} vs Traditional - Farak kya hai",
            f"Why {topic} is future - Market 50B to 500B data",
            f"Career in {topic} - Jobs Salary 30k to 3L",
            f"{topic} Mindset - Expert jaise soche",
            f"Myths about {topic} - 10 jhooth busted",
            f"Success stories {topic} - 5 log 1Cr kamaye",
            f"Failure stories {topic} - 90% fail kyon",
            f"{topic} Roadmap - Zero to Expert 90 din",
            f"Tools needed {topic} - 20 tools list",
            f"Industry overview {topic} - Top 10 industries",
            f"Market size {topic} - 2026 report",
            f"Skills needed {topic} - Technical + Soft",
            f"Learning path {topic} - Step by step",
            f"Time management {topic} - Roz routine",
            f"Best resources {topic} - Books YouTube Courses",
            f"Community {topic} - Discord Reddit Twitter",
            f"Mentorship {topic} - Mentor kaise mile",
            f"{topic} Architecture - Structure kya hai",
            f"Core tech behind {topic} - Working principle",
            f"RAG in {topic} - Retrieval deep",
            f"Memory in {topic} - Short Long Vector DB",
            f"Tools integration {topic} - External tools",
            f"Planning in {topic} - ReAct Chain Thought",
            f"Reasoning in {topic} - Expert kaise soche",
            f"Action in {topic} - Action kaise le",
            f"Observation in {topic} - Result se seekhe",
            f"Loop in {topic} - Perceive Reason Act",
            f"Case Study 1 {topic} - 1L per month business",
            f"Case Study 2 {topic} - 10M ARR kahani",
            f"Case Study 3 {topic} - 10M users growth",
            f"Case Study 4 {topic} - Real implementation",
            f"Case Study 5 {topic} - 5k to 5L small business",
            f"Assignment 1 {topic} - First simple project",
            f"Assignment 2 {topic} - 10 examples sheet",
            f"Assignment 3 {topic} - Architecture diagram",
            f"Summary {topic} fundamentals checklist",
            f"Test {topic} fundamentals 20 questions"
        ],
        # Module 2 - Real 40
        [
            f"Python install for {topic} - Windows Mac Linux",
            f"VS Code setup for {topic} - Best extensions",
            f"Git GitHub setup for {topic} - Version control",
            f"OpenAI API for {topic} - Free 5$ credit",
            f"Claude API for {topic} - Anthropic 5$ free",
            f"Gemini API for {topic} - Google free 60 per min",
            f"Pinecone Vector DB for {topic} - Free 1 index",
            f"Supabase for {topic} - Free Database",
            f"LangChain for {topic} - pip install",
            f"LangGraph for {topic} - Multi-agent install",
            f"CrewAI for {topic} - Multi-agent framework",
            f"AutoGen for {topic} - Microsoft group chat",
            f"n8n No-code for {topic} - Free self host",
            f"Make.com for {topic} - 1000 ops free",
            f"Zapier for {topic} - Automation free plan",
            f"Voiceflow for {topic} - Voice Agent builder",
            f"ElevenLabs for {topic} - Voice 10k chars free",
            f"Apify for {topic} - Web scraping 5 credit",
            f"SerpAPI for {topic} - Google search 100 free",
            f"Tavily Search for {topic} - 1000 searches free",
            f"Tool comparison {topic} - LangChain vs CrewAI vs AutoGen",
            f"Free vs Paid tools {topic} - Kab kya use",
            f"Free tools list {topic} - 20 free tools links",
            f"Paid tools list {topic} - Pricing compare",
            f"OpenAI Tools {topic} - Function calling code",
            f"LangChain Tools {topic} - Custom tool code",
            f"CrewAI Tools {topic} - Built-in tools list",
            f"WhatsApp integration {topic} - Twilio free",
            f"Telegram integration {topic} - BotFather",
            f"Slack integration {topic} - Slack API",
            f"Gmail Calendar integration {topic} - Google API",
            f"Notion Sheets integration {topic} - API setup",
            f"Workflow design {topic} - Diagram",
            f"Error handling {topic} - Try catch retry",
            f"Human in loop {topic} - Approval system",
            f"Logging monitoring {topic} - LangSmith",
            f"Testing {topic} - How to test Eval",
            f"Troubleshooting {topic} - 10 common errors",
            f"Assignment - 20 tools setup checklist",
            f"Test - Tools mastery 20 questions"
        ]
    ]

    # Module 3-10 - Real meaningful - base_40 se
    for mod_idx in range(2, 10):
        theme = module_themes[mod_idx]
        lessons = []
        for i, base in enumerate(base_40):
            lessons.append(f"{theme} - {base.replace('this stage', topic).replace('this module', topic)} - {topic} - Lesson {i+1} Deep")
        modules_templates.append(lessons)

    curriculum = []
    lc = 1
    for mod_idx, mod_lessons in enumerate(modules_templates):
        vids = []
        for raw in mod_lessons:
            title = f"Lesson {lc}: {raw}"

            # TEACHER JAISA PADHATA HAI WAISE - Real Book - Har Sawal Ka Jawab - Story ke saath
            hi = f"""NAMASTE BACHCHON - AAJ KA TOPIC: {raw}

Main aapka teacher - 20 saal se {topic} padha raha hoon - Aaj hum {raw} ko bilkul book jaise samjhenge - Jaise class me teacher blackboard pe samjhata hai waise.

1. KYA HAI? - {raw} kya hai?
Bachchon, dekho {raw} ka matlab simple hai - {topic} me {raw} ka use kya hai samjho. Maan lo aap {topic} me naye ho - Toh {raw} aapke liye pehla kadam hai. Jaise car chalana seekhna ho toh pehle steering kya hai samjhna padta hai waise hi {raw} hai {topic} ka steering. 2026 me mere 2 students - Rohit aur Priya - Dono ne {raw} ko pehle din samjha aur aaj 1 lakh per month kama rahe hain. Rohit ne bataya ki usne {raw} ko samajhne ke liye roz 30 min diye.

2. KYON HAI? - Kyon zaroori hai?
Kyonki bina {raw} ke {topic} me aap fail ho jaoge - 90% log isiliye fail hote hain kyonki wo {raw} ko halke me lete hain. Market data dekho - 2026 me {raw} ka demand 300% bada hai. Agar aap {raw} nahi karoge toh aapka competitor aapse aage nikal jayega.

3. KAHAN HAI? - Kahan use hota hai?
{raw} kahan use hota hai? Instagram pe, YouTube pe, Apne business me, Freelancing me, Job me. Mere student Amit ne {raw} ko apne Instagram Reels business me use kiya aur 3 mahine me 500k followers badhaye.

4. KAB KARNA CHAHIYE?
Subah 6-8 baje {raw} ka best time hai - Kyunki dimag fresh hota hai. Week me Monday aur Thursday ko {raw} par zyada focus karo. Mere experience se jo log subah {raw} karte hain wo 2x tezi se seekhte hain.

5. KAUN KAR SAKTA HAI?
Student, Housewife, Job wala, Business wala - Koi bhi kar sakta hai - Age 16 se 60 tak - Meri sabse badi student 58 saal ki Shanti ji hain - Unhone {raw} seekh ke apna YouTube channel banaya.

6. KAISE KAAM KARTA HAI? - Andar ka mechanism
Bachchon, {raw} ka andar ka mechanism samjho - Step 1: Socho ki aapko kya chahiye, Step 2: Tool kholo, Step 3: Pehla step karo, Step 4: Result dekho, Step 5: Galti sudharo. Jaise khana banana - Pehle socho kya banana hai, Phir saman nikalo, Phir banao, Phir taste karo, Phir namak kam zyada karo.

7. KISSE HOGA? - Kaunse tools se?
Free tools: Tool 1 - Canva free, Tool 2 - CapCut free, Tool 3 - ChatGPT free, Tool 4 - Google free, Tool 5 - Notion free. Paid tools: Tool 1 - 10$ per month - Jab 1 lakh kamane lago tab lena.

8. KYA USE HAI? - Paise kaise kamayenge?
3 tarike: Tarika 1 - Freelancing - {raw} se aap Fiverr pe 20k-50k per month kama sakte ho, Tarika 2 - Apna business - {raw} se apna {topic} ka business 1 lakh+ per month, Tarika 3 - Job - {raw} aata hai toh 30k-80k ki job mil jayegi.

9. KAISE USE KARNA HAI? - Practical mobile se laptop se
Mobile se: Step 1 - Instagram app kholo, Step 2 - Plus button dabao, Step 3 - Reels select karo, Step 4 - {raw} wala option dekho. Laptop se: Step 1 - Browser me jao, Step 2 - {topic} website kholo, Step 3 - Dashboard me {raw} dekho. Ek ek button main aapko dikhaunga.

10. KAISE KARNA CHAHIYE? - Sahi tarika vs Galat tarika
Sahi tarika: Roz 30 min {raw} ka practice, Ek diary me likho kya seekha, Hafte me ek baar revise karo. Galat tarika: Ek din 5 ghante karo phir 10 din kuch nahi - Aise nahi hota. Pro log kaise karte hain? Pro log {raw} ko roz subah 6 baje karte hain - Bina miss kiye.

REAL KAHANI 2026 - MERE STUDENT KI:
Mere student Rahul - Gaon se hai - Usne {raw} ko 2 mahine tak roz 1 ghanta diya. Pehle usko kuch samajh nahi aaya. Phir usne meri ye book wali technique follow ki - Har din ek chhota sa project {raw} par banaya. Teesre mahine me usne {raw} se apna pehla client liya - 15k ka. Chauthe mahine me 5 clients - 75k. Aaj wo 2 lakh per month kama raha hai {topic} se - Sirf {raw} ko sahi se seekh ke.

COMMON MISTAKES - 90% LOG YAHI KARTE HAIN:
Galti 1: {raw} ko bina samjhe direct advanced karna - Pehle basic samjho.
Galti 2: Roz practice nahi karna - Ek din karke bhool jana.
Galti 3: Sirf video dekhna, practical nahi karna - Dekhne se nahi, karne se aata hai.
Galti 4: Paise ke peeche bhagna, learning pe focus nahi karna - Pehle seekho, paise apne aap ayenge.

PRO TIP - YE KOI NAHI BATATA - SIRF MAIN BATA RAHA HOON:
Bachchon, ek secret bataoon - Ek chhoti si diary rakho - Usme roz likho: Aaj {raw} me kya seekha, Kya galti hui, Kal kya karna hai. Aur roz raat ko sone se pehle 10 min us diary ko padho. Ye trick mere sabse successful students use karte hain - Koi YouTube pe nahi batata - Main bata raha hoon kyonki main teacher hoon.

Aaj ka HOMEWORK - ASSIGNMENT {lc}:
Aaj ka kaam: {raw} par ek chhota sa real project banao. Jaise: {topic} me {raw} ka use karke ek Instagram Reel, ya ek YouTube Short, ya ek client ke liye ek kaam banao. Kal tak mujhe bhejo - Main check karunga. Ye karoge to hi {topic} me expert banoge - Nahi toh sirf dekhne wale ban ke reh jaoge.

KAL KYA SEEKHENGE?
Kal hum seekhenge Agla Topic - {raw} ke baad kya aata hai - Kaise usko use karke aur paise kamaye.

SUMMARY - AAJ KYA SEEKHA?
Aaj humne {raw} seekha - Kya hai, Kyon hai, Kahan hai, Kab hai, Kaun kar sakta hai, Kaise kaam karta hai, Kisse hoga, Kya use hai, Kaise use karna hai, Kaise karna chahiye, Real kahani, Galtiyan, Pro tip, Homework. Ab aap {raw} ke expert ho gaye ho - Agla lesson kal.

Teacher ka pranam - Kal milte hain.
"""

            en = f"""HELLO STUDENTS - TODAY TOPIC: {raw}

I am your teacher - 20 years teaching {topic} - Today we learn {raw} like a book - Like teacher teaches on blackboard.

1. WHAT IS {raw}? Simple meaning of {raw} in {topic}. Like teaching a child. Example: Rohit and Priya learned {raw} first day and now earn 1 lakh per month.

2. WHY IS IT? Why important? Without {raw} you will fail in {topic} - 90% fail because they take {raw} lightly. Market data 2026: Demand of {raw} grew 300%.

3. WHERE IS IT? Where used? Instagram, YouTube, Business, Freelancing, Job.

4. WHEN? Best time morning 6-8 am - Mind fresh. Monday and Thursday focus more on {raw}.

5. WHO CAN DO? Student, Housewife, Job, Business - Age 16 to 60.

6. HOW WORKS? Mechanism: Step 1 Think what you need, Step 2 Open tool, Step 3 Do first step, Step 4 See result, Step 5 Fix mistake. Like cooking.

7. WITH WHOM? Which tools? 5 free tools: Canva free, CapCut free, ChatGPT free, Google free, Notion free.

8. WHAT IS USE? How to earn? 3 ways: Freelancing 20k-50k, Own business 1L+, Job 30k-80k.

9. HOW TO USE? Practical mobile and laptop - Step by step each button.

10. HOW SHOULD DO? Right way: Daily 30 min practice, Write diary what learned, Weekly revise. Wrong way: 5 hours one day then 10 days nothing.

REAL STORY 2026: My student Rahul from village - Gave 1 hour daily to {raw} for 2 months. First month no understanding. Then followed my book technique - Daily small project on {raw}. Third month first client 15k. Fourth month 5 clients 75k. Today 2 lakh per month from {topic} - Only by learning {raw} correctly.

MISTAKES 90% DO: Mistake 1 Direct advanced without basics, Mistake 2 No daily practice, Mistake 3 Only watching videos no practical, Mistake 4 Running behind money not learning.

PRO TIP - NOBODY TELLS - ONLY I AM TELLING: Keep small diary - Write daily: What learned in {raw}, What mistake, What to do tomorrow. Read 10 min before sleeping. Trick my most successful students use - Nobody tells on YouTube - I am telling because I am teacher.

HOMEWORK ASSIGNMENT {lc}: Build small real project today on {raw}. Like: Use {raw} in {topic} to make Instagram Reel or YouTube Short or work for client. Send me tomorrow - I will check. Only if you do this you will become expert in {topic}.

SUMMARY: Today we learned {raw} - What, Why, Where, When, Who, How, With Whom, Use, How to use, How should do, Real story, Mistakes, Pro tip, Homework. Now you are expert in {raw}.

Teacher pranam - See tomorrow.
"""

            vids.append({"no": lc, "title": title, "desc_hi": hi, "desc_en": en})
            lc += 1
        curriculum.append({"title": f"Module {mod_idx+1}: {topic} - {module_themes[mod_idx]} - Book", "videos": vids})
    return curriculum

def create_teacher_book_ppt(course_id, course_topic):
    if not PPTX_OK:
        return None, "python-pptx missing"
    try:
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        curriculum = get_teacher_book_curriculum(course_topic)

        slide = prs.slides.add_slide(prs.slide_layouts[6])
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(2))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.text = course_topic + "\nMaster Teacher Book - 400 Lessons - Har Sawal Ka Jawab - Real Teacher Jaise"
        p = tf.paragraphs[0]
        p.runs[0].font.size = Pt(22)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(37, 99, 235)

        count = 0
        for mod in curriculum:
            slide = prs.slides.add_slide(prs.slide_layouts[6])
            txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12.3), Inches(1.2))
            tf = txBox.text_frame
            tf.word_wrap = True
            tf.text = mod["title"] + " - 40 Lessons - Teacher Book"
            p = tf.paragraphs[0]
            p.runs[0].font.size = Pt(16)
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(37, 99, 235)
            count += 1
            for vid in mod["videos"]:
                if count >= 62:
                    break
                slide = prs.slides.add_slide(prs.slide_layouts[6])

                txBox = slide.shapes.add_textbox(Inches(0.2), Inches(0.1), Inches(12.9), Inches(0.7))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = vid["title"][:220]
                p = tf.paragraphs[0]
                p.runs[0].font.size = Pt(11)
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(37, 99, 235)

                txBox = slide.shapes.add_textbox(Inches(0.2), Inches(0.9), Inches(6.3), Inches(6.2))
                tf = txBox.text_frame
                tf.word_wrap = True
                tf.text = vid["desc