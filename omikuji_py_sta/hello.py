# -*- coding: utf-8 -*-
#https://www.seleniumqref.com/api/python/window_set/Python_close.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#https://qiita.com/zaburo/items/5091041a5afb2a7dffc8
from flask import Flask, render_template
#import chromedriver_binary
from time import sleep

app = Flask(__name__)

options = webdriver.ChromeOptions()
options.add_argument('--start-fullscreen')

@app.route('/<user>')
def top(user=None):
    driver = webdriver.Chrome(options=options)
    url = "http://127.0.0.1:8888/execution/" + user
    driver.get(url)
    #return render_template('index.html',title='running')
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=8887, threaded=True)
