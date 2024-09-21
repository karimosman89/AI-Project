import unittest
import os
import tensorflow as tf

class TestPreprocessing(unittest.TestCase):
    def test_data_loading(self):
        """Test that preprocessed data exists and loads correctly"""
        processed_data_path = "data/processed/x_train"
        self.assertTrue(os.path.exists(processed_data_path))

        # Check if the data is a valid TensorFlow dataset
        dataset = tf.data.experimental.load(processed_data_path)
        self.assertIsInstance(dataset, tf.data.Dataset)

if __name__ == "__main__":
    unittest.main()
