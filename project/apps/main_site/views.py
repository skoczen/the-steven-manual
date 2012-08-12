import datetime
from annoying.decorators import render_to, ajax_request
from main_site.models import GutterBumper
from main_site.forms import GutterBumperForm


@render_to("main_site/home.html")
def home(request):
    return locals()


@render_to("main_site/monthly.html")
def monthly(request):
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
    print request.POST
    try:
        bumper = GutterBumper.objects.get(pk=bumper_pk)
        form = GutterBumperForm(request.POST, instance=bumper)
        if form.is_valid():
            form.save()
            success=True
        else:
            print form.errors
    except:
        from traceback import print_tb
        print_tb()
        pass
    return {"success":success}
