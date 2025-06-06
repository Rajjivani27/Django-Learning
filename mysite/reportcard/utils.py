from .models import Student
import time
from django.core.mail import send_mail
from mysite.settings import *

def send_email():
    subject =  "Subject of the mail"
    message = "Message you want to send to the other party"
    from_email = EMAIL_HOST_USER #Email Address from you are sending email(You have to add this in settings.py file)
    recepient_list = ["mail_of_receiver"]

    send_mail(
        subject,
        message,
        from_email,
        recepient_list,
        fail_silently=False
    )