########################################################
# Required Python Packages
########################################################
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

########################################################
# Sentiment_Analysis
# Description:
#   Builds a simple RNN model to classify sentiment
#   on a tiny dataset (Positive = 1, Negative = 0)
# Steps:
#   1) Create small dataset
#   2) Tokenize and pad sequences
#   3) Build and compile RNN model
#   4) Train the model
#   5) Test the model on unseen sentences
########################################################
def Sentiment_Analysis():
    ########################################################
    # 1) Tiny dataset (Positive = 1, Negative = 0)
    ########################################################
    sentences = [
        "I love this movie", "This film was great", "What a fantastic experience",
        "I really enjoyed it", "Absolutely wonderful acting",
        "I hate this movie", "This film was terrible", "What a bad experience",
        "I really disliked it", "Absolutely horrible acting"
    ]
    print("Input dataset:")
    print(sentences)
    labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

    ########################################################
    # 2) Tokenize text → convert words to integers
    ########################################################
    tokenizer = Tokenizer(num_words=50)
    tokenizer.fit_on_texts(sentences)
    X = tokenizer.texts_to_sequences(sentences)
    print("Word Index:", tokenizer.word_index)

    ########################################################
    # 3) Pad sequences → same length input
    ########################################################
    maxlen = 5
    X = pad_sequences(X, maxlen=maxlen)
    y = np.array(labels)

    ########################################################
    # 4) Build simple RNN model
    ########################################################
    model = Sequential()
    model.add(Embedding(input_dim=50, output_dim=8, input_length=maxlen))
    model.add(SimpleRNN(8, activation="tanh"))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    ########################################################
    # 5) Train the model
    ########################################################
    model.fit(X, y, epochs=30, verbose=0)

    ########################################################
    # 6) Test on new examples
    ########################################################
    test_sentences = ["I enjoyed this film", "I hated this film"]
    test_seq = tokenizer.texts_to_sequences(test_sentences)
    test_seq = pad_sequences(test_seq, maxlen=maxlen)
    pred = model.predict(test_seq)

    for s, p in zip(test_sentences, pred):
        print(f"Sentence: {s} -> Sentiment:", "Positive" if p > 0.5 else "Negative")

########################################################
# Main Execution
# Case Study : Sentiment Analysis using RNN
# Author: Rohit Pawar
# Date: 17-09-2025
########################################################
def main():
    print("-" * 90)
    print("Case Study: Sentiment Analysis using RNN".center(90))
    print("Author: Rohit Pawar".center(90))
    print("Date: 17-09-2025".center(90))
    print("-" * 90)

    Sentiment_Analysis()

########################################################
# Run the main function
########################################################
if __name__ == "__main__":
    main()
