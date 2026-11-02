import streamlit as st, json, hashlib, datetime, urllib.parse
from pathlib import Path
D=Path('data')
D.mkdir(exist_ok=True)
MH=D/'.master_hash'
AS=D/'.admin_session'
CF=D/'courses.json'
PD=D/'ppts'
PD.mkdir(exist_ok=True)
PF=D/'purchases.json'
AF=D/'api_keys.json'
UQ=D/'upi_qr.jpg'
UID='parveen39179@okicici'
NM='Parveen Kumar'

def load(p,d):
    try:
        if p.exists():
            t=p.read_text(encoding='utf-8')
            if len(t)>2:
                return json.loads(t)
    except:
        pass
    return d

def save(p,d):
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')

class MT:
    def ttl(self,t,n):
        return t
    def cnt(self,t,n):
        return t+' Deep detail master teacher '
    def make(self,cid,ctopic):
        from pptx import Presentation
        from pptx.util import Inches, Pt
        prs=Presentation()
        prs.slide_width=Inches(13.33)
        prs.slide_height=Inches(7.5)
        for i in range(40):
            s=prs.slides.add_slide(prs.slide_layouts[6])
            tb=s.shapes.add_textbox(Inches(0.3), Inches(0.2), Inches(12.7), Inches(0.9))
            tf=tb.text_frame
            tf.word_wrap=True
            tf.text=self.ttl(ctopic,i+1)
            tf.paragraphs[0].font.size=Pt(20)
            tf.paragraphs[0].font.bold=True
            bb=s.shapes.add_textbox(Inches(0.3), Inches(1.2), Inches(12.7), Inches(6.1))
            bf=bb.text_frame
            bf.word_wrap=True
            bf.text=self.cnt(ctopic,i+1)
            bf.paragraphs[0].font.size=Pt(13)
        out=PD/(cid+'.pptx')
        prs.save(str(out))
        return out

mt=MT()
courses=load(CF,[])
if len(courses)<100:
    courses=[]
    for i in range(100):
        courses.append({'id':'BRAHMA'+str(1000+i),'topic':'Course '+str(i+1),'price':99})
    save(CF,courses)
else:
    need=False
    for c in courses:
        if c.get('price',999)>200:
           