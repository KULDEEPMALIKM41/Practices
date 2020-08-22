import jsonify, requests, json
url = "https://www.google.com/search?source=hp&ei=PDTuXKPgO9uVwgOi9oboBg&q=ted.com"
print(url)
response = requests.get(url, timeout=1000000)
pyth = response.text
print(pyth)