from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order. ' \
              'Your order id is {}.'.format(order.first_name, order.id)
    send_mail(subject=subject, message=message,
                          from_email='xaos79@yandex.ru', recipient_list=[order.email])
    # return mail_sent
