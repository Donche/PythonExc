#-*- coding:utf-8 -*-

import url_manager, Downloader, Parser, Outputer
import time

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = Downloader.Downloader()
        self.parser = Parser.Parser()
        self.outputer = Outputer.Outputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        try:
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                print 'parsing'
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                print 'adding new urls'
                self.urls.add_new_urls(new_urls)
                print 'collecting data'
                self.outputer.collect_data(new_data)
                time.sleep(1)
                if count == 10:
                    break
                count += 1

        except:
            print 'craw failed'

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "https://music.douban.com/subject/26590388/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
