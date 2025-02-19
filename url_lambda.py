# Backend: AWS Lambda (Python) for URL Shortening
import json
import boto3
import os
import hashlib
import base64

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('url_shortener', 'url_shortener') # replace with your DynamoDB table name 
table = dynamodb.Table(table_name)

BASE_URL = os.environ.get('BASE_URL', 'https://qcko9iw74m.execute-api.us-east-2.amazonaws.com/dev')# replace with your base URL

def generate_short_code(url):
    hash_object = hashlib.md5(url.encode())
    return base64.urlsafe_b64encode(hash_object.digest())[:6].decode('utf-8')

def lambda_handler(event, context):
    method = event.get("httpMethod")
    
    if method == "POST":  # Shorten URL
        body = json.loads(event.get("body", "{}"))
        original_url = body.get("url")
        if not original_url:
            return {"statusCode": 400, "body": json.dumps({"error": "URL is required"})}
        
        short_code = generate_short_code(original_url)
        table.put_item(Item={"short_code": short_code, "original_url": original_url})
        short_url = f"{BASE_URL}/{short_code}"
        return {"statusCode": 200, "body": json.dumps({"short_url": short_url})}
    
    elif method == "GET":  # Redirect
        path_params = event.get("pathParameters")
        if path_params and "short_code" in path_params:
            short_code = path_params["short_code"]
            response = table.get_item(Key={"short_code": short_code})
            
            if "Item" in response:
                original_url = response["Item"]["original_url"]
                return {"statusCode": 301, "headers": {"Location": original_url}}
            else:
                return {"statusCode": 404, "body": json.dumps({"error": "URL not found"})}
    
    return {"statusCode": 405, "body": json.dumps({"error": "Method Not Allowed"})}