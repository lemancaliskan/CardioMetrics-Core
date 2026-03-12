# ❤️ CardioMetrics Core - Cardiovascular Risk Analysis Tool

*CardioMetrics is a modern desktop application designed to analyze cardiovascular risk using machine learning algorithms. It provides meaningful health insights by processing clinical data through a user-friendly interface.*
---
📺 Demo
---
### 🎨 Visual Experience
*The application features a dedicated toggle for seamless switching between light and dark modes.*
<br><img src="https://github.com/user-attachments/assets/2767a64c-49b6-4da9-b17c-cbb079b90c93" width="670" alt="CardioMetrics Dark/Light Mode Switch">

### 🔍 Desktop Application (EN/TR)

*Optimized for a 980x666 centered window layout, this standalone application delivers a precision-focused, localized experience through a theme-aware ``CustomTkinter`` UI designed for both global and local users.*

**ENGLISH UI:**
<br><img width="670" height="685" alt="image" src="https://github.com/user-attachments/assets/de83e81b-0e34-4841-a060-c9d58731d3bc" />

**TURKISH UI:**
<br><img width="670" alt="image" src="https://github.com/user-attachments/assets/fac83157-0527-4bae-939b-e8f063c4e4a4" />

### 🌐 Web Application (Streamlit):
A responsive and lightweight web version for instant access from any device.
<br><img width="670" alt="image" src="https://github.com/user-attachments/assets/db682eb8-3be1-4a86-baae-fbe30c5c6576" />

---
✨ Features
---
- ***Dual Language Support:*** Optimized interfaces for both English (EN) and Turkish (TR).

- ***Modern GUI:*** A sleek design powered by CustomTkinter with native Dark and Light mode support.

- ***Smart Analysis:*** Real-time risk estimation using scikit-learn models (Logistic Regression / Random Forest).

- ***Visual Reporting:*** Integrated health comparison charts to visualize patient data against risk factors.
  
- ***Medical Disclaimer System***: Dynamic recommendation engine and mandatory legal disclaimer components.

---
🧬 Technical Architecture
---
*The application is structured into three main layers:*

- **UI Components:** Custom-styled input fields, combo boxes, and dashboard elements.

- **Engine:** The core logic where ML models are loaded and used for predictions.

- **Assets Manager:** Handles dynamic asset loading (icons, logos) for a consistent UI experience.

---
📊 Data Foundation
---
*The intelligence of CardioMetrics is built upon a synthesis of high-quality clinical data:*

**[Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)**: Provides the core clinical metrics including age, sex, chest pain type, resting blood pressure, cholesterol, and more.

The data was pre-processed through a custom pipeline to normalize biometric features and handle categorical variables, ensuring the models remain robust across diverse user profiles.

---
## ⚙️ Backend Engine
The core engine utilizes machine learning to evaluate cardiovascular risks. Below is a snapshot of the model training phase:

  <img width="300" alt="image" src="https://github.com/user-attachments/assets/205bcf1b-9e36-406e-80b1-7f925c32c915">

- **Model Integrity:** Fully validated via `CARDIOMETRICS-ENGINE`.
- **Performance:** Achieved a prediction accuracy of **68.29%**.
- **Regulation:** Active clinical sensitivity adjustment for risk assessment.

---
🚀 Live Demo (Web Version)
---
You can now try the application directly in your browser without any installation:
Go to the **[ CardioMetrics Streamlit App](https://cardiometrics-core.streamlit.app)**

---
🛠️ Installation & Usage
---

- ***Cloud Version (Recommended for quick use)***
  <br>Access the web application instantly: **[ CardioMetrics Streamlit App](https://cardiometrics-core.streamlit.app)**
  
- ***Standalone Executable***
<br>To run the app without installing Python:

    - Go to the **[Releases Page](https://github.com/lemancaliskan/CardioMetrics-Core/releases/tag/v2.6)**
    - Download the .exe file for your preferred language (CardioMetrics_EN.exe or CardioMetrics_TR.exe)
    - Double-click to run

- ***For Developers (Source Code)***
<br>If you want to run the project locally or contribute:

```bash
# Clone the repository
git clone https://github.com/lemancaliskan/CardioMetrics-Core.git

# --- For Desktop (CustomTkinter) ---
pip install -r requirements-wapp.txt

# To run the Turkish version:
cd v_TR
python main.py

# To run the English version:
cd v_EN
python main.py

# --- For Web (Streamlit) ---
# (Back to root directory)
pip install -r requirements.txt
streamlit run web_app.py
```

---
📁 Project Structure
---

```bash
CardioMetrics-Core/
├── 📁 assets/                  # App icons and logos
├── 📁 v_EN/                    # English Version (Desktop UI)
│   ├── 📄 main.py
│   └── 📄 ui_components.py
├── 📁 v_TR/                    # Turkish Version (Desktop UI)
│   ├── 📄 main.py
│   └── 📄 ui_components.py
├── 📄 web_app.py               # Web Application (Streamlit Implementation)
├── 📄 engine.py                # Core ML Logic
└── 📄 assets_manager.py        # Asset & Color Management
├── 📄 heart.csv/               # CSV dataset
├── 📜 requirements.txt         # Web/Streamlit requirements
└── 📜 requirements-wapp.txt    # Desktop App requirements
├── ⚙️ .gitignore               # Files to be ignored by Git
├── 📖 README.md                # Project documentation
└── ⚖️ LICENSE                  # License information
```

---
🤝 Contributing
---
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

```bash
# Fork the Project

# Create your Feature Branch 
(git checkout -b feature/AmazingFeature)

# Commit your Changes 
(git commit -m 'Add some AmazingFeature')

# Push to the Branch 
(git push origin feature/AmazingFeature)

# Open a Pull Request
```

---
⚠️ Medical Disclaimer
---
This software is for informational purposes only. The results provided do not constitute a formal medical diagnosis. Always consult with a professional healthcare provider before making any medical decisions.
