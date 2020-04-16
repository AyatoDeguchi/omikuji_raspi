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

@app.route('/')
def top():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8888/execution/mya-")
    return render_template('index.html',title='running')


if __name__ == "__main__":
    app.run(debug=True, port=8887, threaded=True)
