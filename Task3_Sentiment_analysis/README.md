# Sentiment Analysis using Machine Learning

## Project Overview
This project is a **Sentiment Analysis System** developed using **Natural Language Processing (NLP)** and **Machine Learning** techniques. The model analyzes textual data and predicts whether the sentiment expressed in the text is:

- Positive
- Negative
- Neutral

The project uses a Twitter dataset to train the model and classify sentiments from user input.

---

# Features

- Text preprocessing using NLP
- TF-IDF feature extraction
- Machine Learning-based sentiment classification
- Real-time sentiment prediction
- Supports multiple sentence predictions
- Data visualization using graphs
- Confusion matrix and classification report

---

# Technologies Used

## Programming Language
- Python

## Libraries
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- scikit-learn

---

# Dataset

The project uses the **Twitter Sentiment Dataset** containing:
- Tweet text
- Sentiment labels

## Sentiment Labels
| Label | Sentiment |
|------|-----------|
| -1 | Negative |
| 0 | Neutral |
| 1 | Positive |

---

# Project Workflow

```text
Data Collection
      ↓
Text Preprocessing
      ↓
Feature Extraction (TF-IDF)
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Sentiment Prediction
      ↓
Performance Evaluation
```

---

# NLP Preprocessing Steps

The following preprocessing techniques are applied:

- Lowercasing
- Removing URLs
- Removing special characters
- Tokenization
- Stopword removal
- Lemmatization

---

# Machine Learning Model

The project uses:

## Logistic Regression
A supervised machine learning algorithm used for text classification and sentiment prediction.

---

# Installation

## Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn
```

---

# Running the Project

## Execute the Python File

```bash
python sentiment_analysis.py
```

---

# Example Prediction

## Input

```text
I really love this product
```

## Output

```text
Predicted Sentiment: Positive
```

---

# Multiple Predictions Feature

The project supports continuous predictions using a loop.

Example:

```text
Enter a sentence:
This movie is amazing

Predicted Sentiment: Positive

Enter a sentence:
The service is terrible

Predicted Sentiment: Negative
```

Type `exit` to stop the program.

---

# Model Evaluation

The project evaluates performance using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# Visualizations

The project includes:
- Sentiment distribution graph
- Confusion matrix heatmap

---

# Folder Structure

```text
sentiment-analysis/
│
├── Twitter_Data.csv
├── sentiment_analysis.py
├── README.md
```

---

# Future Enhancements

- Deep Learning models (LSTM/BERT)
- Real-time Twitter sentiment analysis
- Web application deployment
- Multilingual sentiment detection
- Emotion analysis

---

# Applications

- Social media monitoring
- Customer feedback analysis
- Product review analysis
- Brand reputation management
- Market research

---

# Conclusion

This project demonstrates how NLP and Machine Learning can be used to automatically analyze sentiments from text data. It helps organizations understand public opinion and customer feedback efficiently.

---
