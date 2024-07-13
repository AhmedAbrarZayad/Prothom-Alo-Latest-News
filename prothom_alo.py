import requests
from bs4 import BeautifulSoup
#for sending email
import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
#import data
import json
#system date & time
import datetime
date = datetime.datetime.now()
#email content
content = ""
def news(url):
    print("Lets get some news for you")
    global content
    cnt = '<br>Latest news for You<br>'+'<br>'+'-'*50+'<br>'+'\n'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for i,tag in enumerate(soup.find_all('h3')):
        if i >=10:
            continue
        title = tag.text.strip()
        link = tag.find('a')['href']
        if not link.startswith('http'):
            link = 'https://www.prothomalo.com'+link
        cnt += f'{i+1} :: <a href="{link}">{title}</a><br>\n'
    return cnt
# SERVER = 'smtp.gmail.com' PORT = 587
def send_email(SERVER,PORT,FROM,PASS,TO,msg):
    print("Initializing Email")
    server = smtplib.SMTP(SERVER,PORT)
    #server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM,PASS)
    server.sendmail(FROM,TO,msg.as_string())
    server.quit()
    print("Email Sent")
def email(SERVER,PORT):
    print("Composing Email")
    FROM = '' #Assuming the sender is always the same, input your email here
    TO = [] #Assuming your
    PASS = ''
    try:
        with open('senders.json', 'r') as file:
            data = json.load(file)
            FROM = data["FROM"]
            PASS = data["PASS"]
    except FileNotFoundError:
        print("senders.json can't be found. Run the sender_data.py. Then, run this file")
        return
    except KeyError:
        print("Either FROM or PASS key is missing in senders.json. Running sender_data.py")
        return
    try:
        with open('receivers.json', 'r') as file:
            TO = json.load(file)  
    except FileNotFoundError:
        print("Receivers.json can't be found. Running receivers_data.py")
    msg = MIMEMultipart()
    msg['FROM'] = FROM
    msg['TO'] = ", ".join(TO)
    msg['Subject'] = 'Latest news for you'+ ' ' + str(date.day) + ' '+ str(date.month) + ' '+ str(date.year) + '\n'
    msg.attach(MIMEText(content,'html'))
    send_email(SERVER,PORT,FROM,PASS,TO,msg)

def main():
    # Get Content 
    global content
    content+=news('https://www.prothomalo.com/collection/latest')
    content+=('<br>----------<br>')
    content+=('<br><br>End of Message')
    #Compose Email
    SERVER = 'smtp.gmail.com'
    PORT = 587
    email(SERVER,PORT)


if __name__=='__main__':
    main()