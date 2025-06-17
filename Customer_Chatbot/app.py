import streamlit as st
import random
import json
import nltk
import string
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from streamlit_chat import message

with open("intents.json") as file:
    intents = json.load(file)

with open("package/model.pkl", "rb") as f:
    model = pickle.load(f)
with open("package/vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)
with open("package/label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

stemmer = PorterStemmer()
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_input(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

def get_response(user_input):
    processed = preprocess_input(user_input)
    vect_input = tfidf.transform([processed]).toarray()
    pred_tag_index = model.predict(vect_input)[0]
    tag = le.inverse_transform([pred_tag_index])[0]
    st.session_state['last_intent'] = tag
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm not sure I understand. Could you rephrase that?"

st.set_page_config(page_title="E-Commerce Bot", page_icon="🛍️")
st.markdown("<h1 style='text-align: center; color: black;font: italic;'>🛒 E-Commerce Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Hi there! Ask me about store hours, orders, refunds, or anything else related to your shopping experience.</p>", unsafe_allow_html=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'last_intent' not in st.session_state:
    st.session_state.last_intent = None

with st.form(key='chat_form'):
    user_input = st.text_input("Your message:", "")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
    response = get_response(user_input)
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

for i in range(len(st.session_state.chat_history)-1, -1, -1):
    role, msg = st.session_state.chat_history[i]
    is_user = role == "user"
    message(msg, is_user=is_user, key=str(i))
