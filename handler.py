import json
import requests
import datetime
import boto3

class GetDataController(object):
    def __init__(self):
        self.urls = {
            'wind_farm_data': 'https://www.thecrownestate.co.uk/api/energy-map/wind-farm-data',}
    
    def generate_file_name(self):
        return str(datetime.datetime.utcnow())
        
    def execute(self,data_dir='data'):
        data = []
        for filename, endpoint_url in self.urls.items():
            data.append(requests.get(endpoint_url))
            #filename = ''.join([filename,"-",self.generate_file_name()])
        return data

def handle(event,context):
    controller = GetDataController()
    return {
        "data" : json.dumps(controller.execute())
    }