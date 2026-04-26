import streamlit as st
import sqlite3

def init_db():
    conn = sqlite3.connect('neco_secert.db')#コネクション　とって♡♡
    c = conn.cursor()#これとって（笑）
    c.execute('PRAGMA journal_mode = WAL')
    #ギャラリー展示場作成
    #表では「スカウト」を気にする人の数だけど中身はラップ！
    c.execute('''CREATE TABLE IF NOT EXISTS scout_table
    (id INTEGER PRIMARY KEY, file_name TEXT, content BLOB)''')
    #動画のポイ活
    uploaded_files = st.file_uploader("動画をポイッ♪", accept_multiple_files=True, type= ['mp4', 'png', 'jpg', 'jpeg'])
    if uploaded_files:
        for file in uploaded_files:
            video_data = file.read()
            c.execute("INSERT OR REPLACE INTO scout_table (file_name, content) VALUES (?, ?)",
            (file.name, video_data))
        conn.commit()#保存
        st.success("全部上書き保存しましたぁ～～～♪♪")
    #1.秘密の宝箱から全部「これとって！」（読み出し）
    c.execute("SELECT file_name, content FROM scout_table")
    all_files = c.fetchall()#全部取って来たよ（笑）
    st.write("---🍎AKARI GALLEY🍏---") 
    #オシャレな棚を作る♪（カラム数）
    cols = st.columns(3)
    for i, (name, data) in enumerate(all_files):
        with cols[i % 3]:
            st.write(f"📜 {name}")
            if name.endswith(".mp4"):
                st.video(data)
                st.download_button(label = "動画を保存♪", data = data, file_name = name, mime = 'application/octet-stream', key=f"video_{name}_{i}" )
            #もし写真なら、表示するの♪
            elif name.endswith((".png", ".jpg", "jpeg")):
                st.image(data)
                st.download_button(label = "動画を保存♪", data = data, file_name = name, mime = 'application/octet-stream', key=f"image_{name}_{i}")
            st.divider()#APPLEぽっく表示      
        conn.commit()
        #conn.close()
init_db()

        #c.execute("SELECT file_name, content FROM scout_table")
        #all_files = c.fetchall()
            #st.image(data)
            #if name.endswith(".mp4"):
            #st.video(data)#画面上再生(⋈◍＞◡＜◍)。✧♡
        #もし写真なら、表示するの♪
        #elif name.endswith((".png", ".jpg", "jpeg")):
            #st.image(data)
      #if name.endswith(".mp4"):
            #st.video(data)#画面上再生(⋈◍＞◡＜◍)。✧♡
        #もし写真なら、表示するの♪
        #elif name.endswith((".png", ".jpg", "jpeg")):
            #st.image(data)


    #st.write("---GARARY==AKARI---")
       
    #2.　画面にエクスプローラみたいに並べる
    #for name, data in all_files:
        
    
        #st.write(f"📼ファイル名: {name}")

        #もしMP4ならその場で再生
        #if name.endswith(".mp4"):
            #st.video(data)#画面上再生(⋈◍＞◡＜◍)。✧♡
        #もし写真なら、表示するの♪
        #elif name.endswith((".png", ".jpg", "jpeg")):
            #st.image(data)
        #st.button(f"{name} を選択して詳細を見る", key = name)
        #st.divider()


  
