from django.contrib import admin
from main_site.models import Emotion, Value, GutterBumper, WeeklyMeal
    

class GutterBumperOptions(admin.ModelAdmin):
    list_display = ("date", "sleep_hrs","work_hrs","alone_hrs","friend_hrs","relationship_hrs","public_hrs","off","worked_out","mediated","number_of_beers","presence","happiness","creativity","morning_mood")
    list_filter = ("date",)
    # search_fields = ('name','description',)
    # exclude = ("slug",)
    

admin.site.register(Emotion)
admin.site.register(Value)
admin.site.register(WeeklyMeal)
admin.site.register(GutterBumper, GutterBumperOptions)