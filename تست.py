


	
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