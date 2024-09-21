import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='model_performance.log', format='%(asctime)s - %(levelname)s - %(message)s')

def log_performance(accuracy):
    """Log model performance metrics."""
    logging.info(f'Model Accuracy: {accuracy:.2f}')

if __name__ == "__main__":
    from model_monitoring import ModelMonitor

    monitor = ModelMonitor('src/model/model.h5', 'data/processed/test_data.csv')
    accuracy = monitor.evaluate_model()
    log_performance(accuracy)
