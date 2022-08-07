from numpy import number
import requests
import json
import folium
import webbrowser

url = 'https://api.ibb.gov.tr/ispark-bike/GetAllStationStatus'

response = requests.get(url)
data = json.loads(response.text)
map = folium.Map(location=[ 41.0203, 28.9339 ],zoom_start=12)


for stations in data["dataList"]:
    try:
        ad = stations["adi"]
    
        longx = float(stations["lon"])
        latx = float(stations["lat"])
        müsait = stations["dolu"]

        if int(müsait)>0 :
            folium.Marker(location=[latx,longx],popup=f"{müsait} tane bisiklet müsait.",tooltip=ad,icon=folium.Icon(color="green")).add_to(map)
        else:
            folium.Marker(location=[latx,longx],popup=f"{müsait} tane bisiklet müsait.",tooltip=ad,icon=folium.Icon(color="red")).add_to(map)
    except:
        print("hata")
map.save("bikes.html")

webbrowser.open_new_tab("bikes.html")