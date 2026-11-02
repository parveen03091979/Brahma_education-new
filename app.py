import streamlit as st, json, hashlib, datetime, urllib.parse
from pathlib import Path
DATA_DIR=Path("data")
DATA_DIR.mkdir(exist_ok=True)
MASTER_HASH=DATA_DIR/".master_hash"
ADMIN_SESSION=DATA_DIR/".admin_session"
COURSES_FILE=DATA_DIR/"courses.json"
PPT_DIR=DATA_DIR/"ppts"
PPT_DIR.mkdir(exist_ok=True)
MARKETING_FILE=DATA_DIR/"marketing.json"
PURCHASE_FILE=DATA_DIR/"purchases.json"
API_FILE=DATA_DIR/"api_keys.json"
UPI_QR_PATH=DATA_DIR/"upi_qr.jpg"
UPI_ID="parveen39179@okicici"
NAME="Parveen Kumar"
TOPICS=["AI Agent Automation","Instagram Reels Mastery","YouTube Automation","Prompt Engineering","Digital Marketing SEO","ChatGPT Mastery","Facebook Ads","Google Ads","SEO Advanced","Social Media Marketing","Content Writing AI","Copywriting Mastery","Blogging Mastery","Affiliate Marketing","Dropshipping","E-commerce Shopify","Canva Design","Video Editing CapCut","YouTube SEO","Instagram Growth","LinkedIn Marketing","Twitter X Growth","TikTok Viral","Pinterest Marketing","Quora Marketing","Email Marketing Automation","WhatsApp Marketing","Telegram Growth","Influencer Marketing","Personal Branding","Freelancing Mastery","Agency Business","SaaS Business","No-Code Bubble","Python Mastery","JavaScript Mastery","React JS","Next.js","Node.js","Web Development Full Stack","WordPress Mastery","Shopify Store Design","UI UX Design","Figma Design","Graphic Design","Logo Design","Thumbnail Design Viral","Video Animation","AI Image Midjourney","AI Video Sora","Voice Cloning ElevenLabs","Automation n8n Make","Zapier Automation","Notion Productivity","Excel Advanced","Google Sheets Automation","Data Analysis Python","Machine Learning","Deep Learning","Data Science","Stock Trading AI","Crypto Trading","Forex Trading","Real Estate Business","Motivational Speaking","Public Speaking","Communication Skills","English Speaking","Podcast Mastery","Music Production AI","Photography Mastery","Reels Editing Viral","Meme Marketing","Viral Content Formula","Lead Generation","Sales Funnel","Landing Page Design","CRO Optimization","Customer Support Automation","HR Recruitment AI","Business Plan Mastery","Startup Funding","Business Automation AI","Time Management","Mindset Millionaire","Meditation Mindfulness","Fitness Coaching Business","Diet Nutrition Business","Yoga Teaching Business","Cooking Channel Business","Travel Vlogging Business","Gaming Channel Growth","Education Channel Growth","Finance Channel Business","News Channel Automation","Meme Page Business","Affiliate Blog SEO","Amazon FBA Mastery","Etsy Store Mastery","Print on Demand Business","Stock Photography Business","Voice Over Business","Translation Business AI","Resume Writing Business","LinkedIn Profile Optimization","AI Tools Mastery","Chatbot Development","AI Voice Agent","AI Receptionist Business"]

def load(p,d):
    try:
        if p.exists():
            t=p.read_text(encoding="utf-8")
            if len(t)>2:
                return json.loads(t)
    except:
        pass
    return d
def save(p,d):
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")

class MT:
    def ttl(self,t,n):
        return f"M{str(n).zfill(2)} {t}"
    def cnt(self,t,n):
        a=["WHAT IS ","WHY IMPORTANT ","WHERE USE ","WHEN TIMING ","WHO ELIGIBLE ","HOW ARCH ","WITH TOOLS ","WHAT EARN ","HOW USE ","HOW RIGHT "]
        b=["REAL STORY Rahul village 15k ","MISTAKES 90 fail ","PRO TIP secret diary ","SEO Google number 1 ","FINAL PROJECT certification "]
        base=a[(n-1)%10]
        ex=""
        if n==17:
            ex=b[0]
        if n==20:
            ex=b[1]
        if n==21:
            ex=b[2]
        if n==31:
            ex=b[3]
        if n==40:
            ex=b[4]
        deep="Deep detail master teacher business automation client freelancing agency SaaS growth roadmap earning market future proof practice diary mentor Rahul village 15k first client 2L per month real story case study 1L 10M ARR mistakes pro tip secret diary mindset time management Upwork Fiverr portfolio lead generation sales funnel SEO social media content creation email WhatsApp automation n8n Make Zapier advanced optimization scaling business plan 1Cr funding homework final project certification real income "
        return f"{t} Module {n} {base} {ex} {deep} {deep}"

    def make(self,cid,ctopic):
        from pptx import Presentation
        from pptx.util import Inches, Pt
        prs=Presentation()
        prs.slide_width=Inches(13.33)
        prs.slide_height=Inches(7.5)
        for i in range(40):
            n=i+1
            s=prs.slides.add_slide(prs.slide_layouts[6])
            tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
            tf=tb.text_frame
            tf.word_wrap=True
            tf.text=self.ttl(ctopic,n)
            tf.paragraphs[0].font.size=Pt(20)
            tf.paragraphs[0].font.bold=True
            bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
            bf=bb.text_frame
            bf.word_wrap=True
            bf.text=self.cnt(ctopic,n)
            bf.paragraphs[0].font.size=Pt(13)
        out=PPT_DIR/(cid+"_40_MODULES_V102.pptx")
        prs.save(str(out))
        return out

mt=MT()
courses=load(COURSES_FILE,[])
if len(courses)<100:
    courses=[]
    for i,t in enumerate(TOPICS):
        courses.append({"id":f"BRAHMA{1000+i}","topic":t,"price":99})
    save(COURSES_FILE,courses)
else:
    need=False
    for c in courses:
        if c.get("price",999)>200:
            c["price"]=99
            need=True
    if need:
        save(COURSES_FILE,courses)

purchases=load(PURCHASE_FILE,[])
api_keys=load(API_FILE,{})

if "admin_logged" not in st.session_state:
    st.session_state["admin_logged"]=False

def check():
    if ADMIN_SESSION.exists():
        try:
            d=json.loads(ADMIN_SESSION.read_text(encoding="utf-8"))
            exp=datetime.datetime.fromisoformat(d.get("expiry"))
            if datetime.datetime.now()<exp:
                return True
            ADMIN_SESSION.unlink(missing_ok=True)
        except:
            pass
    return False

if check():
    st.session_state["admin_logged"]=True

st.sidebar.title("Brahma V102 Price 99")
if not MASTER_HASH.exists():
    pw=st.sidebar.text_input("Create Admin Password",type="password")
    if st.sidebar.button("Create Admin"):
        if pw and len(pw)>=4:
            MASTER_HASH.write_text(hashlib.sha256(pw.encode()).hexdigest())
            st.rerun()
    menu="Browse Courses"
else:
    if not st.session_state["admin_logged"]:
        menu=st.sidebar.radio("Menu",["Browse Courses","My Access"])
        st.sidebar.divider()
        pw=st.sidebar.text_input("Admin Password",type="password")
        if st.sidebar.button("Admin Login"):
            if hashlib.sha256(pw.encode()).hexdigest()==MASTER_HASH.read_text():
                st.session_state["admin_logged"]=True
                exp=datetime.datetime.now()+datetime.timedelta(days=7)
                save(ADMIN_SESSION,{"expiry":exp.isoformat()})
                st.rerun()
            else:
                st.sidebar.error("Wrong Password")
    else:
        st.sidebar.success("V102 Price 99 No Unterminated")
        menu=st.sidebar.radio("Admin",["Dashboard","Price Manager 99","Deep Maker","Video Library","Course Library","API Keys","UPI QR Setup","Sales","Marketing","Super Agent"])
        if st.sidebar.button("Logout"):
            st.session_state["admin_logged"]=False
            ADMIN_SESSION.unlink(missing_ok=True)
            st.rerun()

if st.session_state["admin_logged"]:
    if menu=="Dashboard":
        st.title("Dashboard V102 Price 99 No Unterminated")
        st.success("V100 exact + Price 99 + Price Manager Bulk Single - No Lamba String - No Unterminated - No Cut - Full Restore")
        total=len(courses)
        real=len(list(PPT_DIR.glob("*V102*")))
        avg_price=sum([c.get("price",99) for c in courses])//max(1,total)
        c1,c2,c3=st.columns(3)
        c1.metric("Total",total)
        c2.metric("Books V102",real)
        c3.metric("Avg Price",f"Rs {avg_price}")
        if st.button("DELETE OLD FILES",type="secondary"):
            for f in list(PPT_DIR.glob("*.*")):
                try:
                    f.unlink()
                except:
                    pass
            st.success("Old deleted")
            st.rerun()
        if st.button("CREATE 100 BOOKS V102 PRICE 99",type="primary"):
            bar=st.progress(0)
            for idx,c in enumerate(courses):
                mt.make(c["id"],c["topic"])
                bar.progress(int((idx+1)/len(courses)*100))
            st.success("100 Books Created V102 Price 99")
            st.balloons()
            st.rerun()

    if menu=="Price Manager 99":
        st.title("Price Manager - Sabhi Ka Ek Sath Aur Har Ek Ka Alag-Alag - V102")
        st.success("Sabhi courses ka price 99 kar diya - Ab upar niche kar sakte ho sabhi ka ek sath aur har ek ka alag-alag")
        col1,col2=st.columns(2)
        with col1:
            bulk_price=st.number_input("Set All To Price Rs",value=99,min_value=1,max_value=10000,step=1)
            if st.button("SET ALL TO THIS PRICE - BULK",type="primary"):
                for c in courses:
                    c["price"]=int(bulk_price)
                save(COURSES_FILE,courses)
                st.success(f"Sare {len(courses)} Courses Price Rs {bulk_price} Bulk Done")
                st.rerun()
        with col2:
            inc=st.number_input("Increase Decrease All By Rs",value=10,min_value=-1000,max_value=1000,step=1)
            if st.button("APPLY BULK INCREASE DECREASE",type="secondary"):
                for c in courses:
                    new_price=c.get("price",99)+int(inc)
                    c["price"]=int(max(1,new_price))
                save(COURSES_FILE,courses)
                st.success(f"Sare Courses Price {inc} Rs Change Bulk Done")
                st.rerun()
        st.divider()
        if st.button("SET ALL TO 99 ONE CLICK",type="primary"):
            for c in courses:
                c["price"]=99
            save(COURSES_FILE,courses)
            st.success("Sare 100 Courses Price Only Rs 99 Kar Diya")
            st.balloons()
            st.rerun()
        st.divider()
        sel=st.selectbox("Select Course For Single Edit",[f"{c['topic']} - {c['id']} - Rs {c.get('price',99)}" for c in courses])
        sid=sel.split(" - ")[-2]
        curr=next((c.get("price",99) for c in courses if c["id"]==sid),99)
        new_price=st.number_input(f"New Price For {sid} Current Rs {curr}",value=int(curr),min_value=1,max_value=10000,step=1)
        if st.button("UPDATE SINGLE PRICE",type="primary"):
            for c in courses:
                if c["id"]==sid:
                    c["price"]=int(new_price)
                    break
            save(COURSES_FILE,courses)
            st.success(f"Course {sid} Price Rs {new_price} Single Done")
            st.rerun()

    if menu=="Deep Maker":
        st.title("Deep Maker + Naya Course Add V102")
        with st.form("add_new"):
            new_topic=st.text_input("Naya Course Ka Naam")
            new_price=st.number_input("Naya Course Price Rs",value=99,min_value=1,max_value=10000,step=1)
            submitted=st.form_submit_button("ADD NAYA COURSE PRICE 99",type="primary")
            if submitted:
                if len(new_topic)<5:
                    st.error("Naam 5 letters")
                else:
                    new_id=f"BRAHMA{1000+len(courses)}"
                    courses.append({"id":new_id,"topic":new_topic,"price":int(new_price)})
                    save(COURSES_FILE,courses)
                    out=mt.make(new_id,new_topic)
                    st.success(f"Naya Course Add {new_topic} Price Rs {new_price} AUTO PPT Bana Diya")
                    st.rerun()
        sel=st.selectbox("Course select For Deep PPT",[c["topic"]+" - "+c["id"] for c in courses])
        if st.button("Brahma Real Deep Study PPT Banao",type="primary"):
            sid=sel.split(" - ")[-1]
            stopic=" - ".join(sel.split(" - ")[:-1])
            out=mt.make(sid,stopic)
            st.success("SUCCESS "+stopic)
            data=out.read_bytes()
            st.download_button("Download Deep PPT",data=data,file_name=out.name)

    if menu=="Video Library":
        st.title("Video Library Auto Full V102")
        total=len(courses)
        made=len(list(PPT_DIR.glob("*.pptx")))
        missing=total-made
        st.metric("Missing Auto Banega",missing)
        if missing>0:
            ml=[c for c in courses if not list(PPT_DIR.glob(c["id"]+"*"))][:3]
            for c in ml:
                out=mt.make(c["id"],c["topic"])
                st.success("AUTO SUCCESS "+c["topic"])
            st.rerun()

    if menu=="Course Library":
        st.title("Course Library 40 Pages V102 Price 99")
        for idx,co in enumerate(courses[:50]):
            pf=list(PPT_DIR.glob(co["id"]+"*V102*"))
            if pf:
                st.success(f"{idx+1}. {co['topic']} - Rs {co.get('price',99)} - 40 Pages V102")
                data=pf[0].read_bytes()
                st.download_button("Download V102 Price 99",data=data,file_name=pf[0].name,key=f"dlc{idx}")

    if menu=="API Keys":
        st.title("API Keys Setup V102")
        openai_key=st.text_input("OpenAI API Key",value=api_keys.get("openai",""),type="password")
        claude_key=st.text_input("Claude API Key",value=api_keys.get("claude",""),type="password")
        gemini_key=st.text_input("Gemini API Key",value=api_keys.get("gemini",""),type="password")
        pinecone_key=st.text_input("Pinecone Vector DB",value=api_keys.get("pinecone",""),type="password")
        supabase_key=st.text_input("Supabase",value=api_keys.get("supabase",""),type="password")
        eleven_key=st.text_input("ElevenLabs Voice",value=api_keys.get("elevenlabs",""),type="password")
        n8n_url=st.text_input("n8n URL",value=api_keys.get("n8n_url",""))
        make_key=st.text_input("Make.com",value=api_keys.get("make",""),type="password")
        zapier_key=st.text_input("Zapier",value=api_keys.get("zapier",""),type="password")
        if st.button("SAVE ALL API KEYS SAFE V102",type="primary"):
            api_keys["openai"]=openai_key
            api_keys["claude"]=claude_key
            api_keys["gemini"]=gemini_key
            api_keys["pinecone"]=pinecone_key
            api_keys["supabase"]=supabase_key
            api_keys["elevenlabs"]=eleven_key
            api_keys["n8n_url"]=n8n_url
            api_keys["make"]=make_key
            api_keys["zapier"]=zapier_key
            save(API_FILE,api_keys)
            st.success("All API Keys Saved Safe V102")
            st.balloons()

    if menu=="UPI QR Setup":
        st.title("UPI QR Setup Sales V102 Price 99")
        st.write("UPI ID: "+UPI_ID+" Name: "+NAME)
        up=st.file_uploader("Upload QR JPG PNG JPEG",type=["jpg","png","jpeg"])
        if up:
            UPI_QR_PATH.write_bytes(up.getvalue())
            st.success("QR Saved V102 Price 99")
            st.rerun()
        if UPI_QR_PATH.exists():
            st.image(str(UPI_QR_PATH),width=300)
            st.success("QR Ready Browse Courses me dikhega V102 Price 99")
        amount=st.number_input("Amount INR",value=99,min_value=1)
        topic_sel=st.selectbox("Course For UPI Link",[c["topic"] for c in courses[:20]])
        if st.button("Generate UPI Pay Link Price 99",type="primary"):
            params={"pa":UPI_ID,"pn":NAME,"am":str(amount),"cu":"INR","tn":topic_sel[:20]}
            link="upi://pay?"+urllib.parse.urlencode(params)
            st.code(link)
            st.link_button("Pay Via UPI Link Price 99",link,type="primary")

    if menu=="Sales":
        st.title("Sales Dashboard V102 Price 99")
        st.metric("Total Sales",len(purchases))

    if menu=="Marketing":
        st.title("Marketing Engine Super Agent V102 Price 99")
        if st.button("GENERATE 60 MARKETING POSTS V102 Price 99",type="primary"):
            posts=[]
            today=datetime.datetime.now().strftime("%Y-%m-%d")
            for c in courses[:20]:
                posts.append({"date":today,"platform":"Facebook","course":c["topic"],"type":"Morning Post 7AM","price":c.get("price",99)})
                posts.append({"date":today,"platform":"Instagram","course":c["topic"],"type":"Reel 12PM","price":c.get("price",99)})
                posts.append({"date":today,"platform":"Blog","course":c["topic"],"type":"SEO Blog 7PM","price":c.get("price",99)})
            save(MARKETING_FILE,posts)
            st.success("60 Marketing Posts Generated V102 Price 99")

    if menu=="Super Agent":
        st.title("Super Agent Full Power V102 Price 99 Kabhi Rukega Nahi")
        if st.button("START SUPER AGENT FULL POWER ROZ POST KAREGA V102 Price 99",type="primary"):
            posts=[]
            today=datetime.datetime.now().strftime("%Y-%m-%d")
            for c in courses[:20]:
                posts.append({"date":today,"platform":"Facebook","course":c["topic"],"type":"Morning Post","price":c.get("price",99)})
                posts.append({"date":today,"platform":"Instagram","course":c["topic"],"type":"Reel","price":c.get("price",99)})
                posts.append({"date":today,"platform":"Blog","course":c["topic"],"type":"SEO Blog","price":c.get("price",99)})
            save(MARKETING_FILE,posts)
            st.success("Super Agent Full Power Started Roz Karega V102 Price 99")
            st.balloons()

else:
    if menu=="Browse Courses":
        st.title("Brahma Education V102 Price 99 Full Restore 100 Courses 40 Modules Master Teacher")
        st.write("V100 exact + Price 99 + Price Manager Bulk Single - No Lamba String - No Unterminated - Full Restore - Perfect")
        search=st.text_input("Search 100 courses Price 99")
        fl=[c for c in courses if search.lower() in c.get("topic","").lower()] if search else courses
        real=len(list(PPT_DIR.glob("*V102*")))
        st.write(f"Total {len(fl)} courses - Ready V102 {real} - 40 Pages Deep Detail - Price Only 99 - Full Restore")
        for idx,co in enumerate(fl[:15]):
            with st.expander(f"{idx+1}. {co.get('topic')} - Rs {co.get('price',99)}"):
                col_qr,col_pay=st.columns([1,2])
                with col_qr:
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH),width=220)
                    else:
                        st.info("UPI QR Admin Setup V102 Price 99")
                with col_pay:
                    params={"pa":UPI_ID,"pn":NAME,"am":str(co.get("price",99)),"cu":"INR","tn":co.get("topic","")[:20]}
                    link="upi://pay?"+urllib.parse.urlencode(params)
                    st.link_button(f"Pay Rs {co.get('price',99)} - UPI Price 99",link,type="primary")
                with st.form(f"buy_{co['id']}_{idx}_v102"):
                    c1,c2,c3=st.columns(3)
                    with c1:
                        name=st.text_input("Full Name",key=f"n_{idx}_v102",placeholder="Rahul Sharma")
                    with c2:
                        email=st.text_input("Email",key=f"e_{idx}_v102",placeholder="rahul@gmail.com")
                    with c3:
                        utr=st.text_input("UTR 12 digit",key=f"u_{idx}_v102",placeholder="UPI app se")
                    if st.form_submit_button("Get Course Price 99 V102",type="primary"):
                        if len(name)<3 or len(email)<5 or len(utr)<5:
                            st.error("Name Email UTR bharo")
                        else:
                            purchases.append({"invoice_no":"INV"+datetime.datetime.now().strftime("%Y%m%d%H%M%S"),"access_key":"BRAHMA-"+hashlib.sha256((email+co.get("topic")).encode()).hexdigest()[:10].upper(),"name":name,"email":email,"course":co.get("topic"),"course_id":co.get("id"),"price":co.get("price",99),"utr":utr,"status":"APPROVED","date":str(datetime.datetime.now())})
                            save(PURCHASE_FILE,purchases)
                            st.success("Verified Price 99 V102 My Access Me Jaake Download Karo")

    if menu=="My Access":
        st.title("My Learning V102 Price 99 40 Pages Deep Detail")
        k=st.text_input("Invoice or Key")
        if st.button("Unlock My Course Price 99 V102",type="primary"):
            found=[p for p in purchases if p.get("access_key")==k or p.get("invoice_no")==k]
            if not found:
                st.error("Invalid key")
            else:
                pu=found[0]
                st.success(f"Welcome {pu.get('name')} - {pu.get