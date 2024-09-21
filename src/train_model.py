import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from mlflow import log_metric, log_param, log_artifact
import mlflow

def train_model(data_dir, model_save_path):
    """
    Train a CNN on CIFAR-10 and log the results to MLflow.
    """
    mlflow.start_run()
    
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])

    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

    log_param("optimizer", "Adam")
    log_param("batch_size", 32)

    # Load data
    train_data = tf.keras.preprocessing.image_dataset_from_directory(data_dir, batch_size=32, image_size=(32, 32))

    # Train
    history = model.fit(train_data, epochs=10)

    log_metric("accuracy", history.history['accuracy'][-1])
    model.save(model_save_path)
    mlflow.log_artifact(model_save_path)
    
    mlflow.end_run()

if __name__ == '__main__':
    train_model('data/processed/', 'src/model/model.h5')
