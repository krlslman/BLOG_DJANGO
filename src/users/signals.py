from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


#* Normally, we needed to create a Profile after we create the user. 
#* But we wanna make this automatic as follows
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwarg):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwarg):
    instance.profile.save()