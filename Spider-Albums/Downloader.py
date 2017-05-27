#-*- coding:utf-8 -*-
import urllib2

class Downloader(object):
    def download(self, url):
        if url is None:
            print 'url None'
            return None
        try:
            print 'Requesting'
            request = urllib2.Request(url)
            request.add_header('user-agent', 'Mozilla/5.5')
            print 'Opening url'
            response = urllib2.urlopen(request)
            print 'checking attributes'
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
        if response.getcode() != 200:
            print 'get_new_url failed'
            return None
        return response.read()
