import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer

# Download required resources once
nltk.download('stopwords')

# Load saved model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

# Define text preprocessing function
ps = PorterStemmer()
tokenizer = TreebankWordTokenizer()


def transform_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)

    # Tokenize
    tokens = tokenizer.tokenize(text)

    # Remove stopwords and apply stemming
    clean_tokens = [ps.stem(word) for word in tokens if word not in stopwords.words('english')]

    return " ".join(clean_tokens)


# Streamlit UI
st.set_page_config(page_title="Spam Classifier", page_icon="📩")
st.title("📩 SMS Spam Classifier")
st.markdown("This app predicts whether a given message is **Spam** or **Not Spam** using Machine Learning.")

# User input
input_sms = st.text_area("✍️ Enter the message below:")

if st.button("🚀 Predict"):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)

    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])

    # 3. Predict
    result = model.predict(vector_input)[0]

    # 4. Output
    if result == 1:
        st.error("🚫 This message is **SPAM**!")
    else:
        st.success("✅ This message is **NOT SPAM**.")
