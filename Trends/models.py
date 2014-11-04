from django.db import models

# Create your models here.
class beeptimetrends(models.Model):
    beep_id = models.IntegerField()
    beep_freq = models.IntegerField()
    trend_type = models.IntegerField()

    def __unicode__(self):
        return self.beep_id

class individualbeeptrends(models.Model):
    bbs_id = models.IntegerField()
    beep_freq = models.IntegerField()
    trend_type = models.IntegerField()


    def __unicode__(self):
        return self.bbs_id