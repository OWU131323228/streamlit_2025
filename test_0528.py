import streamlit as st

st.title("フォーム機能 基本コード例")
st.caption("st.form の基本的な使い方")

st.markdown("---")

# st.form 例
st.markdown("**st.form 例:**")
with st.form("user_form_basic"):
   st.write("ユーザー情報を入力してください (フォーム例)")
   name = st.text_input("名前", key="form_name_basic") # Add key
   age = st.number_input("学年", min_value=0, max_value=120, key="form_age_basic") # Add key
   act = st.selectbox("好きな活動", options=["文化祭", "合宿", "勉強会", "交流会"])
   comment = st.text_area("意気込み", placeholder="自由にコメントどんぞ")
   # フォーム送信ボタン
   if st.form_submit_button("申し込む")　# Add key
      st.succcess("申し込みが完了しました！")
      st.write(f"名前: {name}")
      st.write(f"学年: {age}")
      st.write(f"好きな活動: {act}")
      st.write(f"意気込み: {comment}")

st.markdown("---")
st.info("これはフォーム機能の基本コード例です。") 
