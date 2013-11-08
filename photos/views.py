# Create your views here.'
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from photos.models import Photo
import flickr

def home(request):
	tags = ["dctech"]
    	photos = flickr.photos_search(tags=tags, per_page=40)
	urls = []
	for photo in photos:
		urls.append(photo.getURL(size='Square', urlType='source'))
	return render_to_response("photo/photos.html", dict(photos=urls))


