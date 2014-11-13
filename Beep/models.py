from django.db import models
from datetime import datetime


class BeepManager(models.Manager):
    def get_by_natural_key(self, beep_id):
        return self.get(beepid=beep_id)

# Create your models here.
class Beep(models.Model):
    objects = BeepManager()
    beepid = models.AutoField(primary_key=True)
    beep_str = models.CharField(max_length=140)
    created_by = models.IntegerField(null=False)  # bbsid of creator
    beeplevel = models.IntegerField(default=3)
    image_str = models.CharField(max_length=255,null=True)
    rebeeps = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    date_created = models.DateTimeField(null=False,default=datetime.now())
    misc_col1 = models.CharField(max_length=255)
    misc_col2 = models.CharField(max_length=255)
    misc_col3 = models.IntegerField(null=True)

    def natural_key(self):
        return self.beepid,self.beep_str

    def __unicode__(self):
        return unicode(self.beepid)


class SentBeep(models.Model):
    beep = models.ForeignKey(Beep,null=False)
    from_id = models.IntegerField(null=False)
    to_id = models.IntegerField(null=False)
    date_time = models.DateTimeField(null=False,default=datetime.now())
    misc_col1 = models.CharField(max_length=255)
    misc_col2 = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.beep)
