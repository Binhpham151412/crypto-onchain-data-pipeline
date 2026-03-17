import requests

url = "https://api.blockchair.com/bitcoin/stats"

response = requests.get(url)

data = response.json()

print(data)
