#coding=utf-8
import os
import re
import time
import urllib2
class MeiPaiVideo():

	#  获取网页源码
	def getHtml(self,url):
		html = urllib2.urlopen(url).read()
		return html

	def getName(self,html):
		reg = re.compile(r'<title>([\s\S]*?)</title>')
		result = reg.findall(html)
		name = time.time()
		if len(result) != 0:
			name = result[0]
		return name

	def getUrl(self,html):
		reg = re.compile(r'<meta content="(https://[\s\S]*?mp4)" property="og:video:url">')
		result = reg.findall(html)
		if len(result)==0:
			return 
		else:
			return result[0]
	

	def getVideoUrl(self,url):
		html = self.getHtml(url)
		#name = self.getName(html)
		url = self.getUrl(html)
		if url:
			return 1,url
		else:
			return 0,''