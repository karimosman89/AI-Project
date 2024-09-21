import numpy as np
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

class ModelMonitor:
    def __init__(self, model_path, test_data_path, threshold=0.8):
        self.model = joblib.load(model_path)
        self.test_data = pd.read_csv(test_data_path)
        self.threshold = threshold

    def evaluate_model(self):
        """Evaluate the model and check if accuracy exceeds the threshold."""
        X_test = self.test_data.drop('label', axis=1)  # Adjust according to your data
        y_test = self.test_data['label']
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        
        print(f"Model Accuracy: {accuracy:.2f}")
        if accuracy < self.threshold:
            print("Warning: Model accuracy is below the threshold!")
        return accuracy

if __name__ == "__main__":
    monitor = ModelMonitor('src/model/model.h5', 'data/processed/test_data.csv')
    monitor.evaluate_model()
