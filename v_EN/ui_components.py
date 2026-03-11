import customtkinter as ctk
from assets_manager import AppColors

class StyledInput(ctk.CTkFrame):
    def __init__(self, master, label_text, default_value=None, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.label = ctk.CTkLabel(self, text=label_text, font=ctk.CTkFont(size=11, weight="bold"))
        self.label.pack(anchor="w", padx=2)

        self.input_type = "entry"
        self.combo_options = []

        if any(x in label_text for x in ["Exercise-Induced", "Angina"]):
            self.input_type = "combo"
            self.combo_options = ["0: No", "1: Yes"]
        elif "Chest" in label_text:
            self.input_type = "combo"
            self.combo_options = ["0: Typical Angina", "1: Atypical Angina", "2: Non-anginal Pain", "3: Asymptomatic"]
        elif "ECG" in label_text:
            self.input_type = "combo"
            self.combo_options = ["0: Normal", "1: ST-T Wave Abnormality", "2: Hypertrophy"]
        elif "Slope" in label_text:
            self.input_type = "combo"
            self.combo_options = ["0: Upsloping", "1: Flat", "2: Downsloping"]
        elif "Thal" in label_text:
            self.input_type = "combo"
            self.combo_options = ["1: Fixed Defect", "2: Normal", "3: Reversible Defect"]
            default_value = "2"
        elif "Vessels" in label_text:
            self.input_type = "combo"
            self.combo_options = ["0: No Blockage", "1: 1 Vessel", "2: 2 Vessel", "3: 3 Vessel", "4: 4 Vessel"]
            default_value = "0"

        if self.input_type == "entry":
            placeholder = str(default_value) if default_value else ""
            self.entry = ctk.CTkEntry(self, placeholder_text=placeholder, height=32, border_color=AppColors.PRIMARY)
            self.entry.pack(pady=(2, 0), fill="x")
        else:
            self.combo = ctk.CTkComboBox(self, values=self.combo_options, height=32, border_color=AppColors.PRIMARY, state="readonly")
            selected_opt = [opt for opt in self.combo_options if opt.startswith(str(default_value))]
            self.combo.set(selected_opt[0] if selected_opt else self.combo_options[0])
            self.combo.pack(pady=(2, 0), fill="x")

    def get_value(self):
        try:
            if self.input_type == "entry":
                val = self.entry.get().strip()
                return float(val) if val else float(self.entry._placeholder_text)
            else:
                return float(self.combo.get().split(":")[0])
        except: return 0.0


class StyledComboBox(ctk.CTkFrame):
    def __init__(self, master, label_text, options=None, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.label = ctk.CTkLabel(self, text=label_text, font=ctk.CTkFont(size=11, weight="bold"))
        self.label.pack(anchor="w", padx=2)
        if not options: options = ["Male", "Female"]
        self.combo = ctk.CTkComboBox(self, values=options, height=32, border_color=AppColors.PRIMARY, state="readonly")
        self.combo.set(options[0])
        self.combo.pack(pady=(2, 0), fill="x")

    def get_value(self):
        return 1.0 if "Male" in self.combo.get() else 0.0


class SemiCircleGauge(ctk.CTkCanvas):
    def __init__(self, master, width=200, height=120, **kwargs):
        super().__init__(master, width=width, height=height, highlightthickness=0, **kwargs)
        self.width, self.height = width, height
        self.thickness = 20
        self.gauge_color = "#f2c94c"
        self.current_value = 0
        self.draw_gauge(0)

    def draw_gauge(self, value):
        self.current_value = value
        self.delete("all")
        is_dark = ctk.get_appearance_mode() == "Dark"
        bg_color = "#2b2b2b" if is_dark else "white"
        base_circle_color = "#3d3d3d" if is_dark else "#e0e0e0"
        text_primary = "white" if is_dark else "black"
        self.configure(bg=bg_color)
        cx, cy, r = self.width / 2, self.height - 15, (self.width / 2) - self.thickness
        self.create_arc(cx - r, cy - r, cx + r, cy + r, start=0, extent=180, style="arc", width=self.thickness,
                        outline=base_circle_color)
        if value > 0:
            self.create_arc(cx - r, cy - r, cx + r, cy + r, start=180, extent=-(value / 100 * 180), style="arc",
                            width=self.thickness, outline=self.gauge_color)
        self.create_text(cx, cy - r / 2.2, text=f"{int(value)}", font=("Arial", 32, "bold"), fill=text_primary)
        self.create_text(cx, cy - 8, text="Total Risk Score (0-100)", font=("Arial", 9, "normal"), fill="#888888")


class ResultDisplay(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=("white", "#2b2b2b"), corner_radius=15, **kwargs)
        ctk.CTkLabel(self, text="Cardiovascular Risk Analysis", font=ctk.CTkFont(size=13, weight="bold")).pack(pady=(10, 0))
        self.gauge = SemiCircleGauge(self)
        self.gauge.pack(pady=(5, 2))
        self.status_label = ctk.CTkLabel(self, text="Status: Awaiting Analysis...", font=ctk.CTkFont(size=11))
        self.status_label.pack(pady=(0, 10))

    def update_result(self, score):
        color = AppColors.DANGER if score > 70 else (AppColors.WARNING if score > 30 else AppColors.SUCCESS)
        self.gauge.gauge_color = color
        self.gauge.draw_gauge(score)
        self.status_label.configure(text="Assessment Complete", text_color=color)

    def _set_appearance_mode(self, mode_string):
        super()._set_appearance_mode(mode_string)
        self.after(50, lambda: self.gauge.draw_gauge(self.gauge.current_value))


class ComparisonBar(ctk.CTkFrame):
    def __init__(self, master, label, ref_value, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.ref_value = ref_value
        self.label_name = label

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x")
        ctk.CTkLabel(header, text=label, font=ctk.CTkFont(size=11, weight="bold")).pack(side="left")
        ctk.CTkLabel(header, text=f"(Ref: {ref_value})", font=ctk.CTkFont(size=10), text_color="#888888").pack(
            side="right")

        self.bar_container = ctk.CTkFrame(self, fg_color="transparent", height=20)
        self.bar_container.pack(fill="x", pady=2)

        self.bar = ctk.CTkProgressBar(self.bar_container, height=10, corner_radius=4)
        self.bar.set(0)
        self.bar.pack(fill="x", pady=(5, 0))

        self.ref_line = ctk.CTkFrame(self.bar_container, width=2, height=12, fg_color="#A7BBC7")
        self.ref_line.place(relx=0.5, rely=0.5, anchor="center")

    def update_val(self, current_val):
        progress = min((current_val / (self.ref_value * 2)), 1.0) if self.ref_value > 0 else 0
        if "Sugar" in self.label_name:
            is_healthy = 70 <= current_val <= 100
            progress = 0.5 if is_healthy else (0.8 if current_val > 100 else 0.3)
        else:
            is_healthy = current_val <= self.ref_value

        color = "#2eb82e" if is_healthy else "#ff4b4b"
        self.bar.set(progress)
        self.bar.configure(progress_color=color)

class HealthComparisonChart(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=("white", "#2b2b2b"), corner_radius=15, **kwargs)
        ctk.CTkLabel(self, text="Clinical Parameter Comparison", font=ctk.CTkFont(size=13, weight="bold")).pack(
            pady=8, padx=15, anchor="w")
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.grid_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.bars = {}
        metrics = [
            ("Systolic Blood Pressure", 120, 0, 0), ("Total Cholesterol", 200, 0, 1),
            ("Fasting Blood Sugar", 100, 1, 0), ("Maximum Heart Rate", 150, 1, 1), ("Resting Heart Rate", 70, 0, 2)
        ]
        for label, ref, r, c in metrics:
            b = ComparisonBar(self.grid_frame, label, ref)
            b.grid(row=r, column=c, padx=8, pady=5, sticky="ew")
            self.bars[label] = b

    def update_bars(self, data_dict):
        self.bars["Systolic Blood Pressure"].update_val(data_dict[3])
        self.bars["Total Cholesterol"].update_val(data_dict[4])
        self.bars["Fasting Blood Sugar"].update_val(data_dict["raw_sugar"])
        self.bars["Maximum Heart Rate"].update_val(data_dict[7])
        self.bars["Resting Heart Rate"].update_val(data_dict["rest_hr"])


class RecommendationCard(ctk.CTkFrame):
    def __init__(self, master, title, text, icon, color, **kwargs):
        super().__init__(master, corner_radius=8, border_width=1, border_color=color, fg_color="transparent", **kwargs)
        ctk.CTkLabel(self, text=icon, font=ctk.CTkFont(size=18), text_color=color).pack(side="left", padx=10)
        f = ctk.CTkFrame(self, fg_color="transparent")
        f.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        ctk.CTkLabel(f, text=title, font=ctk.CTkFont(size=11, weight="bold"), text_color=color).pack(anchor="w")
        ctk.CTkLabel(f, text=text, font=ctk.CTkFont(size=10), wraplength=200, justify="left").pack(anchor="w")


class RecommendationBox(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=("white", "#2b2b2b"), corner_radius=15, **kwargs)

        ctk.CTkLabel(self, text="✨ Personalized Health Recommendations",
                     font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=AppColors.PRIMARY).pack(pady=(12, 8), padx=15, anchor="w")

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

    def update_recommendations(self, data, score):
        for widget in self.container.winfo_children():
            widget.destroy()

        recs = []
        bp = data.get(3, 0)
        chol = data.get(4, 0)
        sugar = data.get("raw_sugar", 0)

        if score > 70:
            recs.append(
                ("Critical Risk", "It is recommended that you consult a cardiologist as soon as possible.", "🚨", "#c0392b"))
            recs.append(
                ("Immediate Action", "Start keeping a regular record of your blood pressure and cholesterol levels.", "📋", "#e74c3c"))

        elif score > 30:
            recs.append(
                ("Moderate Risk", "A daily 30-minute brisk walk supports your heart health", "👟", "#f39c12"))
            recs.append(
                ("Nutrition", "Switch to a Mediterranean-style diet by reducing salt and saturated fat intake.", "🥗", "#d35400"))

        else:
            recs.append(
                ("Low Risk", "Your heart health looks good. Don't neglect regular sleep and water consumption.", "✅",
                 "#27ae60"))
            recs.append(
                ("Prevention", "You can maintain this healthy outlook by getting your annual routine check-ups.", "🩺", "#2ecc71"))

        if bp > 140:
            recs.append(("High Blood Pressure", "Restrict salt intake and increase monitoring.", "⚠️", "#ff4b4b"))
        elif 0 < bp < 90:
            recs.append(("Low Blood Pressure", "Increase fluid intake.", "💧", "#3498db"))

        if sugar > 120:
            recs.append(("High Blood Sugar", "Reduce carbohydrate intake.", "🍭", "#e67e22"))

        if chol > 240:
            recs.append(("High Cholesterol", "Eliminate high-fat foods.", "🥩", "#e74c3c"))
        elif chol > 200:
            recs.append(("Borderline High", "Follow a Mediterranean diet.", "🥗", "#f1c40f"))

        for i, (title, text, icon, color) in enumerate(recs):
            row = i // 2
            col = i % 2

            card = ctk.CTkFrame(self.container,
                                fg_color=("#f8f9fa", "#343434"),
                                corner_radius=10,
                                border_width=1,
                                border_color=color,
                                height=60)
            card.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
            card.grid_propagate(False)

            lbl_title = ctk.CTkLabel(card, text=f"{icon} {title}",
                                     font=ctk.CTkFont(size=11, weight="bold"),
                                     text_color=color)
            lbl_title.pack(anchor="w", padx=8, pady=(5, 0))

            lbl_text = ctk.CTkLabel(card, text=text,
                                    font=ctk.CTkFont(size=10),
                                    wraplength=200,
                                    justify="left")
            lbl_text.pack(anchor="w", padx=10, pady=(0, 5))

            card.bind("<Configure>", lambda e, l=lbl_text: l.configure(wraplength=e.width - 20))

class MedicalDisclaimer(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        text_box = ctk.CTkFrame(self, fg_color=("#fff5f5", "#2d1f1f"), corner_radius=6, border_width=1,
                                border_color="#ffcccc")
        text_box.pack(fill="x", padx=10, pady=2)

        disclaimer = ("⚠️ CardioMetrics Core - Cardiovascular Risk Assessment Tool:"
                     "\nThis calculation tool is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment."
                     "\nIf you have concerns about your health, please consult a qualified healthcare professional.")
        self.label = ctk.CTkLabel(text_box, text=disclaimer,
                                  font=ctk.CTkFont(size=10, slant="italic"),
                                  wraplength=500,
                                  justify="center",
                                  text_color="#d9534f")
        self.label.pack(pady=2, padx=10)