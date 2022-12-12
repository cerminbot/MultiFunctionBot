import os
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from flask import Flask, request

app = Flask(__name__)

def pahe(title: str) -> str:
    chromedriver_autoinstaller.install()

    AGREE_BUTTON = "//*[contains(text(), 'AGREE')]"
    LINK_TYPE = ["//*[contains(text(), 'GD')]"]
    GENERATE = "#generater > img"
    SHOW_LINK = "showlink"
    CONTINUE = "Continue"

    os.chmod("/usr/src/app/chromedriver", 755)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/usr/bin/google-chrome"
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    wd = webdriver.Chrome("/usr/src/app/chromedriver", chrome_options=chrome_options)
    wd.get(f"https://pahe.li/?s={title}")
    retun wd.page_source

@app.route('/')
def root():
    return "MultiFunction Bot is Up & Running!"

@app.route('/pahe')
def pahe():
    if request.args.get('q'):
        judul = request.args.get('q')
        parse = pahe(judul)
        return str(parse)
    else:
        return {
            'success': False,
            'msg': 'Isi parameter query, ex: https://yasirapi.eu.org/yt-search?q=scraping%20tutorial',
            'info': 'Join telegram channel @YasirPediaChannel for updates.',
        }

app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
