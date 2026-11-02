import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path

st.set_page_config(page_title="Brahma V105", layout="wide")

DATA=Path("data")
PPT_DIR=DATA/"ppts"
DATA.mkdir(exist_ok=True)
PPT_DIR.mkdir(exist_ok=True)

CF=DATA/"courses.json"
PF=DATA/"purchases.json"
QF=DATA/"upi_qr.jpg"
MH=DATA/".master_hash"
AS=DATA/".admin_session"

UID="parveen39179@okicici"
OWNER="Parveen Kumar"

def load(p,d):
    try:
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    except:
        pass
    return d

def save(p,d):
    t=p.with_suffix(".tmp")
    t.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
    t.replace(p)

def init_courses():
    data=load(CF,[])
    if len(data)<100:
        data=[]
        for i in range(100):
            data.append({"id":"BRAHMA"+str(1000+i),"topic":"Course "+str(i+1),"price":99})
        save(CF,data)
    for c in data:
        if c.get("price",999)>200:
            c["price"]=99
    save(CF,data)
    return data

courses=init_courses()
purchases=load(PF,[])

MODS=["WHAT IS","WHY IMPORTANT","WHERE USE","WHEN USE","WHO LEARN","HOW WORKS","TOOLS","EARNING","PRACTICAL","RIGHT WAY","FOUNDATION","CORE CONCEPT","ADVANCED","STEP PROCESS","EXAMPLE","CLIENT REQ","REAL STORY","PLANNING","IMPLEMENT","MISTAKES","PRO TIP","EXPERT","COMPARE","FREE PAID","PORTFOLIO","CLIENT FIND","FREELANCING","AGENCY","BUSINESS MODEL","SCALING","SEO MARKETING","LEAD GEN","SALES","AUTOMATION","OPTIMIZATION","CASE STUDY","DAILY PRACTICE","HOMEWORK","REVISION","FINAL PROJECT"]

def en_content(topic,num):
    t=MODS[num-1]
    return f"{topic} M{num} {t} ENGLISH\nGOAL Master {t}\nWHY Important for job business\nCONCEPT Core idea of {t}\nSTEP1 Define\nSTEP2 Example\nSTEP3 Tool open\nSTEP4 Practice 15m\nSTEP5 Diary\nTASK Make 1 project"

def hi_content(topic,num):
    t=MODS[num-1]
    return f"{topic} M{num} {t} HINDI Translation\nLAKSHYA {t} seekhna\nKYU Job business ke liye zaruri\nAVADHARNA {t} ka core\nKADAM1 Paribhasha\nKADAM2 Udaharan\nKADAM3 Tool kholo\nKADAM4 Abhyas 15m\nKADAM5 Diary\nKARYA 1 project banao"

def make_bilingual(course):
    from pptx import Presentation
    from pptx.util import Inches, Pt
    cid=course["id"]
    topic=course["topic"]
    out_en=PPT_DIR/(cid+"_ENGLISH_V100.pptx")
    out_hi=PPT_DIR/(cid+"_HINDI_V100.pptx")
    prs=Presentation()
    prs.slide_width=Inches(13.33)
    prs.slide_height=Inches(7.5)
    for n in range(1,41):
        slide=prs.slides.add_slide(prs.slide_layouts[6])
        tb=slide.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
        tf=tb.text_frame
        tf.word_wrap=True
        tf.text=f"M{n} {topic} {MODS[n-1]} English Step By Step"
        tf.paragraphs[0].font.size=Pt(14)
        tf.paragraphs[0].font.bold=True
        bb=slide.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
        bf=bb.text_frame
        bf.word_wrap=True
        bf.text=en_content(topic,n)
        bf.paragraphs[0].font.size=Pt(11)
    prs.save(str(out_en))
    prs2=Presentation()
    prs2.slide_width=Inches(13.33)
    prs2.slide_height=Inches(7.5)
    for n in range(1,41):
        slide=prs2.slides.add_slide(prs2.slide_layouts[6])
        tb=slide.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
        tf=tb.text_frame
        tf.word_wrap=True
        tf.text=f"M{n} {topic} {MODS[n-1]} Hindi Translation"
        tf.paragraphs[0].font.size=Pt(14)
        tf.paragraphs[0].font.bold=True
        bb=slide.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
        bf=bb.text_frame
        bf.word_wrap=True
        bf.text=hi_content(topic,n)
        bf.paragraphs[0].font.size=Pt(11)
    prs2.save(str(out_hi))
    return out_en,out_hi

def make_hash(pw):
    salt=secrets.token_bytes(16)
    h=hashlib.scrypt(pw.encode(), salt=salt, n=16384, r=8, p=1)
    return salt.hex()+":"+h.hex()

def verify(pw,stored):
    try:
        s_hex,h_hex=stored.split(":")
        s=bytes.fromhex(s_hex)
        a=hashlib.scrypt(pw.encode(), salt=s, n=16384, r=8, p=1)
        return secrets.compare_digest(a.hex(), h_hex)
    except:
        old=hashlib.sha256(pw.encode()).hexdigest()
        return secrets.compare_digest(old, stored)

def sess_valid():
    try:
        d=load(AS,{})
        exp=datetime.datetime.fromisoformat(d["expiry"])
        return datetime.datetime.now()<exp
    except:
        return False

if "admin_logged"