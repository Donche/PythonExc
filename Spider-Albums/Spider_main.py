#-*- coding:utf-8 -*-

import Downloader, Parser, mongoDBThing
import time

class Spider(object):
    def __init__(self):
        self.mongo = mongoDBThing.MongoDBThing()
        self.downloader = Downloader.Downloader()
        self.parser = Parser.Parser()

    def craw(self, root_url):
        count = 1
        self.mongo.add_new_url(root_url)
        while self.mongo.has_new_url():
            try:
                new_url = self.mongo.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                if html_cont == 404:
                    self.mongo.add_404_url(new_url)
                else:
                    print('parsing')
                    new_urls, new_data = self.parser.parse(new_url, html_cont)
                    print('adding new urls')
                    self.mongo.add_new_urls(new_urls)
                    print('collecting data')
                    self.mongo.collect_data(new_data)
                time.sleep(1)
                if count == 50000:
                    break
                count += 1
            except:
                print('craw failed')
        self.mongo.output()

if __name__ == "__main__":
    obj_spider = Spider()
    url_start = 'https://music.douban.com/subject/26590388/'
    obj_spider.craw(url_start)
