import os

class Config:
    # Load environment variables
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    MODEL_PATH = os.getenv('MODEL_PATH', 'model/model.pkl')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'warning')

    # Machine Learning specific hyperparameters
    RANDOM_STATE = 42
    TEST_SIZE = 0.2
    N_ESTIMATORS = 100  # for RandomForest
