# 💳 Credit Card Fraud Detection App  
A machine learning web app built using **XGBoost, Optuna, Scikit-Learn, and Streamlit** to classify credit card transactions as **Fraud** or **Not Fraud**.

This project uses the highly imbalanced **Credit Card Fraud Dataset**, applies preprocessing, scaling, hyperparameter tuning with Optuna, and deploys a simple UI for real-time fraud prediction.

---

## 🚀 Features

### 🔍 Fraud Detection  
- Input 30 features: Time, V1 ... V28, Amount  
- Predicts **Fraud (1)** or **Not Fraud (0)**  
- Shows **fraud probability score**

---

### ⚙️ Machine Learning  
- Optuna-optimized **XGBoost Classifier**  
- **StandardScaler** for normalization  
- Handles imbalanced dataset  

---

### 🖥️ Web App (Streamlit)  
- Clean UI for entering transaction features  
- One-click fraud prediction  
- Shows fraud / non-fraud output with probability  

---

## 🧠 Tech Stack

**Python**, **NumPy**, **Pandas**, **Scikit-Learn**, **XGBoost**, **Optuna**, **Streamlit**, **Joblib**

---

## 📁 Project Structure

creditcard-fraud-detection/
│── app.py # Streamlit UI
│── requirements.txt # dependencies
│── README.md
│── models/
│ ├── optuna_xgb_fraud_model.pkl
│ └── scaler.pkl
│── .gitignore
└── venv/ (ignored)


---

## 📥 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/rishabhfit2026/creditcard-fraud-detection.git
cd creditcard-fraud-detection

2️⃣ Create a virtual environment
python -m venv venv
venv/Scripts/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running the App
streamlit run app.py


The app will open at:

📌 http://localhost:8501/

🔬 Model Training (Optional)

Dataset preprocessing

StandardScaler fitting

Optuna hyperparameter optimization

XGBoost model training

Model saved as .pkl using joblib

🌟 Prediction Example
Input

A transaction with features (Time, V1–V28, Amount)

Output
⚠️ FRAUD DETECTED! (Probability = 0.9821)


or

✅ NOT Fraud (Probability = 0.0123)

👨‍💻 Author

Rishabh Rajput
GitHub: https://github.com/rishabhfit2026

📜 License

MIT License

🚀 Thank you for using the Credit Card Fraud Detection App!
