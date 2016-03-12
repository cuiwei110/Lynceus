# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import render_template
from flask import request

from views.todos import todos_view
from spider.video import Video
from json import *

app = Flask(__name__)

# 动态路由
app.register_blueprint(todos_view, url_prefix='/todos')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    return str(datetime.now())

@app.route('/url',methods=['GET','POST'])
def test():
	url = request.form.to_dict()['url']
	print "[+]"+url
	video = Video()
	code,videoUrl = video.start(url)
	ret = {}
	ret["code"] = code
	ret["url"] = videoUrl
	return JSONEncoder().encode(ret)