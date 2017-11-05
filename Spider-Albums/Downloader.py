#-*- coding:utf-8 -*-
import urllib.request
import urllib
from time import sleep

class Downloader(object):

    def _download(self, url):
        if url is None:
            print('url None')
            return None
        try:  
            print('Requesting')
            headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
            'Accept-Language':' zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection':'keep-alive',
            'referer':'baidu.com'}
            opener = urllib.request.build_opener()
            headall = []
            for key,value in headers.items():
                item = (key,value)
                headall.append(item)
            opener.addheaders = headall
            urllib.request.install_opener(opener)
            print('Opening url')
            response = urllib.request.urlopen(url, timeout = 10)
            print('checking attributes')
        except urllib.error.HTTPError as e:
            print('error: ' + str(e))
            if e.code == 403:
                return 403
            elif e.code == 404:
                return 404
            else:
                return
        if response.getcode() != 200:
            print('get_new_url failed')
            return None
        return response.read()

    def download(self, url):
        count = 1
        sleeptime = 30
        while True:
            res = self._download(url)
            if res == 404:
                return 404
            elif res == 403:
                if count > 30:
                    return
                print('waiting 403, waiting time:',sleeptime * count)
                sleep(sleeptime * count)
                count += 1
            else:
                return res