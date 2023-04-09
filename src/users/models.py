from django.db import models
from django.contrib.auth.models import User

def user_profile_path(instance, filename):
    return "user/{0}/{1}".format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_profile_path, default='default_user_avatar.jpg')
    bio = models.TextField(blank=True)

    def __str__(self):
        return "{}{}".format(self.user,"'s profile")