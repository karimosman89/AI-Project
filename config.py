import os

class Config:
    MODEL_PATH = os.getenv('MODEL_PATH', 'src/model/model.h5')
    DATA_PATH = os.getenv('DATA_PATH', 'data/processed/')
    EPOCHS = int(os.getenv('EPOCHS', 10))
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', 32))
    FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
