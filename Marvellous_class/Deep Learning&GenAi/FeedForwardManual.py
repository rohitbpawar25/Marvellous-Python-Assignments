# ----------------------------------------------------------
# Manual Feedforward Pass of a Simple 2-Layer Neural Network
#
# - Input layer with 2 features
# - Hidden layer with 2 neurons using ReLU activation
# - Output layer with 1 neuron using Sigmoid activation
# - Performs step-by-step calculation and prints intermediate values
# ----------------------------------------------------------

import math

# Activation functions
def relu(x):
    return max(0.0, x)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Input vector
x = [2.0, 3.0]

# Hidden layer weights and biases
W1 = [[0.5, -0.2], [0.8, 0.4]]
b1 = [0.1, -0.1]

# Hidden neuron 1 computation
z1 = W1[0][0]*x[0] + W1[0][1]*x[1] + b1[0]
a1 = relu(z1)
print(f"Neuron1: z={z1:.3f}, a={a1:.3f}")

# Hidden neuron 2 computation
z2 = W1[1][0]*x[0] + W1[1][1]*x[1] + b1[1]
a2 = relu(z2)
print(f"Neuron2: z={z2:.3f}, a={a2:.3f}")

# Output layer weights and bias
W2 = [1.2, -0.7]
b2 = 0.05

# Output neuron computation
z_out = W2[0]*a1 + W2[1]*a2 + b2
yhat = sigmoid(z_out)
print(f"Output: z={z_out:.3f}, sigmoid(y)={yhat:.4f}")
