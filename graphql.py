import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Function to retrieve the public API token
def get_public_api_token(url, mutation, variables):
    response = requests.post(url, json={'query': mutation, 'variables': variables})
    if response.status_code == 200:
        data = response.json()
        token = data['data']['publicAPIToken']
        return token
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        return None

# GraphQL endpoint URL
url = 'https://graphql.wnwd.com'

# GraphQL mutation to retrieve the public API token
mutation = '''
mutation Mutation($clientId: String!, $clientSecret: String!) {
  publicAPIToken(clientId: $clientId, clientSecret: $clientSecret)
}
'''

# Define the values for clientId and clientSecret
variables = {
    'clientId': client_id,
    'clientSecret': client_secret,
}

# Get the initial token
token = get_public_api_token(url, mutation, variables)
if token:
    print("Initial Public API Token:", token)
    # Record the time when the token was obtained
    token_time = time.time()

    # Timer loop
    while True:
        # Check if 30 minutes have elapsed
        if time.time() - token_time >= 30 * 60:  # 30 minutes in seconds
            print("Token expired. Refreshing...")
            # Get a new token
            token = get_public_api_token(url, mutation, variables)
            if token:
                print("New Public API Token:", token)
                # Update the token time
                token_time = time.time()
        # Wait for 1 minute before checking again
        time.sleep(60)  # 1 minute in seconds
else:
    print("Failed to retrieve initial token.")
