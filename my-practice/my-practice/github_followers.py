import urllib.request
import json

url = "https://api.github.com/users/torvalds"

with urllib.request.urlopen(url) as response:
    body = response.read()

data = json.loads(body)

print("torvalds 的 follower 數量是：", data["followers"])