import os

class Config:
    # Paths
    MODEL_PATH = os.getenv("MODEL_PATH", "/app/src/model/model.h5")
    DATA_PATH = os.getenv("DATA_PATH", "/app/data/processed/")

    # Training Parameters
    EPOCHS = int(os.getenv("EPOCHS", 10))
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", 32))

    # Flask Server Config
    FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
    FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))

    # MLFlow tracking URI
    MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5001")

config = Config()
