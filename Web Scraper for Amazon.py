  
from bs4 import BeautifulSoup
import requests
import smtplib
import time

def check_price():
    URL = 'https://www.amazon.com/Seiko-SKX007K2-Divers-Automatic-Watch/dp/B000B5OD4I/ref=sr_1_2?keywords=seiko+skx&qid=1575598534&sr=8-2'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id= "productTitle").get_text()
    price = soup2.find(id= "priceblock_ourprice").get_text()

    converted_price = float(price[1:5])

    if(converted_price < 250):
        send_mail()


    print(title.strip())
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('TheBergSource@gmail.com','Current Password')
    
    subject = "The Watch is below $250! Now is your chance to buy!"
    body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the watch of your dreams. Link here: https://www.amazon.com/Seiko-SKX007K2-Divers-Automatic-Watch/dp/B000B5OD4I/ref=sr_1_2?keywords=seiko+skx&qid=1575598534&sr=8-2"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'TheBergSource@gmail.com',
        'alex.freberg@yahoo.com',
        msg
     
    )
    
    print("Hey Email Has Been Sent!")
    
    
while(True):
    check_price()
    time.sleep(1000)
    
