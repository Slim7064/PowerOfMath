# import the JSON utility package
import json
# import python math library
import math
# import AWS SDK (Python package name is boto3)
import boto3
# import two packages to help with dates and date formatting
from time import gmtime, strftime

# create DynamoDB object using AWS SDK
# NOTE NOTE NOTE change "PowerofMathDatabase" to working DB name
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PowerOfMathDatabase')

# store current time in human readible format
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define handler function that Lambda service will use as an entry point
def lambda_handler(event, context):
    
    # extract two numbers from Lambda service's event object
    mathResult = math.pow(int(event['base']), int(event['exponent']))
    
    # write result and time to DynamoDB table using object
    response = table.put_item(
        Item={
            'ID': str(mathResult),
            'LatestGreetingTime':now
        })
    
    # return properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps('Your result is ' + str(mathResult))
        }