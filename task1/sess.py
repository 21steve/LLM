import requests
import json
import time
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

class GraphQLClient:
    def __init__(self, url:str ,clientID:str , client_secret:str):
   
        self.url = url
        self.auth_token = client_secret
        self.mutation = """
        mutation PublicAPIToken($clientId: String!, $clientSecret: String!) {
            publicAPIToken(clientId: $clientId, clientSecret: $clientSecret)
        }
        """
        self.variables = {
            "clientId": f"{clientID}",
            "clientSecret": f"{client_secret}"
        }
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer{self.auth_token}"
        }
        self.auth_token=None
        self.last_request_time = 0
        self.retry=False 

    def send_request(self,makelogs=True):
        payload = {
            "query": self.mutation,
            "variables": self.variables
        }

        response = requests.post(self.url, json=payload, headers=self.headers)
        self.last_request_time=time.time()

        if response.status_code == 200:
            data = response.json()
            self.auth_token=data['data']['publicAPIToken']
            if makelogs:
                with open("logs.txt","a") as f:
                    f.write(f"Request made at {time.ctime()} with status code {response.status_code}\n token: {self.auth_token}\n\n")
            self.retry=False
            return self.auth_token
        else:
            if makelogs:
                with open("logs.txt","a") as f:
                    f.write(f"Request made at {time.ctime()} with status code {response.status_code}\n\n error: {response.text}\n\n")
            self.auth_token=None
            self.retry=True
            return False

    async def start_timed_requests(self, interval,makelogs=True):
        while True:
            
            if self.auth_token is None or time.time()-self.last_request_time>interval:
                self.send_request(makelogs)
            
            if not self.retry:
                await asyncio.sleep(interval)
        
# Example usage
if __name__ == "__main__":
    
    client_secret = os.getenv("CLIENT_SECRET")
    clientID = os.getenv("CLIENT_ID")
    client = GraphQLClient("https://graphql.wnwd.com", clientID, client_secret)
    reqtime=os.getenv("REQUEST_TIME")
    # client.start_timed_requests(int(reqtime),makelogs=True)
    
    asyncio.run(client.start_timed_requests(int(reqtime),makelogs=True))