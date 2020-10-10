import requests
import json

customerId = 'Pothyn'
apiKey = '2bd4021425dbdbbb6aafac992c0ad0a8'

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

payload = {
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

customer = {
  "code": 0,
  "message": "string",
  "fields": "string"
}

# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

print(url)
response = requests.post(url = url, data = payload)
print(response.text)

if response.status_code == 201:
	print('account created')
print('confirm')
