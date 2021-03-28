from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #one to one rel with User model
    # taken_polls = models.ManyToManyField('polls.Poll')
    class Meta:
       verbose_name = 'Профиль'
       verbose_name_plural = 'Профили'

    def __str__(self):
        return f"{self.user.username}"



