import requests

#params = {
#    "name" : "Mike",
#    "age" : 25
# }

#response = requests.get("https://httpbin.org/get", params=params)
# print(response.url)

# print(response.status_code)
# print(response.text)

#payload = {
# "name" : "Mike",
#    "age" : 25
#}

#response = requests.post("https://httpbin.org/post", data=payload)
#print(response.url)


#response = requests.get("https://httpbin.org/status/500")
#if response.status_code == requests.codes.not_found:
#    print("Not Found")
#else:
#    print(response.status_code)


headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.5563.101 Mobile/15E148 Safari/604.1",
    "Accept": "image/jpeg"
}

response = requests.get("https://httpbin.org/image",
                        headers=headers)

with open("myimage.jpg","wb") as f:
    f.write(response.content)


proxies = {
    "http": "139.99.237.62:80",
    "https": "139.99.237.62:80"
}
response = requests.get("http://httpbin.org/get", proxies=proxies)
print(response.text)

#print(response.status_code)


#res_json = response.json()
#print(res_json)