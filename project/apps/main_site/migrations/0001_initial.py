# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Emotion'
        db.create_table('main_site_emotion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cause', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('symptoms', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('helpful', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('main_site', ['Emotion'])

        # Adding model 'EmotionEvent'
        db.create_table('main_site_emotionevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emotion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main_site.Emotion'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('main_site', ['EmotionEvent'])

        # Adding model 'Value'
        db.create_table('main_site_value', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('explanation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('main_site', ['Value'])


    def backwards(self, orm):
        # Deleting model 'Emotion'
        db.delete_table('main_site_emotion')

        # Deleting model 'EmotionEvent'
        db.delete_table('main_site_emotionevent')

        # Deleting model 'Value'
        db.delete_table('main_site_value')


    models = {
        'main_site.emotion': {
            'Meta': {'object_name': 'Emotion'},
            'cause': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'helpful': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'symptoms': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'main_site.emotionevent': {
            'Meta': {'object_name': 'EmotionEvent'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'emotion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main_site.Emotion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'main_site.value': {
            'Meta': {'object_name': 'Value'},
            'explanation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main_site']