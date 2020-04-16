# -*- coding: utf-8 -*-
#https://www.seleniumqref.com/api/python/window_set/Python_close.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#https://qiita.com/zaburo/items/5091041a5afb2a7dffc8
from flask import Flask, render_template
#import chromedriver_binary
from time import sleep
import pyautogui as pgui

app = Flask(__name__)

@app.route('/')
def top():
    return render_template('index.html', title='待機')

@app.route('/execution/<user>')
def execution(user=None):
    pgui.keyDown('f11')
    pgui.keyUp('f11')
    name = "who"
    #return name
    return render_template('execution/index.html', title='実行', name=user)

@app.route('/animation/<user>')
def animation(user=None):
    return render_template('execution/animation.html', title='実行', name=user)

@app.route('/result/<user>')
def result(user=None):
    return render_template('result/index.html', title='結果', name=user , num=33)

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
・flaskのインストール
・※もう一つの方のegrokでブラウザup
・seleniumのインストール
python -m pip install selenium
・chromeドライバー
https://watlab-blog.com/2019/08/10/chromedriver-path/
https://pypi.org/project/chromedriver-binary/#history

'''