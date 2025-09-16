# ------------------------------------------------------------------------
# Simple 2-Layer Neural Network Forward Pass (ReLU + Sigmoid)
#
# - Takes 2 inputs and feeds them through:
#     1. A hidden layer with 2 neurons (ReLU activation)
#     2. An output layer with 1 neuron (Sigmoid activation)
# - Prints detailed step-by-step calculations
# - Shows how inputs are transformed through the network
# ------------------------------------------------------------------------

import math

# ----- Activation Functions -----
def relu(x):
    return max(0, x)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# ----- Forward Pass with Step-by-Step Printing -----
def Marvellous_forward_pass(inputs):
    print("=== INPUT LAYER ===")
    print(f"Inputs: x1 = {inputs[0]}, x2 = {inputs[1]}")

    # ----- Hidden Layer -----
    weights_hidden = [
        [0.5, -0.2],  # Neuron 1 weights
        [0.8, 0.4]    # Neuron 2 weights
    ]
    bias_hidden = [0.1, -0.1]  # Bias for each hidden neuron

    hidden_outputs = []
    print("\n=== HIDDEN LAYER ===")
    for i in range(len(weights_hidden)):
        print(f"\nNeuron {i+1}:")
        w = weights_hidden[i]
        b = bias_hidden[i]

        print(" Step 1: Multiply inputs by weights:")
        print(f" ({w[0]} * {inputs[0]}) = {w[0] * inputs[0]:.3f}")
        print(f" ({w[1]} * {inputs[1]}) = {w[1] * inputs[1]:.3f}")

        z = sum(w_j * x_j for w_j, x_j in zip(w, inputs)) + b
        print(f" Step 2: Add results and bias {b}: z = {z:.3f}")

        a = relu(z)
        print(f" Step 3: Apply ReLU: max(0, {z:.3f}) = {a:.3f}")
        hidden_outputs.append(a)

    # ----- Output Layer -----
    weights_output = [1.0, -1.5]
    bias_output = 0.2

    print("\n=== OUTPUT LAYER ===")
    print(" Step 1: Multiply hidden outputs by weights:")
    print(f" ({weights_output[0]} * {hidden_outputs[0]}) = {weights_output[0] * hidden_outputs[0]:.3f}")
    print(f" ({weights_output[1]} * {hidden_outputs[1]}) = {weights_output[1] * hidden_outputs[1]:.3f}")

    z_out = sum(w_o * h for w_o, h in zip(weights_output, hidden_outputs)) + bias_output
    print(f" Step 2: Add results and bias {bias_output}: z = {z_out:.3f}")

    y_hat = sigmoid(z_out)
    print(f" Step 3: Apply Sigmoid: 1 / (1 + e^(-{z_out:.3f})) = {y_hat:.3f}")
    print(f"\nFinal Output: {y_hat:.3f} → {y_hat*100:.2f}% confidence in Positive Class")

# ----- Run Example -----
if __name__ == "__main__":
    inputs = [2.0, 3.0]  # Example input features
    Marvellous_forward_pass(inputs)
