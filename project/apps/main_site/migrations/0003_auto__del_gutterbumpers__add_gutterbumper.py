# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'GutterBumpers'
        db.delete_table('main_site_gutterbumpers')

        # Adding model 'GutterBumper'
        db.create_table('main_site_gutterbumper', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('sleep_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('work_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('alone_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('friend_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('relationship_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('off', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('worked_out', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mediated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('number_of_beers', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('presence', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('happiness', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('creativity', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('morning_mood', self.gf('django.db.models.fields.IntegerField')(default=False)),
        ))
        db.send_create_signal('main_site', ['GutterBumper'])


    def backwards(self, orm):
        # Adding model 'GutterBumpers'
        db.create_table('main_site_gutterbumpers', (
            ('work_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('friend_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('presence', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('sleep_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('number_of_beers', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('mediated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('alone_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('happiness', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('worked_out', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('off', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('morning_mood', self.gf('django.db.models.fields.IntegerField')(default=False)),
            ('relationship_hrs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('main_site', ['GutterBumpers'])

        # Deleting model 'GutterBumper'
        db.delete_table('main_site_gutterbumper')


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
        'main_site.gutterbumper': {
            'Meta': {'object_name': 'GutterBumper'},
            'alone_hrs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'creativity': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'friend_hrs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'happiness': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'morning_mood': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'number_of_beers': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'default': 'False'}),
            'relationship_hrs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_hrs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'work_hrs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'worked_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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