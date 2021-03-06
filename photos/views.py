# Create your views here.'
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from photos.models import Photo
import flickr
import get_dctech

def home(request):
	tags = ["dctech"]
	sort = "interestingness-desc"
	extras = "url_m,views,tags"
    	photos = get_dctech.photos_search_adv(tags=tags, per_page=40, sort=sort, extras=extras)
	urls_and_views = []
	for photo in photos:
		urls_and_views.append(photo)
	photos = sorted(photos, key=lambda photo: -int(photo.views)) 
	return render_to_response("photo/photos.html", dict(photos=photos))

