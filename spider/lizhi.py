#coding=utf-8
import os
import sys
import re
import urllib2

class LiZhi():
	def getHtml(self,url):
		html = urllib2.urlopen(url).read()
		return html

	def getUrl(self,html):
		reg = re.compile(r'data-title="([\S\s]*?)"[\S\s]*?data-url="([\S\s]*?)"')
		result = reg.findall(html)
		return result

	def getVoiceUrl(self,url):
		#获取html
		html=self.getHtml(url);
		result = self.getUrl(html)
		if len(result)<1:
			print "[-] download faild:" + url
			return 0,''
		else:
			return 1,result[1][1]
