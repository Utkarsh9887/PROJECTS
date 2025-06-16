import streamlit as st
import pickle
import numpy as np

# Load the model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# App title
st.title("Iris Flower Prediction App")
st.write("This app uses a trained model to predict the **Iris** species based on user inputs.")

# Input features
sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.5)
sepal_width  = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 4.0)
petal_width  = st.slider('Petal Width (cm)', 0.1, 2.5, 1.2)

# Predict button
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    species = ['Setosa', 'Versicolor', 'Virginica']
    st.write(f"### Prediction: {species[prediction[0]]}")
    st.write("#### Class Probabilities:")
    for i, prob in enumerate(probability[0]):
        st.write(f"{species[i]}: {prob:.2f}")
