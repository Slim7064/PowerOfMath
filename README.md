# PowerOfMath
Simple project to build web app using AWS Amplify

# AWS Project to build simple Web Application hosted on AWS
# Follows "AWS Project: Architect and Build an End-to-End Web Application by Scratch" video 
# from Tiny Technical Tutorials

FLOW:
Create S3 Bucket for html file ->
Create AWS Amplify App deployment (Copy URL) ->
Crreate lambda function ->
Create DynamodDB and allow lambda to write to it ->
Create REST API Gateway to connect client with Amplify/App

USER -> Amplify -> API Gateway -> Lambda Function -> DynamoDB

# Creates web application calculating a power-to mathmatical expression based on the lambda.py code
# STEP 0: Create S3 bucket to house html code
# STEP 1: Create Lambda function using lambda.py code 
# STEP 2: Use AWS Amplify to host Web server using index.html code
# STEP 3: Create Dynamodb database to house results and queries
# STEP 4: Give lambda function permission to write to DB -> Use JSON.txt permissions
# STEP 5: Create AWS API Gateway 
    a: Create "dev" stage
    b: Create POST method to call to the lambda function
    c. Enable CORS in / folder -> ALLOW POST 
    d. Deploy API


Lessons Learned:
1. Remember to update DynamoDB ARN in JSON.txt
2. Remember to update API Gateway URL in index.html
3. Remember to update lambda code with created dynamoDB name
4. Give permission to lambda to write to DynamoDB using JSON.txt policy
5. Remember that index.html file has to be zipped to be deployed to gateway
