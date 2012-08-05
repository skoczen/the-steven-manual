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