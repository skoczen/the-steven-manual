import datetime
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

@render_to("main_site/home.html")
def home(request):
    return locals()


@render_to("main_site/monthly.html")
def monthly(request):
    gutterbumpers = GutterBumper.objects.filter(date__gte=datetime.date.today()-datetime.timedelta(days=31))
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
    bumper = GutterBumper.objects.get(pk=bumper_pk)
    return {"success":success, "sleep_hrs": bumper.sleep_hrs, "id": bumper_pk}


@ajax_request
def get_sleep_hrs(request, bumper_pk):
    bumper = GutterBumper.objects.get(pk=bumper_pk)
    return {"success":True, "sleep_hrs": bumper.sleep_hrs, "id": bumper_pk}
