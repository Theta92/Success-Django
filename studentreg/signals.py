from django.db.models.signals import post_save
from django.dispatch import receiver

from studentreg.models import Module
from .utils import send_mail

@receiver(post_save, sender=Module)
def notify_students(sender, instance, **kwargs):
    student_emails= [registration.student.user.email for registration in instance.registrations.all()]
    send_mail(email=student_emails,subject=f"Module {instance.name} has a new update", message="Some message goes here")