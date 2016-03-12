#coding=utf-8
import urllib2
import os
import re

class MiaoPaiVideo():
	
	URL_PREFIX = "http://dlcdn.yixia.com/stream/"
	def getHtml(self,url):
		html = urllib2.urlopen(url).read()
		return html

	def getDescription(self,html):
		reg = re.compile(r'meta name="description" content="([\s\S]*?)"');
		result = reg.findall(html)
		return result[0]

	def getToken(self,url):
		result = url[28:].split('.')
		return result[0]

	def getVideoUrl(self,url):
		token = self.getToken(url)
		#html = self.getHtml(url)
		#filename = self.getDescription(html)
		url = self.URL_PREFIX + token+'.mp4'
		return 1,url
