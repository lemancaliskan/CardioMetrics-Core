import streamlit as st
import plotly.graph_objects as go
from engine import CardioEngine
from PIL import Image
import os

PRIMARY = "#758A93"
SECONDARY = "#A7BBC7"
SUCCESS = "#2eb82e"
WARNING = "#ffa500"
DANGER = "#ff4b4b"
TEXT_MAIN = "#ffffff"
TEXT_MUTED = "#aaaaaa"

ASSETS_PATH = "assets"

def get_logo(is_dark_mode):
    logo_name = "logo_dark.png" if is_dark_mode else "logo.png"
    logo_path = os.path.join(ASSETS_PATH, logo_name)
    if os.path.exists(logo_path):
        return Image.open(logo_path)
    return "❤️"

st.set_page_config(
    page_title="CardioMetrics Web",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_resource
def load_engine():
    return CardioEngine()

engine = load_engine()

langs = {
    "TR": {
        "app_title": "",
        "btn_run": "RİSK ANALİZİ YAP",
        "status_wait": "Analiz bekleniyor...",
        "status_done": "Değerlendirme Tamamlandı",
        "title_risk": "Kardiyovasküler Risk Analizi",
        "title_param": "Klinik Parametre Karşılaştırması",
        "title_rec": "✨ Size Özel Sağlık Notları",
        "fields": {
            "age": "Yaş", "sex": "Cinsiyet", "sex_opts": ["Erkek", "Kadın"],
            "sys_bp": "Sistolik Kan Basıncı", "rest_hr": "Dinlenme Nabzı",
            "max_hr": "Maksimum Nabız", "ex_ang": "Egzersiz Anjini", "ex_ang_opts": ["0: Hayır", "1: Evet"],
            "cp": "Göğüs Ağrısı", "cp_opts": ["0: Tipik", "1: Atipik", "2: Non-Anjinal", "3: Asemptomatik"],
            "fbs": "Kan Şekeri (Açlık)", "chol": "Kolesterol",
            "ecg": "EKG Sonucu", "ecg_opts": ["0: Normal", "1: ST-T Dalga", "2: Hipertrofi"],
            "vessels": "Damar Sayısı",
            "vessels_opts": ["0: Tıkanıklık Yok", "1: 1 Damar", "2: 2 Damar", "3: 3 Damar", "4: 4 Damar"],
            "st_dep": "ST Çökmesi", "st_slope": "ST Eğimi", "st_slope_opts": ["0: Yükselen", "1: Düz", "2: Alçalan"],
            "thal": "Thal", "thal_opts": ["1: Sabit Defekt", "2: Normal", "3: Geri Dönüşümlü"]
        },
        "recs": {
            "crit_title": "Kritik Risk", "crit_desc": "En kısa sürede bir kardiyoloji uzmanına muayene olmanız önerilir.",
            "urg_title": "Acil Önlem", "urg_desc": "Tansiyon ve kolesterol değerlerinizi kayıt altına almaya başlayın.",
            "mod_title": "Orta Risk", "mod_desc": "Günlük 30 dakika orta tempolu yürüyüş kalp sağlığınızı destekler.",
            "diet_title": "Beslenme", "diet_desc": "Tuz ve doymuş yağ tüketimini azaltarak Akdeniz tipi beslenmeye geçin.",
            "low_title": "Düşük Risk", "low_desc": "Kalp sağlığınız iyi görünüyor. Düzenli uykuyu ve su tüketimini ihmal etmeyin.",
            "prot_title": "Koruma", "prot_desc": "Yıllık rutin kontrollerinizi yaptırarak bu tabloyu koruyabilirsiniz.",
            "bp_high": "Yüksek Tansiyon", "bp_high_desc": "Tuzu kısıtlayın, takibi artırın.",
            "bp_low": "Düşük Tansiyon", "bp_low_desc": "Sıvı alımını artırın.",
            "sugar_high": "Yüksek Şeker", "sugar_high_desc": "Karbonhidratı azaltın.",
            "chol_high": "Yüksek Kolesterol", "chol_high_desc": "Yağlı gıdaları kesin.",
            "chol_border": "Sınırda Değer", "chol_border_desc": "Akdeniz tipi beslenin."
        },
        "disclaimer": "⚠️ CardioMetrics Core - Kardiyovasküler Risk Değerlendirme Aracı: "
                      "<br>Bu hesaplama aracı sadece bilgilendirme amaçlıdır ve profesyonel tıbbi tavsiye, teşhis veya tedavinin yerini tutmaz. "
                      "<br>Sağlık durumunuz hakkında endişeleriniz varsa, mutlaka bir sağlık profesyoneline başvurun."
    },
    "EN": {
        "app_title": "",
        "btn_run": "RUN RISK ANALYSIS",
        "status_wait": "Awaiting analysis...",
        "status_done": "Assessment Complete",
        "title_risk": "Cardiovascular Risk Analysis",
        "title_param": "Clinical Parameter Comparison",
        "title_rec": "✨ Personalized Health Notes",
        "fields": {
            "age": "Age", "sex": "Sex", "sex_opts": ["Male", "Female"],
            "sys_bp": "Systolic Blood Pressure", "rest_hr": "Resting Heart Rate",
            "max_hr": "Maximum Heart Rate", "ex_ang": "Exercise Angina", "ex_ang_opts": ["0: No", "1: Yes"],
            "cp": "Chest Pain Type", "cp_opts": ["0: Typical", "1: Atypical", "2: Non-Anginal", "3: Asymptomatic"],
            "fbs": "Fasting Blood Sugar", "chol": "Total Cholesterol",
            "ecg": "ECG Result", "ecg_opts": ["0: Normal", "1: ST-T Wave", "2: Hypertrophy"],
            "vessels": "Major Vessels",
            "vessels_opts": ["0: None", "1: 1 Vessel", "2: 2 Vessels", "3: 3 Vessels", "4: 4 Vessels"],
            "st_dep": "ST Depression", "st_slope": "ST Slope",
            "st_slope_opts": ["0: Upsloping", "1: Flat", "2: Downsloping"],
            "thal": "Thal", "thal_opts": ["1: Fixed Defect", "2: Normal", "3: Reversable Defect"]
        },
        "recs": {
            "crit_title": "Critical Risk", "crit_desc": "It is recommended that you consult a cardiologist as soon as possible.",
            "urg_title": "Urgent Precaution", "urg_desc": "Start keeping a regular record of your blood pressure and cholesterol levels.",
            "mod_title": "Moderate Risk", "mod_desc": "A daily 30-minute brisk walk supports your heart health.",
            "diet_title": "Diet", "diet_desc": "Switch to a Mediterranean-style diet by reducing salt and saturated fat intake.",
            "low_title": "Low Risk", "low_desc": "Your heart health looks good. Don't neglect regular sleep and water consumption.",
            "prot_title": "Prevention", "prot_desc": "You can maintain this healthy outlook by getting your annual routine check-ups.",
            "bp_high": "High Blood Pressure", "bp_high_desc": "Restrict salt intake and increase monitoring.",
            "bp_low": "Low Blood Pressure", "bp_low_desc": "Increase fluid intake.",
            "sugar_high": "High Blood Sugar", "sugar_high_desc": "Reduce carbohydrate intake.",
            "chol_high": "High Cholesterol", "chol_high_desc": "Eliminate high-fat foods.",
            "chol_border": "Borderline Value", "chol_border_desc": "Follow a Mediterranean diet."
        },
        "disclaimer": "⚠️ CardioMetrics Core - Cardiovascular Risk Assessment Tool:"
                     "<br>This calculation tool is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment."
                     "<br>If you have concerns about your health, please consult a qualified healthcare professional."
    }
}

if 'lang' not in st.session_state: st.session_state.lang = "TR"
if 'theme_mode' not in st.session_state: st.session_state.theme_mode = "light"

def toggle_lang():
    st.session_state.lang = "EN" if st.session_state.lang == "TR" else "TR"

def toggle_theme():
    st.session_state.theme_mode = "dark" if st.session_state.theme_mode == "light" else "light"

is_dark = st.session_state.theme_mode == "dark"
bg_color = "#1e1e1e" if is_dark else "#f2f2f2"
card_bg = "#2b2b2b" if is_dark else "#ffffff"
text_col = TEXT_MAIN if is_dark else "#000000"
border_col = "#3d3d3d" if is_dark else "#e0e0e0"

current_logo = get_logo(is_dark)

st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg_color}; color: {text_col}; }}

    div[data-testid="stButton"] > button[kind="primary"] {{ 
        width: 100% !important; 
        border-radius: 12px !important; 
        font-weight: bold !important; 
        background-color: {PRIMARY} !important; 
        color: {TEXT_MAIN} !important; 
        height: 50px !important; 
        border: none !important;
    }}
    div[data-testid="stButton"] > button[kind="primary"]:hover {{ 
        background-color: {SECONDARY} !important; 
        color: {TEXT_MAIN} !important;
    }}

    div[data-testid="stButton"] > button[kind="secondary"] {{
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
        padding: 0 !important;
        width: 100% !important;
        color: {text_col} !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    div[data-testid="stButton"] > button[kind="secondary"]:hover,
    div[data-testid="stButton"] > button[kind="secondary"]:active,
    div[data-testid="stButton"] > button[kind="secondary"]:focus {{
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: {text_col} !important;
    }}

    div[data-testid="stButton"] > button[kind="secondary"] p {{
        font-size: 26px !important;
        margin: 0 !important;
        line-height: 1 !important;
    }}

    .panel-box {{ background-color: {card_bg}; padding: 15px; border-radius: 15px; margin-bottom: 15px; border: 1px solid {border_col}; }}
    .rec-card {{ background-color: {card_bg}; padding: 10px; border-radius: 10px; border: 1px solid; height: 85px; }}
    .rec-title {{ font-size: 13px; font-weight: bold; margin-bottom: 3px; }}
    .rec-text {{ font-size: 11px; line-height: 1.2; color: {text_col}; }}

    div[data-testid="stVerticalBlock"]:has(> div.element-container > div.stMarkdown div.risk-target) {{
        background-color: {card_bg};
        padding: 15px;
        border-radius: 15px;
        border: 1px solid {border_col};
        margin-bottom: 15px;
    }}
    .risk-target {{ display: none; }}

    div[data-testid="stNumberInput"] label p, div[data-testid="stSelectbox"] label p {{ color: {text_col} !important; }}
    div[data-testid="stNumberInput"] input {{ background-color: {card_bg} !important; color: {text_col} !important; border-color: {border_col} !important; }}
    div[data-baseweb="select"] > div {{ background-color: {card_bg} !important; color: {text_col} !important; border-color: {border_col} !important; }}
    div[data-baseweb="select"] span {{ color: {text_col} !important; }}
    </style>
""", unsafe_allow_html=True)

t = langs[st.session_state.lang]
f = t["fields"]

top_col1, top_col2 = st.columns([15, 1.2])
with top_col2:
    sub_c1, sub_c2 = st.columns(2, gap="small")
    with sub_c1:
        st.markdown('<div class="icon-btn">', unsafe_allow_html=True)
        st.button("🌐", on_click=toggle_lang, key="lang_toggle")
        st.markdown('</div>', unsafe_allow_html=True)
    with sub_c2:
        st.markdown('<div class="icon-btn">', unsafe_allow_html=True)
        st.button("☀️" if is_dark else "🌙", on_click=toggle_theme, key="theme_toggle")
        st.markdown('</div>', unsafe_allow_html=True)

col_left, col_space, col_right = st.columns([1.1, 0.05, 1.85])

with col_left:
    l_spacer1, l_logo, l_spacer2 = st.columns([1, 4, 1])
    with l_logo:
        st.image(current_logo, width=250)

    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input(f["age"], 20, 100, 50)
        sys_bp = st.number_input(f["sys_bp"], 90, 200, 120)
        max_hr = st.number_input(f["max_hr"], 60, 220, 150)
        cp = st.selectbox(f["cp"], range(4), format_func=lambda x: f["cp_opts"][x])
        chol = st.number_input(f["chol"], 100, 400, 200)
        vessels = st.selectbox(f["vessels"], range(5), format_func=lambda x: f["vessels_opts"][x])
        st_slope = st.selectbox(f["st_slope"], range(3), format_func=lambda x: f["st_slope_opts"][x], index=1)
    with c2:
        sex_val = st.selectbox(f["sex"], [1, 0], format_func=lambda x: f["sex_opts"][0] if x == 1 else f["sex_opts"][1])
        rest_hr = st.number_input(f["rest_hr"], 40, 140, 70)
        ex_ang = st.selectbox(f["ex_ang"], [0, 1], format_func=lambda x: f["ex_ang_opts"][x])
        fbs = st.number_input(f["fbs"], 70, 300, 90)
        ecg = st.selectbox(f["ecg"], [0, 1, 2], format_func=lambda x: f["ecg_opts"][x])
        st_dep = st.number_input(f["st_dep"], 0.0, 6.0, 0.0, step=0.1)
        thal = st.selectbox(f["thal"], [1, 2, 3], format_func=lambda x: f["thal_opts"][x - 1], index=1)

    st.write("")
    analyze_clicked = st.button(t["btn_run"], type="primary", use_container_width=True)

with col_right:
    risk_score = 0
    if analyze_clicked:
        fbs_for_model = 1.0 if fbs > 120 else 0.0
        model_input = [age, sex_val, cp, sys_bp, chol, fbs_for_model, ecg, max_hr, ex_ang, st_dep, st_slope, vessels, thal]
        risk_score = engine.get_risk(model_input)

    with st.container():
        st.markdown('<div class="risk-target"></div>', unsafe_allow_html=True)
        st.markdown(f"<h5 style='text-align: center; margin-bottom: 0;'>{t['title_risk']}</h5>", unsafe_allow_html=True)
        gauge_color = SUCCESS if risk_score <= 30 else (WARNING if risk_score <= 70 else DANGER)
        status_text = t["status_done"] if analyze_clicked else t["status_wait"]
        fig = go.Figure(go.Indicator(
            mode="gauge+number", value=risk_score,
            gauge={'axis': {'range': [0, 100], 'visible': False}, 'bar': {'color': "rgba(0,0,0,0)"},
                   'steps': [{'range': [0, risk_score], 'color': gauge_color if analyze_clicked else border_col},
                             {'range': [risk_score, 100], 'color': border_col}]}))
        fig.update_layout(height=180, margin=dict(l=10, r=10, t=10, b=0), paper_bgcolor='rgba(0,0,0,0)', font={'color': text_col})
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(f"<p style='text-align: center; color: {gauge_color}; font-size: 12px; margin-top: -30px;'>{status_text}</p>", unsafe_allow_html=True)

    def render_bar(label, ref, val, max_val, is_sugar=False):
        is_healthy = (70 <= val <= 100) if is_sugar else (val <= ref)
        color = SUCCESS if is_healthy else DANGER
        pct = min((val / max_val) * 100, 100)
        return f"""<div style="margin-bottom: 15px;">
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: bold; margin-bottom: 4px; color: {text_col};">
                <span>{label}</span><span style="color: {TEXT_MUTED}; font-size: 10px;">(Ref: {ref})</span>
            </div>
            <div style="background-color: {border_col}; border-radius: 4px; height: 10px; width: 100%; position: relative;">
                <div style="background-color: {color}; height: 10px; border-radius: 4px; width: {pct}%;"></div>
                <div style="position: absolute; left: 50%; top: -2px; width: 2px; height: 14px; background-color: {SECONDARY};"></div>
            </div>
        </div>"""

    st.markdown(f"""
        <div class='panel-box'>
            <h6>{t['title_param']}</h6>
            <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 150px;">
                    {render_bar(f["sys_bp"], 120, sys_bp, 240)}
                    {render_bar(f["max_hr"], 150, max_hr, 250)}
                </div>
                <div style="flex: 1; min-width: 150px;">
                    {render_bar(f["chol"], 200, chol, 400)}
                    {render_bar(f["rest_hr"], 70, rest_hr, 140)}
                </div>
                <div style="flex: 1; min-width: 150px;">
                    {render_bar(f["fbs"], 100, fbs, 200, is_sugar=True)}
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    notes_html = f"<div class='panel-box'><h6 style='color: {PRIMARY}; margin-bottom: 15px;'>{t['title_rec']}</h6>"

    if analyze_clicked:
        r_t, recs = t["recs"], []
        if risk_score > 70:
            recs.extend(
                [(r_t["crit_title"], r_t["crit_desc"], "🚨", DANGER), (r_t["urg_title"], r_t["urg_desc"], "📋", DANGER)])
        elif risk_score > 30:
            recs.extend([(r_t["mod_title"], r_t["mod_desc"], "👟", WARNING),
                         (r_t["diet_title"], r_t["diet_desc"], "🥗", WARNING)])
        else:
            recs.extend([(r_t["low_title"], r_t["low_desc"], "✅", SUCCESS),
                         (r_t["prot_title"], r_t["prot_desc"], "🩺", SUCCESS)])

        if sys_bp > 140: recs.append((r_t["bp_high"], r_t["bp_high_desc"], "⚠️", DANGER))
        if fbs > 120: recs.append((r_t["sugar_high"], r_t["sugar_high_desc"], "🍭", WARNING))
        if chol > 240:
            recs.append((r_t["chol_high"], r_t["chol_high_desc"], "🥩", DANGER))
        elif chol > 200:
            recs.append((r_t["chol_border"], r_t["chol_border_desc"], "🥗", WARNING))

        notes_html += "<div style='display: flex; flex-wrap: wrap; gap: 8px; width: 100%; align-items: stretch; justify-content: flex-start;'>"

        for title, desc, icon, color in recs:
            notes_html += f"""<div style="flex: 0 0 calc(50% - 4px); min-width: 220px; border: 1px solid {color};
            border-radius: 10px; padding: 10px; background-color: {card_bg};
            box-sizing: border-box; display: flex; flex-direction: column; margin-bottom: 0;">
            <div style="display: flex; align-items: center; margin-bottom: 5px;">
            <span style="font-size: 18px; margin-right: 8px;">{icon}</span>
            <span style="color: {color}; font-weight: bold; font-size: 13px;">{title}</span>
            </div>
            <div style="color: {text_col}; font-size: 11px; line-height: 1.3;">{desc}</div>
            </div>"""
        notes_html += "</div>"
    else:
        notes_html += f"<p style='font-size: 12px; color: {TEXT_MUTED};'>{t['status_wait']}</p>"

    notes_html += "</div>"
    st.markdown(notes_html, unsafe_allow_html=True)

    st.markdown(f"""<div style="background-color: {'#2d1f1f' if is_dark else '#fff5f5'}; border: 1px solid {DANGER}; border-radius: 6px; padding: 10px; text-align: center;">
            <span style="color: {DANGER}; font-size: 11px; font-style: italic;">{t['disclaimer']}</span>
        </div>""", unsafe_allow_html=True)