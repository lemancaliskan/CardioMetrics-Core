import os
from PIL import Image
import customtkinter as ctk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
png_path = os.path.join(ASSETS_DIR, "logo.png")
ico_path = os.path.join(ASSETS_DIR, "favicon.ico")

def initialize_assets():
    if os.path.exists(ico_path):
        return

    try:
        if not os.path.exists(ASSETS_DIR):
            os.makedirs(ASSETS_DIR)

        if os.path.exists(png_path):
            img = Image.open(png_path)
            icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            img.save(ico_path, sizes=icon_sizes)
            print("İkon başarıyla oluşturuldu.")
    except Exception as e:
        print(f"İkon oluşturulurken hata oluştu: {e}")

class AppColors:
    PRIMARY = "#758A93"
    SECONDARY = "#A7BBC7"
    SUCCESS = "#2eb82e"
    WARNING = "#ffa500"
    DANGER = "#ff4b4b"
    TEXT_MAIN = "#ffffff"
    TEXT_MUTED = "#aaaaaa"

class AppImages:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    LOGO_LIGHT_PATH = os.path.join(BASE_PATH, "assets", "logo.png")
    LOGO_DARK_PATH = os.path.join(BASE_PATH, "assets", "logo_dark.png")
    DAY_ICON_PATH = os.path.join(BASE_PATH, "assets", "day.png")
    NIGHT_ICON_PATH = os.path.join(BASE_PATH, "assets", "night.png")
    ICON_PATH = os.path.join(BASE_PATH, "assets", "icon.png")

    @classmethod
    def get_logo(cls, width=250, height=39):
        light_img = None
        if os.path.exists(cls.LOGO_LIGHT_PATH):
            light_img = Image.open(cls.LOGO_LIGHT_PATH)

        dark_img = None
        if os.path.exists(cls.LOGO_DARK_PATH):
            dark_img = Image.open(cls.LOGO_DARK_PATH)
        else:
            dark_img = light_img

        if light_img:
            return ctk.CTkImage(light_image=light_img, dark_image=dark_img, size=(width, height))
        return None

    @classmethod
    def get_theme_icons(cls):
        day_img = None
        night_img = None

        if os.path.exists(cls.DAY_ICON_PATH):
            img = Image.open(cls.DAY_ICON_PATH)
            day_img = ctk.CTkImage(light_image=img, dark_image=img, size=(20, 20))

        if os.path.exists(cls.NIGHT_ICON_PATH):
            img = Image.open(cls.NIGHT_ICON_PATH)
            night_img = ctk.CTkImage(light_image=img, dark_image=img, size=(20, 20))

        return day_img, night_img

class AppConfig:
    TITLE = "CardioMetrics CORE v2.6"
