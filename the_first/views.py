from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Track

@login_required
def index(request):
    tracks = request.user.track_set.all()
    context = { "tracks": tracks }
    return render(request, "tracks/index.html", context)

def search(request):
     # if this is a POST request we need to process the form data
    if request.method == "POST":
        tracks = Track.spotify_track_search(request.POST['search_text'])

    # if a GET (or any other method) we'll create a blank form
    else:
        tracks = []

    return render(request, "tracks/search.html", {'tracks': tracks})

def create(request):
    tparams = request.POST
    track = Track(name=tparams['name'], image_url=tparams['image_url'], spotify_id=tparams['spotify_id'], artist=tparams['artist'], user_id=request.user.id)
    track.save()
    return redirect('index')

def delete(request, id):
    obj = get_object_or_404(Track, id = id)
    obj.delete()
    return redirect('index')
