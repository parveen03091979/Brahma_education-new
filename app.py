import streamlit as st, json, hashlib, secrets, datetime, urllib.parse
from pathlib import Path

st.set_page_config(page_title="Brahma V105 Bilingual", layout="wide")

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

MODS_EN=["WHAT IS","WHY IMPORTANT","WHERE USE","WHEN TO USE","WHO CAN LEARN","HOW IT WORKS ARCHITECTURE","TOOLS YOU NEED","HOW YOU EARN MONEY","HOW TO USE PRACTICALLY","RIGHT WAY TO LEARN","BEGINNER FOUNDATION","CORE CONCEPTS","ADVANCED CONCEPTS","STEP BY STEP PROCESS","REAL BUSINESS EXAMPLES","CLIENT REQUIREMENTS","REAL STORY OF SUCCESS","PROJECT PLANNING","IMPLEMENTATION","MISTAKES 90 PERCENT FAIL","PRO TIP SECRET","EXPERT STRATEGY","TOOLS COMPARISON","FREE VS PAID","PORTFOLIO BUILDING","HOW TO FIND CLIENTS","FREELANCING START","AGENCY BUSINESS","BUSINESS MODEL","HOW TO SCALE","SEO AND MARKETING","LEAD GENERATION","SALES CLOSING","AUTOMATION SETUP","OPTIMIZATION","CASE STUDY ANALYSIS","DAILY PRACTICE ROUTINE","HOMEWORK TASK","REVISION METHOD","FINAL PROJECT AND NEXT STEPS"]

MODS_HI=["YE KYA HAI","KYU ZAROORI HAI","KAHAN USE HOTA HAI","KAB USE KARNA HAI","KAUN SEEKH SAKTA HAI","YE KAISE KAAM KARTA HAI","KAUN SE TOOLS CHAHIYE","PAISE KAISE KAMAYENGE","VYAVAHARIK UPYOG KAISE KARE","SAHI TARIKA KAISE SEEKHE","SHURUATI NEENV","MUKHYA AVADHARNA","ADVANCED AVADHARNA","KADAM DAR KADAM PRAKRIYA","VASTAVIK BUSINESS UDAHARAN","CLIENT KI ZAROORAT","SAFALTA KI SACCHI KAHANI","PROJECT YOJANA","KARYANVAYAN","90 PERCENT LOG KAUN SI GALTI KARTE HAIN","PRO TIP GUPT TARIKA","EXPERT RANNEETI","TOOLS TULNA","FREE VS PAID","PORTFOLIO BANANA","CLIENT KAISE DHUNDE","FREELANCING SHURU","AGENCY BUSINESS","BUSINESS MODEL","SCALE KAISE KARE","SEO AUR MARKETING","LEAD GENERATION","SALES BAND KARNA","AUTOMATION SETUP","OPTIMIZATION","CASE STUDY V