#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):

    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    host = filename.split('_')[1]
    urls_sorted_2 = []
    urls_sorted_3 = []

    with open(filename) as file:
        str = file.read()
        list = re.findall(r'[\w/\-]+puzzle[\w/\-\.]+', str)
    urls = ['https://'+host + x for x in list]
    urls_sorted = sorted(urls)
    for element in urls_sorted:
        if element not in urls_sorted_2:
            urls_sorted_2.append(element)

    for i in urls_sorted_2:
        urls_sorted_3.append([i[-8:],i])

    urls_sorted_no_repeat = sorted(urls_sorted_3)
    list_url = [url for x, url in urls_sorted_no_repeat]

    return list_url


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    count = 0
    srcImg = []
    for url in img_urls:
        dir = dest_dir+'/'+'img'+str(count)+'.png'
        urllib.request.urlretrieve(url, dir)
        srcImg.append("<img src='%s'>"%dir)
        count += 1

    str_html = ''.join(srcImg)
    html = '<html><body>%s</body></html>'%str_html

    with open(dest_dir+'.html', 'w') as file:
        file.write(html)



def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
