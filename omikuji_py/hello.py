# -*- coding: utf-8 -*-
#https://www.seleniumqref.com/api/python/window_set/Python_close.html
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#https://qiita.com/zaburo/items/5091041a5afb2a7dffc8
from flask import Flask, render_template, request
#import chromedriver_binary
from time import sleep
import pyautogui as pgui
import random


app = Flask(__name__)
num = -1

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])
options.add_argument('--start-fullscreen')

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

@app.route('/')
def top():
    return render_template('index.html', title='待機')

@app.route('/execution/<run_id>')
def execution(run_id=None):
    #pgui.keyDown('f11')
    #pgui.keyUp('f11')
    #return name
    return render_template('execution/index.html', title='実行', run_id=run_id)

@app.route('/animation/<run_id>')
def animation(run_id=None):
    url = "https://mediacore.jp/omikuji/api/result_maxid.php"
    maxnum = int(requests.get(url).text)
    if(maxnum >= 1):
        num = random.randint(1,maxnum)
    else:
        num = random.randint(1,1)
    return render_template('execution/animation.html', title='実行', run_id=run_id , num = num)

@app.route('/result/<run_id>', methods=['GET', 'POST'])
def result(run_id=None):
    num = request.args.get('num')
    url = "http://mediacore.jp/omikuji/api/deactivated.php?run_id=" + run_id + "&num=" + num
    requests.get(url)
    url = "http://mediacore.jp/omikuji/api/result_raspi_imgurl_get.php?num=" + num
    img_url = requests.get(url).text
    return render_template('result/index.html', title='結果', run_id=run_id , num=num , img_url=img_url)

@app.route('/webclose')
def webclose():
    pgui.keyDown('alt')
    pgui.keyDown('f4')
    pgui.keyUp('alt')
    pgui.keyUp('f4')




'''
@app.route('/good')
def good():
    name = "Good"
    return name
'''

if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)


'''
・requestsのインストール

・flaskのインストール
・※もう一つの方のegrokでブラウザup
・seleniumのインストール
python -m pip install selenium
・chromeドライバー
https://watlab-blog.com/2019/08/10/chromedriver-path/
https://pypi.org/project/chromedriver-binary/#history

'''
