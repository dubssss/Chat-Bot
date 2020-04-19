
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendemailmsg(excelfile):

    email_user = os.environ.get('email_user')
    email_password = os.environ.get('email_password')
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_user
    msg['Subject'] = "Email from BOT"
    body = "Please find the attached form below. \n\n\n\nThanks\nRPA ChatBot"
    msg.attach(MIMEText(body, 'plain'))
    filename = "exceldocu"+excelfile+".xlsx"
    attachment = open("exceldocu"+excelfile+".xlsx", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_user,email_password)
    text = msg.as_string()
    s.sendmail(email_user, email_user, text)
    s.quit()

if __name__=="__main__":
    sendemailmsg("1")
