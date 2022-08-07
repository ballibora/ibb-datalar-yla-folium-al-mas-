import folium
import requests
import json
import webbrowser

url = "https://data.ibb.gov.tr/api/3/action/datastore_search?resource_id=d588f256-2982-43d2-b372-c38978d7200b"
response = requests.get(url)
parklar = json.loads(response.text)

map = folium.Map(location=[ 41.0203, 28.9339 ])

for i in parklar["result"]["records"]:

    park_adi = i["NAME"]
    park_long = i["LONGITUDE"]
    park_lat = i["LATITUDE"]
    folium.Marker([park_lat,park_long], popup= park_adi).add_to(map)

map.save("parklar.html")
webbrowser.open_new_tab('otoparklar.html')