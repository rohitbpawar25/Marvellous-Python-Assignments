# ----------------------------------------------------------
# Basic TensorFlow Arithmetic Operations Example
#
# - Creates two constant tensors a and b
# - Performs addition, subtraction, multiplication, and division
# - Prints results using .numpy() to get values from tensors
# ----------------------------------------------------------

import tensorflow as tf

a = tf.constant(5)
b = tf.constant(3)

add = tf.add(a, b)
sub = tf.subtract(a, b)
mul = tf.multiply(a, b)
div = tf.divide(a, b)

print("a + b =", add.numpy())
print("a - b =", sub.numpy())
print("a * b =", mul.numpy())
print("a / b =", div.numpy())
