#-*-coding:UTF-8-*-

import pymongo
import csv

class MongoDBThing(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.MyMusic
        self.newUrlsCol = db.newUrls
        self.oldUrlsCol = db.oldUrls 
        self.notFoundUrls = db.notFoundUrls
        self.music = db.music
        
    def add_new_url(self, url):
        if url is None:
            return
        if self.newUrlsCol.find({'url':url}).count() == self.oldUrlsCol.find({'url':url}).count() == 0:
            self.newUrlsCol.insert({'url': url})

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def add_new_url_forcibly(self, url):
        self.oldUrlsCol.remove({'url': url})
        self.newUrlsCol.insert({'url': url})    
            
    def has_new_url(self):
        return self.newUrlsCol.find().count() != 0
    
    def get_new_url(self):
        urlDoc = self.newUrlsCol.find_one()
        self.newUrlsCol.remove(urlDoc)
        self.oldUrlsCol.insert(urlDoc)
        return urlDoc['url']
    
    def add_404_url(self, url):
        self.notFoundUrls.insert({'url':url})
         
    def collect_data(self, data):
        if data is None: 
            return
        self.music.insert(data)
        
    def output(self):
        allDatas = self.music.find()
        with open('MyMusic.csv', 'w', encoding = 'utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Num', 'AlnumName', 'GroupName', 'Score', 'ScoreNum', 'Genre', 'Type' , 'Time' ,'url'])
            row = 1
            for data in allDatas:
                writer.writerow([row,data['AlbumName'],data.get('performer','None'),data.get('score', 0),data.get('sco_num', 0), data.get('genre', 'None'),data.get('type', 'None'), data.get('time', 'None'), data.get('url', 'None')])
                row += 1



