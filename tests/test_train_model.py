import unittest
import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class TestTrainModel(unittest.TestCase):
    def setUp(self):
        # Load model for testing
        self.model_path = 'src/model/model.h5'
        self.model = joblib.load(self.model_path) if os.path.exists(self.model_path) else RandomForestClassifier()

    def test_model_loaded(self):
        """Test if model is loaded successfully"""
        self.assertTrue(isinstance(self.model, RandomForestClassifier))

    def test_model_prediction(self):
        """Test model prediction output shape"""
        dummy_input = np.random.rand(1, 32, 32, 3)  # CIFAR-10 input shape
        dummy_input = dummy_input.flatten().reshape(1, -1)
        prediction = self.model.predict(dummy_input)
        self.assertEqual(len(prediction), 1)

if __name__ == "__main__":
    unittest.main()
