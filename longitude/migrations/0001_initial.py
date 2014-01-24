# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brand'
        db.create_table(u'longitude_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'longitude', ['Brand'])

        # Adding model 'Location'
        db.create_table(u'longitude_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['longitude.Brand'])),
        ))
        db.send_create_signal(u'longitude', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Brand'
        db.delete_table(u'longitude_brand')

        # Deleting model 'Location'
        db.delete_table(u'longitude_location')


    models = {
        u'longitude.brand': {
            'Meta': {'object_name': 'Brand'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'longitude.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['longitude.Brand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['longitude']