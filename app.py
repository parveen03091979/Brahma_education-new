    if menu=="📚 Browse Courses":
        st.title(f"📚 {len(courses)} Courses - V17.2 QR Fixed - No Blank")
        st.info("💰 UPI ID: parveen39179@okicici - QR Scan karke pay karo - 100% FREE Voice + Hindi+English")
        search=st.text_input("🔍 Search Course")
        filtered=[c for c in courses if search.lower() in c.get('topic','').lower()] if search else courses
        page_size=20; total_pages=max(1,(len(filtered)+page_size-1)//page_size)
        page=st.selectbox(f"Page {total_pages} Pages - Total {len(filtered)} Courses", range(1,total_pages+1), format_func=lambda x: f"Page {x} - {((x-1)*page_size)+1} to {min(x*page_size,len(filtered))}")
        page_courses=filtered[(page-1)*page_size:page*page_size]
        
        for idx,c in enumerate(page_courses, start=(page-1)*page_size+1):
            with st.expander(f"{idx}. {c.get('topic','')} - ₹{c.get('price',999)} - 400 Videos Hindi+English", expanded=False):
                col_qr, col_pay = st.columns([1,2])
                with col_qr:
                    st.write("**📱 QR Scan Karke Pay Karo**")
                    if UPI_QR_PATH.exists():
                        st.image(str(UPI_QR_PATH), caption=f"UPI: {MY_UPI_ID}", width=250)
                        st.success("✅ QR Available")
                    else:
                        st.warning("⚠️ QR Abhi Upload Nahi Hua - Admin -> UPI QR Setup me jao - QR upload karo")
                        # Show UPI ID as QR text fallback
                        st.code(f"UPI ID:\n{MY_UPI_ID}\nName: {MY_NAME}\nAmount: ₹{c.get('price',999)}")
                
                with col_pay:
                    st.write(f"**💰 Course: {c.get('topic','')}**")
                    st.write(f"**Price: ₹{c.get('price',999)} | Videos: 400 | Hindi+English**")
                    params={"pa":MY_UPI_ID,"pn":MY_NAME,"am":str(c.get('price',999)),"cu":"INR","tn":c.get('topic','')[:25]}
                    upi_link=f"upi://pay?{urllib.parse.urlencode(params)}"
                    st.link_button(f"📱 UPI App Se Pay ₹{c.get('price',999)}", upi_link, type="primary", use_container_width=True)
                    st.caption(f"UPI: {MY_UPI_ID} - Manual pay bhi kar sakte ho")
                
                st.divider()
                # Payment form with UTR
                with st.form(f"buy_{c.get('id')}_{idx}", clear_on_submit=False):
                    st.write("**🔑 Payment Ke Baad Details Bharo - UTR Daalo**")
                    c1,c2,c3=st.columns(3)
                    with c1: name=st.text_input("Name*", key=f"n_{idx}")
                    with c2: email=st.text_input("Email*", key=f"e_{idx}")
                    with c3: utr=st.text_input("UTR Number* (12 digit)", key=f"u_{idx}", help="UPI App me payment history me milega")
                    
                    if st.form_submit_button(f"✅ Request Access - {c.get('topic','')[:20]}", type="primary", use_container_width=True):
                        if name and email and utr:
                            inv=f"INV{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                            key=f"BRAHMA-{hashlib.sha256((email+c.get('topic','')+inv+utr).encode()).hexdigest()[:12].upper()}"
                            purchases.append({"invoice_no":inv,"access_key":key,"date":str(datetime.datetime.now()),"name":name,"email":email,"course":c.get('topic',''),"price":c.get('price',999),"course_id":c.get('id',''),"utr":utr,"status":"PENDING"})
                            save_purchases(purchases)
                            st.warning(f"⏳ Request Sent - Pending Approval - Invoice: {inv} - Key: {key} - Admin approve karega toh unlock hoga")
                            st.info("QR Scan karke pay kiya? UTR sahi daala? Admin 2-4 ghante me approve karega")
                        else:
                            st.error("❌ Name, Email, UTR - Teenon bharo - Tabhi request jayegi")
    if menu=="🌐 UPI QR Setup":
        st.header("🌐 UPI QR Setup - QR Kabhi Gayab Nahi Hoga - V17.2 Fixed")
        st.info(f"Current UPI: {MY_UPI_ID} - Name: {MY_NAME} - Yahan QR upload karo - Browse Courses me auto dikhega")
        
        col1,col2=st.columns(2)
        with col1:
            st.subheader("📤 Naya QR Upload Karo")
            up=st.file_uploader("QR Image Upload Karo - JPG/PNG", type=["jpg","png","jpeg"], key="qr_upload_v172")
            if up:
                UPI_QR_PATH.write_bytes(up.getvalue())
                st.success("✅ QR Saved - Ab Browse Courses me har course me dikhega - Kabhi gayab nahi hoga")
                st.balloons()
                st.rerun()
        with col2:
            st.subheader("👀 Current QR - Preview")
            if UPI_QR_PATH.exists():
                st.image(str(UPI_QR_PATH), caption=f"Current QR - UPI: {MY_UPI_ID}", width=350)
                st.success(f"✅ QR Exists - Path: {UPI_QR_PATH} - Size: {UPI_QR_PATH.stat().st_size} bytes")
                if st.button("🗑️ QR Delete Karo", type="secondary"):
                    UPI_QR_PATH.unlink(missing_ok=True)
                    st.error("QR Deleted - Naya upload karo")
                    st.rerun()
            else:
                st.error("❌ QR Abhi Nahi Hai - Left side se upload karo - Tabhi Browse me dikhega")
                st.code(f"Fallback UPI:\n{MY_UPI_ID}\n{MY_NAME}\nAgar QR nahi hai toh UPI ID se pay karo")