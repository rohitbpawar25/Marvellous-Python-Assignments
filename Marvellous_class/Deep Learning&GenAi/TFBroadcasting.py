# ----------------------------------------------------------
# TensorFlow Broadcasting Example
#
# - Defines a 1D tensor C and a scalar tensor D
# - Demonstrates broadcasting by adding and multiplying C with D
# - Prints the original tensor and results
# ----------------------------------------------------------

import tensorflow as tf

C = tf.constant([1, 2, 3], dtype=tf.float32)
D = tf.constant(2.0)

broadcast_add = C + D
broadcast_mul = C * D

print("C:", C.numpy())
print("C + D:", broadcast_add.numpy())
print("C * D:", broadcast_mul.numpy())
