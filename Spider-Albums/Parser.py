#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re

class Parser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print('page_url is none')
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        print('getting new urls')
        new_urls = self._get_new_urls(soup)
        print('getting new data')
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, soup):
        new_urls = set()
        recommend = soup.find('div', class_='content clearfix')
        links = recommend.find_all('a', href=re.compile(r"https://music\.douban\.com/subject/\d+/$")) 
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url
        print('parse url success')
        try:
            res_data['AlbumName'] = soup.find('div', id='wrapper').h1.text.strip()
            res_data['score'] = soup.find('strong', class_='ll rating_num').string
            res_data['sco_num'] = soup.find('div',class_='rating_sum').a.span.text
            info = soup.find('div', id='info')
            if info.find(text=re.compile('表演者')):
                res_data['performer'] = info.find(text=re.compile('表演者')).next_element.text.strip()
            else:
                res_data['performer'] = 'None'
            if info.find(text=re.compile('流派')):
                res_data['genre'] = info.find(text=re.compile('流派')).next_element.strip()
            else:
                res_data['genre'] = 'None'
            if info.find(text=re.compile('专辑类型')):
                res_data['type'] = info.find(text=re.compile('专辑类型')).next_element.strip()
            else:
                res_data['type'] = 'None'
            if info.find(text=re.compile('发行时间')):
                res_data['time'] = info.find(text=re.compile('发行时间')).next_element.strip()
            else:
                res_data['time'] = 'None'
        except:
            print('parse data failed')
        finally:
            return res_data
