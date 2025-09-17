# 💬 Sentiment Analysis Using Simple RNN (Keras)

---

## 🧾 Project Overview

**Title:** Sentiment Analysis Using Simple RNN  
**Objective:** Build and train a simple Recurrent Neural Network (RNN) using Keras to classify text sentences as **Positive** or **Negative** sentiments.

---

## ⚙️ Features

- Small custom dataset with positive and negative movie review sentences
- Text tokenization and sequence padding
- Embedding layer + SimpleRNN layer + Dense output layer
- Binary classification output (`Positive` or `Negative`)
- Tests on new unseen sentences

---

## 🧰 Dependencies

Install the required packages using:

```bash
pip install numpy tensorflow
```

---

## 🧠 Model Architecture

| Layer         | Type        | Details                         |
|---------------|--------------|---------------------------|
| 1             | Embedding       | `input_dim=50`, `output_dim=8` |
| 2             | SimpleRNN      | `units=8`, activation=`tanh` |
| 3             | Dense             | `units=1`, activation=`sigmoid` |

- **Loss:** Binary Crossentropy  
- **Optimizer:** Adam  
- **Metrics:** Accuracy  

---

## 📂 Workflow

1. **Prepare Dataset**  
   A small set of positive and negative sentences with labels (1 = Positive, 0 = Negative).

2. **Tokenize Text**  
   Use `Tokenizer` to convert words into integer sequences.

3. **Pad Sequences**  
   Make all sequences the same length using `pad_sequences`.

4. **Build Model**  
   Embedding → SimpleRNN → Dense architecture using Keras `Sequential` API.

5. **Train Model**  
   Fit the model on the labeled dataset for 30 epochs.

6. **Test Model**  
   Provide new sentences and get predicted sentiment (Positive or Negative).

---

## 🚀 Running the Project

1. Save the script as `Assignment35.py`.
2. Run it using:

```bash
python3 Assignment35.py
```

3. View predictions for new sentences in the console output.

---

## 📊 Example Output

```
Input dataset:
['I love this movie', 'This film was great', ... , 'Absolutely horrible acting']

Word Index: {'i': 1, 'this': 2, 'movie': 3, ...}

Sentence: I enjoyed this film -> Sentiment: Positive  
Sentence: I hated this film -> Sentiment: Negative
```

---

## 📜 Author

- **Name:** Rohit Pawar  
- **Date:** 17-09-2025

---
