# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        last_sleep = 8
        for gb in orm['main_site.GutterBumper'].objects.order_by("date").all():
            cur_sleep = gb.sleep_hrs
            gb.sleep_hrs = last_sleep
            gb.save()
            last_sleep = cur_sleep

        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."

    def backwards(self, orm):
        "Write your backwards methods here."

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
            'left_the_house': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        },
        'main_site.weeklymeal': {
            'Meta': {'object_name': 'WeeklyMeal'},
            'how_it_went': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'week_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main_site']
    symmetrical = True
