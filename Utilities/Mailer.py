# encoding=utf8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import email_config


class Mailer:
    def __init__(self):
        self.PASSWORD = email_config['PASSWORD']
        self.SMTP = email_config['SMTP']
        self.PORT = email_config['PORT']
        self.FROM_ADDR = email_config['ADDRESS']

    # takes kwargs dict: toaddr, subject, html
    def send(self, **kwargs):
        try:
            toaddr = kwargs.get('toaddr')
            msg = MIMEMultipart()
            msg['From'] = self.FROM_ADDR
            msg['To'] = toaddr
            msg['Subject'] = kwargs.get('subject')

            # set email template
            html = self.template(**kwargs)

            msg.attach(MIMEText(html.encode('utf-8'), 'html', 'utf-8'))
            server = smtplib.SMTP(self.SMTP, self.PORT)
            server.starttls()
            server.login(self.FROM_ADDR, self.PASSWORD)
            text = msg.as_string()
            server.sendmail(self.FROM_ADDR, toaddr, text)
            server.quit()
        except Exception as e:
            print(e)
            pass

    def template(self, **kwargs):
        html = kwargs.get('html')
        return html
