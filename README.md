# 🤖 FAQ Chatbot using NLP

## 📌 Project Description

This project is a simple FAQ Chatbot built using Natural Language Processing (NLP).
It matches user queries with a predefined set of FAQs and returns the most relevant answer.

The chatbot uses:

* **TF-IDF Vectorization**
* **Cosine Similarity**

to determine the best possible response.

---

## 🚀 Features

* Answers user queries based on FAQs
* Fast and lightweight (no model training required)
* Built with **Streamlit** for interactive UI
* Covers queries related to orders, payments, delivery, and products

---

## 🧠 Technologies Used

* Python
* Streamlit
* Scikit-learn (TF-IDF, Cosine Similarity)

---

## 📂 Project Structure

```
app.py          # Main Streamlit application
faqs.py         # FAQ dataset
requirements.txt
README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone <your-repo-link>
cd <project-folder>
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
streamlit run app.py
```

---

## 💡 How It Works

1. User enters a question
2. Text is preprocessed (lowercase, punctuation removed)
3. Converted into TF-IDF vectors
4. Compared with stored FAQ questions
5. Best match is returned as response

---

## ❗ Supported Questions (Important)

This chatbot works best for the following types of queries:

### 🛒 Orders

* Where is my order?
* How to cancel my order?
* Why is my order delayed?

### 💳 Payments

* Why did my payment fail?
* What payment methods are available?
* Is cash on delivery available?

### 🔄 Returns & Refunds

* How to return a product?
* Where is my refund?
* How long does refund take?

### 🚚 Delivery

* How to track my package?
* Do you deliver on weekends?
* What is delivery time?

### 🛍️ Products

* Is this product in stock?
* Does the product have warranty?
* What are available sizes or colors?

### 👤 General

* Hello
* Thank you
* Bye

---

## ⚠️ Limitations

* This is a **retrieval-based chatbot**, not generative AI
* It only answers from predefined FAQs
* Unrelated questions may return:

  > "Sorry, I didn’t understand that."

---

## 🎯 Tips for Best Results

* Ask short and clear questions
* Use keywords like: **order, refund, payment, delivery**
* Avoid long or complex sentences

---

## 📌 Future Improvements

* Add chat history
* Improve UI design
* Expand FAQ dataset
* Use advanced NLP models

---

## 👨‍💻 Author

Damini Tomer
