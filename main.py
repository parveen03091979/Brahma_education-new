import streamlit as st
import json, os, sqlite3
from datetime import datetime
import random
import pandas as pd

st.set_page_config(page_title="Brahma Education", page_icon="👑", layout="wide")

CONFIG_FILE = "brahma_config.json"
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)
else:
    config = {}

st.sidebar.title("👑 Brahma Education")
menu = st.sidebar.radio("Menu", ["🏠 Courses", "⚙️ Settings (Pehle Yahan Jao)", "📊 Sale Record"])

if menu == "⚙️ Settings (Pehle Yahan Jao)":
    st.header("⚙️ Sab Kuch Yahan Bhao - Code Mein Kuch Nahi")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Email + UPI")
        gmail = st.text_input("Aapka Gmail", value=config.get("gmail",""))
        app_pass = st.text_input("Gmail App Password", type="password", value=config.get("app_pass",""))
        upi_id = st.text_input("Aapki UPI ID", value=config.get("upi_id",""))
        owner_name = st.text_input("Aapka Naam", value=config.get("owner_name",""))
    with col2:
        st.subheader("📱 Social API")
        fb_token = st.text_input("Facebook Token", type="password", value=config.get("fb_token",""))
        insta_token = st.text_input("Instagram Token", type="password", value=config.get("insta_token",""))
        youtube_key = st.text_input("YouTube Key", type="password", value=config.get("youtube_key",""))
        openai_key = st.text_input("OpenAI Key", type="password", value=config.get("openai_key",""))
    if st.button("💾 SAVE KARO"):
        new_config = {"gmail":gmail,"app_pass":app_pass,"upi_id":upi_id,"owner_name":owner_name,"fb_token":fb_token,"insta_token":insta_token,"youtube_key":youtube_key,"openai_key":openai_key}
        with open(CONFIG_FILE, 'w') as f:
            json.dump(new_config, f)
        st.success("Save ho gaya!")

elif menu == "🏠 Courses":
    st.header("Brahma Education")
    course = st.selectbox("Course", ["AI Video Empire", "Digital Marketing", "ChatGPT Business"])
    c_name = st.text_input("Customer Naam")
    c_mobile = st.text_input("Mobile")
    c_whatsapp = st.text_input("WhatsApp")
    c_email = st.text_input("Email")
    if st.button("Pay & Get Course + Invoice"):
        from invoice import create_invoice
        from email_sender import send_email
        code = f"BRAHMA-{random.randint(10000,99999)}"
        invoice_file = create_invoice(c_name, c_email, course, 499, config.get("owner_name","Brahma"))
        conn = sqlite3.connect('sales.db')
        conn.execute('CREATE TABLE IF NOT EXISTS sales (name TEXT, mobile TEXT, whatsapp TEXT, email TEXT, course TEXT, code TEXT, date TEXT)')
        conn.execute("INSERT INTO sales VALUES (?,?,?,?,?,?,?)", (c_name,c_mobile,c_whatsapp,c_email,course,code,datetime.now().isoformat()))
        conn.commit()
        try:
            send_email(config["gmail"], config["app_pass"], c_email, course, code, invoice_file)
            st.success(f"Invoice {c_email} par bhej diya. Code: {code}")
        except Exception as e:
            st.warning(f"Save ho gaya, Email Error: {e} Code: {code}")
else:
    st.header("Sale Record")
    if os.path.exists('sales.db'):
        conn = sqlite3.connect('sales.db')
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        st.dataframe(df)
        st.download_button("Download CSV", df.to_csv(index=False).encode('utf-8'), "all_customers.csv")
    else:
        st.write("Koi sale nahi")