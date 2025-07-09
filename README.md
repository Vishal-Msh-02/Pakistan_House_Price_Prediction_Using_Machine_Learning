# 🏠 Pakistan House Price Prediction App 🇵🇰

This is a machine learning-powered web application built with **Streamlit** that predicts house prices across major cities in Pakistan using real estate data scraped from Zameen.com.

![image](https://github.com/user-attachments/assets/b3666749-d4e6-41f1-8988-52d9899ead1a)
![image](https://github.com/user-attachments/assets/df6313fb-78d5-43d7-9823-164285f8cb2d)
![image](https://github.com/user-attachments/assets/b1ab01b4-aaf3-40b1-b531-b7b596e9b0f2)
![image](https://github.com/user-attachments/assets/79680da5-295f-4224-8242-687fdf492aae)
![image](https://github.com/user-attachments/assets/f6c24aea-be3d-4137-b1ec-232c42a4bec5)

# 🏠 App Link

https://pakistanhousepricepredictionusingmachinelearning-oqr5dlw8pqg7m.streamlit.app/
---

## 🚀 Demo Features

- 📍 Predict house prices in **Karachi, Lahore, Islamabad, Rawalpindi, and Faisalabad**
- 🏘️ Select property type: `Flat`, `House`, or `Penthouse`
- 📏 Input total area, number of bedrooms and bathrooms
- ⚡ Instant price prediction using a trained **XGBoost Regressor**
- 💻 Built as a web app with **Streamlit**

---

## 🧠 Model Information

- Trained using **XGBoost** on real property listings (168,000+ entries)
- Features used: bedrooms, baths, area (scaled), city (one-hot), property type, purpose
- Evaluation:
  - ✅ MAE: ~5.7 Million PKR
  - ✅ R² Score: ~0.71

---

## 📚 Key Learnings

This project helped me strengthen my skills in:

- 📊 **Data Preprocessing**: Handling missing values, feature engineering, and one-hot encoding categorical variables like city and property type.
- 🤖 **Machine Learning**: Training and evaluating regression models using **XGBoost** and **Random Forest**, tuning for R² and MAE.
- ⚙️ **Model Deployment**: Building a user-friendly prediction interface using **Streamlit**, converting ML pipelines into real-world applications.
- 🧠 **Feature Importance & Model Interpretation**: Analyzing which features most impact house price predictions.
- 🌐 **End-to-End Workflow**: From raw CSV to deployed app — this project reinforced the complete lifecycle of a machine learning solution.


## 📁 Project Structure
├── app.py # Streamlit app
├── xgboost_house_price_model.pkl
├── requirements.txt
├── screenshot.png # UI preview
├── data/
│ └── pakistan_house_data.csv
├── notebook/
│ └── House_Price_Model_Training.ipynb
└── README.md

📊 Dataset
Data Source: Zameen.com

Columns include: city, bedrooms, baths, Total_Area, property_type, price, etc.

Cleaned, preprocessed and one-hot encoded for model training.

👨‍💻 Author
Vishal Maheshwary
Data Analyst | Aspiring Data Scientist
www.linkedin.com/in/vishal-maheshwary


