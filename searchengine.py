#! /usr/bin/env python
# -*- coding=utf-8 -*- 

import urllib2
from Beautiful import *
from urlparse import urljoin

#构造一个单词列表，这些单词将被忽略
ignorewoed = set(['the','of','to','and','a','in','is','it'])

class crawler(self,pages,depth = 2):
	"""dbnamering for crawler"""
	#初始化crawler类并传入数据库名称
	def __init__(self, dbname)
    	pass
	def __del_ _(self)
        pass
	def dbcommit(self):
		pass
	#辅助函数，用于获取条目的ID，并且如果条目不存在，就将其加入数据库中
	def getentryid(self,table,field,value,createnew=True):
		return None

	#为每个网页建立索引	
	def addtoindex(self,url,soup):
		print 'Indexing %s' % url
    #从一个HTML网页提取文字（不带标签）
    def gettextonly(self,soup):
    	return None
    #根据任何非空白字符进行分词处理
    def separatewords(self,text):
    	return None
    #如果url已经索引过了，则返回ture
    def isindexed(self,url):
    	return False
    #添加一个关联两个网页的链接
    def addlinkref(self,urlFrom,urlTo,linkText):
    	pass
    #从一个小组网页开始进行广度优先搜索，直至某一给定深度
    #期间为数据建立索引
    def crawl(self,pages,depth=2):
    	for i in range(depth):
            newpages = set ()
            for page in pages:
                try:
                    c = urllib2.urlopen(page)
                except:
                    print"Could not open %s" % page 
                    continue
                soup = BeautifulSoup(c.read())
                self.addtoindex(page,soup)

                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url = urljoin(page,link['href'])
                        if url.find("'")!=-1:
                            continue
                        url  =url.split('#')[0] #去掉位置部分
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newpages.add(url)
                        linkText = self.gettextonly(link)
                        self.sddlinkref(page,url,linkText)
                self.dbcommit()
            pages = newpages            
    #创建数据表
    def crearteindextable(self):
    	pass