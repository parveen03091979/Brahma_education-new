import streamlit as st, json, hashlib, datetime, urllib.parse
from pathlib import Path
DATA_DIR=Path('data')
DATA_DIR.mkdir(exist_ok=True)
MH=DATA_DIR/'.master_hash'
AS=DATA_DIR/'.admin_session'
CF=DATA_DIR/'courses.json'
PD=DATA_DIR/'ppts'
PD.mkdir(exist_ok=True)
MF=DATA_DIR/'marketing.json'
PF=DATA_DIR/'purchases.json'
AF=DATA_DIR/'api_keys.json'
UQ=DATA_DIR/'upi_qr.jpg'
UID='parveen39179@okicici'
NM='Parveen Kumar'
TOPICS=['AI Agent Automation','Instagram Reels Mastery','YouTube Automation','Prompt Engineering','Digital Marketing SEO','ChatGPT Mastery','Facebook Ads','Google Ads','SEO Advanced','Social Media Marketing','Content Writing AI','Copywriting Mastery','Blogging Mastery','Affiliate Marketing','Dropshipping','E-commerce Shopify','Canva Design','Video Editing CapCut','YouTube SEO','Instagram Growth','LinkedIn Marketing','Twitter X Growth','TikTok Viral','Pinterest Marketing','Quora Marketing','Email Marketing Automation','WhatsApp Marketing','Telegram Growth','Influencer Marketing','Personal Branding','Freelancing Mastery','Agency Business','SaaS Business','No-Code Bubble','Python Mastery','JavaScript Mastery','React JS','Next.js','Node.js','Web Development Full Stack','WordPress Mastery','Shopify Store Design','UI UX Design','Figma Design','Graphic Design','Logo Design','Thumbnail Design Viral','Video Animation','AI Image Midjourney','AI Video Sora','Voice Cloning ElevenLabs','Automation n8n Make','Zapier Automation','Notion Productivity','Excel Advanced','Google Sheets Automation','Data Analysis Python','Machine Learning','Deep Learning','Data Science','Stock Trading AI','Crypto Trading','Forex Trading','Real Estate Business','Motivational Speaking','Public Speaking','Communication Skills','English Speaking','Podcast Mastery','Music Production AI','Photography Mastery','Reels Editing Viral','Meme Marketing','Viral Content Formula','Lead Generation','Sales Funnel','Landing Page Design','CRO Optimization','Customer Support Automation','HR Recruitment AI','Business Plan Mastery','Startup Funding','Business Automation AI','Time Management','Mindset Millionaire','Meditation Mindfulness','Fitness Coaching Business','Diet Nutrition Business','Yoga Teaching Business','Cooking Channel Business','Travel Vlogging Business','Gaming Channel Growth','Education Channel Growth','Finance Channel Business','News Channel Automation','Meme Page Business','Affiliate Blog SEO','Amazon FBA Mastery','Etsy Store Mastery','Print on Demand Business','Stock Photography Business','Voice Over Business','Translation Business AI','Resume Writing Business','LinkedIn Profile Optimization','AI Tools Mastery','Chatbot Development','AI Voice Agent','AI Receptionist Business']

def load(p,d):
    try:
        if p.exists():
            t=p.read_text(encoding='utf-8')
            if len(t)>2:
                return json.loads(t)
    except:
        pass
    return d
def save