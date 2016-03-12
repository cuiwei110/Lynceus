from meipaivideo import MeiPaiVideo
from miaopaivideo import MiaoPaiVideo
from vlook import VLook
from changba import ChangBa
from lizhi import LiZhi
from xmly import Xmly

class Video():
	FILE_VOICE_PATH = "/Users/cheng/Documents/PyScript/res/voice/"
	SINAVIDEO_PRIFIX = "http://video.weibo.com"
	MIAOPAI_PRIFIX = "http://www.miaopai.com"
	MEIPAI_PRIFIX = "http://www.meipai.com"
	VLOOK_PRIFIX = "http://www.vlook.cn"
	CHANGRBA_PRIFIX = "http://changba.com"
	LIZHI_PRIFIX = "http://www.lizhi.fm"
	XMLY_PRIFIX = "http://www.ximalaya.com"

	def start(self,url):
		if url.startswith(self.MEIPAI_PRIFIX):
			print "[+]MeiPai:" + url
			meipaivideo = MeiPaiVideo()
			return meipaivideo.getVideoUrl(url)
		elif url.startswith(self.MIAOPAI_PRIFIX):
			print "[+]MiaoPai:" + url
			miaopaivideo = MiaoPaiVideo()
			return miaopaivideo.getVideoUrl(url)
		elif url.startswith(self.VLOOK_PRIFIX):
			print "[+]vlook:" + url 
			vlook = VLook()
			return vlook.getVideoUrl(url)
		elif url.startswith(self.CHANGRBA_PRIFIX):
			print "[+]ChangBa:" + url
			changba = ChangBa()
			return changba.getVideoUrl(url)
		elif url.startswith(self.LIZHI_PRIFIX):
			print "[+]Lizhi:" + url
			lizhi = LiZhi()
			return lizhi.getVoiceUrl(url)
		elif url.startswith(self.XMLY_PRIFIX):
			print "[+]Xmly: " + url
			xmly = Xmly()
			return xmly.getVoiceUrl(url)
		else:
			return 0,''