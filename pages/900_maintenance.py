import streamlit as st
import os

st.title('Maintenance(一部工事中)')

# dataフォルダの相対パス（このファイルと同じ階層に置いてください）
folder_path = os.path.join(os.path.dirname(__file__), "../data")
folder_path = os.path.abspath(folder_path)

# フォルダが存在するか確認
if not os.path.exists(folder_path):
    st.error(f"フォルダが存在しません: {folder_path}")
    st.stop()

st.markdown(
    """
### メンテナンス  
- 更新したいエクセルファイルを選択して更新してください。  
- ファイルのアップロードを行うと自動的に更新されます。  
"""
)

st.markdown("---")
st.markdown("### アイテム追加")
st.text("更新したいエクセルファイルを選択して更新してください。")
st.text("ファイルのアップロードを行うと自動的に更新されます。")

# ファイルのアップロードと保存
uploaded_file = st.file_uploader("ファイルをアップロードしてください", type=['xlsx', 'xls'])
if uploaded_file is not None:
    save_path = os.path.join(folder_path, uploaded_file.name)
    with open(save_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"アップロード完了: {uploaded_file.name}")

# 📌 最新のフォルダ内のファイルリストをここで再取得
file_list = os.listdir(folder_path)

# フォルダ内のファイルを表示
st.markdown("---")
st.markdown("### フォルダ内のファイル")

if file_list:
    for file in file_list:
        st.write(file)
else:
    st.write("フォルダにファイルがありません。")


