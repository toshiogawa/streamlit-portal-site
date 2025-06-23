import streamlit as st
import os

st.title('Maintenance')
# フォルダパスを指定
# folder_path = r'\\gfgij13\第１技術課\CA活動\チーム１F\1FグループCA21年度\工場長報告\新テーマ及びグループ（小川L、池田L）\PS\data'
# folder_path = r'\\data'
folder_path = os.path.join(os.path.dirname(__file__), "..\data")

# フォルダ内のファイルリストを取得
file_list = os.listdir(folder_path)

st.markdown(
    """

                        
###  メンテナンス
アクセス方法は以下の通り
- 更新したいエクセルファイルを選択して更新してください。
- ファイルのアップロードを行うと自動的に更新されます。

            
"""
    )


# フォルダパスで指定したフォルダを開く
if st.button("フォルダを開く"):
    os.startfile(folder_path)  # フォルダを開く

st.markdown("""
---
###  アイテム追加
            
""")

# フォルダパスのアクセス
st.text("更新したいエクセルファイルを選択して更新してください。")
st.text("ファイルのアップロードを行うと自動的に更新されます。")

# folder_pathで指定したフォルダにエクセルファイルを選んだあと、自動でアップロードする
uploaded_file = st.file_uploader("ファイルをアップロードしてください", type=['xlsx', 'xls'])
if uploaded_file is not None:
    with open(os.path.join(folder_path, uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer()) # ファイルを保存
        st.write("アップロードが完了しました。")

st.markdown("""
      
---
###  フォルダ内のファイル           
"""
            )

# ファイルリストをStreamlitに表示
st.write("フォルダ内のファイル:")
for file in file_list:
    st.write(file)
