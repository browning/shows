from django.http import Http404
from django.shortcuts import render_to_response
from showlist.models import Show
import datetime

def index(request):
	# get a list of shows from yesterday to 2 weeks in the future
    shows = Show.objects.filter(datetime__gte=datetime.date.today() + datetime.timedelta(days=-1),
    	datetime__lte=datetime.date.today() +datetime.timedelta(days=14))
    return render_to_response('showlist/index.html', {'shows': shows})