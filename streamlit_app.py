import streamlit as st
import base64

st.markdown("---")

# フォームでユーザー情報を入力

st.markdown("""
    <style>
    div[data-testid="stForm"] {
        background-color: #EAD9FF
    }
    </style>
""", unsafe_allow_html=True)

if "music_cards" not in st.session_state:
    st.session_state.music_cards = []


with st.form("music_form"):
    st.subheader("おすすめの音楽を教えて下さい！")

    artistname = st.text_input("アーティスト名")

    option = st.selectbox("性別", ["女性", "男性", "その他"])
    from_option = st.selectbox("出身地", ["日本", "海外", "その他"])
    kinds_option = st.selectbox("アーティストの特徴", [
        "アイドル", "バンド", "ソロアーティスト", "ダンス&ボーカルグループ", "その他"
    ])

    popular = st.text_input("人気曲")
    music = st.text_input("おすすめの曲")

    recommended = st.text_area("おすすめな理由", placeholder="この曲のここが好き！")

    icon_image = st.file_uploader(
        "ジャケット画像をアップロード", 
        type=['png', 'jpg', 'jpeg'],
        help="PNG、JPG、JPEG形式の画像をアップロードできます"
    )

    rink = st.text_input("曲のリンクを貼って下さい（任意）", placeholder="YouTubeやSpotifyのリンクを入力")

    col1, col2 = st.columns(2)
    with col1:
        card_color = st.color_picker("カードの背景色", "#D0B0FF")
    with col2:
        accent_color = st.color_picker("アクセントカラー", "#7B3CFF")

        st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #9933ff;
        color: white;
    }
    div.stButton > button:hover {
        background-color: #9933ff;
    }
    </style>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button("私のおすすめ曲紹介を作成する", use_container_width=True)


#もしボタンが押されたら
if submitted:
    if not artistname or not music or not recommended or not icon_image:
        st.error("アーティスト名、おすすめの曲、おすすめな理由、ジャケット画像は必須です。")
    else:
        image_bytes = icon_image.read()
        encoded = base64.b64encode(image_bytes).decode()


        new_card = {
            "artistname": artistname,
            "option": option,
            "from_option": from_option,
            "kinds_option": kinds_option,
            "popular": popular,
            "music": music,
            "recommended": recommended,
            "encoded_img": encoded,
            "rink": rink,
            "card_color": card_color,
            "accent_color": accent_color
        }

        st.session_state.music_cards.append(new_card)
        st.success("完了しました！以下があなたのおすすめ曲紹介です。　お友達に紹介してみましょう！！")

# カード表示エリア
st.markdown("---")
st.subheader("私のおすすめ曲紹介")

        # 画像をBase64でエンコードしてHTMLで埋め込み
        #img_html = f'<img src="data:image/png;base64,{encoded}" width="180" style="border-radius:12px;" />'

for card in st.session_state.music_cards:
        # カードスタイル全体
        st.markdown(f"""
        <div style="
            background: {card['card_color']};
            border-radius: 16px;
            padding: 20px;
            max-width: 700px;
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-shadow: 0 8px 24px rgba(0,0,0,0.6);
            margin: 20px auto;
        ">
            <div style="display: flex; gap: 20px;">
                <div style="min-width: 180px;">
                    <img src="data:image/png;base64,{card['encoded_img']}" width="180" style="border-radius:12px;" />
                </div>
                <div style="flex: 1;">
                    <h2 style="margin: 0; font-size: 28px; font-weight: 700; color: {card['accent_color']};">「{card['music']}」</h2>
                    <h3 style="margin: 5px 0 15px 0; font-weight: 600; color: #000;">{card['artistname']}</h3>
                    <p style="font-size: 14px; line-height: 1.5; color: #000;">
                        {card['recommended']}
                    </p>
                    <div style="margin-top: 20px; font-size: 12px; color: #888;">
                        性別: {card['option']} &nbsp; | &nbsp;
                        出身地: {card['from_option']} &nbsp; | &nbsp;
                        特徴: {card['kinds_option']}
                    </div>
        """, unsafe_allow_html=True)

        if popular:
            st.markdown(f"""
                <div style="margin-top: 10px; font-size: 20px; color: #000;">
                    人気曲: {card['popular']}
                </div>
            """, unsafe_allow_html=True)

        if rink:
            st.markdown(f"""
                <a href="{card['rink']}" target="_blank" style="
                    display: inline-block;
                    margin-top: 20px;
                    background-color: {card['accent_color']};
                    color: white;
                    padding: 10px 20px;
                    border-radius: 50px;
                    text-decoration: none;
                    font-weight: 600;
                    box-shadow: 0 4px 12px {card['accent_color']}88;
                ">
                    ▶️ 再生する
                </a>
            """, unsafe_allow_html=True)

        st.markdown("</div></div></div>", unsafe_allow_html=True)
else:
    st.info("フォームに必要情報を入力し、「おすすめ曲紹介を作成」を押してください。")
