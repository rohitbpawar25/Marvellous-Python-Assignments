# ----------------------------------------------------------
# Create and display TensorFlow constant tensors
#
# - Defines two scalar constant tensors a and b
# - Prints the tensor objects (not their values)
# ----------------------------------------------------------

import tensorflow as tf

# Create constant tensors
a = tf.constant(5)
b = tf.constant(3)

print("Tensor a:", a)
print("Tensor b:", b)
