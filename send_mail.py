import smtplib
from email.mime.text import MIMEText

def execute():
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465

    USERNAME = 'kkkl@gmail.com'
    PASSWORD = ''

    from_addr = 'kkk@weecode.com.br'
    to_addrs = ['kk@gmail.com']

    message = MIMEText('Dae Bisquila')
    message['subject'] = 'Receba'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(USERNAME, PASSWORD)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()

if __name__ == "__main__":
    execute()

