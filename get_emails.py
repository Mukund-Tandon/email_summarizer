import imaplib
import email
import os

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
# from gensim import keywords

host = 'imap.gmail.com'
username = 'mukund.projects.test@gmail.com'
password = os.environ.get('MUKUND_PROJECTS_TEST_PASS')

def summarize_email(email_body):
    print(summarize(email_body,ratio=0.5))
def get_email():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                summarize_email(body.decode())
            


if __name__ == "__main__":
    get_email()