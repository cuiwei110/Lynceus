#coding=utf-8
import os
import re
import urllib2
import urllib 
# from common import Common
import common
class SinaVideo():

	URL_PIRFIX = "http://us.sinaimg.cn/"
	def getM3u8(self,html):
		reg = re.compile(r'list=([\s\S]*?)&fid')
		result = reg.findall(html)
		return result[0]


	def getName(self,url):
		 return url.split('=')[1]

	def getSinavideoUrl(self,filepath):
		f = open(filepath,'r')
		lines = f.readlines()
		f.close()
		for line in lines:
			if line[0] !='#':
				return line

	def download(self,url,filepath):
		#获取名称
		name = self.getName(url)
		html = common.getHtml(url)
		m3u8 = self.getM3u8(html)
		common.download(urllib.unquote(m3u8),filepath,name + '.m3u8')
		url = self.URL_PIRFIX + self.getSinavideoUrl(filepath+name+'.m3u8')
		common.download(url,filepath,name+'.mp4')
# if __name__ == '__main__':
# 	url = "http://video.weibo.com/show?fid=1034:d886e0143103de81ff0ae37046890af3"
# 	name = getName(url)
# 	html = getHtml(url)
# 	m3u8 = getM3u8(html)
# 	print "[+] m3u8url:"urllib.unquote(m3u8)
# 	download(urllib.unquote(m3u8),name+'.m3u8')
# 	videourl = "http://us.sinaimg.cn/"+getSinavideoUrl(name+'.m3u8')
# 	print "[+] videourl:"+videourl
# 	download(videourl,name+'.mp4')

