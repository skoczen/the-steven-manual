from django.db import models
import datetime

# Create your models here.
class Emotion(models.Model):
    name = models.CharField(max_length=200)
    one_liner = models.TextField(blank=True, null=True)
    cause = models.TextField(blank=True, null=True, verbose_name="Causes")
    symptoms = models.TextField(blank=True, null=True)
    helpful = models.TextField(blank=True, null=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

class Value(models.Model):
    name = models.CharField(max_length=200)
    explanation = models.TextField(blank=True, null=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name


class GutterBumper(models.Model):
    date = models.DateField(default=datetime.date.today())
    sleep_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Sleep")
    work_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Work")
    alone_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Alone")
    friend_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Friend")
    public_hrs = models.FloatField(default=0, blank=True, null=True, help_text="Not specifically hanging with people, but in a larger crowd", verbose_name="Public")
    relationship_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Relationship")

    off = models.BooleanField(default=False)
    worked_out = models.BooleanField(default=False)
    mediated = models.BooleanField(default=False)
    number_of_beers = models.IntegerField(blank=True, null=True, verbose_name="# of beers")
    presence = models.IntegerField(blank=True, null=True, help_text="1-10")
    happiness = models.IntegerField(blank=True, null=True, help_text="1-10")
    creativity = models.IntegerField(blank=True, null=True, help_text="1-10")
    morning_mood = models.IntegerField(blank=True, null=True, help_text="1-10")
    notes = models.TextField(blank=True, null=True)
    
    emotions = models.ManyToManyField(Emotion, blank=True, null=True, verbose_name="Top three emotions")

    @property
    def saw_friend(self):
        return self.friend_hrs > 0

    def __unicode__(self):
        return "%s" % self.date
    

class WeeklyMeal(models.Model):
    name = models.CharField(max_length=200)
    how_it_went = models.TextField(blank=True, null=True)
    week_start_date = models.DateField(blank=True, null=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name