Load Balancing and Auto Scaling with EC2 Instances
This section documents how I set up EC2 instances behind an Application Load Balancer (ALB) with an Auto Scaling Group (ASG) using the AWS Console. Below are the steps I followed, including configuration and validation.

Step 1: Launch EC2 Instances
I launched two EC2 instances using the same AMI (Amazon Linux 2) and instance type t2.micro. Both were initially placed in two subnet in different Availability Zone.

Security group was configured to allow HTTP (port 80) traffic.

I installed Apache (sudo yum install httpd -y) and added a basic HTML index file to test.

Screenshot:


Step 2: Create an Application Load Balancer
I created an Application Load Balancer for routing HTTP traffic to the instances.

Listener was set to HTTP :80.

Target group was configured and both instances were registered and marked as healthy.

Subnets were selected across two different AZs for high availability.

Screenshot:


Step 3: Configure Auto Scaling Group (ASG)
I created an Auto Scaling Group using the EC2 launch template.

Desired capacity: 2

Minimum: 1

Maximum: 4

Associated the ASG with the previously created ALB.

Screenshot:


Step 4: Configure Scaling Policies
I defined CPU-based scaling policies:

Scale out when CPU > 70%

This was done via CloudWatch alarms linked to the Auto Scaling Group.

Screenshot:


Step 5: To test if the Auto Scaling policies work, I simulated CPU load on one of the EC2 instances by installing and running the stress tool:

stress --cpu 160 --timeout 60
This command puts pressure on 2 CPU cores for 1 minute, which helped push the instance's CPU usage above the 60% threshold.

As the CPU utilization increased, CloudWatch triggered the scale-out policy, and the Auto Scaling Group launched new EC2 instances to handle the load.

Step 6: Simulating Load
I used Apache Benchmark to simulate traffic and observed new EC2 instances being launched as CPU utilization increased.

Screenshot:


Step 7: Monitoring Auto Scaling Activity
Using CloudWatch, I monitored:

Instance count changes

Triggered scaling actions

EC2 and ALB health