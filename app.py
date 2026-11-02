# ... (V31 ka same code, sirf 2 cheez add ki hain)

# Admin menu me naya option add karo:
menu = st.sidebar.radio('Admin', ['Dashboard', 'Video Library', 'Sales', 'Super Brain', 'QR Setup', 'Price Edit', 'Settings'])

# Aur Video Library ka page add karo - Ye naya page hai:
if menu == 'Video Library':
    st.title('Video Library - Check Videos Bani Ya Nahi - Apna Course - No YouTube')
    st.write('Yahan aap check kar sakte ho ki kaunsi video bani hai - Hindi voice + English voice - 400 lessons')
    st.divider()
    
    # Sab courses ki list
    for co in courses:
        co_id = co.get('id')
        co_topic = co.get('topic')
        hi_path = VOICE_DIR / f"{co_id}_hi.mp3"
        en_path = VOICE_DIR / f"{co_id}_en.mp3"
        
        with st.expander(f"{co_topic} - {co_id} - 400 Lessons - Check Video Status"):
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric('Total Lessons', '400')
                st.write(f"Price Rs {co.get('price')}")
            with c2:
                if hi_path.exists():
                    st.success('Hindi Voice - Bani Hai ✅')
                    st.audio(str(hi_path))
                else:
                    st.error('Hindi Voice - Nahi Bani ❌')
                    if st.button(f'Generate Hindi - {co_id}', key=f'hi_{co_id}'):
                        make_voice(f"Welcome to {co_topic} Hindi me 400 lessons", 'hi', hi_path)
                        st.rerun()
            with c3:
                if en_path.exists():
                    st.success('English Voice - Bani Hai ✅')
                    st.audio(str(en_path))
                else:
                    st.error('English Voice - Nahi Bani ❌')
                    if st.button(f'Generate English - {co_id}', key=f'en_{co_id}'):
                        make_voice(f"Welcome to {co_topic} English 400 lessons", 'en', en_path)
                        st.rerun()
            
            st.divider()
            # 400 lessons ka preview
            st.write(f'**{co_topic} - 400 Lessons Preview - No YouTube - Apna Content:**')
            curriculum = get_course_content(co_topic)
            for mod in curriculum[:2]:  # Pehle 2 modules dikhao
                st.write(f"**{mod['title']}** - {len(mod['videos'])} lessons")
                for vid in mod['videos'][:3]:  # Har module ke 3 lessons
                    st.write(f"{vid['no']}. {vid['title']} - {vid['duration']}")
                    st.caption(f"Hindi: {vid['desc_hi'][:60]}...")
                    st.caption(f"English: {vid['desc_en'][:60]}...")
            st.info(f"Total 10 Modules x 40 Lessons = 400 Lessons - Apna content - No YouTube - Super agent created")

# ... baaki same code