# Tweet Sentiment Classifier using Semi-Supervised Learning

This project uses **semi-supervised learning** to classify the sentiment of tweets using a dataset with text content and sentiment labels. It leverages the power of **Self-Training Classifier** with a base Ridge Classifier to handle both labeled and unlabeled data.

---

## 📌 Features

- Text classification using NLP techniques
- CountVectorizer + TF-IDF transformation
- Semi-supervised learning via `SelfTrainingClassifier`
- Sentiment prediction on new sample inputs

---

## 🧠 How It Works

1. Load and split the tweet dataset.
2. Preprocess the text using CountVectorizer and TF-IDF.
3. Train a `SelfTrainingClassifier` (with `RidgeClassifier` as base).
4. Predict sentiment on unseen texts.

---

## 📂 Dataset

Place a `tweet_emotions.csv` file in the project directory.

### Sample Format:

| content                           | sentiment   |
|----------------------------------|-------------|
| I love this!                     | happy       |
| I'm so sad right now             | sad         |
| This is terrible                 | angry       |

---
