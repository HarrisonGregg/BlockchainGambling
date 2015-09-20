import requests
import json
import time

def payToServer(payer_id, pay_amount):
	responseAction = {
		201 : lambda : print('It worked'),
		404 : lambda : print('Uh oh, something in your payload is wrong'),
	}

	url = 'http://api.reimaginebanking.com/accounts/{}/purchases?key=eee099222a7c7b3d9f6048e27122e51b'.format(payer_id)

	purchase = {
		"merchant_id": "55fda8063c3ce2100041183b",
		"medium": "balance",
		"purchase_date":time.strftime('%Y-%m-%d',time.localtime(time.time())),
		"amount": int(pay_amount),
		"status": "pending",
		"description": "bet4charity"
	}
	
	req = requests.post(
		url, 
		data= json.dumps(purchase),
		headers={'content-type':'application/json'},
	)
	print(req.text)

	url1 = 'http://api.reimaginebanking.com/accounts/55fdbb19ce1cef140015e272/deposits?key=eee099222a7c7b3d9f6048e27122e51b'

	deposit = {
                "medium": "balance",
                "transaction_date":time.strftime('%Y-%m-%d',time.localtime(time.time())),
                "status": "pending",
				"amount": int(pay_amount),
                "description": payer_id
        }
	
	req1 = requests.post(
                url1,
                data = json.dumps(deposit),
                headers = {'content-type':'application/json'},
        )
	print(req.text)

if __name__ == '__main__':
	payToServer('55e94a6cf8d8770528e617f8', 150)
