import time
from flask import Request
from selenium import  webdriver
from selenium.webdriver.edge.service import Service
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
from webdriver_manager.microsoft import EdgeChromiumDriverManager





def send_email(email,subject, body):
    try:
        sender_email = 'support@bixid.in'
        sender_password = 'support@bixid'
        recipient_email =email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('mum2.hostarmada.net', 465, context=context) as server:
            # server.starttls()
            print(' email server started ')
            server.login(sender_email, sender_password)
            print(' email logged in  ')
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print('email sent')
            data={"Status": "Success","Message":"Thanks for placing your request, our customer success team will ping you shortly"}
            return  data 
    except Exception as e:
        data= {"Status": "Fail","Message":f"There is some error contact to our customer care for support {e}"}
        return data 
class ONLOGIN:
    def __init__(self):
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        options.add_argument("headless")
        options.add_argument("disable-gpu")
        service = Service(EdgeChromiumDriverManager().install())
        self.driver=webdriver.Edge(service=service,options=options)
        # self.driver=webdriver.Edge()
        print(self.driver.capabilities)
    def auto_email(self,email):
        try:
            print("clvdnvdovhsfushss;hufgf;lufjh;vuv;sa")
            self.driver.get("https://google.com")
            title=self.driver.title
            send_email(email,title , f"got this as title :- {title}")
        except Exception as e :
            print(e)    
            
            
            
def senf_email(email):
        obj=ONLOGIN()
        obj.auto_email(email)
        
       