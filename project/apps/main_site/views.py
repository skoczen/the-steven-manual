import datetime
import math
from annoying.decorators import render_to, ajax_request
from main_site.models import GutterBumper
from main_site.forms import GutterBumperForm

def turn_friendly_time_into_python_time(time_with_ampm):
    time = time_with_ampm[:5]
    ampm = time_with_ampm[5:]
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    if hour == 12 and ampm.lower() == "am":
        hour = 0
    if ampm.lower() == "pm":
        hour += 12
    if hour == 24:
        hour = 0
    timestr = "%02d:%02d:00" % (hour, minute)
    return timestr


def success_and_statii_for_bumper(success, bumper_pk):
    bumper = GutterBumper.objects.get(pk=bumper_pk)
    return {
        "success": success, 
        "sleep_hrs": bumper.sleep_hrs, 
        "id": bumper_pk,
        "meditated_status": bumper.meditated_status,
        "off_status": bumper.off_status,
        "worked_out_status": bumper.worked_out_status,
        "left_the_house_status": bumper.left_the_house_status,
        "nature_time_status": bumper.nature_time_status,
    }

@render_to("main_site/home.html")
def home(request):
    return locals()


@render_to("main_site/monthly.html")
def monthly(request):
    gutterbumpers = GutterBumper.objects.filter(date__gte=datetime.date.today()-datetime.timedelta(days=31))
    total_days = gutterbumpers.count()
    total_workdays = total_days - math.floor(total_days/7*2)
    total_sleep = 0
    total_work = 0
    total_alone = 0
    total_friend = 0
    total_public = 0
    total_relationship = 0
    for g in gutterbumpers:
        total_sleep += g.sleep_hrs or 0
        total_work += g.work_hrs or 0
        total_alone += g.alone_hrs or 0
        total_friend += g.friend_hrs or 0
        total_public += g.public_hrs or 0
        total_relationship += g.relationship_hrs or 0

    avg_sleep = total_sleep / total_days
    avg_work = total_work / total_days
    avg_alone = total_alone / total_days
    avg_friend = total_friend / total_days
    avg_public = total_public / total_days
    avg_relationship = total_relationship / total_days
    avg_work_per_workday = total_work / total_workdays
    return locals()

@render_to("main_site/daily.html")
def daily(request):
    today = datetime.date.today()
    yesterday_bumper = GutterBumper.objects.get_or_create(date=today-datetime.timedelta(days=1))[0]
    yesterday_form = GutterBumperForm(instance=yesterday_bumper)

    today_bumper = GutterBumper.objects.get_or_create(date=today)[0]
    today_form = GutterBumperForm(instance=today_bumper)

    return locals()

@ajax_request
def update_bumpers(request, bumper_pk):
    success = False

    try:
        data = request.POST.copy()
        data["woke_up_at"] = turn_friendly_time_into_python_time(data["woke_up_at"])
        data["fell_asleep_at"] = turn_friendly_time_into_python_time(data["fell_asleep_at"])
        bumper = GutterBumper.objects.get(pk=bumper_pk)
        form = GutterBumperForm(data, instance=bumper)
        if form.is_valid():
            form.save()
            success=True
        else:
            print form.errors
    except:
        from traceback import print_exc
        print print_exc()
        pass
    
    return success_and_statii_for_bumper(success, bumper_pk)


@ajax_request
def get_sleep_hrs(request, bumper_pk):
    return success_and_statii_for_bumper(True, bumper_pk)
