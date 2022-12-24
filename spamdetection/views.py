from django.shortcuts import render
import pandas as pd
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

model = joblib.load('./models/spam_model.pkl')
cv = joblib.load('./models/cv.pkl')


def demo(request):
    return render(request, 'demo.html')


def home(request):
    return render(request, 'index.html')


def detect(request, ans={'prediction': "", 'classes': ""}):
    return render(request, 'spamDetection.html', ans)


def predict(request):

    user_text = request.GET['fulltext']

    if predict_spam(user_text):
        prediction = "Gotcha it's a spam!"
        classes = "heading-secondary--3"
    else:
        prediction = "It's a Ham! :)"
        classes = "heading-secondary--4"

    ans = {'prediction': prediction, 'classes': classes}

    return detect(request, ans)


def predict_spam(sample_message):
    sample_message = re.sub(
        pattern='[^a-zA-Z]', repl=' ', string=sample_message)
    sample_message = sample_message.lower()
    sample_message_words = sample_message.split()
    sample_message_words = [word for word in sample_message_words if not word in set(
        stopwords.words('english'))]
    ps = PorterStemmer()
    final_message = [ps.stem(word) for word in sample_message_words]
    final_message = ' '.join(final_message)

    temp = cv.transform([final_message]).toarray()
    return model.predict(temp)
