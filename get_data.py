import json
import requests
import datetime
import boto3

class GetDataController(object):
    def __init__(self):
        self.urls = {
            'wind_farm_data': 'https://www.thecrownestate.co.uk/api/energy-map/wind-farm-data',}
    
    
    def execute(self,data_dir='data'):
        for filename, endpoint_url in self.urls.items():
            r = requests.get(endpoint_url)
            return r
            

def handle(event,context):
    controller = GetDataController()
    return {
        "data" : json.dumps(controller.execute())
    }
