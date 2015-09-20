import json
import requests
import time

def userWin (user_account, bet_amount):
	#print(user_account)
	#print(bet_amount)
	responseAction = {
			201 : lambda : print("It worked."),
			404 : lambda : print("NOT WORKING."),
	}
	
	url = "http://api.reimaginebanking.com/accounts/55fdbb19ce1cef140015e272/transfers?key=eee099222a7c7b3d9f6048e27122e51b"

	total_win = int(int(bet_amount)*0.3)
	
	model1 = {
		"medium": "balance",
		"payee_id": user_account,
		"amount": total_win,
		"transaction_date": time.strftime('%Y-%m-%d', time.localtime(time.time())),
		"status": "pending",
		"description": "user winning total"
	}	

	r = requests.post(
		url,
		data = json.dumps(model1), 
		headers = {'content-type': 'application/json'},
	)

		#responseAction[r.status_code]()

def userLost (donate_account, bet_amount):
	#print(donate_account)
	#print(bet_amount)
	responseAction = {
			201 : lambda : print("It worked."),
			404 : lambda : print("NOT WORKING."),
	}

	total_donate = int(int(bet_amount) * 0.3)

	model2 = {
				"merchant_id": donate_account, 
				"medium": "balance",
				"purchase_date": time.strftime('%Y-%m-%d', time.localtime(time.time())),
				"amount": total_donate,
				"status": "pending",
				"description": "this is the money donating to the website"
	}

	url = "http://api.reimaginebanking.com/accounts/55fdbb19ce1cef140015e272/purchases?key=eee099222a7c7b3d9f6048e27122e51b"

	s = requests.post(
			url,
			data = json.dumps(model2), 
			headers = {'content-type': 'application/json'},
	)

	#responseAction[s.status_code]()


if __name__ == '__main__':
	userWin(['55e94a6cf8d8770528e617f8','55fd0ce93c3ce2100041179d'], 100, 5)
	userLost('55fda9d43c3ce2100041183e',100)


