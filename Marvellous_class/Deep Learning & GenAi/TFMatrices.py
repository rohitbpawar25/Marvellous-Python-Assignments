# ----------------------------------------------------------
# Basic matrix operations with TensorFlow
#
# - Defines two constant matrices A and B
# - Computes matrix multiplication A x B
# - Computes transpose of matrix A
# - Prints results
# ----------------------------------------------------------

import tensorflow as tf

# Define matrices
A = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
B = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)

matmul = tf.matmul(A, B)       # Matrix multiplication
transpose = tf.transpose(A)    # Transpose

print("Matrix A:\n", A.numpy())
print("Matrix B:\n", B.numpy())
print("A x B:\n", matmul.numpy())
print("Transpose of A:\n", transpose.numpy())
