# SmartSpam-Shield
Overview

SmartSpam Shield is a machine learning-based system for detecting SMS spam messages. Leveraging NLP preprocessing techniques and multiple ML classifiers, it accurately classifies messages as spam or ham. The project aims to enhance user security and reduce exposure to fraudulent or unwanted messages.

Features

Detects SMS spam in real-time.

Implements multiple ML algorithms: Support Vector Classifier (SVC), Random Forest, Logistic Regression, Decision Tree, KNN, and XGBoost.

Preprocessing techniques: lowercasing, tokenization, stopword removal, stemming, and TF-IDF vectorization.

Interactive Streamlit web interface for user-friendly experience.

Evaluation metrics: Accuracy, Precision, Recall, F1-score.

Dataset

Source: SMS Spam Collection Dataset

Labeled as spam or ham.

Used for training and testing ML models.

Methodology

Data Preprocessing – Cleaned SMS data, removed special characters, stopwords, and applied stemming.

Feature Extraction – TF-IDF vectorization to convert text into numerical features.

Model Training – Trained multiple ML classifiers to compare performance.

Evaluation – Measured models using accuracy, precision, recall, and F1-score.

Deployment – Integrated the best-performing model into a Streamlit web app for real-time predictions.

Results
Model	Accuracy	Precision
SVC	97.21%	97.03%
Random Forest	97.13%	100%
Logistic Regression	95.42%	96.52%
Decision Tree	92.46%	87.75%
KNN	90.76%	100%
XGBoost	96.50%	99.17%

Best Models: Random Forest and SVC (>97% accuracy)

Technologies Used

Languages: Python

Libraries: Scikit-learn, Pandas, NumPy, NLTK

Web Interface: Streamlit
