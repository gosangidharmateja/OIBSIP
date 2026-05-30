# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# %%
nltk.download('stopwords')
nltk.download('wordnet')

# %%
df = pd.read_csv("Twitter_Data.csv")

print(df.head())


# %%
print("\nDataset Shape:")
print(df.shape)

# %%
print("\nMissing Values:")
print(df.isnull().sum())

# %%
df.dropna(inplace=True)

# %%
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()



# %%
def preprocess_text(text):

    
    text = text.lower()

    
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)

    
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    
    words = text.split()

    
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


# %%
df['processed_text'] = df['clean_text'].apply(preprocess_text)

print("\nPreprocessing Completed")


# %%
tfidf = TfidfVectorizer(max_features=5000)

X = tfidf.fit_transform(df['processed_text'])

y = df['category']

# %%
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# %%
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("\nModel Training Completed")

# %%
y_pred = model.predict(X_test)


# %%
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# %%
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()


# %%
sns.countplot(x=df['category'])

plt.title("Sentiment Distribution")

plt.show()


# %%
def predict_sentiment(text):

    
    processed = preprocess_text(text)

    
    vectorized = tfidf.transform([processed]).toarray()

    
    prediction = model.predict(vectorized)[0]

    
    if prediction == 1:
        return "Positive"

    elif prediction == 0:
        return "Neutral"

    else:
        return "Negative"


# %%
sample_text = "The service was excellent and fast"

result = predict_sentiment(sample_text)

print("\nSample Prediction:")
print("Text:", sample_text)
print("Sentiment:", result)


while True:

    user_text = input("\nEnter a sentence (or type 'exit' to stop): ")

    # Exit condition
    if user_text.lower() == 'exit':
        print("Program stopped.")
        break

    # Predict sentiment
    result = predict_sentiment(user_text)

    print("Predicted Sentiment:", result)
