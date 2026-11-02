import streamlit as st
import json, hashlib, datetime
from pathlib import Path
import pandas as pd

st.set_page_config(page_title='Brahma Education V90', layout='wide')
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

def load_json(p,d):
    if p.exists():
        t=p.read_text(encoding='utf-8')
        if len(t)>2:
            try: return json.loads(t)
            except: return d
    return d
def save_json(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')

class MasterTeacherAI:
    def get_module_title(self, topic, n):
        titles={
            1:'M01 KYA HAI What Is '+topic+' - 5 Examples - Master Teacher',
            2:'M02 KYON HAI Why Important Future Proof '+topic,
            3:'M03 KAHAN HAI Where Use Market Scope '+topic,
            4:'M04 KAB Best Timing Morning Evening Seasonal '+topic,
            5:'M05 KAUN Who Eligible Student Housewife Job Business '+topic,
            6:'M06 KAISE Architecture Perceive Reason Act Loop '+topic,
            7:'M07 KISSE Tools Setup Free Paid Canva CapCut ChatGPT '+topic,
            8:'M08 KYA USE Earning Model Freelancing 20k-50k Business 1L '+topic,
            9:'M09 KAISE USE Practical Mobile Reels Laptop Hands On '+topic,
            10:'M10 KAISE KARNA Right Way Daily 30 Min Diary '+topic,
            11:'M11 Fundamentals Deep Dive Core Concepts '+topic,
            12:'M12 Tools Mastery Part1 Canva CapCut Design '+topic,
            13:'M13 Tools Mastery Part2 ChatGPT Notion Make Zapier '+topic,
            14:'M14 Perceive Reason Act ReAct Chain Of Thought '+topic,
            15:'M15 RAG Memory System Vector DB Pinecone '+topic,
            16:'M16 Prompt Engineering 100 Prompts Mastery '+topic,
            17:'M17 REAL KAHANI Rahul Village Se '+topic+' - 15k First Client',
            18:'M18 Case Study 1L Per Month 5 Clients Scaling '+topic,
            19:'M19 Case Study 10M ARR SaaS Story '+topic,
            20:'M20 MISTAKES 90 Percent Fail 5 Galtiyan '+topic,
            21:'M21 PRO TIP Secret Diary Millionaire Trick '+topic+' - YouTube Pe Nahi',
            22:'M22 Mindset Millionaire Focus Meditation '+topic,
            23:'M23 Time Management 30 Din Me Complete '+topic,
            24:'M24 Freelancing Upwork Fiverr 7 Din Me First Client '+topic,
            25:'M25 Agency Business Model Team Building '+topic,
            26:'M26 SaaS Business Model Recurring Income '+topic,
            27:'M27 Client Handling Pricing Negotiation Contract '+topic,
            28:'M28 Portfolio Building Behance Dribbble GitHub '+topic,
            29:'M29 Lead Generation LinkedIn Instagram YouTube '+topic,
            30:'M30 Sales Funnel Landing Page CRO '+topic,
            31:'M31 SEO Search Engine Optimizing Blog Keyword '+topic,
            32:'M32 Social Media Marketing Reels Shorts LinkedIn '+topic,
            33:'M33 Content Creation Reels Viral Formula Hook Story CTA '+topic,
            34:'M34 Email WhatsApp Marketing Sequences Automation '+topic,
            35:'M35 Automation n8n Make Zapier 80 Percent Auto '+topic,
            36:'M36 Advanced Strategies Pro Tricks Competition Beat '+topic,
            37:'M37 Optimization Scaling 1L Se 10L Team Ads '+topic,
            38:'M38 Business Plan 1Cr Startup Funding Pitch Deck '+topic,
            39:'M39 Homework Assignments Project Research Test '+topic,
            40:'M40 FINAL PROJECT Certification Business Level Real Income '+topic
        }
        return titles.get(n, 'Module '+str(n)+' '+topic)

    def get_module_content(self, topic, n):
        # Har module ka alag content - Ek hi matter 40 page pe nahi
        base={
            1: topic+' KYA HAI. Simple definition Master Teacher 20 saal se. Example1 Business automation se 80% time save. Example2 Client project Upwork se 15k first client. Example3 Freelancing Fiverr gig 20k-50k. Example4 Agency model team 2L plus. Example5 SaaS product recurring. Scope 2026 me 300% growth Google Trends proof. Beginner to expert roadmap 30 din. Foundation strong. First month earning kaise start. Definition 5 examples ke saath detailed.',
            2: topic+' KYON HAI Why Important Future. Market data 2026 demand high salary 3x. AI aa raha hai future proof skill. 90% fail kyon: bina samjhe advanced shuru foundation skip, roz practice nahi sirf video dekhte practical nahi, paise peeche bhagte learning nahi, diary nahi rakhte bhool jate, mentor nahi akele struggle. Kyon seekhna abhi: job safe freelancing high business banao. Proof Rahul village 15k first client. Future me iski value 10x hogi. Abhi seekhoge to 2027 me expert.',
            3: topic+' KAHAN HAI Where Use. Instagram Reels YouTube Shorts Business Automation Job Promotion Freelancing Agency Startup me use hota hai. Kahan clients milte hain: Upwork Fiverr LinkedIn Instagram DM Facebook groups AngelList. India market plus global market. Gaon se bhi mobile se kar sakte. Real places: e-commerce store, education coaching, real estate lead, health clinic, finance advisor, restaurant automation. Kahan use nahi karna common mistake. Market scope list.',
            4: topic+' KAB Best Timing. Morning 6 to 8 best learning time brain fresh. Monday Thursday best posting days engagement 40% high. Product launch best time Diwali New Year season summer. Kab scale kare business: jab 3 clients stable 1 month retainer ho. Kab pricing badhana: har 3 clients ke baad 20% increase. Seasonal timing kaise use kare festival offers. Time management daily 1 hour kaise nikalna job ke saath. Kab nahi karna mistake.',
            5: topic+' KAUN Eligible Who Can Do. Student 16 plus class 10 ke baad, Housewife ghar se, Job person evening me, Business owner apne business ke liye, 60 tak koi bhi kar sakta. Koi degree nahi chahie. Kaun nahi kar sakta: jo roz practice nahi karega sirf video dekhega, jo English se darega (Hindi me bhi kar sakte), jo paise pehle maangta hai. Har koi eligible hai agar daily 30 min de sake. Age gender location matter nahi.',
            6: topic+' KAISE Architecture. Perceive = Input samjho user kya bola, Reason = Socho kaise karna best approach, Act = Action lo tool use karo. Loop: Perceive Reason Act Observe Repeat. Example: User bola Instagram Reel banao. Perceive: topic samjha, Reason: best time hook story, Act: Canva me design ChatGPT se script. Chain Of Thought kaise use kare. ReAct pattern code example. Architecture diagram simple language.',
            7: topic+' KISSE Tools Setup. Free tools: Canva free design, CapCut free video edit, ChatGPT free content, Notion free management, Google Sheets free data. Paid tools: ElevenLabs voice 5 dollar, n8n automation self host free, Make.com 1000 ops free, Zapier 100 tasks free. Setup kaise kare step by step video jaisa likh ke. Free vs paid kab use karna. Tool stack for beginners 0 cost, pro stack 20 dollar. Installation link.',
            8: topic+' KYA USE Earning Model. Freelancing: Upwork Fiverr se 20k-50k first month, 3 months me 1L. Business: Agency model 2L plus 5 clients. SaaS: recurring 29 dollar monthly 100 customers = 3k dollar. Job: Promotion salary 40% hike. E-commerce: apna store automate. Kitna charge karna beginner 15k, intermediate 35k, expert 75k. Earning proof Rahul 15k se 2L.',
            9: topic+' KAISE USE Practical. Mobile se kaise: Reels banao InShot CapCut se, Canva mobile se design, ChatGPT app se script. Laptop se kaise: browser dashboard, automation setup. Hands on: Step1 topic choose, Step2 script ChatGPT se, Step3 design Canva, Step4 video CapCut, Step5 post scheduling. Practical demo daily 30 min. Bina laptop ke bhi mobile se 100% kar sakte.',
            10: topic+' KAISE KARNA Right Way. Daily 30 min diary: 15 min learning 15 min practical. Weekly revise Sunday ko. Best practice: Roz 1 project, Roz 10 min diary. Kaise nahi karna: Sirf video dekh ke chhod dena, ek din me 5 ghante phir 5 din kuch nahi. Right way: Consistency. 30 din challenge. Kaise motivation banaye. Common mistake se kaise bache. Master Teacher ka right way.',
        }
        if n in base: return base[n]
        if n==11: return topic+' Fundamentals Deep Dive. Core concepts jo 90% YouTubers skip kar dete hain. Deep definition, working principle, history, types, sub-types, real world use. Example: '+topic+' ke 3 core pillars. Har pillar ka deep explanation 5 examples ke saath. Fundamentals strong to advanced easy. 20 years teaching ka nichod. Foundation strong to building strong.'
        if n==12: return topic+' Tools Mastery Part1 Design. Canva me kaise pro design banate hain, CapCut me kaise viral video edit, Thumbnail kaise viral banaye, Hook kaise lagaye. Step by step Canva tutorial: template choose, font color, element. CapCut tutorial: cut, transition, text animation, auto caption. Design mastery practical.'
        if n==13: return topic+' Tools Mastery Part2 AI Automation. ChatGPT se kaise best prompts likhe, Notion me kaise project manage, Make.com se kaise automation banaye, Zapier se kaise 100 apps connect. ChatGPT prompt formula: Role+Task+Context+Example. Notion database kaise banaye client tracking. Make scenario kaise banaye Instagram auto post. Practical tool mastery.'
        if n==14: return topic+' Perceive Reason Act ReAct. Expert kaise sochta hai Chain Of Thought. Example: Client bola mujhe leads chahie. Perceive: client ko kya chahie samjha, Reason: kaunsa channel best hai, Act: landing page banao ads chalao. ReAct loop kaise kaam karta hai code ke saath. Simple language me ReAct samjho.'
        if n==15: return topic+' RAG Memory System. Vector DB Pinecone Supabase kaise use karte hain memory ke liye. Short term memory: conversation history. Long term memory: Vector DB me store. Example: Client ka data yaad rakhna, purani chat se seekhna. RAG kaise banate hain: Document upload, chunk, embed, store, retrieve. Practical RAG setup.'
        if n==16: return topic+' Prompt Engineering 100 Prompts. Best prompts jo Master Teacher 20 saal me banaye. Prompt formula: Act as [role], Task [task], Context [context], Example [example], Format [format]. 10 best prompts: Content, Reel script, Ad copy, Email, SEO blog, Client proposal, Pricing, Portfolio, Lead gen, Sales. Har prompt ka use kaise karna.'
        if n==17: return 'Real Kahani Rahul Village Se '+topic+'. Rahul gaon se tha, phone purana, internet slow, 2 mahine roz 1 ghanta project kiya Master Teacher roadmap se. Teesre mahine Upwork se 15k first client AI Agent project. Chauthe mahine 5 clients 75k. Aaj 2 lakh per month. Kaise kiya: daily diary, 30 min practice, 1 project roz, PRO TIP secret diary. Tum bhi kar sakte ho same roadmap. Real story motivation proof.'
        if n==18: return 'Case Study 1L Per Month '+topic+'. 5 clients kaise laaye: LinkedIn se 2 cold message se, Instagram DM se 2 reels se, Upwork se 1 proposal se. Pricing: 15k se start 25k second month 35k third. Portfolio: 3 sample projects Canva behance pe. Lead gen: daily 10 DM 5 LinkedIn connection. Scaling 1L tak retainer model 20k per client 5 clients = 1L. Real numbers income proof blueprint.'
        if n==19: return 'Case Study 10M ARR SaaS Story '+topic+'. Kaise SaaS banaya 10M annual recurring revenue. Idea validation: 10 customers interview. MVP building 30 din me Bubble No-code. Launch Product Hunt #1. Pricing 29 dollar monthly. Team building 5 log: dev, design, marketing. Funding kaise liya pitch deck. Startup journey real. 1Cr business roadmap. SaaS model recurring income har mahine aata hai.'
        if n==20: return topic+' MISTAKES 90 Percent Fail. Galti1 bina samjhe advanced shuru foundation skip kar dete. Galti2 roz practice nahi sirf video dekhte practical nahi. Galti3 paise ke peeche bhagte learning nahi karte. Galti4 diary nahi rakhte kya seekha bhool jate. Galti5 mentor nahi dhundhte akele struggle karte. Galti6 ek din me 5 ghante phir 5 din kuch nahi. Kaise bache Master Teacher roadmap follow karo daily 30 min.'
        if n==21: return 'PRO TIP Secret Diary '+topic+' Millionaire Trick. Roz raat 10 min diary likho: Aaj kya seekha, kya galti hui, kal kya karna hai, ek naya idea. Ye trick successful students use karte hain koi YouTube pe nahi batata. Millionaire mindset kaise bane: focus, meditation 5 min, time management, no distraction. Secret diary 30 din me expert banoge. Master Teacher 20 saal se yehi batata hai jo koi nahi batata.'
        if n==22: return topic+' Mindset Millionaire. Kaise sochte hain millionaires: abundance mindset vs scarcity. Daily habit: 5am uthna, exercise, learning, diary. Kaise failure ko handle kare: fail = learning. Kaise confidence banaye: small wins. Kaise focus banaye: phone off 1 hour deep work. Mindset hi 80% success hai skill 20%. Millionaire mindset practical exercise.'
        if n==23: return topic+' Time Management 30 Din Me Complete. Daily routine: Morning 30 min learning, evening 30 min practical. Job ke saath kaise time nikale: lunch break 15 min, travel time 15 min, raat 30 min. Weekend pe 2 hour extra. 30 din calendar: Day1-5 fundamentals, Day6-10 tools, Day11-20 practical, Day21-30 client projects. Time management sheet. 30 din me complete kaise kare.'
        if n==24: return topic+' Freelancing Upwork Fiverr 7 Din Me First Client. Upwork profile kaise banaye: title, overview, portfolio, skills, hourly rate 15 dollar. Gig kaise banaye: Fiverr pe 3 gigs: basic standard premium. Proposal kaise likhe: client ka naam, uski problem samjho, solution batao, proof dikhao. 7 din me first client: Day1-2 profile, Day3-5 proposal 10 roz, Day6-7 interview. Pricing kaise badhana.'
        if n==25: return topic+' Agency Business Model Team Building. Akela freelancing se agency kaise bane: Pehle 3 clients khud handle, phir 1 intern hire, phir 2-3 team. Client acquisition: LinkedIn, Instagram, referral, cold email. Team kaise manage: Notion, Slack, daily standup. Pricing agency: 25k per client retainer, 10 clients = 2.5L per month. Agency scaling roadmap.'
        if n==26: return topic+' SaaS Business Model Recurring Income. Kaise SaaS idea dhoondhe: Apni problem se. MVP kaise banaye: No-code Bubble Softr. Pricing: 19, 49, 99 dollar tiers. Marketing: Product Hunt, AppSumo, LinkedIn. Recurring income kaise aata hai har mahine. Churn kaise kam kare. SaaS metrics: MRR, ARR, Churn. SaaS business plan 1Cr tak.'
        if n==27: return topic+' Client Handling Pricing Negotiation Contract. Client se kaise baat kare: Discovery call me kya puchna, uski problem samjho. Pricing: beginner 15k, intermediate 35k, expert 75k. Kaise charge badhana: har 3 clients ke baad 20% increase. Negotiation: client bola mehenga hai to kya bolo value dikhao. Contract me kya likhna: scope, timeline, payment 50% advance, revision. Client handling pro tips.'
        if n==28: return topic+' Portfolio Building Behance Dribbble GitHub. Portfolio kaise banaye bina client ke: 3 fake projects apne liye banao. Behance pe kaise upload: title, description, tools, result. Dribbble pe shots. GitHub pe code. Portfolio me kya dikhana: before after, result numbers. 10 samples kaise banao 10 din me roz 1. Portfolio se client kaise impress hota hai proof.'
        if n==29: return topic+' Lead Generation LinkedIn Instagram YouTube. Organic lead: LinkedIn pe daily 1 post value, 10 connection, 5 DM. Instagram pe daily 1 reel, story poll, DM. YouTube pe weekly 1 video SEO. Paid lead: Facebook ads 200 per day, Google ads. Cold email: 100 emails daily kaise bheje tools se. Lead gen funnel kaise banaye. Daily 10 leads kaise laaye.'
        if n==30: return topic+' Sales Funnel Landing Page CRO. Funnel kya hai: Awareness, Interest, Desire, Action. Landing page kaise banaye high converting: headline, sub-headline, benefits, testimonials, CTA, form. CRO kya hai Conversion Rate Optimization: A/B testing, headline test, CTA color test. Funnel example: Reel -> Landing page -> WhatsApp -> Sale. Sales funnel practical.'
        if n==31: return topic+' SEO Search Engine Optimizing Blog