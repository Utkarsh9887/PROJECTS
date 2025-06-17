# 🛍️ E-Commerce Chatbot

This project is a simple AI-powered chatbot built using **Python**, **scikit-learn**, and **Streamlit**. The chatbot is designed to simulate a customer support assistant for an e-commerce website.

---

## 🚀 Features

- Understands common customer queries about orders, payments, returns, and store hours.
- Uses **TF-IDF** and **Logistic Regression** for intent classification.
- Pretrained model with vectorizer and label encoder.
- Fully interactive **chat UI** using `streamlit_chat`.
- Maintains session memory for ongoing chat.

---

## 📂 Project Structure

```
├── app.py                    # Main Streamlit chatbot UI
├── intents.json             # Dataset of intents, patterns, and responses
├── model.pkl                # Trained Logistic Regression model
├── vectorizer.pkl           # TF-IDF vectorizer
├── label_encoder.pkl        # Encoded labels for intents
├── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ecommerce-chatbot.git
cd ecommerce-chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the chatbot**
```bash
streamlit run app.py
```

---

## 🧠 Training the Model (Optional)
If you'd like to train the model yourself:
```python
# Preprocess the data
# Train LogisticRegression()
# Save model, vectorizer, and label encoder using pickle
```

---

## 📚 Requirements
```
streamlit
nltk
scikit-learn
pandas
numpy
streamlit-chat
```

Create a `requirements.txt` using:
```bash
pip freeze > requirements.txt
```

---

## 📸 Demo
![Chatbot UI](demo_screenshot.png)

---

## 🧾 License
This project is licensed under the MIT License.

---

## 🙋‍♂️ Author
**Your Name**  
[LinkedIn](www.linkedin.com/in/utkarsh-verma-6124362a8)  |  [GitHub](https://github.com/Utkarsh9887)
