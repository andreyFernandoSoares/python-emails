import imaplib

def execute():
    imaplib._MAXLINE = 1000000

    EMAIL = 'kkkk@gmail.com'
    PASSWORD = ''
    SERVER = 'imap.gmail.com'

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)

    mail.select('caixa_lotada')

    status, search_data = mail.search(None, 'ALL')

    mail_ids = []

    for block in search_data:
        mail_ids += block.split()

    start = mail_ids[0].decode()
    end = mail_ids[-1].decode()

    mail.store(f'{start}:{end}'.encode(), '+X-GM-LABELS', '\\Trash')


    mail.select('[Gmail]/Trash')
    mail.store("1:*", '+FLAGS', '\\Deleted')

    mail.expunge()

    mail.close()
    mail.logout()

if __name__ == "__main__":
    execute()