# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EmotionEvent'
        db.delete_table('main_site_emotionevent')

        # Adding field 'Emotion.one_liner'
        db.add_column('main_site_emotion', 'one_liner',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field emotions on 'GutterBumper'
        db.create_table('main_site_gutterbumper_emotions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gutterbumper', models.ForeignKey(orm['main_site.gutterbumper'], null=False)),
            ('emotion', models.ForeignKey(orm['main_site.emotion'], null=False))
        ))
        db.create_unique('main_site_gutterbumper_emotions', ['gutterbumper_id', 'emotion_id'])


    def backwards(self, orm):
        # Adding model 'EmotionEvent'
        db.create_table('main_site_emotionevent', (
            ('emotion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main_site.Emotion'])),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('main_site', ['EmotionEvent'])

        # Deleting field 'Emotion.one_liner'
        db.delete_column('main_site_emotion', 'one_liner')

        # Removing M2M table for field emotions on 'GutterBumper'
        db.delete_table('main_site_gutterbumper_emotions')


    models = {
        'main_site.emotion': {
            'Meta': {'object_name': 'Emotion'},
            'cause': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'helpful': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'one_liner': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'symptoms': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'main_site.gutterbumper': {
            'Meta': {'object_name': 'GutterBumper'},
            'alone_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'creativity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 11, 0, 0)'}),
            'emotions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['main_site.Emotion']", 'null': 'True', 'blank': 'True'}),
            'friend_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'happiness': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'morning_mood': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_beers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'presence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'public_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'relationship_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'sleep_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'work_hrs': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
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