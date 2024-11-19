import requests


for i in range(200):
    p = {'name':f'user_{i}','age':22}
    res = requests.post("http://127.0.0.1:8000/users", params=p) 
    print(res.json())