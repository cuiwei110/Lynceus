#coding=utf-8
import os
import re
import urllib2
class ChangBa():
	def getHtml(self,url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		return response.read()

	def getId(self,html):
		pattern = re.compile(r'data-workid="([\s\S]*?)"')
		result = pattern.findall(html)
		return result[0]
		
	def getMp4Url(self,url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		return response.geturl()

	def getVideoUrl(self,url):
		# url = "http://changba.com/s/LNlB0vWS7zri3n9tNRXv8w?&code=Kxhsv6044ik"
		html = self.getHtml(url)
		videoId = self.getId(html)
		videoUrl = "http://letv.cdn.changba.com/userdata/video/"+videoId+'.mp4'
		return 1,self.getMp4Url(videoUrl)

