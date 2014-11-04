# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserDetails'
        db.create_table(u'User_userdetails', (
            ('bbdid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('date_joined', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'User', ['UserDetails'])

        # Adding model 'Friend'
        db.create_table(u'User_friend', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bbdid', self.gf('django.db.models.fields.IntegerField')()),
            ('friend_bbd_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'User', ['Friend'])


    def backwards(self, orm):
        # Deleting model 'UserDetails'
        db.delete_table(u'User_userdetails')

        # Deleting model 'Friend'
        db.delete_table(u'User_friend')


    models = {
        u'User.friend': {
            'Meta': {'object_name': 'Friend'},
            'bbdid': ('django.db.models.fields.IntegerField', [], {}),
            'friend_bbd_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'User.userdetails': {
            'Meta': {'object_name': 'UserDetails'},
            'bbdid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'date_joined': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['User']