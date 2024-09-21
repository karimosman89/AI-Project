from setuptools import setup, find_packages

setup(
    name="AI-Project-CIFAR10",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow==2.6.0",
        "flask",
        "pandas",
        "mlflow",
        "numpy",
        "Pillow",
        "airflow",
        "boto3",
        "kubernetes",
        "scikit-learn",
        "matplotlib"
    ],
    entry_points={
        "console_scripts": [
            "train_model=src.train_model:train_model",
            "preprocess_images=src.preprocessing:preprocess_images"
        ]
    }
)

