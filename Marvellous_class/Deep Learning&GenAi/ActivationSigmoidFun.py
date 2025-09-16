# ------------------------------------------------------------------------
# Single Neuron Forward Pass using Sigmoid Activation + Sigmoid Plot
#
# - Computes output of a single neuron: z = w·x + b
# - Applies the Sigmoid activation function
# - Prints step-by-step calculations
# - Plots the Sigmoid activation function for visualization
# ------------------------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

# Sigmoid activation function
def sigmoid(z):
    """Sigmoid function: squashes values to (0,1) range."""
    return 1 / (1 + math.exp(-z))

# ---- Neuron calculation ----
def Marvellous_neuron_forward(inputs, weights, bias):
    print("Inputs (x): ", inputs)
    print("Weights (w):", weights)
    print("Bias (b): ", bias)
    z = sum(w * x for w, x in zip(weights, inputs)) + bias
    print("Summation (z = w·x + b):", z)
    y_hat = sigmoid(z)
    print("Activation Function: Sigmoid")
    print("Output (ŷ = sigmoid(z)):", y_hat)
    return z, y_hat

# ---- Plot Sigmoid function ----
def plot_sigmoid():
    z_values = np.linspace(-10, 10, 200)
    sigmoid_values = 1 / (1 + np.exp(-z_values))
    plt.figure(figsize=(8, 5))
    plt.plot(z_values, sigmoid_values, label="Sigmoid", linewidth=2, color="blue")
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axhline(y=1, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")
    plt.title("Sigmoid Activation Function", fontsize=16)
    plt.xlabel("Summation (z)", fontsize=14)
    plt.ylabel("Activation Output", fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()

def main():
    inputs = [1.0, 2.0, 3.0]
    weights = [0.6, 0.4, -0.2]
    bias = 0.5
    z, y_hat = Marvellous_neuron_forward(inputs, weights, bias)
    plot_sigmoid()

if __name__ == "__main__":
    main()
