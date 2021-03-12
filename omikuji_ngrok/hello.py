# -*- coding: utf-8 -*-
#https://www.seleniumqref.com/api/python/window_set/Python_close.html
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#https://qiita.com/zaburo/items/5091041a5afb2a7dffc8
from flask import Flask, render_template
#import chromedriver_binary
from time import sleep

app = Flask(__name__)

@app.route('/<ngrok_url>')
def top(ngrok_url=None):
    url = "http://my-16421.azurewebsites.net/omikuji/api/ngrok_update.php"
    get_url_info = requests.get(url,{'ngrok_url':ngrok_url}).text
    return render_template('ngrok.html',title='running',ngrok_url= ngrok_url)


if __name__ == "__main__":
    app.run(debug=True, port=8886, threaded=True)
