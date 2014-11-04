from django.db import models

# Create your models here.
class Beep(models.Model):
    beepid = models.AutoField(primary_key=True)
    beep_str = models.CharField(max_length=140)
    created_by = models.IntegerField(null=False)  # bbsid of creator
    beeplevel = models.IntegerField()
    misc_col1 = models.CharField(max_length=255)
    misc_col2 = models.CharField(max_length=255)
    misc_col3 = models.IntegerField(null=True)

    def __unicode__(self):
        return str(self.beepid)


class SentBeep(models.Model):
    beepid = models.IntegerField(null=False)
    from_id = models.IntegerField(null=False)
    to_id = models.IntegerField(null=False)
    date_time = models.DateTimeField(null=False)
    misc_col1 = models.CharField(max_length=255)
    misc_col2 = models.CharField(max_length=255)

    def __unicode__(self):
        return str(self.beepid)