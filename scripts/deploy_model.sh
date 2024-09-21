#!/bin/bash
# Deploy model using Kubernetes
echo "Deploying model to Kubernetes..."
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
echo "Model deployment completed!"
