#-*- coding:utf-8 -*-
u = u'wocao卧槽'
print u

s = u.encode('utf-8')
print s


d = s.decode('utf-8')
print d

g = u.encode('gbk')
print g

m = u.find(u'卧')
print m
m = s.find('卧')
print m
m = g.find(u'卧'.encode('gbk'))
print m
