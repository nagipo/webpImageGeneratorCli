import argparse
from PIL import Image, ImageDraw, ImageFont
import sys

# 限定可以使用的背景顏色
ALLOWED_COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "gray": (128, 128, 128),
    "blue": (0, 120, 215),
    "red": (200, 30, 30),
    "green": (0, 158, 47),
    "yellow": (255, 221, 0)
}

def generate_image(width, height, color_name, output_filename="test_image.webp"):
    if color_name not in ALLOWED_COLORS:
        print(f"不支援的顏色：{color_name}")
        print("請使用以下顏色：", ', '.join(ALLOWED_COLORS.keys()))
        sys.exit(1)

    bg_color = ALLOWED_COLORS[color_name]
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except IOError:
        font = ImageFont.load_default()

    text = "TEST IMAGE"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_position = ((width - text_width) // 2, (height - text_height) // 2)

    draw.text(text_position, text, fill='black', font=font)
    img.save(output_filename, "WEBP")
    print(f"已儲存：{output_filename}")

def main():
    parser = argparse.ArgumentParser(description="產生測試用 WebP 圖片")
    parser.add_argument("--width", type=int, default=1160, help="圖片寬度（像素）")
    parser.add_argument("--height", type=int, default=624, help="圖片高度（像素）")
    parser.add_argument("--bg", type=str, default="white", help="背景顏色（限定選項）")
    parser.add_argument("--out", type=str, default="test_image.webp", help="輸出檔名")

    args = parser.parse_args()
    generate_image(args.width, args.height, args.bg.lower(), args.out)

if __name__ == "__main__":
    main()
