# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Show.hype'
        db.add_column(u'showlist_show', 'hype',
                      self.gf('django.db.models.fields.IntegerField')(default=3),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Show.hype'
        db.delete_column(u'showlist_show', 'hype')


    models = {
        u'showlist.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'showlist.show': {
            'Meta': {'object_name': 'Show'},
            'acts': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['showlist.Genre']"}),
            'hype': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['showlist.Venue']"})
        },
        u'showlist.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['showlist']