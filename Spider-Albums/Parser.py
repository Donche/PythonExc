#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re

class Parser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print 'page_url is none'
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        print 'getting new urls'
        new_urls = self._get_new_urls(soup)
        print 'getting new data'
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, soup):
        new_urls = set()
        recommend = soup.find('div', class_='content clearfix')
        links = recommend.find_all('a', href=re.compile(r"https://music\.douban\.com/subject/\d+/$")) #在推荐区域中寻找所有含有豆瓣书籍url的结点
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        print 'parse url success'
        res_data['AlbumName'] = soup.find('div', id='wrapper').h1.text.strip()
        print 'parse Name success: %s' % res_data['AlbumName']
        res_data['score'] = soup.find('strong', class_='ll rating_num').string
        print 'parse score success: %s' % res_data['score']

        res_data['sco_num'] = soup.find('div',class_='rating_sum').a.span.text
        print 'parse sco_num success: %s' % res_data['sco_num']
        info = soup.find('div', id='info')
        try:
            print 'searching performer'
            if info.find(text=re.compile(u'表演者')):
                res_data['performer'] = info.find(text=re.compile(u'表演者')).next_element.text
            else:
                res_data['performer'] = 'No data'
            print 'performer:',res_data['performer'],'\n'

            print 'searching genre'
            if info.find(text=re.compile(u'流派')):
                res_data['genre'] = info.find(text=re.compile(u'流派')).next_element.strip()
            else:
                res_data['genre'] = 'No data'
            print 'genre:',res_data['genre'],'\n'

            print 'searching album type'
            if info.find(text=re.compile(u'专辑类型')):
                res_data['type'] = info.find(text=re.compile(u'专辑类型')).next_element.strip()
            else:
                res_data['type'] = 'No data'
            print 'Type:',res_data['type'],'\n'

            print 'searching publishing time'
            if info.find(text=re.compile(u'发行时间')):
                res_data['time'] = info.find(text=re.compile(u'发行时间')).next_element.strip()
            else:
                res_data['time'] = 'No data'
            print 'publish time:',res_data['time'],'\n'

            print 'searching publisher'
            if info.find(text=re.compile(u'出版者')):
                res_data['publisher'] = info.find(text=re.compile(u'出版者')).next_element.text
            else:
                res_data['publisher'] = 'No data'
            print 'Publisher:',res_data['publisher'],'\n'

            print 'searching info'
            if soup.find('div', id='link-report'):
                res_data['info'] = soup.find('div', id='link-report').span.text.strip()
            else:
                res_data['info'] = 'No info data'
            print 'info:',res_data['info'],'\n'

            print 'searching content'
            res_data['content'] = soup.find('div', class_='track-list').text.strip()
            res_data['content'] = re.sub('\n+\s+','\n',res_data['content'])
            print 'content:',res_data['content'],'\n'

        except:
            print 'lack of information'
            return None
        if res_data['content'] == None:
            print 'No content'
            return None

        return res_data
