import unittest
import requests
import json

class TestIntegration(unittest.TestCase):
    def test_prediction_endpoint(self):
        """Test the Flask prediction endpoint for a valid response"""
        url = "http://localhost:5000/predict"
        headers = {"Content-Type": "application/json"}
        data = {
            "image": [0.5] * 32 * 32 * 3  # Flattened 32x32x3 image for CIFAR-10
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json())

if __name__ == "__main__":
    unittest.main()
