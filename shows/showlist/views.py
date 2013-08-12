from django.http import Http404
from django.shortcuts import render_to_response
from showlist.models import Show

def index(request):
    shows = Show.objects.all()
    return render_to_response('showlist/index.html', {'shows': shows})