AWS IAM Use Cases and Implementations
This repository contains step-by-step AWS IAM use cases implemented via the AWS Console. Each section includes a breakdown of tasks and corresponding screenshots.

Use Case 1: Developer Access with Permissions Boundaries
Scenario:
Set up a development environment with specific access controls.

Requirements:
Groups:

Developers: Full access to EC2 and S3.

Jr. Developers: Read-only access to EC2 and S3.

Users:

Alice: Member of Developers group.

Bob: Member of Jr. Developers group.

Permissions Boundary:

Restrict maximum permissions for Developers group.

Task Breakdown:
Create IAM Groups

Developers

Jr. Developers

Create IAM Users

Add Alice to Developers

Add Bob to Jr. Developers

Create and Attach Policies

Full access for Developers

Read-only for Jr. Developers

Apply Permissions Boundary

Attach boundary to restrict IAM user management for Developers

Snapshot Reference : (/sna)

Use Case 2: Temporary Administrative Access
Scenario:
Charlie needs temporary admin access for a week.

Task Breakdown:
Create IAM User: Charlie

Create IAM Role: ProjectAdminRole with admin permissions

Set Temporary Credentials: Duration of one week

Assign Role to User: Provide Charlie access

Use Case 3: Role for Application Access
Scenario:
Allow EC2 application access to S3 and CloudWatch.

Task Breakdown:
Create IAM Role: AppAccessRole for S3 bucket + CloudWatch logs