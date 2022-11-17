import smtplib
import mimetypes
import pandas as pd
from os import getenv
from pathlib import Path
from dotenv import load_dotenv
from email.utils import formatdate
from email.message import EmailMessage
from os.path import abspath, dirname, join

# Path
path = dirname(dirname(abspath(__file__)))
mail_path = join(path, 'email')

# Load dotenv variable
load_dotenv(join(path, '.env'))

# Load mail list
used_mails = list(pd.read_csv(join(mail_path, 'used_mail.csv'))['mails'])
mails = list(pd.read_csv(join(mail_path, 'mail.csv'))['mails'])

# Server start and login with credentials
server = smtplib.SMTP('SMTP.office365.com', 587)
server.connect('SMTP.office365.com', 587)
server.ehlo()
server.starttls()
server.login(getenv("EMAIL"), getenv("PASSWORD"))

# Iterate through mails list
for mail in mails:
    email = mail.strip()
    if email not in used_mails:
        # Headers : your personal address, date, subject, message
        msg = EmailMessage()
        msg['From'] = f'Firstname Lastname <{getenv("EMAIL")}>'
        msg['To'] = email
        msg["Date"] = formatdate(localtime=True)
        msg['Subject'] = 'Open application for an internship'
        msg.set_content("""\
        To whom it may concern,

        As part of my studies, I am looking for an assignment abroad between <month> <day> and <month> <day> <year> , in my field of study, namely <your_field_of_study>.

        I've looked at what you do in the company and I would be very interested in doing an internship with you.

        I am attaching my CV if you want to know more about me.

        Don't hesitate to contact me, I'm available for any discussion.

        Yours faithfully,

        <Firstname Lastname>
        """)

        # Load the CV
        cfile = Path(join(path, '<your_cv>.pdf'))
        ctype, encoding = mimetypes.guess_type(cfile)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        msg.add_attachment(cfile.read_bytes(), maintype=maintype, subtype=subtype, filename=cfile.name)

        # Trying to send the message, catch if there are any error
        try:
            server.send_message(msg)
            print('{0} : send'.format(email))
            with open(join(mail_path, 'used_mail.csv'), 'a') as f:
                f.write('\n{0}'.format(email))
        except smtplib.SMTPException as e:
            print('{0} : {1}'.format(email, e))
            exit(1)

# Quit server
server.quit()
