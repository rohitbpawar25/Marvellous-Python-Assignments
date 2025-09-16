# Simple RNN cell manual calculation:
# Processes a sequence step-by-step, updating hidden state using tanh activation,
# simulating how RNN captures sequential dependencies.

import numpy as np

sequence = [1, 2, 3]  # Encoded sentence: "I love AI"
Wx, Wh, b = 0.5, 0.8, 0.1
h = 0  # Initial hidden state

print("Processing sequence step by step:")
for t, x in enumerate(sequence):
    h = np.tanh(Wx * x + Wh * h + b)
    print(f"Timestep {t+1} | Input={x} | Hidden State={h:.4f}")
