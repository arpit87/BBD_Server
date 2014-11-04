from django.db import models

# Create your models here.
class UserDetails(models.Model):
    bbdid = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=60)
    date_joined = models.DateField('date joined')

    def __unicode__(self):
        return self.name


class Friend(models.Model):
    bbdid = models.IntegerField(null=False)
    friend_bbd_id = models.IntegerField(null=False)

    def __unicode__(self):
        return str(self.bbdid)


