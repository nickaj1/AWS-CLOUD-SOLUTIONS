AWS VPC & EC2 Setup – Practical Implementation
This project demonstrates how I configured a Virtual Private Cloud (VPC), configured internet-gateway and route table,created subnets, attached security settings, and launched EC2 instances using the AWS Management Console. Below are the exact steps I followed with supporting screenshots for each task.


Task 1: Created VPC and Subnets
I navigated to the VPC service in the AWS Console and created a new VPC with the following configuration:

VPC Name: nick-vpc

CIDR Block: 10.0.0.0/16

Screenshot:

Next, I created two subnets in different Availability Zones under the same VPC:

Subnet 1:

AZ: us-east-1a

CIDR: 10.0.1.0/24

Subnet 2:

AZ: us-east-1b

CIDR: 10.0.2.0/24

Screenshots:



Task 2: Configured Security and Routing
I created an Internet Gateway, attached it to the VPC, and then:

Created a Route Table

Added a route for 0.0.0.0/0 pointing to the Internet Gateway

Associated this route table with both subnets

Screenshots:


Then I configured a Security Group named AllowSSH:

Inbound Rule: SSH (Port 22)

Source: 0.0.0.0/0 (for testing, but normally would restrict to specific IP)

Screenshot:


Task 3: Launched EC2 Instances
I launched two EC2 instances using Amazon Linux 2 AMI and t2.micro instance type:

Instance 1: Placed in Subnet-1 (us-east-1a)

Instance 2: Placed in Subnet-2 (us-east-1b)

Assigned both instances the AllowSSH security group

Used an existing key pair for access

Screenshots:


Task 4: Access and Testing
After both instances were running, I used their public IPs to SSH into them from my terminal using: