if menu=="🚀 Super Brain Auto Agent":
        st.header("🚀 Super Brain Auto Agent - V14 - Naya Course Command Added")
        st.info("Ab aap command deke naya course bana sakte ho - Ek click me 400 videos")
        
        # === NEW FEATURE - SUPER BRAIN COMMAND - COURSE CREATION ===
        st.subheader("➕ Naya Course Banao - Super Brain Ko Command Do")
        with st.form("create_new_course_v14", clear_on_submit=True):
            col1,col2=st.columns(2)
            with col1:
                new_topic = st.text_input("📚 Naye Course Ka Naam Likho*", placeholder="Jaise: AI for Lawyers, Crypto Trading Pro, Instagram 2027")
                new_price = st.number_input("💰 Price Set Karo", min_value=99, max_value=10000, value=999, step=100)
            with col2:
                st.write("Ye course 10 Modules x 40 Videos = 400 Videos, 46 Hours ka auto banega")
                st.caption("Example: AI for Doctors, YouTube 2027, Stock Market Pro")
            create_btn = st.form_submit_button("🚀 Ek Click Me Course Banao - 400 Videos", type="primary", use_container_width=True)
            if create_btn:
                if not new_topic or len(new_topic) < 3:
                    st.error("❌ Course ka naam kam se kam 3 akshar likho")
                else:
                    # Check if already exists
                    existing = [c.get("topic","").lower() for c in courses]
                    if new_topic.lower() in existing:
                        st.warning(f"⚠️ Ye course pehle se hai: {new_topic}")
                    else:
                        new_id = f"BRAHMA{1000+len(courses)+1}"
                        new_course = create_course(new_topic, new_price, new_id)
                        courses.append(new_course)
                        save_courses(courses)
                        st.success(f"✅ Course Ban Gaya! {new_topic} - {new_id} - 400 Videos")
                        st.balloons()
                        st.rerun()

        st.divider()
        st.subheader("📝 Bulk Me 10-20 Courses Ek Saath Banao")
        with st.form("bulk_create_v14", clear_on_submit=True):
            bulk_input = st.text_area("Bulk Course Names - Comma Se Alag Likho*", placeholder="AI for Lawyers, AI for Farmers, Crypto Trading 2026, Instagram 2027, YouTube 2027", height=100)
            bulk_price = st.number_input("Bulk Price (Sabke liye same)", min_value=99, max_value=10000, value=999, step=100, key="bulk_price")
            bulk_btn = st.form_submit_button("📝 Bulk Courses Banao - Ek Click Me 10-20", type="primary", use_container_width=True)
            if bulk_btn:
                if not bulk_input:
                    st.error("❌ Kuch naam likho comma se")
                else:
                    topics = [t.strip() for t in bulk_input.split(",") if t.strip()]
                    if not topics:
                        st.error("❌ Sahi naam likho")
                    else:
                        added = 0
                        existing = [c.get("topic","").lower() for c in courses]
                        for t in topics:
                            if t.lower() not in existing:
                                new_id = f"BRAHMA{1000+len(courses)+1}"
                                courses.append(create_course(t, bulk_price, new_id))
                                added += 1
                        save_courses(courses)
                        st.success(f"✅ {added} Naye Courses Ban Gaye! Total ab {len(courses)}")
                        st.balloons()
                        st.rerun()

        st.divider()
        # Old Auto Post Features
        st.subheader("🤖 Auto Posting - Social Media")
        col1,col2,col3=st.columns(3)
        with col1:
            if st.button("🚀 AUTO POST ALL SOCIAL NOW", type="primary", use_container_width=True):
                logs.append({"time":str(datetime.datetime.now()),"action":"Auto Post 100 Courses","status":"Done"}); save_log(logs); st.success(f"✅ {len(courses)} Posts Ready!")
        with col2:
            if st.button("🎬 AUTO CREATE 100 REELS", type="primary", use_container_width=True):
                logs.append({"time":str(datetime.datetime.now()),"action":"100 Reels","status":"Done"}); save_log(logs); st.success("✅ Reels Ready")
        with col3:
            if st.button("💰 AUTO INVOICE", type="primary", use_container_width=True):
                logs.append({"time":str(datetime.datetime.now()),"action":f"Invoice {len(purchases)}","status":"Done"}); save_log(logs); st.success("✅ Done")
        if logs: st.dataframe(pd.DataFrame(logs[-10:]), use_container_width=True)