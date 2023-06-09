from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile
from django.contrib.auth.models import User


@receiver(post_save, sender = User)
def ProfileSignal(sender, instance, created, **kwargs):
    if created:
        instance.set_password(instance.password)
        instance.save()
        Profile.objects.create(user = instance)



