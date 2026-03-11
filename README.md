# ❤️ CardioMetrics Core - Cardiovascular Risk Analysis Tool

*CardioMetrics is a modern desktop application designed to analyze cardiovascular risk using machine learning algorithms. It provides meaningful health insights by processing clinical data through a user-friendly interface.*
---
📺 Demo
---
### 🎨 Visual Experience
*The application features a modern interface with native support for system themes.*
<br><img src="https://github.com/user-attachments/assets/2767a64c-49b6-4da9-b17c-cbb079b90c93" width="670" alt="CardioMetrics Dark/Light Mode Switch">

### 🔍 Application Modules (EN/TR)

**ENGLISH UI:**
<br><img width="670" height="685" alt="image" src="https://github.com/user-attachments/assets/de83e81b-0e34-4841-a060-c9d58731d3bc" />
<br><img width="670" height="687" alt="image" src="https://github.com/user-attachments/assets/99eb2d58-ce04-4169-bb69-bdf65a73e1ae" />

**TURKISH UI:**
<br><img width="670" alt="image" src="https://github.com/user-attachments/assets/fac83157-0527-4bae-939b-e8f063c4e4a4" />
<br><img width="670" alt="image" src="https://github.com/user-attachments/assets/65fb3c5d-669f-4c21-9b2f-ef5833cabd93" />

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
## ⚙️ Backend Engine
The core engine utilizes machine learning to evaluate cardiovascular risks. Below is a snapshot of the model training phase:

  <img width="300" alt="image" src="https://github.com/user-attachments/assets/205bcf1b-9e36-406e-80b1-7f925c32c915">

- **Model Integrity:** Fully validated via `CARDIOMETRICS-ENGINE`.
- **Performance:** Achieved a prediction accuracy of **68.29%**.
- **Regulation:** Active clinical sensitivity adjustment for risk assessment.

---
🛠️ Installation & Usage
---
- ***Standalone Executable (Recommended)***
<br>To run the app without installing Python:

     Go to the **[ page](https://github.com/lemancaliskan/CardioMetrics-Core-WApp-Desktop)**
     <br>Download the .exe file for your preferred language (CardioMetrics_EN.exe or CardioMetrics_TR.exe)
     <br>Double-click to run

- ***For Developers (Source Code)***
<br>If you want to run the project locally or contribute:

```bash
# Clone the repository
git clone https://github.com/lemancaliskan/CardioMetrics-Core-WApp-Desktop.git

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
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
