from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import ManageTask
from django.core.mail import send_mail


@receiver(post_save, sender=ManageTask)
def send_email(sender, instance, *args, **kwargs):
    subject = instance.title
    for mail in instance.user.all():
        from_email = 'cefer.h2018@mail.ru'
        message = f'Title: {instance.title}\nDescription: {instance.description}\nDeadline: {instance.deadline}'
        send_mail(subject, message, from_email, [f'{mail.email}'])
