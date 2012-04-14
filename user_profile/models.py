from django.contrib.auth.models import User
from django.db import models
from show.models import *

def UserProfile(models.Model):
    user  = models.OneToOneField(User)
    shows = models.ManyToManyField(Show)
    subs  = models.ManyToManyField(Provider)
