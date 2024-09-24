from keras.models import load_model
import unittest
import os
import numpy as np

class TestTrainModel(unittest.TestCase):
    def setUp(self):
        # Load Keras model for testing
        self.model_path = 'src/model/model.h5'
        self.model = load_model(self.model_path) if os.path.exists(self.model_path) else None

    def test_model_loaded(self):
        """Test if model is loaded successfully"""
        self.assertIsNotNone(self.model)

    def test_model_prediction(self):
        """Test model prediction output shape"""
        dummy_input = np.random.rand(1, 32, 32, 3)  # CIFAR-10 input shape
        prediction = self.model.predict(dummy_input)
        self.assertEqual(prediction.shape[0], 1)

if __name__ == "__main__":
    unittest.main()

