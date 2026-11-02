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
UPI_QR_PATH = DATA_DIR / 'upi_qr.jpg'
PPT_DIR = DATA_DIR / 'ppts'
PPT_DIR.mkdir(exist_ok=True)

TOPICS = []
TOPICS.append('AI Agent Automation 2026')
TOPICS.append('Instagram Reels Mastery')
TOPICS.append('YouTube Automation AI')
TOPICS.append('Prompt Engineering Pro')
TOPICS.append('Digital Marketing SEO Mastery')
TOPICS.append('ChatGPT Mastery 2026')
TOPICS.append('Facebook Ads Mastery')
TOPICS.append('Google Ads Mastery')
TOPICS.append('SEO Advanced 2026')
TOPICS.append('Social Media Marketing Pro')
TOPICS.append('Content Writing AI')
TOPICS.append('Copywriting Mastery')
TOPICS.append('Blogging Mastery 2026')
TOPICS.append('Affiliate Marketing Pro')
TOPICS.append('Dropshipping Business')
TOPICS.append('E-commerce Mastery Shopify')
TOPICS.append('Canva Design Mastery')
TOPICS.append('Video Editing CapCut Pro')
TOPICS.append('YouTube SEO Mastery')
TOPICS.append('Instagram Growth Hack')
TOPICS.append('LinkedIn Marketing Pro')
TOPICS.append('Twitter X Growth Mastery')
TOPICS.append('TikTok Viral Mastery')
TOPICS.append('Pinterest Marketing')
TOPICS.append('Quora Marketing')
TOPICS.append('Email Marketing Automation')
TOPICS.append('WhatsApp Marketing Pro')
TOPICS.append('Telegram Channel Growth')
TOPICS.append('Influencer Marketing')
TOPICS.append('Personal Branding Mastery')
TOPICS.append('Freelancing Mastery')
TOPICS.append('Agency Business Mastery')
TOPICS.append('SaaS Business 2026')
TOPICS.append('No-Code Business Bubble')
TOPICS.append('Python Programming Mastery')
TOPICS.append('JavaScript Mastery 2026')
TOPICS.append('React JS Mastery')
TOPICS.append('Next.js Mastery')
TOPICS.append('Node.js Backend Mastery')
TOPICS.append('Web Development Full Stack')
TOPICS.append('WordPress Mastery')
TOPICS.append('Shopify Store Design')
TOPICS.append('UI UX Design Mastery')
TOPICS.append('Figma Design Pro')
TOPICS.append('Graphic Design Mastery')
TOPICS.append('Logo Design Mastery')
TOPICS.append('Thumbnail Design Viral')
TOPICS.append('Video Animation Mastery')
TOPICS.append('AI Image Generation Midjourney')
TOPICS.append('AI Video Generation Sora')
TOPICS.append('Voice Cloning ElevenLabs')
TOPICS.append('Automation n8n Make')
TOPICS.append('Zapier Automation Mastery')
TOPICS.append('Notion Productivity Mastery')
TOPICS.append('Excel Advanced Mastery')
TOPICS.append('Google Sheets Automation')
TOPICS.append('Data Analysis Python')
TOPICS.append('Machine Learning Mastery')
TOPICS.append