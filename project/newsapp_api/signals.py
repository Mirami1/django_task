from newsapp.models import News
from django.db.models import signals
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(signals.post_save, sender=News)
def new_news(sender, instance, created, **kwargs):
    subject = "News '{}' created!".format(
        instance.title, instance.id)
    message = instance.description
    send_mail(subject, message, '',
              [''])
