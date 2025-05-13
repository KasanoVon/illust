import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

# 画像フォルダのパス
IMAGE_DIR = "images"

st.set_page_config(page_title="かさのぼん☂️イラスト展", layout="wide")
st.title("Thank You🐈️🐾")

# フォルダがなければ作成
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)
    st.warning(f"{IMAGE_DIR} フォルダを作成しました。画像をその中に入れてください。")

# フォルダ内の画像ファイル一覧
image_files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

if image_files:
    cols = st.columns(2)
    for idx, image_file in enumerate(image_files):
        image_path = os.path.join(IMAGE_DIR, image_file)
        img = Image.open(image_path).convert("RGBA")

        # Illustrator名（_より前の部分）
        illustrator_name = os.path.splitext(image_file)[0].split('_')[0]
        label_text = f"Illustrator@{illustrator_name}"

        # 描画準備
        draw = ImageDraw.Draw(img)
        font_size = max(20, img.width // 30)

        # 日本語対応フォントのパス
        font_path = "font/NotoSansJP-Regular.ttf"

        try:
            font = ImageFont.truetype(font_path, font_size)
        except OSError:
            st.error("フォントが読み込めませんでした。'HGRPP1.TTC' が存在するか確認してください。")
            font = ImageFont.load_default()

        # テキストサイズの取得
        bbox = font.getbbox(label_text)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = img.width - text_width - 10
        y = img.height - text_height - 10

        # テキストを描画（白・半透明）
        draw.text((x, y), label_text, font=font, fill=(0, 0, 0, 255))  # #000000


        with cols[idx % 2]:
            st.image(img, caption=None, use_container_width=True)
else:
    st.info("画像が見つかりません。'images' フォルダに画像を追加してください。")
