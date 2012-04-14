from django.db import models

class Provider(models.Model):
    name      = models.CharField(max_length=40)
    cost      = models.FloatField()
    base_url  = models.URLField()
    # api_key = models.CharField(max_length=140)

class Show (models.Model):
    name   = models.CharField(max_length=140)
    status = models.CharField(max_length=10, null=True) #running or done
    def __unicode__(self):
        return self.name

class Episode(models.Model):
    season    = models.IntegerField()
    ep_num    = models.IntegerField()
    title     = models.CharField(max_length=100)
    desc      = models.CharField(max_length=400)
    show      = models.ForeignKey(Show)
    providers = models.ManyToManyField(Provider)
