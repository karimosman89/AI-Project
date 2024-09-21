#!/bin/bash
# Start Airflow with Docker Compose
echo "Starting Apache Airflow..."
docker-compose -f airflow/docker-compose.yaml up -d
echo "Apache Airflow started!"
