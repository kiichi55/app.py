import streamlit as st

# アプリのタイトル
st.title("規則・財務審査 自動化システム")
st.write("議案書や収支予算書のPDFをアップロードしてください。")

# PDFアップロード機能
uploaded_file = st.file_uploader("ここにPDFファイルをドラッグ＆ドロップ", type="pdf")

if uploaded_file is not None:
    st.success("ファイルのアップロードに成功しました！")
    st.info("※現在はテスト画面です。今後のステップでここにAIの審査結果が表示されます。")
