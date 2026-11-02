# V17 - 100% FREE - NO API KEY NEEDED - gTTS + MoviePy
# Requirements.txt me bas ye daalo:
# streamlit
# pandas
# gtts
# Pillow

from gtts import gTTS
from PIL import Image, ImageDraw

def free_hindi_voice(text, save_path):
    # NO API - Direct Google Free
    tts = gTTS(text=text, lang='hi', slow=False)
    tts.save(save_path)
    return save_path # Hindi MP3 ready

def free_english_voice(text, save_path):
    # NO API - Direct Google Free
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(save_path)
    return save_path # English MP3 ready

def free_thumbnail(text, save_path):
    # NO API - Pillow se thumbnail
    img = Image.new('RGB', (1280, 720), color=(20,20,80))
    draw = ImageDraw.Draw(img)
    draw.text((100,300), text, fill=(255,255,255))
    img.save(save_path)
    return save_path