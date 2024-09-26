#  AI Project

This repository contains an end-to-end AI project that covers data ingestion, preprocessing, model training, and deployment, along with CI/CD and orchestration tools.
# CIFAR-10 Image Classification

A complete project using CIFAR-10 for image classification, showcasing Data Engineering, AI, Machine Learning, and DevOps skills. The project includes a fully automated pipeline using Airflow, Docker, and Kubernetes.

### Main Features:
- **Model Training**: CNN with TensorFlow.
- **Deployment**: Flask API containerized and deployed on Kubernetes (EKS).
- **Monitoring**: Real-time monitoring with Prometheus and Grafana.

## Setup Instructions
1. Clone the repository.
2. Install dependencies with:


         pip install -r requirements.txt 

   
3. Run the Docker container:

  
       `docker-compose up`.

   
4. Access the Flask API at


          `http://localhost:5000/predict`


## Key Technologies
- Apache Airflow for orchestration.
- TensorFlow for model training.
- Flask for API deployment.
- Docker & Kubernetes for containerization and orchestration.
- Terraform for infrastructure as code.

## Features

- **Data Ingestion:** Uses Apache Airflow for ETL
- **Model Training:** Scikit-learn Random Forest Classifier
- **Deployment:** Flask API serving the trained model
- **CI/CD:** GitHub Actions for Continuous Integration and Continuous Deployment
- **Containerization:** Docker for containerizing the API and pipeline
- **Orchestration:** Kubernetes for deployment on EKS

## Project Structure

       AI-Project/
                 │
                 ├── data/                                # Raw and processed data
                         │   
                         ├── raw/                             # Raw data (downloaded)
                         │   
                         └── processed/                       # Processed data after ETL
                 │
                 ├── dags/                                # Apache Airflow DAGs for orchestration
                         │ 
                         ├── data_ingestion.py                # Airflow DAG for data ingestion
                         │
                         └── data_preprocessing.py            # Airflow DAG for data preprocessing
                 │
                 ├── src/                                 # Core source code
                        │ 
                        ├── preprocessing.py                 # Python script for data preprocessing
                        │
                        ├── train_model.py                   # Script to train the ML model
                        │ 
                        ├── app.py                           # Flask API for serving the model
                        │
                        └── model/                           # Model-related code and artifacts
                                 │     
                                 └── model.pkl                    # Serialized trained model
                 │
                 ├── notebooks/                           # Jupyter Notebooks for EDA, experiment tracking
                              │
                              └── eda.ipynb                        # Exploratory Data Analysis notebook
                 │
                 ├── mlruns/                              # MLflow artifacts (tracked experiments)
                           │
                           └── 0/                               # MLflow experiment folders
                 │
                 ├── docker/                              # Docker-related files
                           │
                           ├── Dockerfile                       # Dockerfile for containerizing the app
                           │
                           └── docker-compose.yml               # Compose file for multi-container setup
                 │
                 ├── k8s/                                 # Kubernetes configuration for EKS deployment
                        │
                        ├── deployment.yaml                  # Kubernetes deployment configuration
                        │ 
                        ├── service.yaml                     # Kubernetes service configuration
                        │
                        └── configmap.yaml                   # ConfigMap for environment variables
                 │
                 ├── .github/                             # GitHub Actions CI/CD pipeline
                            │
                            └── workflows/
                                         │
                                         └── main.yml                     # GitHub Actions for CI/CD pipeline
                 │
                 ├── requirements.txt                     # Python dependencies
                 ├── Dockerfile                           # Docker configuration for app containerization
                 ├── README.md                            # Documentation
                 ├── app.py                               # Flask API for model inference
                 ├── config.py                            # Configuration file (paths, hyperparameters, etc.)
                 └── setup.py                             # Python package setup file




## Installation

### Prerequisites

- Python 3.8+
- Docker
- Kubernetes (for deployment)
- Apache Airflow (for orchestration)

### Step-by-step Instructions

1. **Clone the repo:**

   ```bash
   git clone https://github.com/your_username/ai_project.git
   cd ai_project



2. **Install dependencies:**

   
        pip install -r requirements.txt

3. **Run Preprocessing:**

   
       python src/preprocessing.py

4. **Train the Model:**

   
       python src/train_model.py

5. **Run the Flask API:**

   
        python src/app.py

## Running with Docker

1. **Build the Docker image:**

       docker build -t flask-app .

2. **Run the container:**


       docker run -p 5000:5000 flask-app


## Deployment with Kubernetes

1. **Apply the deployment:**
 
       kubectl apply -f k8s/deployment.yaml

2. **Apply the service:**

        kubectl apply -f k8s/service.yaml

## CI/CD Pipeline

**The project uses GitHub Actions for CI/CD:**

 1. Build: The code is built and tested.
 2. Test: Unit tests are executed using pytest.
 3.  Deploy: Docker images are built and pushed to a registry, followed by Kubernetes deployment.
   
### License
This project is licensed under the MIT License.


### Summary

- **`configmap.yaml`**: Stores environment variables and configuration for Kubernetes pods.
- **`config.py`**: Centralized configuration file for Python app, loading environment variables and constants.
- **`setup.py`**: Allows packaging the project as a Python package and defining console commands.
- **`README.md`**: Documentation that describes the project structure, setup, installation, and usage.

This completes the advanced and professional project setup, covering AI, Data Engineering, 
   

  
