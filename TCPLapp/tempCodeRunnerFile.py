import requests

url = "http://localhost:8080/geoserver/zone/wfs"
params = {
    "service": "WFS",
    "version": "2.0.0",
    "request": "GetFeature",
    "typeName": "zone:PMC_Missing_Link_Buffer",
    "outputFormat": "application/json"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
