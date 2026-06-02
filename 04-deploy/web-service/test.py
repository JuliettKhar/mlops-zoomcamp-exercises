import requests

ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance":40
}

url = "http://ec2-15-168-7-126.ap-northeast-3.compute.amazonaws.com:9696/predict"
resp = requests.post(url, json=ride)
print(resp.json())