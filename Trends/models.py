from django.db import models
from Beep.models import Beep
# Create your models here.

class beeptimetrends(models.Model):
    beep = models.ForeignKey(Beep,null=False)
    beep_freq = models.IntegerField(default=0)
    trend_type = models.IntegerField(default=1)
    is_new = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.beep)

    class Meta:
        unique_together = (('beep', 'trend_type'))

class individualbeeptrends(models.Model):
    bbs_id = models.IntegerField()
    beep_freq = models.IntegerField()
    trend_type = models.IntegerField()


    def __unicode__(self):
        return unicode(self.bbs_id)

class TrendsUpdateLastTime(models.Model):
    trend_type = models.IntegerField(null=False,default=1)
    last_update_time = models.DateTimeField(null=False)
    freq = models.IntegerField(null=False,default=5)
    misc = models.IntegerField(null=True)

    def __unicode__(self):
        return unicode(self.trend_type)