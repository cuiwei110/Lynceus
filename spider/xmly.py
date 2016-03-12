#coding=utf-8

import urllib2
import re
import json

class Xmly():
	URL_PRIFIX = "http://www.ximalaya.com/tracks/"

	def getHtml(self,url):
		html = urllib2.urlopen(url).read()
		return html

	def getJsonUrl(self,url):
		result = url.split('/')
		return result[len(result)-1] + ".json"

	def getUrl(self,html):
		jsonStr = json.loads(html)
		return jsonStr["play_path"]

	def getVoiceUrl(self,url):
		jsonUrl = self.URL_PRIFIX + self.getJsonUrl(url)
		html = self.getHtml(jsonUrl)
		voiceUrl = self.getUrl(html)
		return 1,voiceUrl;