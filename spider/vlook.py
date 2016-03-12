#coding=utf-8
import urllib
import urllib2
import re
class VLook():
	def getHtml(self,url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		return response.read()

	def getUrl(self,html):
		pattern = re.compile(r'player_src=([\s\S]*?)"')
		result = pattern.findall(html)
		return result[0]

	def getMp4Url(self,url):
	#url = "http://service.vlook.cn:8080/down/servlet/VideoPlayS?bid=3236751&ts=56cd4caa&sn=26e6cd92d131587a1e53c8402816a6d5&vid=ebNv&client=pc&imei=fb521a98d916861e56f9c0740897b666"
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		return response.geturl()

	def getVideoUrl(self,url):
		html = self.getHtml(url)
		xurl = self.getUrl(html)
		return 1,self.getMp4Url(urllib.unquote(xurl))
