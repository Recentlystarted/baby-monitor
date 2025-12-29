from PIL import Image, ImageDraw, ImageFont
import os

def create_baby_icon():
    size = (256, 256)
    
    image = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    font_path = "C:\\Windows\\Fonts\\seguiemj.ttf"
    
    try:
        font = ImageFont.truetype(font_path, 220)
    except OSError:
        print("Segoe UI Emoji font not found. Using default font (might not show emoji correctly).")
        font = ImageFont.load_default()

    text = "👶"
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2 - bbox[1]
    
    draw.text((x, y), text, font=font, embedded_color=True)
    
    output_path = "baby_face.ico"
    image.save(output_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    print(f"Icon saved to {os.path.abspath(output_path)}")

if __name__ == "__main__":
    create_baby_icon()
