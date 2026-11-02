import streamlit as st
import json, hashlib, datetime
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Brahma Education V94 English", layout="wide")

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH = DATA_DIR / ".master_hash"
ADMIN_SESSION = DATA_DIR / ".admin_session"
COURSES_FILE = DATA_DIR / "courses.json"
PPT_DIR = DATA_DIR / "ppts"
PPT_DIR.mkdir(exist_ok=True)
MARKETING_FILE = DATA_DIR / "marketing.json"

TOPICS_STR = "AI Agent Automation 2026|Instagram Reels Mastery|YouTube Automation AI|Prompt Engineering Pro|Digital Marketing SEO Mastery|ChatGPT Mastery 2026|Facebook Ads Mastery|Google Ads Mastery|SEO Advanced 2026|Social Media Marketing Pro|Content Writing AI|Copywriting Mastery|Blogging Mastery 2026|Affiliate Marketing Pro|Dropshipping Business|E-commerce Mastery Shopify|Canva Design Mastery|Video Editing CapCut Pro|YouTube SEO Mastery|Instagram Growth Hack|LinkedIn Marketing Pro|Twitter X Growth Mastery|TikTok Viral Mastery|Pinterest Marketing|Quora Marketing|Email Marketing Automation|WhatsApp Marketing Pro|Telegram Channel Growth|Influencer Marketing|Personal Branding Mastery|Freelancing Mastery|Agency Business Mastery|SaaS Business 2026|No-Code Business Bubble|Python Programming Mastery|JavaScript Mastery 2026|React JS Mastery|Next.js Mastery|Node.js Backend Mastery|Web Development Full Stack|WordPress Mastery|Shopify Store Design|UI UX Design Mastery|Figma Design Pro|Graphic Design Mastery|Logo Design Mastery|Thumbnail Design Viral|Video Animation Mastery|AI Image Generation Midjourney|AI Video Generation Sora|Voice Cloning ElevenLabs|Automation n8n Make|Zapier Automation Mastery|Notion Productivity Mastery|Excel Advanced Mastery|Google Sheets Automation|Data Analysis Python|Machine Learning Mastery|Deep Learning 2026|Data Science Mastery|Stock Market Trading AI|Crypto Trading Mastery|Forex Trading Pro|Real Estate Business|Motivational Speaking Mastery|Public Speaking Pro|Communication Skills Mastery|English Speaking Pro|Hindi Content Creation|Podcast Mastery|Music Production AI|Photography Mastery|Reels Editing Viral|Meme Marketing Mastery|Viral Content Formula|Lead Generation Mastery|Sales Funnel Mastery|Landing Page Design|CRO Conversion Optimization|Customer Support Automation|HR Recruitment AI|Business Plan Mastery|Startup Funding Mastery|Business Automation AI|Time Management Mastery|Mindset Mastery Millionaire|Meditation Mindfulness|Fitness Coaching Business|Diet Nutrition Business|Yoga Teaching Business|Cooking Channel Business|Travel Vlogging Business|Gaming Channel Growth|Education Channel Growth|Finance Channel Business|News Channel Automation|Meme Page Business|Affiliate Blog SEO|Amazon FBA Mastery|Etsy Store Mastery|Print on Demand Business|Stock Photography Business|Voice Over Business|Translation Business AI|Resume Writing Business|LinkedIn Profile Optimization|AI Tools Mastery 100 Tools|Chatbot Development|AI Voice Agent Mastery|AI Receptionist Business"
TOPICS = TOPICS_STR.split("|")

def load_json(p,d):
    if p.exists():
        t=p.read_text(encoding="utf-8")
        if len(t)>2:
            try: return json.loads(t)
            except: return d
    return d
def save_json(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")

class MasterTeacherAI:
    def title(self, topic, n):
        titles={
            1:"M01 WHAT IS "+topic+" - 5 Real Examples Deep Detail",
            2:"M02 WHY IMPORTANT Future Proof Market Data "+topic,
            3:"M03 WHERE USE Market Scope Clients "+topic,
            4:"M04 WHEN Best Timing Morning Evening Seasonal "+topic,
            5:"M05 WHO Eligible Student Professional Business "+topic,
            6:"M06 HOW Architecture Perceive Reason Act Loop "+topic,
            7:"M07 WITH WHAT Tools Setup Free Paid "+topic,
            8:"M08 WHAT USE Earning Model Freelancing Business "+topic,
            9:"M09 HOW TO USE Practical Mobile Laptop Hands On "+topic,
            10:"M10 HOW TO DO Right Way Daily Diary System "+topic,
            11:"M11 Fundamentals Deep Dive Core Concepts "+topic,
            12:"M12 Tools Mastery Part1 Canva CapCut Design "+topic,
            13:"M13 Tools Mastery Part2 ChatGPT Notion Make Zapier "+topic,
            14:"M14 Perceive Reason Act ReAct Chain Of Thought "+topic,
            15:"M15 RAG Memory Vector DB Pinecone Long Memory "+topic,
            16:"M16 Prompt Engineering 100 Prompts Formula "+topic,
            17:"M17 REAL STORY Rahul Village 15k First Client 2L Per Month "+topic,
            18:"M18 Case Study 1L Per Month 5 Clients Scaling "+topic,
            19:"M19 Case Study 10M ARR SaaS Story MVP Launch "+topic,
            20:"M20 MISTAKES 90 Percent Fail 5 Mistakes Solutions "+topic,
            21:"M21 PRO TIP Secret Diary Millionaire Trick Not On YouTube "+topic,
            22:"M22 Mindset Millionaire Focus Meditation Daily Habit "+topic,
            23:"M23 Time Management 30 Days Complete Calendar System "+topic,
            24:"M24 Freelancing Upwork Fiverr 7 Days First Client Proposal "+topic,
            25:"M25 Agency Business Model Team Building Client Acquisition "+topic,
            26:"M26 SaaS Business Recurring Income MVP Pricing "+topic,
            27:"M27 Client Handling Pricing Negotiation Contract Advance "+topic,
            28:"M28 Portfolio Building Behance Dribbble GitHub 10 Samples "+topic,
            29:"M29 Lead Generation LinkedIn Instagram YouTube Cold Email "+topic,
            30:"M30 Sales Funnel Landing Page CRO AB Testing "+topic,
            31:"M31 SEO Search Engine Optimizing Keyword Blog Content "+topic,
            32:"M32 Social Media Marketing Reels Shorts LinkedIn Growth "+topic,
            33:"M33 Content Creation Reels Viral Formula Hook Story CTA "+topic,
            34:"M34 Email WhatsApp Marketing Sequences Automation "+topic,
            35:"M35 Automation n8n Make Zapier 80 Percent Auto Save Time "+topic,
            36:"M36 Advanced Strategies Pro Tricks Competition Beat "+topic,
            37:"M37 Optimization Scaling 1L To 10L Team Ads Systems "+topic,
            38:"M38 Business Plan 1Cr Startup Funding Pitch Deck Investor "+topic,
            39:"M39 Homework Assignments Project Research Test Submission "+topic,
            40:"M40 FINAL PROJECT Certification Business Level Real Income Portfolio "+topic
        }
        return titles.get(n, "Module "+str(n)+" "+topic)

    def content(self, topic, n):
        base = topic+" Module "+str(n)+" "
        parts=[]
        parts.append(base+"WHAT IS definition with 5 real examples business automation 80 percent time save client project Upwork 15k first client freelancing Fiverr gig 20k to 50k agency model team 2L plus SaaS recurring income scope 2026 300 percent growth Google Trends proof roadmap 30 days foundation strong earning first month 15k deep detail English only. ")
        parts.append(base+"WHY IMPORTANT future proof market data 2026 demand high salary 3x AI era future proof job safe freelancing high demand business. 90 percent fail reasons foundation skip no practice no diary no mentor. Village proof Rahul 15k to 2L future value 10x learn now expert 2027. ")
        parts.append(base+"WHERE USE Instagram Reels YouTube Shorts business automation job promotion freelancing agency startup. Clients Upwork Fiverr LinkedIn Instagram DM Facebook groups AngelList India global market village mobile real