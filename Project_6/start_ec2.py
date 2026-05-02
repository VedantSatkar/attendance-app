import boto3

def lambda_handler(event, context):
    # Create EC2 client
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    
    # Your EC2 Instance ID
    instance_id = 'i-0f89382af9b2960e1'
    
    # Start the instance
    response = ec2.start_instances(InstanceIds=[instance_id])
    
    print("Starting EC2 instance:", instance_id)
    print(response)
    
    return {
        "statusCode": 200,
        "body": "EC2 instance started successfully"
    }