#!/usr/bin/python
"""Usage: python wallpaper.py [OPTIONS] TAGS
TAGS is a space delimited list of tags

OPTIONS:
  -w screenwidth or --width screenwidth
  -h screenheight or --height screenheight
  -f filename or --file filename

Requires:
 - Python Imaging Library [http://www.pythonware.com/products/pil/]
"""

__author__ = "James Clarke <james@jamesclarke.info>"
__version__ = "$Rev: 2 $"
__date__ = "$Date: 2007-03-22 15:28:46 -0400 (Thu, 22 Mar 2007) $"
__copyright__ = "Copyright 2004-5 James Clarke"

import sys
import urllib
import math
import random
import Image
import flickr

def photos_search_adv(user_id='', auth=False,  tags='', tag_mode='', text='',\
                  min_upload_date='', max_upload_date='',\
                  min_taken_date='', max_taken_date='', \
                  license='', per_page='', page='', sort='',\
                  safe_search='', content_type='', extras = '', **kwargs):
    """Returns a list of Photo objects.

    If auth=True then will auth the user.  Can see private etc
    """
    method = 'flickr.photos.search'

    data = flickr._doget(method, auth=auth, user_id=user_id, tags=tags, text=text,\
                  min_upload_date=min_upload_date,\
                  max_upload_date=max_upload_date, \
                  min_taken_date=min_taken_date, \
                  max_taken_date=max_taken_date, \
                  license=license, per_page=per_page,\
                  page=page, sort=sort,  safe_search=safe_search, \
                  content_type=content_type, \
                  tag_mode=tag_mode, \
                  extras=extras, **kwargs)
    
    photos = []
    if data.rsp.photos.__dict__.has_key('photo'):
        if isinstance(data.rsp.photos.photo, list):
            for photo in data.rsp.photos.photo:
              photos.append(photo)
        else:
            photos = [data.rsp.photos.photo]
    return photos


def main(*argv):
    from getopt import getopt, GetoptError
  
    try:
        (opts, args) = getopt(argv[1:], 'w:h:f', ['width', 'height', 'file'])
    except GetoptError, e:
        print e
        print __doc__
        return 1
    
    tags = ["dctech"]
    
    photos = photos_search_adv(tags=tags, per_page=40, sort="interestingness-desc", extras="url_m,views")
    
    urls = []
    
    for photo in photos:
        print(photo.url_m)
        print(photo.views)
        

if __name__ == '__main__':
    sys.exit(main(*sys.argv))
