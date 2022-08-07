import requests
import json
from unicode_tr import *

def turkish_upper(value):
    return unicode_tr(value).upper()
    




url = "https://data.ibb.gov.tr/api/3/action/datastore_search?resource_id=d588f256-2982-43d2-b372-c38978d7200b"

response = requests.get(url)

data = json.loads(response.text)

semt = input("Sorgulamak istediğiniz semtin adını giriniz: ")
semt=turkish_upper(semt)


for i in data["result"]["records"] :
    if i["COUNTY_NAME"] == semt:

        print(i["NAME"])