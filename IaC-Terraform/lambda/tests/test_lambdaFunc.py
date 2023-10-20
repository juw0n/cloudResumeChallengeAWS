import json
import pytest
import boto3
from moto import mock_dynamodb2
# Import the Lambda function from separate module
from myLambdaFunc import lambda_handler


# Define fixture to create a mock DynamoDB table
@mock_dynamodb2
@pytest.fixture
def dynamodb_mock():
    awsServices = boto3.resource('dynamodb', region_name='us-east-1')
    table = awsServices.create_table(
        TableName = 'cloudResumeViewsTable',
        KeySchema = [{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )
    yield table

# Define a test for the lambda_handler function
def test_lambda_handler(dynamodb_mock):
    # Prepare a sample event and context
    event = {}
    context = {}

    # Invoke the Lambda function
    result = lambda_handler(event, context)

    # Check if the result is as expected
    assert result == 1

    # Retrieve the updated item from the DynamoDB table and verify the 'views' count
    response = dynamodb_mock.get_item(Key={'id': '1'})
    updated_views = response.get('Item', {}).get('views', None)

    assert updated_views == 1

# Run the tests with pytest
if __name__ == '__main__':
    pytest.main()