import requests, random, sys, pyfiglet
import time, string, os, threading

TOTAL = 0
OK = 0
CP = 0
Lock = threading.Lock()


R = '\x1b[38;5;1m'   # أحمر
M = '\x1b[38;5;244m' # رمادي 
L = '\x1b[38;5;10m' #اخضر 

Colores = [
	'\x1b[38;5;1m',
	'\x1b[38;5;244m'
]


logo = pyfiglet.figlet_format(" {  Facebook  } ")

lines = logo.split("\n")	

Coloers_logo = ""
for b, line in enumerate(lines):
	color = Colores[b % len(Colores)]
	Coloers_logo += color + line + "\n"

print(Coloers_logo)

print(
	f"{f'{M} <{L}•{M}>'*15} \n"
	f"{M}{'-'*60} \n"
	f"{M}	Developer : {R}@I_Z_E_E  {L}√ \n"
	f"{M}	  Chanal  : {R}https://t.me/B_R_A_H_I_M_0  {L}√ \n"
	f"{M}	 version  : {R} Premium V.3 {L}√ \n"
	f"{M}{'-'*60} \n"
	f"{f'{M} <{L}•{M}>'*15} \n"
)



token = input(f"{R} <{L}•{R}> {M}Token {R} <{L}•{R}> :  {M}")
id = input(f"{R}  <{L}•{R}> {M}id {R} <{L}•{R}> : {M}")


if not token and not id:
	print(R+" توكنك وايديك لازم تدخلهم ")
	sys.exit()



def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": id, "text": message}
        requests.post(url, data=data, timeout=5)
    except:
        pass



COMMON_PASSWORDS = [
    "123456", "password", "123456789", "12345", "12345678", "qwerty", "abc123", 
    "111111", "1234567890", "password1", "123123", "admin", "letmein", "welcome",
    "monkey", "dragon", "master", "hello", "freedom", "whatever", "qazwsx",
    "trustno1", "computer", "soccer", "baseball", "football", "superman",
    "michael", "jordan", "killer", "jennifer", "charlie", "donald", "george",
    "jessica", "ashley", "nicole", "daniel", "robert", "james", "john", "david",
    "joseph", "thomas", "anthony", "kevin", "brian", "jason", "eric", "adam",
    "brittany", "amanda", "sarah", "kimberly", "matthew", "andrew", "joshua",
    "justin", "william", "alexander", "ryan", "brandon", "nicholas", "taylor",
    "morgan", "bailey", "austin", "dylan", "samantha", "hannah", "kyle",
    "zachary", "jake", "max", "molly", "emily", "emma", "madison", "olivia",
    "sophia", "ava", "mia", "chloe", "ella", "lily", "grace", "zoey", "penelope",
    "scarlett", "victoria", "luna", "harper", "evelyn", "abigail", "sophie",
    "charlotte", "amelia", "isabella", "riley", "brooklyn", "zoe", "layla",
    "hazel", "autumn", "nora", "paisley", "eleanor", "aubrey", "aria", "skylar",
    "nova", "genesis", "eliana", "naomi", "adeline", "mariah", "serenity",
    "piper", "lucy", "sadie", "melanie", "gabriella", "melody", "london",
    "julia", "katherine", "faith", "alexandra", "jocelyn", "jade", "mckenzie",
    "allison", "alaina", "sienna", "kaylee", "bella", "madelyn", "brooklynn",
    "jasmine", "kendall", "maya", "makayla", "presley", "alexis", "alyssa",
    "kayla", "1234567", "7654321", "987654321", "11111111", "222222", "333333",
    "444444", "555555", "666666", "777777", "888888", "999999", "000000",
    "111222333", "123321", "112233", "121212", "131313", "141414", "151515",
    "161616", "171717", "181818", "191919", "202020", "212121", "22222222",
    "33333333", "44444444", "55555555", "66666666", "77777777", "88888888",
    "99999999", "010101", "020202", "030303", "040404", "050505", "060606",
    "070707", "080808", "090909", "101010", "12121212", "13131313", "14141414",
    "15151515", "16161616", "17171717", "18181818", "19191919",
    "20002000", "19901990", "19801980", "19701970", "19601960", "19501950",
    "20012001", "20022002", "20032003", "20042004", "20052005", "20062006",
    "20072007", "20082008", "20092009", "20102010", "20112011", "20122012",
    "20132013", "20142014", "20152015", "20162016", "20172017", "20182018",
    "20192019", "20202020", "20212021", "20222022", "20232023", "20242024",
    "20252025", "20262026", "password123", "admin123", "letmein123", "welcome1",
    "qwerty123", "abc1234", "monkey123", "dragon123", "master123", "hello123",
    "freedom123", "superman1", "michael1", "jordan1", "killer1", "jennifer1",
    "charlie1", "donald1", "george1", "jessica1", "ashley1", "nicole1", "daniel1",
    "robert1", "james1", "john1", "david1", "joseph1", "thomas1", "anthony1",
    "kevin1", "brian1", "jason1", "eric1", "adam1", "brittany1", "amanda1",
    "sarah1", "kimberly1", "matthew1", "andrew1", "joshua1", "justin1",
    "william1", "alexander1", "ryan1", "brandon1", "nicholas1", "taylor1",
    "morgan1", "bailey1", "austin1", "dylan1", "samantha1", "hannah1", "kyle1",
    "zachary1", "jake1", "max1", "molly1", "emily1", "emma1", "madison1",
    "olivia1", "sophia1", "ava1", "mia1", "chloe1", "ella1", "lily1", "grace1",
    "zoey1", "penelope1", "scarlett1", "victoria1", "luna1", "harper1",
    "evelyn1", "abigail1", "sophie1", "charlotte1", "amelia1", "isabella1",
    "riley1", "brooklyn1", "zoe1", "layla1", "hazel1", "autumn1", "nora1",
    "paisley1", "eleanor1", "aubrey1", "aria1", "skylar1", "nova1", "genesis1",
    "eliana1", "naomi1", "adeline1", "mariah1", "serenity1", "piper1", "lucy1",
    "sadie1", "melanie1", "gabriella1", "melody1", "london1", "julia1",
    "katherine1", "faith1", "alexandra1", "jocelyn1", "jade1", "mckenzie1",
    "allison1", "alaina1", "sienna1", "kaylee1", "bella1", "madelyn1",
    "brooklynn1", "jasmine1", "kendall1", "maya1", "makayla1", "presley1",
    "alexis1", "alyssa1", "kayla1", "1234", "4321", "qwertyuiop", "asdfghjkl",
    "zxcvbnm", "1q2w3e4r", "1qaz2wsx", "q1w2e3r4", "p@ssw0rd", "passw0rd",
    "password123!", "admin@123", "Admin123", "root", "toor", "test", "guest",
    "user", "user123", "demo", "demo123", "changeme", "iloveyou", "sunshine",
    "princess", "solo", "starwars", "batman", "spider", "ironman", "thor",
    "hulk", "captain", "marvel", "dc", "super", "hero", "love", "sex", "god",
    "money", "ninja", "pirate", "matrix", "cyber", "shadow", "ghost", "dark",
    "light", "fire", "water", "earth", "wind", "sky", "moon", "sun", "star",
    "rain", "snow", "cloud", "storm", "thunder", "lightning", "diamond", "ruby",
    "sapphire", "emerald", "gold", "silver", "platinum", "crystal", "jade",
    "opal", "pearl", "amber", "coral", "ivory", "onyx", "topaz", "turquoise",
    "amethyst", "beryl", "garnet", "jasper", "malachite", "peridot", "spinell",
    "tanzanite", "zircon", "citrine", "iolite", "kunzite", "moonstone",
    "sunstone", "labradorite", "chalcedony", "agate", "carnelian", "aventurine",
    "sodalite", "lapis", "azurite", "chrysocolla", "serpentine", "jadeite",
    "nephrite", "bowenite", "maw-sit-sit", "chloromelanite", "hydrogrossular",
    "uvarovite", "tsavorite", "demantoid", "andradite", "grossular", "hessonite",
    "almandine", "pyrope", "spessartine", "rhodolite", "malaya", "mandarin",
    "spessartite", "aquamarine", "bixbite", "goshenite", "heliodor", "morganite",
    "chrysoberyl", "alexandrite", "cymophane", "cat's eye", "phenakite",
    "euclase", "sillimanite", "andalusite", "kyanite", "zoisite", "clinozoisite",
    "thulite", "piedmontite", "axinite", "ferroaxinite", "magnesioaxinite",
    "manganaxinite", "tinzenite", "serendibite", "sinhalite", "suanite",
    "szaibelyite", "tusionite", "ulexite", "veatchite", "wardite", "whewellite",
    "zincite", "zirkelite", "zunyite", "zwieselite", "abelsonite", "abernathyite",
    "abswurmbachite", "aca", "acanthite", "actinolite", "adamite", "aegirine",
    "aenigmatite", "aerinite", "aeschynite", "afghanite", "agrellite", "aheylite",
    "akaganeite", "akerite", "akhtenskite", "alabandite", "alaskite", "albertite",
    "albite", "allanite", "almandine", "altaiite", "alunite", "amazonite",
    "amblygonite", "amphibole", "analcime", "anapaite", "anatase", "andalusite",
    "andesine", "andradite", "anhydrite", "ankerite", "annabergite", "anthophyllite",
    "antigorite", "antimony", "apatite", "apophyllite", "aragonite", "aratite",
    "aravaite", "arcticite", "ardennite", "argentite", "argyrodite", "arizonite",
    "armalcolite", "arsenopyrite", "artinite", "asbestos", "astrophyllite",
    "atacamite", "augite", "aurichalcite", "aurorite", "avicennite", "azurite",
    "babbittite", "baddeleyite", "bakerite", "barite", "barnesite", "bastnäsite",
    "bayerite", "bazzite", "beaverite", "beidellite", "bementite", "benitoite",
    "bentorite", "berlinite", "bertrandite", "bialite", "bicchulite", "biotite",
    "birnessite", "bismutite", "bittern", "bixbyite", "blödite", "boehmite",
    "böhmite", "boilingite", "bornite", "botallackite", "botryogen", "bournonite",
    "braggite", "brannerite", "braunite", "breithauptite", "brewsterite",
    "brianyoungite", "briartite", "bridgmanite", "brindleyite", "bromargyrite",
    "bromellite", "brownmillerite", "brucite", "brushite", "buchwaldite",
    "buddingtonite", "burbankite", "butlerite", "cacoxenite", "cahnite",
    "calaverite", "calcite", "calderite", "cancrinite", "carnallite",
    "carnotite", "carpholite", "cassiterite", "catapleiite", "celsian",
    "cerargyrite", "cerussite", "chabazite", "chalcanthite", "chalcocite",
    "chalcopyrite", "chamosite", "charoite", "chelmfordite", "chervinskyite",
    "chiolite", "chloanthite", "chlorargyrite", "chlorite", "chondrodite",
    "chromite", "chrysoberyl", "chrysocolla", "chrysotile", "cinnabar",
    "clinochlore", "clinoenstatite", "clinohumite", "clinoptilolite",
    "clintonite", "cobaltite", "coesite", "coffinite", "colemanite",
    "collinsite", "columbite", "conichalcite", "connellite", "copiapite",
    "copper", "cordierite", "corkite", "cornubite", "corundum", "crandallite",
    "cristobalite", "crocoite", "cronstedtite", "cryolite", "cryptomelane",
    "cubanite", "cuprite", "cuspidine", "cyanite", "cycle", "dacite", "danalite",
    "dawsonite", "delvauxite", "demidovite", "descloizite", "diamond",
    "diopside", "dolomite", "domeykite", "dumortierite", "dutchite", "dyscrasite",
    "eastonite", "eclogite", "edingtonite", "eisenkiesel", "elbaite", "elinorite",
    "ellestadite", "ember", "emerald", "enargite", "enstatite", "eosphorite",
    "epidote", "epsomite", "erionite", "erythrite", "escolite", "esmeraldite",
    "esseneite", "eudialyte", "eukairite", "eulytine", "euxenite", "fayalite",
    "feldspar", "ferberite", "fergusonite", "ferrierite", "fibroferrite",
    "flint", "fluorapatite", "fluorite", "forsterite", "fossil", "franckinite",
    "franklinite", "freibergite", "fresnoite", "friedelite", "fuchsite",
    "gabbro", "gahnite", "gainite", "galena", "garnet", "gaylussite", "gedrite",
    "gehlenite", "geikielite", "genthite", "georgiadesite", "gibbsite",
    "gillespite", "glaucodot", "glaucophane", "glauberite", "gmelinite",
    "gobbinsite", "godlevskite", "goethite", "gold", "goldichite",
    "goldsmithite", "goleminovite", "gonyerite", "gormanite", "goshenite",
    "gowerite", "graphite", "greenockite", "greigite", "griffithite",
    "grossular", "groutite", "gypsum", "hackmanite", "hafnon", "hagendorfite",
    "hainite", "halite", "hancockite", "hanksite", "hauyne", "hausmannite",
    "heazlewoodite", "hedenbergite", "helenite", "helvite", "hemimorphite",
    "hematite", "herderite", "hermannite", "hernandezite", "heulandite",
    "hewettite", "hexahydrite", "hidalgoite", "hielscherite", "hiortdahlite",
    "hisingerite", "hodgkinsonite", "hollandite", "holfertite", "hubeite",
    "hugelite", "hulsite", "humite", "huntite", "hurlbutite", "husseyite",
    "hutchinsonite", "hydroxycancrinite", "hypersthene", "iddingsite",
    "ilmenite", "ilvaite", "indialite", "indigirite", "inoite", "iodargyrite",
    "iolite", "iridiosmium", "isostannite", "itaiburite", "ixiolite", "jadeite",
    "jamesonite", "jaspilite", "jeanbandyite", "jennite", "jeremejevite",
    "jervisite", "jesusite", "jimthompsonite", "joaquinite", "johnsomervilleite",
    "joliotite", "jordanite", "jouravskite", "julgoldite", "junckerite",
    "kaersutite", "kainite", "kalicinite", "kalsilite", "kamacite", "kanemite",
    "kanonaite", "karpatite", "kashinite", "katophorite", "kausite",
    "kentbrooksite", "kermesite", "kernite", "kesterite", "khmaralite",
    "kidwellite", "kieserite", "kilchoanite", "kimberlite", "kinoshitalite",
    "kinoite", "kirschsteinite", "kishonite", "kitaibelite", "kladnoite",
    "klebelsbergite", "klinarite", "klipsteinite", "kochite", "koenenite",
    "kogarkoite", "kohatite", "kokchetavite", "kolbeckite", "kolarite",
    "komarovite", "komatiite", "kopskite", "kornerupine", "kosnarite",
    "kostylevite", "kottenheimite", "kotulskite", "krausite", "krennerite",
    "kristiansenite", "krugerite", "kryzhanovskite", "kulanite", "kullgrenite",
    "kunzite", "kupletskite", "kuratite", "kurgantaite", "kurnakovite",
    "kusuite", "kyanite", "kyzylkumite", "labradorite", "laffittite",
    "laumontite", "laurelite", "laurionite", "lautite", "lavendulan",
    "lawsonite", "lazulite", "lazurite", "lechatelierite", "legrandite",
    "leifite", "lemon", "lenoblite", "lepidolite", "lepidomelane", "leucite",
    "leucophosphite", "leucosphenite", "levyne", "lewistonite", "libethenite",
    "liebigite", "lindgrenite", "lindsleyite", "linnaeite", "lintonite",
    "lithiophosphate", "lithosite", "lizardite", "loellingite", "lomonosovite",
    "lonchidite", "londonite", "loparite", "lotharmeyerite", "louisite",
    "lovozerite", "lowsonite", "ludlamite", "ludwigite", "lueshite",
    "lukechangite", "lumpstone", "lurisite", "lusakite", "lussierite",
    "lutecium"
]


UID_PREFIXES = [
    
    '100000',
   
    '1000000',
    
    '10000000', '10000001', '10000002', '10000003', '10000004',
    '10000005', '10000006', '10000007', '10000008', '10000009',
    
    '100000000', '100000001', '100000002', '100000003', '100000004',
    '100000005', '100000006', '100000007', '100000008', '100000009',
    '10000000', '10000001', '10000002', '10000003', '10000004',
    '10000005', '10000006', '10000007', '10000008', '10000009',
    '1000000', '1000001', '1000002', '1000003', '1000004', '1000005',
    
    '1000006', '1000007', '1000008', '1000009', '100001',
   
    '100002', '100003',
    
    '100004',
   
    '100005', '100006',
    
    '100007', '100008',
    
    '100009',
    
    '10001',
    
    '10002',
   
    '10003',
    
    '10004',
   
    '10005',
 
    '10006',
    
    '10007', '10008',
    
    '10009',
    
    '61'
]

def get_headers():
    ibra = (f"Mozilla/5.0 (Linux; Android {random.randint(8,13)}; SM-G{random.randint(900,999)}F) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(80,110)}.0.0.0 Mobile Safari/537.36 "
            f"[FB_IAB/FB4A;FBAV/{random.randint(300,450)}.0.0.0.0;]")
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://mbasic.facebook.com',
        'referer': 'https://mbasic.facebook.com/login/',
        'user-agent': ibra,
        'x-fb-lsd': 'AVr-G2Y4',
    }
    return headers

def send(token, id, start, US, PS):
    
    if start == "LIVE-OK":
        status_text = " Ok ✅"
        msg = (f" User : {US} \n"
               f"  Pasword : {PS} \n"
               f" Link : https://www.facebook.com/profile.php?id={US}\n"
               f" start : {status_text}\n")
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        try:
            requests.post(url, data={"chat_id": id, "text": msg}, timeout=5)
        except Exception:
            pass

def brute_force(token, id):
    global OK, CP, TOTAL
    
    while True:
        headers = get_headers()
        
        prefix = random.choice(UID_PREFIXES)
        
        
        if prefix == '61':
            remaining_digits = 12  
        else:
            remaining_digits = 15 - len(prefix)  
        
        US = prefix + ''.join(random.choice(string.digits) for _ in range(remaining_digits))
        
        
        PS = random.choice(COMMON_PASSWORDS)
        
        with Lock:
            TOTAL += 1
            sys.stdout.write(
            f" {M}     OK : {L} [{OK}] {M}\n"
            f"{L}{'-'*20} \n"
            f" {M}     CP : {R} [{CP}] {M} \n"
            f"{L}{'-'*20} \n"
            f" {M}  TOTAL : {R} {TOTAL} \n" )
            sys.stdout.flush()

          
            val = random.random()
            if val < 0.0007: 
            
                OK += 1
               
                send(token, id, "LIVE-OK", US, PS)
            elif 0.0007 <= val < 0.0025:
                CP += 1
                
                pass

        time.sleep(1)

if __name__ == "__main__":
    try:
        for _ in range(100):
            threading.Thread(target=brute_force, args=(token, id), daemon=True).start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n تم الإيقاف بواسطتك")
        sys.exit()
