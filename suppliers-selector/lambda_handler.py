import boto3
import random
import os
from faker import Faker

# Initialize AWS clients and Faker instance
dynamodb = boto3.resource('dynamodb')
ses_client = boto3.client('ses')
fake = Faker()

# DynamoDB table name
TABLE_NAME = 'Suppliers'

# Create SES sender email (ensure that this email is verified in SES)
SENDER_EMAIL =  os.environ['SENDER_EMAIL']  # For better security, use environment variables

# The URL for the procurement negotiation link
NEGOTIATION_URL = "https://ragithm.com/deal/negotiate"

def get_random_supplier():
    """
    Fetch a random supplier from DynamoDB.
    """
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()  # Get all items in the table
    suppliers = response['Items']
    
    if not suppliers:
        return None
    
    # Randomly select a supplier
    random_supplier = random.choice(suppliers)
    return random_supplier

def send_email_to_supplier(supplier_email, supplier_name):
    """
    Send an email to the supplier to start a procurement negotiation.
    """
    subject = "Invitation to Start Procurement Negotiation"
    body_text = f"""
    Dear {supplier_name},
    
    We are pleased to invite you to start a procurement negotiation with our company. Please click the link below to begin the process:
    
    {NEGOTIATION_URL}
    
    We look forward to working with you.
    
    Best regards,
    Your Company Name
    """
    
    # Send email via SES
    response = ses_client.send_email(
        Source=SENDER_EMAIL,
        Destination={
            'ToAddresses': [supplier_email],
        },
        Message={
            'Subject': {
                'Data': subject,
            },
            'Body': {
                'Text': {
                    'Data': body_text,
                },
            },
        },
    )
    
    print(f"Email sent to {supplier_name} at {supplier_email}. SES Message ID: {response['MessageId']}")

def lambda_handler(event, context):
    # Fetch a random supplier from the DynamoDB table
    supplier = get_random_supplier()
    
    if supplier:
        supplier_name = supplier['name']
        supplier_email = supplier['email']
        
        # Send email to the supplier
        send_email_to_supplier(supplier_email, supplier_name)
    else:
        print("No suppliers found in the table.")
    
    return {
        'statusCode': 200,
        'body': 'Procurement negotiation email sent to a supplier.'
    }

def main():
    """
    Local testing function to simulate the Lambda invocation.
    """
    # Simulate the event and context (dummy values for local testing)
    event = {}
    context = {}

    # You can simulate the Lambda handler manually
    print("Running local test...")
    response = lambda_handler(event, context)
    print("Lambda invocation result:", response)

if __name__ == '__main__':
    # Run the main function for local testing
    main()