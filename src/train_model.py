import mlflow
import mlflow.tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
import pandas as pd

def create_model(input_shape=(32, 32, 3), num_classes=10):
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    return model

if __name__ == "__main__":
    mlflow.start_run()  # Start MLflow run
    mlflow.tensorflow.autolog()  # Automatically log TensorFlow model
    
    model = create_model()
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    # Load preprocessed data from S3
    X_train = pd.read_csv('/tmp/X_train_preprocessed.csv').values
    y_train = pd.read_csv('/tmp/y_train.csv').values
    
    model.fit(X_train, y_train, epochs=10, batch_size=64)
    
    # Save model to MLflow
    mlflow.end_run()
