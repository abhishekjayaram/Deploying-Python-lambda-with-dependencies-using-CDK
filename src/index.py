import requests

def handler(event, context):
    response = requests.get('https://catfact.ninja/fact')
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": response.json()
    }