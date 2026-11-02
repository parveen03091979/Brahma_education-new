import streamlit as st
import json, hashlib, datetime
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Brahma Education V92 Deep Detail", layout="wide")

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
        t={
            1:"M01 KYA HAI What Is "+topic+" - 5 Examples Deep Detail",
            2:"M02 KYON HAI Why Important Future Proof Market Data "+topic,
            3:"M03 KAHAN HAI Where Use Market Scope Clients "+topic,
            4:"M04 KAB Best Timing Morning Evening Seasonal Scaling "+topic,
            5:"M05 KAUN Who Eligible Student Housewife Job Business "+topic,
            6:"M06 KAISE Architecture Perceive Reason Act Loop "+topic,
            7:"M07 KISSE Tools Setup Free Paid Canva CapCut ChatGPT "+topic,
            8:"M08 KYA USE Earning Model Freelancing 20k-50k Business 1L "+topic,
            9:"M09 KAISE USE Practical Mobile Laptop Hands On "+topic,
            10:"M10 KAISE KARNA Right Way Daily 30 Min Diary Weekly Revise "+topic,
            11:"M11 Fundamentals Deep Dive Core Concepts "+topic,
            12:"M12 Tools Mastery Part1 Canva CapCut Thumbnail Design "+topic,
            13:"M13 Tools Mastery Part2 ChatGPT Notion Make Zapier "+topic,
            14:"M14 Perceive Reason Act ReAct Chain Of Thought Expert "+topic,
            15:"M15 RAG Memory Vector DB Pinecone Supabase Long Memory "+topic,
            16:"M16 Prompt Engineering 100 Prompts Formula Mastery "+topic,
            17:"M17 REAL KAHANI Rahul Village 15k First Client 2L Per Month "+topic,
            18:"M18 Case Study 1L Per Month 5 Clients Pricing Scaling "+topic,
            19:"M19 Case Study 10M ARR SaaS Story MVP Product Hunt "+topic,
            20:"M20 MISTAKES 90 Percent Fail 5 Galtiyan Kaise Bache "+topic,
            21:"M21 PRO TIP Secret Diary Millionaire Trick YouTube Pe Nahi "+topic,
            22:"M22 Mindset Millionaire Focus Meditation Daily Habit "+topic,
            23:"M23 Time Management 30 Din Complete Routine Calendar "+topic,
            24:"M24 Freelancing Upwork Fiverr 7 Din Me First Client Proposal "+topic,
            25:"M25 Agency Business Model Team Building Client Acquisition "+topic,
            26:"M26 SaaS Business Recurring Income MVP Pricing Marketing "+topic,
            27:"M27 Client Handling Pricing Negotiation Contract 50 Percent Advance "+topic,
            28:"M28 Portfolio Building Behance Dribbble GitHub 10 Samples "+topic,
            29:"M29 Lead Generation LinkedIn Instagram YouTube Cold Email "+topic,
            30:"M30 Sales Funnel Landing Page CRO A/B Testing "+topic,
            31:"M31 SEO Search Engine Optimizing Keyword Research Blog "+topic,
            32:"M32 Social Media Marketing Reels Shorts LinkedIn Growth Hack "+topic,
            33:"M33 Content Creation Reels Viral Formula Hook Story CTA Thumbnail "+topic,
            34:"M34 Email WhatsApp Marketing Sequences Automation Broadcast "+topic,
            35:"M35 Automation n8n Make Zapier 80 Percent Auto Time Save "+topic,
            36:"M36 Advanced Strategies Pro Tricks Competition Beat Value "+topic,
            37:"M37 Optimization Scaling 1L Se 10L Team Hire Ads Systems "+topic,
            38:"M38 Business Plan 1Cr Startup Funding Pitch Deck Angel Investor "+topic,
            39:"M39 Homework Assignments Project Research Test Submission "+topic,
            40:"M40 FINAL PROJECT Certification Business Level Real Income Portfolio "+topic
        }
        return t.get(n, "Module "+str(n)+" "+topic)

    def content(self, topic, n):
        # Deep detail 400 shabd har page - Big font ke liye full page
        if n==1:
            return (
                topic+" KYA HAI DEEP DETAIL Master Teacher 20 Saal Experience Se Samjha Raha Hai.\n\n"
                "Definition: "+topic+" ek aisa system hai jo aapke business ka 80 percent kaam automatic karta hai. "
                "Simple language me: Jo kaam aap roz 4 ghante me karte ho wo "+topic+" 10 minute me kar dega.\n\n"
                "5 Real Examples Deep Detail:\n"
                "1. Business Automation: Ek shop owner roz 100 WhatsApp messages ka jawab deta tha 3 ghante lagte the. "+topic+" se auto reply 10 second me. Time save 80 percent. Sale 2x badhi.\n"
                "2. Client Project: Upwork pe ek client ne bola mujhe Instagram automation chahie. Rahul ne "+topic+" ka use karke 15k ka project 2 din me complete kiya. Client khush 5 star rating.\n"
                "3. Freelancing: Fiverr pe gig banaya I will automate your "+topic+". Pehle mahine 3 orders 20k, dusre mahine 8 orders 50k. Recurring income.\n"
                "4. Agency Model: 5 clients ke liye "+topic+" setup kiya har client se 25k retainer. Total 1.25L per month. Team me 2 log hire kiye. Agency ban gayi.\n"
                "5. SaaS Product: Ek tool banaya "+topic+" par based. 29 dollar per month pricing. 100 customers = 2900 dollar = 2.4L per month recurring. Har mahine aata hai.\n\n"
                "Scope 2026: Google Trends me "+topic+" 300 percent growth. Market size 50B se 500B tak ja raha hai. Abhi seekhoge to 2027 me expert banoge. Beginner to expert roadmap 30 din me. Foundation strong to building strong. First month earning 15k kaise start step by step."
            )
        if n==2:
            return (
                topic+" KYON HAI Why Important Future Proof Deep Detail Market Data Ke Saath.\n\n"
                "Market Data 2026: "+topic+" industry 2023 me 10B thi 2026 me 100B ho gayi. Demand high salary 3x. Companies "+topic+" experts dhoondh rahi hain 50000+ jobs LinkedIn pe.\n\n"
                "90 Percent Log Fail Kyon Hote Hain Deep Detail:\n"
                "Galti1: Bina samjhe advanced shuru kar dete hain foundation skip. Example: Seedha automation tool khol liya bina samjhe KYA HAI. Result fail.\n"
                "Galti2: Roz practice nahi sirf video dekhte hain practical nahi karte. 10 ghante video dekha 1 ghanta bhi practice nahi. Skill nahi banti.\n"
                "Galti3: Paise ke peeche bhagte hain learning nahi karte. Pehle din se puchte kitna kamaunga. Pehle seekho phir paisa aayega.\n"
                "Galti4: Diary nahi rakhte kya seekha bhool jate hain. Master Teacher bolta hai roz raat 10 min diary likho.\n"
                "Galti5: Mentor nahi dhundhte akele struggle karte hain. Mentor se 1 saal ka kaam 1 mahine me hota hai.\n\n"
                "Kyon Seekhna Abhi: Future proof skill AI aa raha hai job safe. Freelancing high demand global clients. Business bana sakte apna.