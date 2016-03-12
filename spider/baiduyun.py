#coding:utf-8
import time
import urllib2
import urllib


url = "http://pan.baidu.com/api/sharedownload"
print url;
postData = {}
postData["sign"]="8d991feb9e90c057e03708bd8256f26dac081822";
postData["timestamp"]="1457229784";
postData["bdstoken"]="";
postData["channel"]="chunlei";
postData["clienttype"] = 0;
postData["web"]=1;
postData["app_id"]=250528

headers = {
"Host": "pan.baidu.com",
"Connection": "keep-alive",
"Content-Length": 276,
"Accept": "*/*",
"Origin": "http://pan.baidu.com",
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"DNT": 1,
"Referer": "http://pan.baidu.com/share/link?shareid=367727&uk=4026861542",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4,zh-TW;q=0.2",
}
data = urllib.urlencode(postData);
req = urllib2.Request(url,data,headers)
response = urllib2.urlopen(req)
print response.read()