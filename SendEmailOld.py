import os
import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import itertools 
import base64
import io
import random
import time
from email.headerregistry import Address


### credentional for mail ###
sender_email = "Vladimir.mochalyuk@tp-link.com"
mailAddressFromPassword = "19_Tpl_75"
subject = "check in/check out"
to = ["kolyada.stanislava@tp-link.com"]
#cc = ["Vladimir.mochalyuk@tp-link.com"]
bcc = ["Vladimir.mochalyuk@tp-link.com"]
recips  = ["Vladimir.mochalyuk@tp-link.com", "kolyada.stanislava@tp-link.com"]

##Отправление письма
def SendMail():
    #time.sleep(random.randint(0,900))
    ### get system date ###
    #curDates = datetime.datetime.now().date().strftime("%d-%m-%Y")
   
	### creating tp_link image from file
    #image_file = io.BytesIO(open("C:\\Scripts\\tp-link.png",'rb').read())
    #encoded_image = base64.b64encode(image_file.getvalue()).decode("utf-8")
    #htmlImg_tp_link = '<img src="data:image/png;base64,%s"/>' % encoded_image

    ### creating message
    html = """\
        <html>
          <body>
            <p style="color: Indigo;font-size:16;"> <br> check in/check out.<br> 
                <br><br>Best regards!<br>
                Vladimir Mochaliuk<br>
                Head of end-users technical support  Department<br>
                <a href="Vladimir.mochalyuk@tp-link.com">Vladimir.mochalyuk@tp-link.com</a><br> 
                Mob: +380681005894<br>
                Tel: +380445905113 (7500)<br></p>
          </body>
        </html>
        """

    messageText = MIMEText(html, "html")

    ##Формирование письма
    subject = "check in/check out"
    message = MIMEMultipart("alternative")       
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = ",".join(to)
    #message["Cc"] = ",".join(cc)
    message["Bcc"] = ",".join(bcc)
    message.attach(messageText) 

    ##Подключение к почтовому серверу и отправка сообщения
    smtpServer = smtplib.SMTP('outlook.office365.com', 587)
    smtpServer.starttls()
    smtpServer.login(sender_email, mailAddressFromPassword)
    smtpServer.sendmail(sender_email, recips, message.as_string())
    smtpServer.quit()
#################################################################################

### run  ####
SendMail()