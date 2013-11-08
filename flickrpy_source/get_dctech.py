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

def main(*argv):
    from getopt import getopt, GetoptError
  
    try:
        (opts, args) = getopt(argv[1:], 'w:h:f', ['width', 'height', 'file'])
    except GetoptError, e:
        print e
        print __doc__
        return 1
    
    tags = ["dctech"]
    
    photos = flickr.photos_search(tags=tags, per_page=40)
    
    urls = []
    
    for photo in photos:
        urls.append(photo.getURL(size='Square', urlType='source'))
        print(photo.getURL(size='Square', urlType='source'))
        

if __name__ == '__main__':
    sys.exit(main(*sys.argv))
