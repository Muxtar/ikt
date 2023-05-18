from django.db.models.signals import pre_save
from django.dispatch import receiver
from home.models import Tag, Storie
from django.utils.text import slugify


@receiver(pre_save, sender = Tag)
def TagSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
    return instance
    # instance.save()

@receiver(pre_save, sender = Storie)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    instance.title = instance.title.upper()
    return instance
    # instance.save()