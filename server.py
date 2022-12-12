import os
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, request

app = Flask(__name__)

def pahe(title: str) -> str:
    options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-dev-shm-usage")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"https://pahe.li/?s={title}")
    return driver.page_source

@app.route('/')
def root():
    return "MultiFunction Bot is Up & Running!"

@app.route('/pahe')
def pahereq():
    if request.args.get('q'):
        judul = request.args.get('q')
        try:
            parse = pahe(judul)
            return str(parse)
        except Exception as err:
            return str(err)
    else:
        return {
            'success': False,
            'msg': 'Isi parameter query, ex: https://yasirapi.eu.org/yt-search?q=scraping%20tutorial',
            'info': 'Join telegram channel @YasirPediaChannel for updates.',
        }

app.run(host="0.0.0.0", port=os.environ.get("PORT", 80))
