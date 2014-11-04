# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Beep'
        db.create_table(u'Beep_beep', (
            ('beepid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beep_str', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('created_by', self.gf('django.db.models.fields.IntegerField')()),
            ('beeplevel', self.gf('django.db.models.fields.IntegerField')()),
            ('misc_col1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('misc_col2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('misc_col3', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'Beep', ['Beep'])

        # Adding model 'SentBeep'
        db.create_table(u'Beep_sentbeep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beepid', self.gf('django.db.models.fields.IntegerField')()),
            ('from_id', self.gf('django.db.models.fields.IntegerField')()),
            ('to_id', self.gf('django.db.models.fields.IntegerField')()),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('misc_col1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('misc_col2', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'Beep', ['SentBeep'])


    def backwards(self, orm):
        # Deleting model 'Beep'
        db.delete_table(u'Beep_beep')

        # Deleting model 'SentBeep'
        db.delete_table(u'Beep_sentbeep')


    models = {
        u'Beep.beep': {
            'Meta': {'object_name': 'Beep'},
            'beep_str': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'beepid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'beeplevel': ('django.db.models.fields.IntegerField', [], {}),
            'created_by': ('django.db.models.fields.IntegerField', [], {}),
            'misc_col1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'misc_col2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'misc_col3': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'Beep.sentbeep': {
            'Meta': {'object_name': 'SentBeep'},
            'beepid': ('django.db.models.fields.IntegerField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'from_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'misc_col1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'misc_col2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['Beep']