import os
import requests

from dotenv import load_dotenv
def main(url):
    payload = {}
    headers = {
        'Cookie': 'WMONID=VTZFfBvSyQu'
    }
    response = requests.request(method="GET",
                                url=url,
                                headers=headers,
                                data=payload)
    print(response.text)
    

if __name__ == "__main__":
    load_dotenv(verbose=True)
    base_url = "http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll"
    service_key = os.getenv("SERVICE_KEY")
    bus_route_id = "100100118"
    result_type = "json"
    url = f'{base_url}?serviceKey={service_key}&busRouteId={bus_route_id}&resultType={result_type}'
    main(url)