# encoding=utf8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import emailConfig

class Mailer:
    def __init__(self):
        self.PASSWORD = emailConfig['PASSWORD']
        self.SMTP = emailConfig['SMTP']
        self.PORT = emailConfig['PORT']
        self.FROM_ADDR = emailConfig['ADDRESS']

    def sendMail(self, **kwargs):
        try:
            toaddr = kwargs.get('toaddr')
            msg = MIMEMultipart()
            msg['From'] = self.FROM_ADDR
            msg['To'] = toaddr
            msg['Subject'] = kwargs.get('subject')

            #set email template
            if kwargs.get('type') == 'reset':
                html = self.resetEmailTemplate(kwargs.get('username'), kwargs.get('uniqueID'))

            msg.attach(MIMEText(html.encode('utf-8'), 'html', 'utf-8'))
            server = smtplib.SMTP(self.SMTP, self.PORT)
            server.starttls()
            server.login(self.FROM_ADDR, self.PASSWORD)
            text = msg.as_string()
            server.sendmail(self.FROM_ADDR, toaddr, text)
            server.quit()
        except Exception as e:
            print (e)
            pass
