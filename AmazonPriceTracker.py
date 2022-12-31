import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Zero-One-Start-Build-Future/dp/0753555190/ref=sr_1_1?crid=2TNO5KJREKF9P&keywords=zero+to+one&qid=1672474096&sprefix=zero+to+on%2Caps%2C186&sr=8-1'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

def check_price():
	page = requests.get(URL, headers = headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="price").get_text()
	converted_price = float(price[1:4])

	if(converted_price < 169990):
		send_mail()

	print(converted_price)
	print(title.strip())

	if(converted_price > 169990):
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('sohamppatil7@gmail.com', 'xmitktcyfxlmedin')

	subject = 'Price decreased!'
	body = 'Check the Amazon link https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?crid=21KO4GFYO8SMP&keywords=sony+a7&qid=1672470045&sprefix=sony+a%2Caps%2C541&sr=8-1'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'sohamppatil7@gmail.com',
		'sohampatil.ai@gmail.com',
		msg
	)

	print('HEY EMAIL HAS BEEN SENT')

	server.quit()

check_price()
