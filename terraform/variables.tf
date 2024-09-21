variable "aws_region" {
  description = "The AWS region where resources will be deployed"
  default     = "us-west-2"
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket"
  default     = "mlflow-artifacts-bucket"
}
