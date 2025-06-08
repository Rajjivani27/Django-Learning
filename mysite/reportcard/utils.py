from django.core.mail import send_mail,EmailMessage
from mysite.settings import *

def send_email():
    subject = "This is testing mail"
    message = "Testing django send_mail() functionality"
    from_email = EMAIL_HOST_USER
    recipient_list = ['email_of_receiver']
    send_mail(subject,message,from_email,recipient_list)
    send_mail_with_attachment(subject,message,from_email,recipient_list)

def send_mail_with_attachment(subject , message ,from_email,recipient_list):
    mail = EmailMessage(
            subject = subject,
            body = message,
            from_email= from_email,
            to=recipient_list,
            bcc=['email_of_person_for_bcc(optional)'],
        )
    
    mail.attach_file(f"{BASE_DIR}/100d_leetcode.png")

    mail.send()