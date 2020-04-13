from django.core.mail import send_mail

from .models import Order
from BookStore.settings import EMAIL_HOST_USER


def order_created(order_id, email):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order number {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.name,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          EMAIL_HOST_USER,
                          [email])
    return mail_sent
