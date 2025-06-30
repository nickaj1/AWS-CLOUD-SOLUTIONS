Project Overview

This project demonstrates the step-by-step deployment of a 3-tier web application architecture on AWS. 
It covers the design and implementation of a secure, scalable, and highly available infrastructure using core AWS services. 

Key features include:
VPC Design: Structured network with public and private subnets to isolate application tiers.

Security Best Practices: Implementation of security groups, network ACLs, and IAM roles to secure all resources.

Load Balancing & Auto Scaling: Setup of load balancers and auto scaling groups to manage traffic and ensure high availability.

Monitoring & Logging: Integration of AWS monitoring and logging tools to track application performance and maintain system health.



Project Challenges
Throughout the project, several infrastructure and operational challenges were addressed:

Security Management: Maintaining a secure environment with restricted access, encryption, and compliance controls.

High Availability: Ensuring consistent performance and reliability through fault-tolerant design.

Auto-Scaling Configuration: Defining appropriate thresholds to scale without incurring unnecessary costs.

Load Balancer Setup: Properly routing traffic and enabling failover for resilient application access.

Database Connectivity: Establishing low-latency, secure communication between application and database layers.

Monitoring and Alerts: Enabling real-time observability and proactive incident response.

Let me know if you’d like to add badges, architecture diagrams, or quick-start steps.



Project Deliverables
This project includes the following artifacts and configurations as part of the final delivery:

VPC Architecture Diagram:
A detailed visual layout of the VPC, including subnets, route tables, NAT gateways, and key networking components.

VPC Configuration:
Step-by-step configuration of subnets, route tables, internet/NAT gateways, and their associations.

Network Security Documentation:
Configuration of Network ACLs and Security Groups with documented rules for controlled access and traffic flow.

Auto-Scaling & Load Balancing Setup:
Auto Scaling policies with defined usage thresholds.
Load Balancer configuration including listeners, target groups, and health checks.

Database Integration:
Setup of the database instance in private subnet(s) with appropriate security groups.
Configuration of secure and low-latency connectivity between the application and database.

Security Documentation:
List of IAM roles, policies, and their permission scopes.
Detailed security group and ACL rules applied to different tiers/components.



Step 1: 
VPC and Subnet Configuration

Create a VPC:
Define a CIDR block (e.g., 10.0.0.0/16).

Create Subnets:
Public subnets for the Load Balancer in two Availability Zones.
Private subnets for the Application Layer in two Availability Zones.

Configure Route Tables:
Public Route Table: Associate with public subnets; route internet-bound traffic to the Internet Gateway.
Private Route Table: Associate with private subnets; route internet-bound traffic via the NAT Gateway.



Step 2: 
Security Configurations
Internet Gateway:
Created and attach an Internet Gateway to the VPC for public internet access.

NAT Gateway:
Set up 2 NAT Gateway in both of the public subnets to allow private subnet instances to access the internet. 

Route Table Updates:
Public Route Table: Added a route for 0.0.0.0/0 pointing to the Internet Gateway.
Private Route Table: Added a route for 0.0.0.0/0 pointing to the NAT Gateway.

Security Groups:
Set up security group for both Public and Private subnet
Allowed only required inbound traffic (e.g., HTTP, HTTPS, SSH) based on instance roles and tiers.

Network ACLs:
Set up network ACLs for both Public and Private subnet
Define inbound/outbound rules to further control traffic at the subnet level, applying a stateless layer of security.



Step 3: 
Launch and Configure EC2 Instances
Launch EC2 Instances:
Deploy EC2 instances (t2.micro / t3.micro) in the public subnets to serve as application servers.

Install & Configure Software:
Set up the web server (e.g., Apache, Nginx) on each public instance and this serves as the reverse proxy.

Create AMI for Auto Scaling:
After configuration, create an Amazon Machine Image (AMI) of the instance to use as the launch template in the Auto Scaling Group.



Step 4: 
Configuring the Elastic Load Balancer (ALB)
To distribute incoming traffic efficiently and ensure high availability, I set up an Application Load Balancer (ALB) using the following steps:

Created the ALB via the EC2 Console:
Navigated to the EC2 Dashboard → Load Balancers and selected Application Load Balancer.
Chose Internet-facing for the scheme to accept public traffic.
Selected at least two public subnets in different Availability Zones to increase fault tolerance.

Configured Target Group and Registered EC2 Instances:
Created a target group (type: instance) and registered the EC2 instances launched earlier.
Ensured the target group used the correct port (e.g., 80 for HTTP).

Set Up Health Checks:
Configured health check path (e.g., / or a specific application route) and set thresholds.
This ensures traffic is routed only to healthy EC2 instances.

With this setup, my ALB can now route traffic intelligently across multiple Availability Zones, automatically removing any unhealthy instance from the rotation.



Step 5: 
Setting Up the Auto Scaling Group (ASG)
To ensure that my application automatically adjusts to traffic demands, I configured an Auto Scaling Group (ASG) using the AMI created earlier. Here's how I did it:

Created the Auto Scaling Group:
Went to the EC2 Dashboard → Auto Scaling Groups and clicked Create ASG.
Selected the AMI I previously created from the configured EC2 instance.
Chose the instance type (e.g., t2.micro) and used the existing key pair and security group.

Configured Availability Zones and Subnets:
Selected multiple Availability Zones by choosing two or more private subnets, ensuring high availability and fault tolerance.

Set Scaling Policies with CloudWatch:
Created CloudWatch alarms

Scale Out: Add instances when CPU utilization is above 60%.

Scale In: Remove instances when CPU utilization drops below 30%.

Attached these alarms as scaling policies to the ASG.

Defined Capacity Settings:
Minimum capacity: 1 instance
Desired capacity: 2 instances (baseline traffic)
Maximum capacity: 4 instances (for handling high traffic)

With this configuration, the ASG automatically maintains performance during usage spikes and reduces cost by scaling in during idle periods.



Step 6: 
Testing and Optimization
After configuring the Auto Scaling Group and Load Balancer, I performed a thorough round of testing and optimization to ensure system resilience and responsiveness. Here's how I handled it:

Tested Connectivity and Firewall Rules
Verified that the Application Load Balancer (ALB) was publicly accessible via its DNS name.
Ensured that traffic flowed properly from the public subnet to the private EC2 instances through the load balancer.
Reviewed security group and network ACL (NACL) rules to confirm HTTP/HTTPS and internal app/database communication were allowed.

Simulated Traffic for Auto Scaling and Load Balancer:
Used tools like ab (Apache Benchmark) and custom scripts to simulate high traffic.
Observed the Auto Scaling Group adding instances when CPU thresholds were exceeded.
Confirmed that the ALB routed traffic evenly across healthy instances using its health checks.

Monitored Logs and Dashboards:
Enabled Amazon CloudWatch for real-time monitoring of:
CPU utilization
Request count

Application logs and system logs:
Reviewed logs to detect bottlenecks or anomalies in performance or access patterns.
Optimization Based on Feedback
Adjusted the scaling thresholds to match observed traffic patterns more closely.
Tuned the health check grace periods to avoid false instance failures.
Updated IAM roles and policies to follow least privilege principle.

With these steps, I ensured the infrastructure is secure, highly available, and optimized for cost and performance.




Prerequisites: DynamoDB Integration
Before proceeding with DynamoDB operations, I ensured the following setup was in place:
EC2 Instance (in a private subnet) with an IAM Role attached that has sufficient permissions to access DynamoDB.
IAM Policy Example: AmazonDynamoDBFullAccess or a custom policy scoped to the Students table.

DynamoDB Table created with the following specifications:
Table Name: Students
Primary Key (Partition Key): StudentID (Type: String)

Python Installed on the EC2 instance:
sudo yum install python3 -y

Boto3 Installed using pip:
pip3 install boto3

With these prerequisites met, I was ready to write Python scripts that interact with the Students table from the EC2 instance securely over the VPC Endpoint for DynamoDB.



Step 7: 
Set Up DynamoDB Table
To begin storing and managing student data, I created a DynamoDB table using the following steps:

Logged into the AWS Management Console.

Navigated to the DynamoDB service.

Clicked "Create table".

Entered the Table name: Students.

Set the Partition key to:

Key Name: StudentID

Key Type: String

Left all other settings as default (billing mode, encryption, etc.).

Clicked "Create", and within seconds, the Students table was provisioned and ready for use.

This table now serves as the backend data store for student-related information that I’ll access from the EC2 instance using Python and Boto3.



Step 8: 
Prepare Your EC2 Instance
To interact with the DynamoDB Students table from an EC2 instance, I prepared the environment as follows:

EC2 Instance Setup
Launched an EC2 instance (Amazon Linux 2 or Amazon Linux 2023 recommended).
Ensured Python 3 was installed:
sudo yum update -y
sudo yum install python3 -y

Attached an IAM Role with DynamoDB full access.
IAM Role Creation (for DynamoDB Access)
To allow the EC2 instance to securely communicate with DynamoDB without managing credentials manually:

Signed into the AWS Management Console.

Navigated to IAM > Roles.

Clicked “Create role”.

Selected:

Trusted entity type: AWS service

Use case: EC2

Clicked Next: Permissions.

Searched and selected the policy:
AmazonDynamoDBFullAccess

Clicked Next: Tags (optional — added tags).

Clicked Next: Review, named the role (e.g., EC2DynamoDBRole), then clicked Create role.

Finally,I attached this IAM role to the running EC2 instance via the EC2 Console > Actions > Security > Modify IAM Role.

The EC2 instance is now fully configured to interact with DynamoDB using Boto3.



Step 9:
Attach IAM Role to EC2 and Test DynamoDB Access
After creating the IAM role with AmazonDynamoDBFullAccess, I attached it to the EC2 instance and verified access:

Attach the Role to Your EC2 Instance
Go to the EC2 Console.

In the left sidebar, click Instances.

Select the EC2 instance you want to attach the role to.

Click the Actions dropdown → Security → Modify IAM Role.

Select the IAM role you previously created (e.g., EC2DynamoDBRole).

Click Save.



Step 11: 
Created a Python Script to Insert Data into DynamoDB which contains student data
On the EC2 instance terminal, i run the Python script
Navigated to the AWS Management Console:

Navigated to DynamoDB > Tables > Students.

Explored table items and use Scan to view the inserted records in the DynamoDB.