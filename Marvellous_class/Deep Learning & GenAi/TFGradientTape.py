# ----------------------------------------------------------
# Compute gradient using TensorFlow's GradientTape
#
# - Defines a variable x
# - Computes y = x^2 + 2x + 1
# - Calculates dy/dx at x=3 using automatic differentiation
# ----------------------------------------------------------

import tensorflow as tf

x = tf.Variable(3.0)

with tf.GradientTape() as tape:
    y = x**2 + 2*x + 1  # Function y

grad = tape.gradient(y, x)

print("Function: y = x^2 + 2x + 1 at x=3")
print("Gradient dy/dx =", grad.numpy())  # Expected: 8
