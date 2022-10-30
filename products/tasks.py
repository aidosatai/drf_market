from celery import shared_task

from django.core.mail import send_mail



@shared_task
def send_email_celery():
    send_mail(
        subject='Hi',
        message='This is my first letter',
        from_email='atayev.aidos@gmail.com',
        recipient_list=['atayev341@gmail.com'],
        fail_silently=True,
        )





