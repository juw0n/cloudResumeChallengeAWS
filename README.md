# cloudResumeChallengeAWS
This is the repo for my cloudResume challenge using AWS cloud

The Cloud Resume Challenge - AWS according to cloudresumechallenge.dev
Step 1: Certification
Your resume needs to have the AWS Cloud Practitioner certification on it. 

Step 2: HTML
Your resume needs to be written in HTML. Not a Word doc, not a PDF. 

Step 3: CSS
Your resume needs to be styled with CSS. No worries if you’re not a designer – neither am I. It doesn’t have to be fancy.

Step 4: Static Website
Your HTML resume should be deployed online as an Amazon S3 static website. Services like Netlify and GitHub Pages are great and I would normally recommend them for personal static site deployments, but they make things a little too abstract for our purposes here. Use S3.

Step 5: HTTPS
The S3 website URL should use HTTPS for security. You will need to use Amazon CloudFront to help with this.

Step 6: DNS
Point a custom DNS domain name to the CloudFront distribution, so your resume can be accessed at something like my-c00l-resume-website.com. You can use Amazon Route 53 or any other DNS provider for this. A domain name usually costs about ten bucks to register.

Step 7: Javascript
Your resume webpage should include a visitor counter that displays how many people have accessed the site. You will need to write a bit of Javascript to make this happen. Here is a helpful tutorial to get you started in the right direction.

Step 8: Database
The visitor counter will need to retrieve and update its count in a database somewhere. I suggest you use Amazon’s DynamoDB for this. (Use on-demand pricing for the database and you’ll pay essentially nothing, unless you store or retrieve much more data than this project requires.) Here is a great free course on DynamoDB.

Step 9: API
Do not communicate directly with DynamoDB from your Javascript code. Instead, you will need to create an API that accepts requests from your web app and communicates with the database. I suggest using AWS’s API Gateway and Lambda services for this. They will be free or close to free for what we are doing.

Step 10: Python
You will need to write a bit of code in the Lambda function; you could use more Javascript, but it would be better for our purposes to explore Python – a common language used in back-end programs and scripts – and its boto3 library for AWS. Here is a good, free Python tutorial.

Step 11: Tests
You should also include some tests for your Python code. Here are some resources on writing good Python tests.

Step 12: Infrastructure as Code

Step 13: Source Control

Step 14: CI/CD (Back end)

Step 15: CI/CD (Front end)

Step 16: Blog post