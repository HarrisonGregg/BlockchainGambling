import requests
import json

apiKey = '575559514bd5cfabb8601f73a09302ad'

responseAction = {
	200 : 'It worked',
	404 : 'Uh oh, something in your payload is wrong',
}

url = 'http://api.reimaginebanking.com/customers/accounts?key={}'.format(apiKey)

payload = '{"id": "string","first_name": "string","last_name": "string","address": {"street_number": "string","street_name": "string","city": "string","state": "string","zip": "string"}}'

#print(json.dumps(payload))

res = requests.get(
	url, 
	data=payload,
	headers={'content-type':'application/json'}
	)
print(res.text)
