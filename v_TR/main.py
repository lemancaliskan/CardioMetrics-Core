import customtkinter as ctk
from ui_components import *
import os
import sys
import ctypes
import warnings

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if base_path not in sys.path:
    sys.path.append(base_path)

from assets_manager import AppImages, initialize_assets, AppColors
from engine import CardioEngine

warnings.filterwarnings("ignore", category=UserWarning)

try:
    myappid = 'cardiometrics.v2.6'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except:
    pass

def resource_path(relative_path):
    import sys, os
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(base_path, relative_path)

os.chdir(base_path)
initialize_assets()

class CardioApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")
        self.title("CardioMetrics CORE v2.6")

        try:
            icon_p = resource_path(os.path.join("assets", "favicon.ico"))

            if os.path.exists(icon_p):
                self.iconbitmap(icon_p)
                self.after(200, lambda: self.iconbitmap(os.path.abspath(icon_p)))
            else:
                print(f"İkon dosyası bulunamadı: {icon_p}")
        except Exception as e:
            print(f"İkon yüklenemedi: {e}")

        self.app_w = 980
        self.app_h = 666

        self.analysis_engine = CardioEngine()

        self.set_top_center()

        self.after(100, self.lift)
        self.setup_ui()

    def set_top_center(self):
        screen_width = self.winfo_screenwidth()
        x = (screen_width // 2) - (self.app_w // 2)
        y = 20
        self.geometry(f"{self.app_w}x{self.app_h}+{int(x)}+{int(y)}")

    def setup_ui(self):
        self.sidebar = ctk.CTkFrame(self, width=380, corner_radius=0, fg_color=("#f2f2f2", "#1e1e1e"))
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        logo_img = AppImages.get_logo(width=220, height=35)
        if logo_img:
            self.logo = ctk.CTkLabel(self.sidebar, text="", image=logo_img)
        else:
            self.logo = ctk.CTkLabel(self.sidebar, text=f"❤️ CARDIOMETRICS",
                                     font=ctk.CTkFont(size=20, weight="bold"), text_color=AppColors.PRIMARY)
        self.logo.pack(pady=(20, 10))

        self.form = ctk.CTkScrollableFrame(self.sidebar, fg_color="transparent")
        self.form.pack(fill="both", expand=True, padx=15, pady=5)
        self.form.grid_columnconfigure((0, 1), weight=1)

        self.inputs = {}
        self.setup_form()

        self.bottom = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.bottom.pack(side="bottom", fill="x", pady=20, padx=25)

        self.btn = ctk.CTkButton(self.bottom, text="RİSK ANALİZİ YAP", command=self.run_analysis,
                                 fg_color=AppColors.PRIMARY, hover_color=AppColors.SECONDARY,
                                 height=50, font=ctk.CTkFont(size=14, weight="bold"),
                                 corner_radius=12)
        self.btn.pack(fill="x")

        self.theme_frame = ctk.CTkFrame(self.bottom, fg_color="transparent")
        self.theme_frame.pack(fill="x", pady=(15, 0))

        day_icon, night_icon = AppImages.get_theme_icons()
        self.btn_dark = ctk.CTkButton(self.theme_frame, text="", image=night_icon, width=35, height=35,
                                      fg_color="transparent", hover_color=AppColors.SECONDARY,
                                      command=lambda: ctk.set_appearance_mode("dark"))
        self.btn_dark.pack(side="right", padx=2)

        self.btn_light = ctk.CTkButton(self.theme_frame, text="", image=day_icon, width=35, height=35,
                                       fg_color="transparent", hover_color=AppColors.SECONDARY,
                                       command=lambda: ctk.set_appearance_mode("light"))
        self.btn_light.pack(side="right", padx=2)

        self.dashboard = ctk.CTkFrame(self, fg_color="transparent")
        self.dashboard.pack(side="right", fill="both", expand=True, padx=20, pady=10)

        self.disclaimer_ui = MedicalDisclaimer(self.dashboard)
        self.disclaimer_ui.pack(side="bottom", fill="x", pady=(5, 5))

        self.scroll_view = ctk.CTkScrollableFrame(self.dashboard, fg_color="transparent")
        self.scroll_view.pack(fill="both", expand=True)

        self.res_ui = ResultDisplay(self.scroll_view)
        self.res_ui.pack(fill="x", pady=5)

        self.chart_ui = HealthComparisonChart(self.scroll_view)
        self.chart_ui.pack(fill="x", pady=5)

        self.rec_ui = RecommendationBox(self.scroll_view)
        self.rec_ui.pack(fill="both", expand=True, pady=5)

    def setup_form(self):
        fields = [
            ("Yaş", 50, 0, "i"), ("Cinsiyet", ["Erkek", "Kadın"], 1, "c"),
            ("Sistolik Kan Basıncı", 120, 3, "i"), ("Dinlenme Nabzı", 70, "rest_hr", "i"),
            ("Maksimum Nabız", 150, 7, "i"), ("Egzersiz Anjini", 0, 8, "i"),
            ("Göğüs Ağrısı (0-3)", 0, 2, "i"), ("Kan Şekeri (Açlık)", 90, 5, "i"),
            ("Kolesterol", 200, 4, "i"), ("EKG Sonucu", 0, 6, "i"),
            ("Damar Sayısı", 0, 11, "i"), ("ST Çökmesi", 0.0, 9, "i"),
            ("ST Eğimi", 1, 10, "i"), ("Thal", 2, 12, "i")
        ]
        for i, (l, d, idx, t) in enumerate(fields):
            row, col = i // 2, i % 2
            w = StyledInput(self.form, l, d) if t == "i" else StyledComboBox(self.form, l, d)
            w.grid(row=row, column=col, padx=5, pady=8, sticky="ew")
            self.inputs[idx] = w

    def run_analysis(self):
        if not hasattr(self, 'analysis_engine'): return

        try:
            raw_data = {k: v.get_value() for k, v in self.inputs.items()}

            user_sugar = raw_data[5]
            fbs_for_model = 1.0 if user_sugar > 120 else 0.0

            model_input = [
                raw_data[0], raw_data[1], raw_data[2], raw_data[3],
                raw_data[4], fbs_for_model, raw_data[6], raw_data[7],
                raw_data[8], raw_data[9], raw_data[10], raw_data[11], raw_data[12]
            ]

            risk = self.analysis_engine.get_risk(model_input)

            self.res_ui.update_result(risk)
            display_data = raw_data.copy()
            display_data["raw_sugar"] = user_sugar
            self.chart_ui.update_bars(display_data)
            self.rec_ui.update_recommendations(display_data, risk)

        except Exception as e:
            print(f"Analiz Hatası: {e}")

if __name__ == "__main__":
    app = CardioApp()
    app.mainloop()