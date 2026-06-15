terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "raw_zone" {
  bucket = "prithiv-ecommerce-raw-751835847273"

  tags = {
    Name        = "Raw Zone"
    Environment = "Dev"
    Project     = "Ecommerce Analytics"
  }
}