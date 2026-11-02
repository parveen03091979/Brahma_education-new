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

MODS=["WHAT IS","WHY IMPORTANT","WHERE USE","WHEN TO USE","WHO CAN LEARN","HOW IT WORKS","TOOLS NEEDED","EARNING","PRACTICAL USE","RIGHT WAY","FOUNDATION","CORE CONCEPT","ADVANCED","STEP BY STEP","BUSINESS EXAMPLE","CLIENT REQ","REAL STORY","PLANNING","IMPLEMENTATION","MISTAKES","PRO TIP","EXPERT","TOOLS COMPARE","FREE VS PAID","PORTFOLIO","CLIENT FINDING","FREELANCING","AGENCY","BUSINESS MODEL","SCALING","SEO MARKETING","LEAD GEN","SALES","AUTOMATION","OPTIMIZATION","CASE STUDY","DAILY PRACTICE","HOMEWORK","REVISION","FINAL PROJECT"]

def en_content(topic,num):
    title=MODS[num-1]
    base="COURSE: "+topic+" | MODULE "+str(num)+" - "+title+" | ENGLISH | Step By Step\n\n"
    if num==17:
        return base+"GOAL: Learn from