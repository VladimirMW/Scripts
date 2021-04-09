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
    time.sleep(random.randint(0,900))
       
    ### creating tp_link image from file
    image_file = io.BytesIO(open("C:\\Scripts\\tp-link.png",'rb').read())
    encoded_image = base64.b64encode(image_file.getvalue()).decode("utf-8")
    htmlImg_tp_link = '<img src="data:image/png;base64,%s"/>' % encoded_image

    ### creating SMB image from file
    image_file = io.BytesIO(open("C:\\Scripts\\SMB.png",'rb').read())
    encoded_image = base64.b64encode(image_file.getvalue()).decode("utf-8")
    htmlImg_SMB = '<a href="https://www.tp-link.com/uk-ua/omada-wifi6/"><img src="data:image/png;base64,%s"/></a>' % encoded_image

    ### creating SOHO image from file
    image_file = io.BytesIO(open("C:\\Scripts\\SOHO.png",'rb').read())
    encoded_image = base64.b64encode(image_file.getvalue()).decode("utf-8")
    htmlImg_SOHO = '<a href="https://www.tp-link.com/uk-ua/wifi6/"><img src="data:image/png;base64,%s"/></a>' % encoded_image

    ### creating fb image from file
    image_file = io.BytesIO(open("C:\\Scripts\\fb.png",'rb').read())
    encoded_image = base64.b64encode(image_file.getvalue()).decode("utf-8")
    htmlImg_fb = '<a href="https://www.facebook.com/TpLinkUkraine/"><img src="data:image/png;base64,%s"/></a>' % encoded_image

    ### creating inst image from file
    image_file = io.BytesIO(open("C:\\Scripts\\inst.png",'rb').read())
    encoded_image = base64.b64encode(image_file.getvalue()).decode("utf-8")
    htmlImg_inst = '<a href="https://www.instagram.com/tplinkua/"><img src="data:image/png;base64,%s"/></a>' % encoded_image

    ### creating youtube image from file
    image_file = io.BytesIO(open("C:\\Scripts\\youtube.png",'rb').read())
    encoded_image = base64.b64encode(image_file.getvalue()).decode("utf-8")
    htmlImg_youtube = '<a href="https://www.youtube.com/channel/UC1nov249KNQ3Gn30oCQxMVQ"><img src="data:image/png;base64,%s"/></a>' % encoded_image

    ### creating message
    html = """\
        <html>
        <head>
        <meta charset="utf-8">
        <style type="text/css">
           p { 
                font-family: Calibri,Candara,Segoe,Segoe UI,Optima,Arial,sans-serif;
                font-weight: normal;
                color: black;
                font-size: 11pt;
             }
        </style>
        </head>
          <body>
            <p>Check in/Check out<br><br></p>
            <p style="font-weight:600">Best regards!<br>
            Vladimir Mochaliuk<br>
            <span style="font-weight:normal">Head of end-users technical support  Department</span><br> """ + htmlImg_tp_link + """<br><br>
            """ + htmlImg_SMB + htmlImg_SOHO +"""<br><br>
            <p> <span style="color: #1BA6A9; font-weight:700"> TP-Link Ukraine</span><br> 
            Mob: +38 068 100 58 94   <span style="color: #1BA6A9">I</span>  Phone: +38 044 590 51 13 (7500)   <span style="color: #1BA6A9">I</span>   Skype: mochaliukv<br>
            20 Metalistiv Street  <span style="color: #1BA6A9">I</span>  03057 Kyiv, Ukraine  <span style="color: #1BA6A9">I</span>  www.tp-link.com/uk-ua<br>
            """ + htmlImg_fb + htmlImg_inst + htmlImg_youtube +"""<p>
          </body>
        </html>
        """


    messageText = MIMEText(html, "html")

    ##Формирование письма
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


