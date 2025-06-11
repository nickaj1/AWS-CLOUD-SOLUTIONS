Creating and Connecting to an RDS MySQL Database with SQL Client (MYSQL WorkBench)
This section details how I created an RDS MySQL instance on AWS and connected to it using MySQL Workbench.


Step 1: Create a New RDS Database Instance
Logged in to AWS Console.

Went to Services > RDS and clicked Create Database.

Screenshot:



Step 2: Select Region
Chose the preferred AWS Region (e.g., eu-north-1).


Step 3: Choose a Database Creation Method
Selected Standard create.

Engine type: MySQL

Template: Free Tier


Step 4: Configure DB Settings
DB instance identifier: my-mysql-db

Master username: admin

Password: Chose a strong password


Step 5: Instance Specifications
DB instance class: db.t2.micro

Storage type: General Purpose (SSD)

Allocated storage: 20 GB

Disabled Storage autoscaling


Step 6: Connectivity Settings
VPC: Default

Subnet group: Default

Public access: Yes

VPC security group: Created new security group

Port: 3306

Availability zone: No preference

RDS Proxy: Disabled


Step 7: Authentication & Monitoring
Authentication: Password authentication

Monitoring: Disabled enhanced monitoring


Step 8: Additional Configuration
Database name: sampledb

Backup retention: 1 day

Auto minor version upgrade: Enabled

Deletion protection: Disabled


Step 9: Create Database
Clicked Create Database



Step 10: Connect with MySQL Workbench
Download and launch MySQL Workbench.

Go to Database > Connect to Database (or Ctrl+U).

Enter the following:

Hostname: Copy from the RDS endpoint in the AWS Console.

Port: 3306

Username: e.g., admin

Password: Store securely using Vault/Keychain

Screenshot:


Step 11: Verify Connection
Successfully connected and viewed schema objects.

Ran sample SQL scripts to test the connection.
Query For Creating  ATable in MySQL Workbench

 CREATE TABLE `employee` (
 `id` int NOT NULL AUTO_INCREMENT,
 `name’ varchar(255) DEFAULT NULL,
 `email` varchar(255) DEFAULT NULL,
 `city` varchar(255) DEFAULT NULL,
 PRIMARY KEY (`id`) )

 I used the script above to create a table in MySQL workbench