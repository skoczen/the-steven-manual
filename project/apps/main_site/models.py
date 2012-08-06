from django.db import models

# Create your models here.
class Emotion(models.Model):
    name = models.CharField(max_length=200)
    cause = models.TextField(blank=True, null=True, verbose_name="Causes")
    symptoms = models.TextField(blank=True, null=True)
    helpful = models.TextField(blank=True, null=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

class EmotionEvent(models.Model):
    emotion = models.ForeignKey(Emotion)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s at %s" % (self.emotion.name, self.date)


class Value(models.Model):
    name = models.CharField(max_length=200)
    explanation = models.TextField(blank=True, null=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name


class GutterBumpers(models.Model):
    date = models.DateField(auto_now_add=True)
    sleep_hrs = models.IntegerField(blank=True, null=True)
    work_hrs = models.IntegerField(blank=True, null=True)
    alone_hrs = models.IntegerField(blank=True, null=True)
    friend_hrs = models.IntegerField(blank=True, null=True)
    relationship_hrs = models.IntegerField(blank=True, null=True)

    off = models.BooleanField(default=False)
    worked_out = models.BooleanField(default=False)
    mediated = models.BooleanField(default=False)
    number_of_beers = models.IntegerField(default=False)
    presence = models.IntegerField(default=False, help_text="1-10")
    happiness = models.IntegerField(default=False, help_text="1-10")
    morning_mood = models.IntegerField(default=False, help_text="1-10")
    
    