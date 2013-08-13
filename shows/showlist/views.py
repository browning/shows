from django.http import Http404
from django.shortcuts import render_to_response
from showlist.models import Show
import datetime
from collections import OrderedDict
import pytz

def index(request):
	# get a list of shows from yesterday to 2 weeks in the future
    shows = Show.objects.filter(datetime__gte=datetime.date.today() + datetime.timedelta(days=-1),
    	datetime__lte=datetime.date.today() +datetime.timedelta(days=14)).order_by('datetime')
    showlist = OrderedDict()
    for show in shows:
    	md = pytz.timezone("America/New_York").normalize(show.datetime).strftime("%A %m/%d")
    	if str(md) in showlist:
    		showlist[md].append(show)
    	else:
    		showlist[md] = [show]
    print "%r" % showlist
    return render_to_response('showlist/index.html', {'shows': showlist})