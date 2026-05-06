from django.shortcuts import render
from .models import Event
# Create your views here.

def home(request):
    upcoming_events = Event.objects.filter(is_upcoming=True).first()
    previous_events = Event.objects.filter(is_previous=True).first()
    return render(request, 'archive/home.html', {'upcoming_events': upcoming_events, 'previous_events': previous_events})