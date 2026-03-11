import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

"""
Machine learning-based prediction engine for cardiovascular risk analysis.
Trains a Logistic Regression model and includes manual coefficient 
adjustments based on clinical risk factors.
"""

class CardioEngine:
    def __init__(self):
        self.data_path = "heart.csv"
        self.model = LogisticRegression(max_iter=1000, C=0.1)
        self.scaler = StandardScaler()
        self.accuracy = 0
        self._initialize()

    def _initialize(self):
        if not os.path.exists(self.data_path):
            print(f"❌ HATA: {self.data_path} bulunamadı! Lütfen veri dosyasını ana dizine ekleyin.")
            return

        df = pd.read_csv(self.data_path)
        df.columns = [c.strip().lower() for c in df.columns]

        X = df.drop('target', axis=1)
        y = df['target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_train_scaled, y_train)

        coefs = self.model.coef_[0]
        # Weight of the gender variable revised to balance model dominance
        coefs[1] = coefs[1] * 0.1
        # Coefficient scaled to increase risk sensitivity of blood pressure values
        coefs[3] = abs(coefs[3]) * 1.2 + 0.1
        # Coefficient adjusted to minimize cholesterol deviations
        coefs[4] = abs(coefs[4]) * 0.8 + 0.2
        # Blood sugar weight regulated for balance in the total risk score
        coefs[5] = abs(coefs[5]) * 0.5 + 0.2
        # Weight increased as the number of major vessels is a critical risk indicator
        coefs[11] = abs(coefs[11]) * 1.5

        self.model.coef_ = np.array([coefs])
        self.accuracy = self.model.score(self.scaler.transform(X_test), y_test)

        print("\n" + "=" * 49)
        print("✅ CARDIOMETRICS-ENGINE MODEL TRAINING COMPLETE")
        print(f"📊 Overall Prediction Accuracy: %{self.accuracy * 100:.2f}")
        print(f"🔬 Risk Sensitivity: ACTIVE (Clinical Regulation)")
        print("=" * 49 + "\n")

    def get_risk(self, input_list):
        try:
            if self.accuracy == 0:
                return 0

            data_scaled = self.scaler.transform([input_list])
            prob = self.model.predict_proba(data_scaled)[0][1]
            risk = prob * 100

            # Included exercise-induced angina (index 8) in the score as a critical risk marker
            if input_list[8] == 1: risk = max(risk, risk + 15)

            return min(max(risk, 1), 99)

        except Exception as e:
            print(f"⚠️ Risk Calculation Error: {e}")
            return 0