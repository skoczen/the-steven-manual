from django.db import models
import datetime


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s" % self.name

class DataSensitivity(BaseModel):
    name = models.CharField(max_length=200)

# Create your models here.
class Emotion(BaseModel):
    name = models.CharField(max_length=200)
    one_liner = models.TextField(blank=True, null=True)
    cause = models.TextField(blank=True, null=True, verbose_name="Causes")
    symptoms = models.TextField(blank=True, null=True)
    helpful = models.TextField(blank=True, null=True)
    
class Value(BaseModel):
    name = models.CharField(max_length=200, verbose_name='Story name')
    explanation = models.TextField(blank=True, null=True)

class GutterBumper(BaseModel):
    date = models.DateField(default=datetime.date.today())
    woke_up_at = models.TimeField(default=datetime.time(7,45))
    fell_asleep_at = models.TimeField(default=datetime.time(23,30))
    sleep_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Sleep", help_text="Sleep this morning")
    work_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Work")
    alone_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Alone")
    friend_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Friend")
    public_hrs = models.FloatField(default=0, blank=True, null=True, help_text="Not specifically hanging with people, but in a larger crowd", verbose_name="Public")
    relationship_hrs = models.FloatField(default=0, blank=True, null=True, verbose_name="Relationship")

    off = models.BooleanField(default=False)
    worked_out = models.BooleanField(default=False)
    mediated = models.BooleanField(default=False, verbose_name="meditated")
    left_the_house = models.BooleanField(default=False)
    inbox_zero = models.BooleanField(default=False)
    travelling_or_out_of_routine = models.BooleanField(default=False, verbose_name="Travelling/Nonroutine")
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
    
    @property
    def yesterday(self):
        try:
            return GutterBumper.objects.get(date=self.date - datetime.timedelta(days=1))
        except:
            return None

    @property
    def tomorrow(self):
        try:
            return GutterBumper.objects.get(date=self.date + datetime.timedelta(days=1))
        except:
            return None
    @property
    def calculated_sleep_hrs(self):
        if self.woke_up_at and self.yesterday.fell_asleep_at:
            today_hrs, today_min, _ = ("%s" % self.woke_up_at).split(":")
            yester_hrs, yester_min, _ = ("%s" % self.yesterday.fell_asleep_at).split(":")
            today_round_length = 1

            today = float(today_hrs) + (float(today_min)/60)
            yester = float(yester_hrs) + (float(yester_min)/60)

            if yester > today:
                # different date
                diff = (today+24) - yester
            else:
                # same date
                diff = today - yester
            rem = diff % 1
            round_len = 1
            if rem % 25:
                round_len = 2
            if rem == 0:
                round_len = 0

            return round(diff, round_len)
        return None

    def save(self, *args, **kwargs):
        try:
            old_fell_asleep_time = GutterBumper.objects.get(pk=self.pk).fell_asleep_at
        except:
            old_fell_asleep_time = None
        
        if self.calculated_sleep_hrs:
            self.sleep_hrs = self.calculated_sleep_hrs

        super(GutterBumper, self).save(*args, **kwargs)
        if old_fell_asleep_time and old_fell_asleep_time != self.fell_asleep_at and self.tomorrow:
            self.tomorrow.save()


class WeeklyMeal(BaseModel):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(blank=True, null=True)
    preparation = models.TextField(blank=True, null=True)
    how_it_went = models.TextField(blank=True, null=True)
    week_start_date = models.DateField(blank=True, null=True)


class MonthlyCheckin(BaseModel):
    month_start_date = models.DateField(default=datetime.date.today())

    happiness_rating = models.IntegerField(blank=True, null=True)
    happiness_notes = models.TextField(blank=True, null=True)
    relationship_health_rating = models.IntegerField(blank=True, null=True)
    relationship_health_notes = models.TextField(blank=True, null=True)
    enough_time_in_nature_rating = models.IntegerField(blank=True, null=True)
    enough_time_in_nature_notes = models.TextField(blank=True, null=True)
    presence_rating = models.IntegerField(blank=True, null=True)
    presence_notes = models.TextField(blank=True, null=True)
    in_touch_with_spirtuality_rating = models.IntegerField(blank=True, null=True)
    in_touch_with_spirtuality_notes = models.TextField(blank=True, null=True)
    making_things_rating = models.IntegerField(blank=True, null=True)
    making_things_notes = models.TextField(blank=True, null=True)
    have_a_space_that_is_just_mine_rating = models.IntegerField(blank=True, null=True)
    have_a_space_that_is_just_mine_notes = models.TextField(blank=True, null=True)
    enough_time_alone_rating = models.IntegerField(blank=True, null=True)
    enough_time_alone_notes = models.TextField(blank=True, null=True)
    finances_on_track_rating = models.IntegerField(blank=True, null=True)
    finances_on_track_notes = models.TextField(blank=True, null=True)
    getting_out_enough_rating = models.IntegerField(blank=True, null=True)
    getting_out_enough_notes = models.TextField(blank=True, null=True)
    sex_life_is_good_rating = models.IntegerField(blank=True, null=True)
    sex_life_is_good_notes = models.TextField(blank=True, null=True)
    making_the_world_a_bit_better_rating = models.IntegerField(blank=True, null=True)
    making_the_world_a_bit_better_notes = models.TextField(blank=True, null=True)
    healthy_eating_rating = models.IntegerField(blank=True, null=True)
    healthy_eating_notes = models.TextField(blank=True, null=True)
    healthy_drinking_rating = models.IntegerField(blank=True, null=True)
    healthy_drinking_notes = models.TextField(blank=True, null=True)
    healthy_activity_rating = models.IntegerField(blank=True, null=True)
    healthy_activity_notes = models.TextField(blank=True, null=True)
    closer_to_two_year_plan_rating = models.IntegerField(blank=True, null=True)
    closer_to_two_year_plan_notes = models.TextField(blank=True, null=True)

    habits_from_last_month = models.TextField(blank=True, null=True)
    habit_success_rating = models.IntegerField(blank=True, null=True)
    habit_success_notes = models.TextField(blank=True, null=True)
    habits_for_next_month = models.TextField(blank=True, null=True)

    what_is_the_work_story_i_am_telling = models.TextField(blank=True, null=True)
    what_is_the_relationship_story_i_am_telling = models.TextField(blank=True, null=True)
    what_is_the_identity_story_i_am_telling = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return "%s" % self.month_start_date.strftime('%B %Y')