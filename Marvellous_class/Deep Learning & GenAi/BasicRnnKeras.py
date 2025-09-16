# ------------------------------------------------------------------------
# Simple RNN Model for Binary Classification (Keras)
#
# - Generates random integer input sequences (shape: 10 samples × 5 timesteps)
# - Uses an Embedding layer to convert tokens to vectors
# - Passes sequences through a SimpleRNN layer (16 units)
# - Outputs binary predictions via a Dense layer with Sigmoid activation
# - Compiles and trains the model on random binary labels
# - Prints a sample prediction for the first input sequence
# ------------------------------------------------------------------------

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding

X = np.random.randint(20, size=(10, 5))  # Input sequences
y = np.random.randint(2, size=(10, 1))   # Binary labels
model = Sequential()
model.add(Embedding(input_dim=20, output_dim=8, input_length=5))
model.add(SimpleRNN(16, activation='tanh'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=5, verbose=1)

print("Sample Prediction:", model.predict(X[:1]))
