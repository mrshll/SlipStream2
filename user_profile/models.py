from django.contrib.auth.models import User
from django.db import models
from show.models import *

class UserProfile(models.Model):
    user      = models.OneToOneField(User)
    shows     = models.ManyToManyField(Show, null=True, blank=True)
    providers = models.ManyToManyField(Provider, null=True, blank=True)
