from django.db import models
from common.util.netflix import flix

class Provider(models.Model):
    name      = models.CharField(max_length=40)
    cost      = models.FloatField()
    base_url  = models.URLField()
    # api_key = models.CharField(max_length=140)

class Show (models.Model):
    name        = models.CharField(max_length=140)
    status      = models.CharField(max_length=10, null=True) #running or done
    netflix_img = models.URLField(null=True)
    netflix_id  = models.URLField(max_length=120, null=True)
    def __unicode__(self):
        return self.name
    def netflix_provides(self):
        n = flix()
        if n.provide(self.name):
            return True
        return False

class Episode(models.Model):
    season    = models.IntegerField()
    ep_num    = models.IntegerField()
    title     = models.CharField(max_length=100)
    desc      = models.CharField(max_length=400)
    show      = models.ForeignKey(Show)
    providers = models.ManyToManyField(Provider)
