import folium
import requests
import json
import webbrowser

url = "https://data.ibb.gov.tr/api/3/action/datastore_search?resource_id=f4f56e58-5210-4f17-b852-effe356a890c"
response = requests.get(url)
otoparklar = json.loads(response.text)

map = folium.Map(location=[ 41.0203, 28.9339 ])

for i in otoparklar["result"]["records"]:

    ad = i["PARK_NAME"]
    park_long= i["LONGITUDE"]
    park_lat= i["LATITUDE"]

    folium.Marker([park_lat,park_long], popup=ad).add_to(map)

map.save("otoparklar.html")
webbrowser.open_new_tab('otoparklar.html')

