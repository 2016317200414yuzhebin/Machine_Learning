import tensorflow as tf
import time

class FileDataset(tf.data.Dataset):
    def read_file_in_batches(num_samples):
        # Opening the file
        time.sleep(0.03)

        for sample_idx in range(num_samples):
            # Reading data (line, record) from the file
            time.sleep(0.015)

            yield (sample_idx,)

    def __new__(cls, num_samples = 3):
        return tf.data.Dataset.from_generator(
            cls.read_file_in_batches,
            output_signature = tf.TensorSpec(shape = (1,), dtype = tf.int64),
            args = (num_samples,)
        )

def benchmark(dataset, num_epochs = 2):
    for _ in range(num_epochs):
        for __ in dataset:
            # Performing a training step
            time.sleep(0.01)

benchmark(FileDataset())
benchmark(FileDataset().prefetch(1))
benchmark(FileDataset().prefetch(tf.data.AUTOTUNE))

dataset = tf.data.Dataset.range(5)
dataset = dataset.map(lambda x: x**2)
dataset = dataset.cache("mycache.txt")

def mapped_function(s):
    # Do some hard pre-processing
    tf.py_function(lambda: time.sleep(0.03), [], ())
    return s

benchmark(FileDataset().map(mapped_function), 5)
benchmark(FileDataset().map(mapped_function).cache(), 5)