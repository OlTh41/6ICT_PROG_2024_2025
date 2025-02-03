import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

print(response)        # <Response [200]>
print(response.json()) # Data in JSON-formaat
print("#"*40) # Scheiding in opdrachtprompt

response_json = response.json()
print(response_json['updated_at']) # Print tijd van update.
