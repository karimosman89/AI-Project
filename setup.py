from setuptools import setup, find_packages

setup(
    name='ai_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'pandas',
        'scikit-learn',
        'mlflow',
        'joblib',
    ],
    entry_points={
        'console_scripts': [
            'preprocess=src.preprocessing:preprocess_data',
            'train=src.train_model:train_model',
        ],
    },
    author='Your Name',
    description='End-to-end AI project with ML training, API deployment, and CI/CD pipeline',
    license='MIT'
)
