# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GutterBumper.work_hrs'
        db.alter_column('main_site_gutterbumper', 'work_hrs', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'GutterBumper.friend_hrs'
        db.alter_column('main_site_gutterbumper', 'friend_hrs', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'GutterBumper.sleep_hrs'
        db.alter_column('main_site_gutterbumper', 'sleep_hrs', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'GutterBumper.relationship_hrs'
        db.alter_column('main_site_gutterbumper', 'relationship_hrs', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'GutterBumper.alone_hrs'
        db.alter_column('main_site_gutterbumper', 'alone_hrs', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'GutterBumper.work_hrs'
        db.alter_column('main_site_gutterbumper', 'work_hrs', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'GutterBumper.friend_hrs'
        db.alter_column('main_site_gutterbumper', 'friend_hrs', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'GutterBumper.sleep_hrs'
        db.alter_column('main_site_gutterbumper', 'sleep_hrs', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'GutterBumper.relationship_hrs'
        db.alter_column('main_site_gutterbumper', 'relationship_hrs', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'GutterBumper.alone_hrs'
        db.alter_column('main_site_gutterbumper', 'alone_hrs', self.gf('django.db.models.fields.IntegerField')(null=True))

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
            'alone_hrs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'creativity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 5, 0, 0)'}),
            'friend_hrs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'happiness': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'morning_mood': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_beers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'relationship_hrs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sleep_hrs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'work_hrs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
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