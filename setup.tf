# Define provider and backend configurations
terraform {
    required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "3.56.0"
        }
    }

    backend "s3" {
        bucket = "my-terraform-state-bucket"
        key    = "terraform.tfstate"
        region = "us-west-2"
    }
}

# Create an AWS EC2 instance
resource "aws_instance" "example" {
    ami           = "ami-0c94855ba95c71c99"
    instance_type = "t2.micro"
    subnet_id     = "subnet-0123456789abcdef0"
}

# Example of handling secrets securely
data "aws_secretsmanager_secret" "example_secret" {
    name = "my-secret"
}

resource "aws_instance" "example_with_secret" {
    ami           = "ami-0c94855ba95c71c99"
    instance_type = "t2.micro"
    subnet_id     = "subnet-0123456789abcdef0"

    user_data = <<-EOF
        #!/bin/bash
        echo "Retrieving secret..."
        secret_value=$(aws secretsmanager get-secret-value --secret-id ${data.aws_secretsmanager_secret.example_secret.arn} --query SecretString --output text)
        echo "Secret value: $secret_value"
        # Rest of the user data script...
    EOF
}
