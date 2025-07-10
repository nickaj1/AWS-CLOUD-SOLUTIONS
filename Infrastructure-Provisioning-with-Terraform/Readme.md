Creating the AWS Lambda Function with Terraform
To begin my infrastructure provisioning, I started by creating an AWS Lambda function using Terraform. 

Here's how I accomplished this step:
Defined the Lambda Function Resource

I used the aws_lambda_function block in my Terraform file to define the Lambda function. This included specifying:
The function name.
The runtime environment (e.g., Python 3.9 or Node.js 18.x).
The handler (e.g., lambda_function.lambda_handler for Python).
The source code location using filename pointing to a zipped deployment package.

Set Up IAM Role and Permissions
I created a basic IAM role using the aws_iam_role resource. This role allowed the Lambda function to execute by attaching the AWSLambdaBasicExecutionRole managed policy.

Attached Role to Lambda
I referenced the IAM role in the role field of the aws_lambda_function resource so the function could write logs to Amazon CloudWatch.