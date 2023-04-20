from django.db.models.signals import pre_save
from django.dispatch import receiver
from home.models import Tag
from django.utils.text import slugify


@receiver(pre_save, sender = Tag)
def TagSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
    return instance
    # instance.save()