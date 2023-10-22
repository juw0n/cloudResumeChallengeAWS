import json
import pytest
from moto import mock_dynamodb
import boto3
from lambdaFunc import lambda_handler

@mock_dynamodb
def test_lambda_handler():
    # Create a mock DynamoDB table
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    dynamodb.create_table(
        TableName='cloudResumeViewsTable',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )
    table = dynamodb.Table('cloudResumeViewsTable')
    table.put_item(Item={'id': '1', 'views': 42})

    # Execute the Lambda function
    event = {}
    context = {}
    result = lambda_handler(event, context)

    # Check the result
    assert result == 43  # Expect the updated 'views' count

if __name__ == '__main__':
    pytest.main()