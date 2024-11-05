import tensorflow as tf

# Create a random tensor with compatible shapes for multiplication
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  # Shape (2, 3)
b = tf.constant([[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]])  # Shape (3, 2)

c = tf.matmul(a, b)  # Now this will work
print("Result of matrix multiplication:", c.numpy())

