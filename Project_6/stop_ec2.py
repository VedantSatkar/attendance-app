import boto3

def lambda_handler(event, context):
    # Create EC2 client
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    # Your EC2 Instance ID
    instance_id = 'i-0f89382af9b2960e1'
    
    # Stop the instance
    response = ec2.stop_instances(InstanceIds=[instance_id])
    
    print("Stopping EC2 instance:", instance_id)
    print(response)
    
    return {
        "statusCode": 200,
        "body": "EC2 instance stopped successfully"
    }