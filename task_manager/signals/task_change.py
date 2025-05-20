from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch import receiver

from ichdjangoproject import settings
from task_manager.models.task import Task


@receiver(pre_save, sender=Task)
def send_status_change_email(sender, instance, **kwargs):
    if not instance.pk:
        # New Task, not an update
        return

    try:
        previous = Task.objects.get(pk=instance.pk)
    except Task.DoesNotExist:
        return

    if previous.status != instance.status:
        # Customize this as needed
        subject = f"Task '{instance.title}' status changed"
        message = f"The status of task '{instance.title}' has changed from '{previous.status}' to '{instance.status}'."
        recipient_list = [instance.owner.email] if instance.owner and instance.owner.email else []

        if recipient_list:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False,
            )
