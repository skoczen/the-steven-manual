# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MonthlyCheckin'
        db.create_table('main_site_monthlycheckin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('month_start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 8, 12, 0, 0))),
            ('happiness_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('happiness_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('relationship_health_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('relationship_health_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('enough_time_in_nature_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('enough_time_in_nature_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('presence_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('presence_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('in_touch_with_spirtuality_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('in_touch_with_spirtuality_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('making_things_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('making_things_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('have_a_space_that_is_just_mine_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('have_a_space_that_is_just_mine_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('enough_time_alone_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('enough_time_alone_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('finances_on_track_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('finances_on_track_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('getting_out_enough_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('getting_out_enough_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sex_life_is_good_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sex_life_is_good_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('making_the_world_a_bit_better_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('making_the_world_a_bit_better_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('healthy_eating_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('healthy_eating_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('healthy_drinking_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('healthy_drinking_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('healthy_activity_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('healthy_activity_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('closer_to_two_year_plan_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('closer_to_two_year_plan_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('habits_from_last_month', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('habit_success_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('habit_success_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('habits_for_next_month', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('main_site', ['MonthlyCheckin'])


    def backwards(self, orm):
        # Deleting model 'MonthlyCheckin'
        db.delete_table('main_site_monthlycheckin')


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
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 12, 0, 0)'}),
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
        'main_site.monthlycheckin': {
            'Meta': {'object_name': 'MonthlyCheckin'},
            'closer_to_two_year_plan_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'closer_to_two_year_plan_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enough_time_alone_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enough_time_alone_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'enough_time_in_nature_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enough_time_in_nature_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'finances_on_track_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'finances_on_track_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'getting_out_enough_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'getting_out_enough_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'habit_success_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'habit_success_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'habits_for_next_month': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'habits_from_last_month': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'happiness_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'happiness_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'have_a_space_that_is_just_mine_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'have_a_space_that_is_just_mine_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_activity_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_activity_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_drinking_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_drinking_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_eating_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'healthy_eating_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_touch_with_spirtuality_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'in_touch_with_spirtuality_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'making_the_world_a_bit_better_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'making_the_world_a_bit_better_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'making_things_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'making_things_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'month_start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 8, 12, 0, 0)'}),
            'presence_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'presence_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'relationship_health_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'relationship_health_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sex_life_is_good_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sex_life_is_good_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
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