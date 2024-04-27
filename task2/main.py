from tokenizer import GraphQLClient
from queries import *
from typing import Union
import requests
import os
from datetime import datetime
import asyncio


class Query():

    def __init__(self,client:GraphQLClient):
        self.client=client
    
    def convert_to_iso_format(self,year, month, day):
        dt = datetime(year, month, day)
        iso_date = dt.isoformat()
        return iso_date

        
    async def check_risk(self, imo: str):
        @self.client.check_token(makelogs=True)
        async def send_request():
            query_string=risk_assessment_query_string
            payload = {
                "query": query_string,
                "variables": {
                    "imo": f"{imo}"
                }
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.client.auth_token}"
            }

            response = await asyncio.to_thread(requests.post, self.client.url, json=payload, headers=headers)
            return response

        return await send_request()
    
    async def activities(self,imo:Union[str,int],from_date:str,to_date:str,polygon:list[list],offset=0,limit=100,includePropertyChanges=True):
        @self.client.check_token(makelogs=True)
        async def send_request():
            query_string=activities_query_string
            from_datestr=self.convert_to_iso_format(*map(int,from_date.split("-")))
            to_datestr=self.convert_to_iso_format(*map(int,to_date.split("-")))

            variables = activities_input(includePropertyChanges=includePropertyChanges,limit=limit,offset=offset,from_date=from_datestr,to_date=to_datestr,vesselIdOrImo=imo,coordinates=polygon)
            payload = {
                "query": query_string,
                "variables": variables
            }
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.client.auth_token}"
            }

            response = await asyncio.to_thread(requests.post, self.client.url, json=payload, headers=headers)
            return response

        return await send_request()

if __name__ == "__main__":
    client_secret = os.getenv("CLIENT_SECRET")
    clientID = os.getenv("CLIENT_ID")
    url=os.getenv("URL")
    interval=os.getenv("REQUEST_INTERVAL")

    query=Query(GraphQLClient(url, clientID, client_secret,interval=interval))
    response = asyncio.run(query.check_risk("9738909"))
    activity=asyncio.run(query.activities(imo="9738909",from_date="2021-01-01",to_date="2021-12-31",polygon=[[113.258057,19.823202],[113.258057,23.007113],[120.629883,23.007113],[120.629883,19.823202],[113.258057,19.823202]]))
    with open ("risk.txt","w") as f:
        f.write(response.text)
    with open ("activities.txt","w") as f:
        f.write(activity.text)