Use Case: Hosting a Static Website on Amazon S3

This section documents how I created an S3 bucket and hosted a static website on it.



Step 1: Create an S3 Bucket

Logged into AWS Console.
Navigated to **S3** under Services.
Clicked **Create bucket**, set a unique bucket name (e.g., `my-static-site-bucket`), and selected a region.
Disabled "Block all public access" to allow website hosting later.


Step 2: Upload Website Files

Uploaded the website files:

`index.html`
`error.html`


Step 3: Enable Public Access

Went to **Permissions > Block public access**.
Clicked **Edit**, unchecked "Block all public access", and saved changes.



✅ Step 4: Add Bucket Policy

Used the **Policy Generator** to create a policy allowing public `GetObject` access:

json
{
  "Version":"2012-10-17",
  "Statement":[{
    "Sid":"PublicReadGetObject",
    "Effect":"Allow",
    "Principal": "*",
    "Action":["s3:GetObject"],
    "Resource":["arn:aws:s3:::my-static-site-bucket/*"]
  }]
}

Applied the policy to the bucket.



Step 5: Enable Static Website Hosting

Went to the **Properties** tab.
Edited **Static website hosting**, selected **Enable**, and provided:

`index.html` for index document
`error.html` for error document



Step 6: Test the Website

Copied the **Bucket website endpoint** under Static website hosting.
Pasted it in the browser and confirmed the static site was working.


