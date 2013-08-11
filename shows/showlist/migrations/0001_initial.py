# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table(u'showlist_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'showlist', ['Genre'])

        # Adding model 'Venue'
        db.create_table(u'showlist_venue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'showlist', ['Venue'])

        # Adding model 'Show'
        db.create_table(u'showlist_show', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acts', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['showlist.Venue'])),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['showlist.Genre'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'showlist', ['Show'])


    def backwards(self, orm):
        # Deleting model 'Genre'
        db.delete_table(u'showlist_genre')

        # Deleting model 'Venue'
        db.delete_table(u'showlist_venue')

        # Deleting model 'Show'
        db.delete_table(u'showlist_show')


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