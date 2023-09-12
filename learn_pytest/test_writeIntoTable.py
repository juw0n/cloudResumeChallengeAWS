import boto3
from moto import mock_dynamodb2
import store_data

@mock_dynamodb2
def test_write_into_table():
    "Test the write_into_table with a valid input data"
    # create an DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    # create a DynamoDB table
    table_name = 'testTable'
    table = dynamodb.create_table(tableNmae, KeySchema=[{
        'AttributeName': 'date','KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'date','AttributeType': 'S'}])
    
    data = {'date':'07-Oct-2020','company':'qxf2 services','client':1000}
    store_data.write_into_table(data,table_name)
    response = table.get_item(Key={'date':data['date']})
    actual_output = response['Item']
    assert actual_output == data