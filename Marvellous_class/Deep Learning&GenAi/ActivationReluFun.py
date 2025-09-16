# ---------------------------------------------------------------
# Single Neuron Forward Pass with ReLU Activation + ReLU Plot
# 
# - Computes output of a neuron: z = w·x + b, then applies ReLU
# - Prints each step of the calculation
# - Plots the ReLU activation function
# ---------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# ReLU activation function
def relu(z):
    return max(0, z)

# ---- Neuron calculation ----
def Marvellous_neuron_forward(inputs, weights, bias):
    print("Inputs (x): ", inputs)
    print("Weights (w):", weights)
    print("Bias (b): ", bias)
    z = sum(w * x for w, x in zip(weights, inputs)) + bias
    print("Summation (z = w·x + b):", z)
    y_hat = relu(z)
    print("Activation Function: ReLU")
    print("Output (ŷ = relu(z)):", y_hat)
    return z, y_hat

def plot_relu():
    z_values = np.linspace(-10, 10, 200)
    relu_values = np.maximum(0, z_values)
    plt.figure(figsize=(8, 5))
    plt.plot(z_values, relu_values, label="ReLU", linewidth=2, color="green")
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")
    plt.title("ReLU Activation Function", fontsize=16)
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
    plot_relu()

if __name__ == "__main__":
    main()
