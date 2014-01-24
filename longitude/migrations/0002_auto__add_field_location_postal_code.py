# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Location.postal_code'
        db.add_column(u'longitude_location', 'postal_code',
                      self.gf('django.db.models.fields.CharField')(default=16367, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Location.postal_code'
        db.delete_column(u'longitude_location', 'postal_code')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['longitude']