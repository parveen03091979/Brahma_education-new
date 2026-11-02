if menu=="📚 Courses List":
        st.header("📚 Courses List - Price Change Option - V15")
        st.info(f"Total {len(courses)} Courses - Yahan se price change karo, delete karo, naya banao")
        
        # === BULK PRICE CHANGE - SAARE COURSES KA EK SAATH ===
        st.subheader("💰 Bulk Price Change - Saare 100 Courses Ka Ek Saath")
        with st.form("bulk_price_v15"):
            col1,col2,col3=st.columns(3)
            with col1:
                bulk_action = st.selectbox("Kya Karna Hai?", ["Sabka Price Same Karo", "Sabka Price % Se Badhao", "Sabka Price % Se Ghatao", "Sabka Price Fixed Amount Se Badhao"])
            with col2:
                bulk_value = st.number_input("Value Daalo (₹ ya %)", min_value=1, max_value=10000, value=999, step=100)
            with col3:
                st.write("Example: Sabka 999 karo, ya 10% badhao")
            if st.form_submit_button("💰 Bulk Price Update Karo - Sab Courses Ka", type="primary", use_container_width=True):
                updated = 0
                if bulk_action == "Sabka Price Same Karo":
                    for c in courses: c["price"] = int(bulk_value); updated+=1
                elif bulk_action == "Sabka Price % Se Badhao":
                    for c in courses: c["price"] = int(c.get("price",999) * (1 + bulk_value/100)); updated+=1
                elif bulk_action == "Sabka Price % Se Ghatao":
                    for c in courses: c["price"] = max(99, int(c.get("price",999) * (1 - bulk_value/100))); updated+=1
                elif bulk_action == "Sabka Price Fixed Amount Se Badhao":
                    for c in courses: c["price"] = int(c.get("price",999) + bulk_value); updated+=1
                save_courses(courses)
                st.success(f"✅ {updated} Courses Ka Price Update Ho Gaya! - Ab Browse Courses me naya price dikhega")
                st.balloons()
                st.rerun()

        st.divider()
        
        # === SINGLE COURSE PRICE CHANGE ===
        st.subheader("✏️ Ek-Ek Course Ka Price Alag-Alag Change Karo")
        st.caption("Neeche list me se course select karo, naya price daalo, update dabao")
        
        # Search
        search_c = st.text_input("🔍 Course Search Karo Price Change Ke Liye", key="search_price")
        if search_c:
            filtered_c = [c for c in courses if search_c.lower() in c.get('topic','').lower()]
        else:
            filtered_c = courses
        
        # Show table with edit
        for idx, c in enumerate(filtered_c[:30]): # 30 per page to avoid lag
            with st.expander(f"{idx+1}. {c.get('topic','')} - Current Price: ₹{c.get('price',999)} - {c.get('total_videos',400)} Videos", expanded=False):
                col1,col2,col3=st.columns(3)
                with col1:
                    st.write(f"**ID:** {c.get('id','')}")
                    st.write(f"**Current Price:** ₹{c.get('price',999)}")
                    st.write(f"**Videos:** {c.get('total_videos',400)}")
                with col2:
                    new_price_single = st.number_input(f"Naya Price - {c.get('id','')}", min_value=99, max_value=20000, value=int(c.get('price',999)), step=50, key=f"price_{c.get('id','')}")
                with col3:
                    if st.button(f"💾 Update Price", key=f"update_{c.get('id','')}", type="primary", use_container_width=True):
                        c["price"] = int(new_price_single)
                        save_courses(courses)
                        st.success(f"✅ {c.get('topic','')} ka price ₹{new_price_single} ho gaya!")
                        st.rerun()
                    if st.button(f"🗑️ Delete Course", key=f"del_{c.get('id','')}", use_container_width=True):
                        courses.remove(c)
                        save_courses(courses)
                        st.error(f"Deleted {c.get('topic','')}")
                        st.rerun()
        
        if len(filtered_c) > 30:
            st.info(f"Showing 30 / {len(filtered_c)} - Search se filter karo")
        
        st.divider()
        st.dataframe(pd.DataFrame([{"No":i+1,"ID":c.get("id",""),"Course":c.get("topic",""),"Price":c.get("price",999),"Videos":c.get("total_videos",400)} for i,c in enumerate(courses)]), use_container_width=True)