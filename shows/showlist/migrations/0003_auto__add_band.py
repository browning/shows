# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Band'
        db.create_table(u'showlist_band', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('youtube_link', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'showlist', ['Band'])

        # Adding M2M table for field bands on 'Show'
        m2m_table_name = db.shorten_name(u'showlist_show_bands')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('show', models.ForeignKey(orm[u'showlist.show'], null=False)),
            ('band', models.ForeignKey(orm[u'showlist.band'], null=False))
        ))
        db.create_unique(m2m_table_name, ['show_id', 'band_id'])


    def backwards(self, orm):
        # Deleting model 'Band'
        db.delete_table(u'showlist_band')

        # Removing M2M table for field bands on 'Show'
        db.delete_table(db.shorten_name(u'showlist_show_bands'))


    models = {
        u'showlist.band': {
            'Meta': {'object_name': 'Band'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'youtube_link': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'showlist.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'showlist.show': {
            'Meta': {'object_name': 'Show'},
            'acts': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'bands': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['showlist.Band']", 'symmetrical': 'False'}),
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