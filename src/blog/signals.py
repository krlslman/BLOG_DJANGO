from django.db.models.signals import pre_save  # To create a slug before saving the post
from django.dispatch import receiver # to make saving wait until sth else is completed
from django.template.defaultfilters import slugify # to put dashs between strings instead of dot
from .models import Post


@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + " " + instance.title)

        