#-*- coding:utf-8 -*-
import urllib2
import re
import sys

class QB:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0(compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.continu = False

    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers = self.headers)
            content = urllib2.urlopen(request).read()
            return content
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'connect error, please try again', e.reason
                return None

    def getItems(self):
        print '\n*****getting stories in page %d*****\n' % self.pageIndex

        # Get content from next page
        content = self.getPage(self.pageIndex)
        if not content:
            print 'getting stories failed'
            return None
        self.pageIndex += 1

        # Deal with the content
        pageStories = []
        pattern = re.compile('title=.*?<h2>(.*?)</h2>.*?content">.*?<span>(.*?)</.*?<div(.*?)number">(\d*?)</.*?number">(\d*?)</', re.S)
        items = re.findall(pattern, content)

        # Add stories
        for item in items:
            haveImg = re.search('img', item[2])
            if not haveImg:
                self.stories.append('User: ' + item[0] + '\r\nContent:\r\n\t' + item[1].replace('<br/>','\r\n\t') + '\r\nFunny Degree: ' + item[3] + '\tComments: ' + item[4] + '\n')
        return pageStories

    def getStories(self):
        # Of course need to deal with different coding systems =_=
        typec = sys.getfilesystemencoding()

        #Always make sure we have stories to tell
        while len(self.stories) != 0:
            inputc = raw_input("Press 'enter' to get a new duanzi, and press 'q' to quit\n")

            if inputc == 'q' or inputc == 'Q':
                self.continu = False
                return

            print self.stories[0].decode('utf-8').encode(typec)
            del self.stories[0]
            print 'Duanzi left : ', len(self.stories)

            if len(self.stories) < 2:
                self.getItems()
        # Well, we have nothing to tell, which is impossible in normal status
        print 'this program just died in peace'

    def start(self):
        print 'Welcome to our duanzi program!'
        self.continu = True
        self.getItems()

        while self.continu:
            if len(self.stories) > 0:
                self.getStories()
            else:
                print 'oh, no more stories. Some errors occured, try again, maybe get more'
                break;

qb = QB()
qb.start()
