import nltk
import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faqs import faqs
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

stop_words = set(stopwords.words('english'))
# PREPROCESS
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words=word_tokenize(text)
    words=[w for w in words if w not in stop_words]
    words=[stemmer.stem(w) for w in words]
    return " ".join(words)



# PREPARE DATA
questions = [preprocess(q) for q, a in faqs]
answers = [a for q, a in faqs]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def reset_question():
    st.session_state.input_text = ""

if "input_text" not in st.session_state: st.session_state.input_text = ""
# UI
st.title("🤖 FAQ Chatbot")

user_input = st.text_input("ChatBot is Ready!, Type 'exit' to stop or Ask your question:",key="input_text")
col1,col2=st.columns(2)
with col1:
  if st.button("Send"):
    if user_input.strip() == "" :
        st.write("Bot: Please enter a question.")
    elif user_input.lower().strip() == "exit":
        st.write("Bot: Goodbye! Have a great day.")
    else:
        cleaned_input = preprocess(user_input)
        user_vector = vectorizer.transform([cleaned_input])

        similarity = cosine_similarity(user_vector, question_vectors)
        best_match_index = similarity.argmax()
        best_score = similarity[0][best_match_index]

        if best_score < 0.5:
            st.write("Bot: Sorry, I didn’t understand that.Please ask something related to orders, payments, or products.")
        else:
            st.write("Bot:", answers[best_match_index])
with col2:
    st.button("New Question",on_click=reset_question)


