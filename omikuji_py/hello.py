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

@app.route('/')
def top():
    return render_template('index.html', title='待機')

@app.route('/execution/<run_id>')
def execution(run_id=None):
    pgui.keyDown('f11')
    pgui.keyUp('f11')
    #return name
    return render_template('execution/index.html', title='実行', run_id=run_id)

@app.route('/animation/<run_id>')
def animation(run_id=None):
    num = random.randint(1,6)
    return render_template('execution/animation.html', title='実行', run_id=run_id , num = num)

@app.route('/result/<run_id>', methods=['GET', 'POST'])
def result(run_id=None):
    num = request.args.get('num')
    url = "http://my-16421.azurewebsites.net/omikuji/api/deactivated.php"
    get_url_info = requests.post(url,{"run_id": run_id,"num": num}).text
    return render_template('result/index.html', title='結果', run_id=run_id , num=num)

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
