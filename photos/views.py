# Create your views here.'
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from photos.models import Photo

def home(request):
	photos = Photo.objects.all()
	return render_to_response("photo/photos.html", dict(photos=photos))


