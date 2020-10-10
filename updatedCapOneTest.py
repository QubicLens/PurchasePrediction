import requests
import json

customerId = 'Pothyn'
apiKey = '2bd4021425dbdbbb6aafac992c0ad0a8'

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

customer = {
  "first_name": "Hunter",
  "last_name": "Davis",
  "address": {
    "street_number": "99",
    "street_name": "MLKJR",
    "city": "Miami",
    "state": "FL",
    "zip": "22323"
  }
}

response = requests.get(url = url)
print(response.status_code)
print(response.text)

response = requests.post(url = url, data = json.dumps(customer), headers = {'content-type':'application/json'})
print(response.status_code)
