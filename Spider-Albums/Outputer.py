#-*- coding:utf-8 -*-
class Outputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            print 'data is none while collecting data'
            return
        print 'appending data while collecting data..'
        self.datas.append(data)


    def output_html(self):
        fout = open('GoodBooks.html', 'w')
        print 'initializing'
        fout.write('<html>')
        fout.write('<meta charset="UTF-8">')
        fout.write('<title>GoodBooks_moverzp</title>')
        fout.write('<body>')
        print 'writing datas...'
        for data in self.datas:
            print data['AlbumName'], data['score']
            print 'creating new table'
            fout.write("<h2><a href='%s' target=_blank>%s</a></h2>" % (data['url'].encode('utf-8'), data['AlbumName'].encode('utf-8')))
            fout.write('<table border="1">')
            print 'writing scores,performer,...'
            fout.write('<tr><td>评分：</td><td><b>%s</b></td></tr>' % data['score'].encode('utf-8'))
            fout.write('<tr><td>评分人数：</td><td><b>%s</b></td></tr>' % data['sco_num'].encode('utf-8'))
            fout.write('<tr><td>表演者：</td><td>%s</td></tr>' % data['performer'].encode('utf-8'))
            fout.write('<tr><td>流派：</td><td>%s</td></tr>' % data['genre'].encode('utf-8'))
            fout.write('<tr><td>专辑类型：</td><td>%s</td></tr>' % data['type'].encode('utf-8'))
            fout.write('<tr><td>出版者：</td><td>%s</td></tr>' % data['publisher'].encode('utf-8'))
            fout.write('<tr><td>发行时间：</td><td>%s</td></tr>' % data['time'].encode('utf-8'))
            fout.write('</table>')
            fout.write('<p>info:\n%s' % data['info'].encode('utf-8'))
            fout.write('</p><hr>')
            fout.write('<p>content:\n%s' % data['content'].encode('utf-8'))
            fout.write('</p><hr>')


        fout.write('</body>')
        fout.write('</html>')
