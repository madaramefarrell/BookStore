from django.core.mail import send_mail

from django.contrib.auth.models import User
from BookStore.settings import EMAIL_HOST_USER


def forgetPassword(email, name):
    """

    Send reset password mail to user

    """

    subject = 'Password Change from BookStore'
    message = 'Dear {}\n\n' \
              'You got the forget password mail'.format(name)
    mail_sent = send_mail(subject,
                          message,
                          EMAIL_HOST_USER,
                          [email])
    return mail_sent
