provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "mlflow_bucket" {
  bucket = "mlflow-artifacts-bucket"
}

resource "aws_eks_cluster" "ai_cluster" {
  name     = "ai-cluster"
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids = aws_subnet.public.*.id
  }
}

resource "aws_iam_role" "eks_role" {
  name = "eksClusterRole"
  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "eks.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  })
}
