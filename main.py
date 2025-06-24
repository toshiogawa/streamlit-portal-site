import streamlit as st
import pandas as pd
import os

# CSSを適用
st.markdown(
    """
    <style>
    @keyframes blink {
    0% { color: #39ff14; text-shadow: 0 0 15px #39ff14; }
    50% { color: #ff073a; text-shadow: 0 0 15px #ff073a; }
    100% { color: #39ff14; text-shadow: 0 0 15px #39ff14; }
    }
    .blinking-text {
        font-size: 32px !important; /* 強制的に変更 */
        font-weight: bold;
        animation: blink 1s infinite;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 点滅する文字を表示
st.markdown('<p class="blinking-text">テスト運用中</p>', unsafe_allow_html=True)


# 表紙の内容を表示

st.markdown("""


# :streamlit: Portal Site : 第１技術課 _ 1F

### アクセス方法 :
アクセス方法は以下の通り
- サイドバーに表示された機種をクリックしてそのページに進むことができます

### 運用ルール : 
更新の運用方法は以下の通り
- 左記のメンテナンスページにある"フォルダを開く"からdataにアクセスしてください
- 更新したいエクセルファイルを選択して更新してください
- ファイルのアップロードを行うと自動的に更新されます

---
> このサイトはフレームワーク[Streamlit](https://streamlit.io/)を使用し運用されています。

"""
)

# サイドバー
# st.sidebar.title("技術サーバー")
st.sidebar.write("関連サイト")
st.sidebar.write("・[防衛装備庁](https://www.mod.go.jp/atla/)")  # リンクを貼る
st.sidebar.write("・[ファイル検索システム](http://hnsvzz0s:9988/webapps/home/session.html?app=SearchApp4)") # リンクを貼る
st.sidebar.write("・[KHI岐阜カレンダー](https://www.khiunion.or.jp/wp-content/themes/kawasakijukou/pdf/calendar/2025/04_2025-gifu-nagoya.pdf)") # リンクを貼る
